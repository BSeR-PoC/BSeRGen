from src.helpers.bundle import insertComposition
import src.generate as gen
from src.cannonicalUrls import CodeSystem_bser_codes
from src.helpers.bundle import addEntries, addEntry, insertComposition, insertMessageHeader
from src.helpers.composition import generateCompositionSection, addSection
from src.helpers.patient import generatePatient
from src.helpers.relatedperson import generateRelatedPersonFromPatient
import orjson, os, json, inquirer
from fhirgenerator.helpers.helpers import default
from src.helpers.bser_practitioner import get_BSeR_Recipient_Practitioner, get_BSeR_Initiator_Practitioner
from src.constants import bundle_type_referral, bundle_type_feedback, bundle_type_both, use_case_arthritis, use_case_diabetes, use_case_ecn, use_case_hypertension, use_case_obesity, use_case_tobacco
from fhir.resources.coding import Coding

days = 1

def main():
    # USER CLI PROMPTS (Skip to buildBundle() if passing type configuration directly)
    questions = [
        inquirer.List('bundle_type',
            message="Please select a bundle type:",
            choices=[
                bundle_type_referral,
                bundle_type_feedback,
                bundle_type_both
            ]
        ),
        inquirer.List('use_case',
            message="Please select a BSeR Use Case:",
            choices=[
                use_case_arthritis,
                use_case_diabetes,
                use_case_ecn,
                use_case_hypertension,
                use_case_obesity,
                use_case_tobacco
            ]
        )
    ]
    answers = inquirer.prompt(questions)

    bundle_type = {
        "bundle_type": answers["bundle_type"],
        "use_case": answers["bundle_type"]
    }
    buildBundles(bundle_type)

## Call this directly to pass the configuration options instead of use user prompts.
'''
Example bundle_type dictionary
--------------------------------
bundle_type = {
    "bundle_type": "Feedback",
    "use_case": "Tobacco Use Cessation"
}
'''
def buildBundles(bundle_type):
    referral_bundle = None
    feedback_bundle = None
    
    config = openConfig()

    core_resource_dict = buildCoreResources(bundle_type["use_case"], config)
    patient_name = getPatientName(core_resource_dict["patient"])

    if bundle_type["bundle_type"] == bundle_type_referral:
        referral_bundle = buildReferralBundle(bundle_type["use_case"], core_resource_dict, config)
    elif bundle_type["bundle_type"] == bundle_type_feedback:
        feedback_bundle = buildFeedbackBundle(bundle_type["use_case"], core_resource_dict, config)
    elif bundle_type["bundle_type"] == bundle_type_both:
        referral_bundle = buildReferralBundle(bundle_type["use_case"], core_resource_dict, config)
        feedback_bundle = buildFeedbackBundle(bundle_type["use_case"], core_resource_dict, config)

    if referral_bundle != None:
        writeFile(bundle_type_referral, referral_bundle, patient_name)
    if feedback_bundle != None:
        writeFile(bundle_type_feedback, feedback_bundle, patient_name)


def buildCoreResources(use_case, config):
    core_resource_dict = {}
    core_resource_dict["patient"] = generatePatient(config["patient"], config["startDate"]) # The Patient helper class provides a means to manage BSER specific considerations of the US Core Patient.
    core_resource_dict["related_person"] = generateRelatedPersonFromPatient(core_resource_dict["patient"])
    core_resource_dict["initiator_practitioner"] = get_BSeR_Initiator_Practitioner()
    core_resource_dict["initiator_organization"] = gen.generate_BSeR_Organization()
    core_resource_dict["initiator_practitioner_role"] = gen.generate_BSeR_ReferralInitiatorPractitionerRole(core_resource_dict["initiator_practitioner"], core_resource_dict["initiator_organization"])
    core_resource_dict["recipient_practitioner"] = get_BSeR_Recipient_Practitioner()
    core_resource_dict["recipient_practitioner_role"] = gen.generate_BSeR_ReferralRecipientPractitionerRole(core_resource_dict["recipient_practitioner"])

    core_resource_dict["service_request"] = gen.generate_BSeR_ReferralServiceRequest(use_case, core_resource_dict["patient"],
            core_resource_dict["initiator_practitioner_role"], core_resource_dict["recipient_practitioner_role"], 
            config["startDate"])
    core_resource_dict["referral_task"] = gen.generate_BSeR_ReferralTask(core_resource_dict["service_request"])

    return core_resource_dict


# TODO: IMPLEMENT REFERRAL BUNDLE
def buildReferralBundle(use_case, core_resource_dict: dict, config) -> dict:
    
    # Step 1 - Generate Message Bundle and Message Header
    message_bundle = gen.generate_BSeR_ReferralMessageBundle()
    message_header = gen.generate_BSeR_ReferralMessageHeader(
        core_resource_dict["recipient_practitioner_role"],
        core_resource_dict["initiator_practitioner_role"],
        core_resource_dict["referral_task"]
        )
    message_bundle = insertMessageHeader(message_bundle, message_header)

    # Step 2 - Add core resources to bundle
    for key in core_resource_dict:
        message_bundle = addEntry(message_bundle, core_resource_dict[key])

    # Step 3 - Referral Request Document Bundle and Composition
    request_document_bundle = gen.generate_BSeR_ReferralRequestDocumentBundle()
    request_composition = gen.generate_BSeR_ReferralRequestComposition(
        core_resource_dict["patient"]["id"],
        core_resource_dict["initiator_practitioner_role"]["id"]
        )

    # Step 4 - Handle Use Case

    # Step 5 - Complete Supporting Info Bundle
    # TODO: Add Sections
    section_coding = { "system" : "http://hl7.org/fhir/us/bser/CodeSystem/bser", "code" : "RSRSI", "display" : "CompositionSectionReferralServiceRequestSupportingInformation"}
    supporting_info_section = generateCompositionSection(section_coding, []) # TODO: ADD RESOURCES
    request_composition = addSection(request_composition, supporting_info_section)
    # TODO: Add Composition to Bundle
    request_document_bundle = insertComposition(request_document_bundle, request_composition)
    # TODO: Add bundle to other bundle
    message_bundle = addEntry(message_bundle, request_document_bundle)

    return message_bundle

def buildFeedbackBundle(use_case, core_resource_dict: dict, config) -> dict:

    # Step 1 - Generate Document Bundle
    document_bundle = gen.generate_BSeR_ReferralFeedbackDocumentBundle()
    
    # Step 2 - Patient, RelatedPerson, Practitioner, and PractitionerRole
    patient = core_resource_dict["patient"]
    patient_id = patient["id"]
    related_person = core_resource_dict["related_person"]
    related_person_id = related_person["id"]

    initiator_practitioner = core_resource_dict["initiator_practitioner"]
    initiator_practitioner_role = core_resource_dict["initiator_practitioner_role"]
    recipient_practitioner = core_resource_dict["recipient_practitioner"]
    recipient_practitioner_role = core_resource_dict["recipient_practitioner_role"]
    recipient_practitioner_role_id = recipient_practitioner_role["id"]

    document_bundle = addEntries(document_bundle, [patient, related_person, recipient_practitioner, recipient_practitioner_role])
    
    # Step 3 - Generate Composition and Task Status resources
    composition = gen.generate_BSeR_ReferralFeedbackComposition(patient_id, recipient_practitioner_role_id, config["startDate"])

    activity_status = gen.generate_BSeR_ReferralActivityStatus(patient_id, config["startDate"], days)
    document_bundle = addEntry(document_bundle, activity_status)

    payor_organization = gen.generate_BSeR_Organization()
    payor_organization_id = payor_organization["id"]
    coverage = gen.generate_BSeR_Coverage(related_person_id, patient_id, payor_organization_id)
    referral_service_request = None # TODO: IMPLEMENT SERVICE REQUEST
    document_bundle = addEntries(document_bundle, [payor_organization, coverage, referral_service_request])

    # HANDLE USE CASE SPLIT HERE, BUILDING THE BUNDLES

    #BSeR_TobaccoUseCessationFeedbackObservation_1 = generate_BSeR_TobaccoUseCessationFeedbackObservation(1, patient_id, start_date, days)
    #BSeR_TobaccoUseCessationFeedbackObservation_2 = generate_BSeR_TobaccoUseCessationFeedbackObservation(2, patient_id, start_date, days)
    #BSeR_TobaccoUseCessationFeedbackObservation_3 = generate_BSeR_TobaccoUseCessationFeedbackObservation(3, patient_id, start_date, days)

    # Step ? - Add Resources to Composition
    rsrfs_section = generateCompositionSection({"system": CodeSystem_bser_codes, "code": "RSRFS"}, [activity_status], focus_reference=referral_service_request)
    composition = addSection(composition, rsrfs_section)

    document_bundle = insertComposition(document_bundle, composition)

    # Step ? - Add Resources to Bundle

    # FINAL - OUTPUT
    bundle = gen.generate_BSeR_TobaccoUseCessationReferralFeedbackSupportingInformation

    return document_bundle


def getPatientName(patient: dict) -> str:
    family = patient["name"][0]["family"]
    given = patient["name"][0]["given"][0]
    return f"{family}, {given}"


def openConfig() -> dict:
    file = open('config.json')
    file_contents = json.load(file)
    file.close()
    return file_contents


def writeFile(bundle_type, resource, patient_name: str):
    output_path = "output/"
    output_path_exists = os.path.isdir(output_path)
    if not output_path_exists:
        os.makedirs(output_path)
    
    file_name = f"{patient_name} ({bundle_type})- {resource['id']}"
    with open(f'{output_path}{file_name}.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))


if __name__ == "__main__":
    main()