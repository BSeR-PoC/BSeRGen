from src.helpers.bundle import insertComposition
from src.profiles.generate_BSeR_ReferralActivityStatus import generate_BSeR_ReferralActivityStatus
from src.profiles.generate_BSeR_ReferralFeedbackDocumentBundle import generate_BSeR_ReferralFeedbackDocumentBundle
from src.profiles.generate_BSeR_TobaccoUseCessationReferralFeedbackSupportingInformation import addEntries, addEntry, generate_BSeR_TobaccoUseCessationReferralFeedbackSupportingInformation
from src.profiles.generate_BSeR_TobaccoUseCessationFeedbackObservation import generate_BSeR_TobaccoUseCessationFeedbackObservation
from src.profiles.generate_BSeR_EducationLevel import generate_BSeR_EducationLevel
from src.profiles.generate_BSeR_ReferralFeedbackComposition import generate_BSeR_ReferralFeedbackComposition, generateCompositionSection, addSection
from src.profiles.generate_BSeR_ReferralRecipientPractitionerRole import generate_BSeR_ReferralRecipientPractitionerRole
from src.profiles.generate_BSeR_Coverage import generate_BSeR_Coverage
from src.cannonicalUrls import CodeSystem_bser_codes
from src.helpers.patient import generatePatient
from src.helpers.relatedperson import generateRelatedPersonFromPatient
import orjson, os, json, random, argparse, inquirer
from fhirgenerator.helpers.helpers import default
from src.helpers.bser_practitioner import get_BSeR_Practitioner

bundle_type_referral = "Referral"
bundle_type_feedback = "Feedback"
bundle_type_both = "Both Referral and Feedback"
use_case_arthritis = "Arthritis"
use_case_diabetes = "Diabetes Prevention"
use_case_ecn = "Early Childhood Nutrition"
use_case_hypertension = "Hypertension"
use_case_obesity = "Obesity"
use_case_tobacco = "Tobacco Use Cessation"

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

    core_resource_dict = buildCoreResources(config)
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


def buildCoreResources(config):
    core_resource_dict = {}
    core_resource_dict["patient"] = generatePatient(config["patient"], config["startDate"]) # The Patient helper class provides a means to manage BSER specific considerations of the US Core Patient.
    core_resource_dict["practitioner"] = get_BSeR_Practitioner()
    core_resource_dict["related_person"] = generateRelatedPersonFromPatient(core_resource_dict["patient"])
    core_resource_dict["practitioner_role"] = generate_BSeR_ReferralRecipientPractitionerRole(core_resource_dict["practitioner"]["id"])

    return core_resource_dict


# TODO: IMPLEMENT REFERRAL BUNDLE
def buildReferralBundle(use_case, core_resource_dict: dict, config) -> dict:
    return None

def buildFeedbackBundle(use_case, core_resource_dict: dict, config) -> dict:
    days = 1

    # Step 1 - Generate Document Bundle
    document_bundle = generate_BSeR_ReferralFeedbackDocumentBundle()
    
    # Step 2 - Patient, RelatedPerson, Practitioner, and PractitionerRole
    patient = core_resource_dict["patient"]
    patient_id = patient["id"]
    related_person = core_resource_dict["related_person"]
    related_person_id = related_person["id"]

    practitioner = core_resource_dict["practitioner"]
    practitioner_role = core_resource_dict["practitioner_role"]
    practitioner_role_id = practitioner_role["id"]

    document_bundle = addEntries(document_bundle, [patient, related_person, practitioner, practitioner_role])
    
    # Step 3 - Generate Composition and Task Status resources
    composition = generate_BSeR_ReferralFeedbackComposition(patient_id, practitioner_role_id, config["startDate"])
    document_bundle = insertComposition(document_bundle, composition)

    activity_status = generate_BSeR_ReferralActivityStatus(patient_id, config["startDate"], days)
    document_bundle = addEntry(document_bundle, activity_status)

    service_request = None # TODO: IMPLEMENT SERVICE REQUEST
    payor_organization = None # TODO: IMPLEMENT BSeR ORGANIZATION
    payor_organization_id = "payor_id_placeholder" #payor_organization["id"]
    coverage = generate_BSeR_Coverage(related_person_id, patient_id, payor_organization_id)


    # HANDLE USE CASE SPLIT HERE, BUILDING THE BUNDLES

    #BSeR_TobaccoUseCessationFeedbackObservation_1 = generate_BSeR_TobaccoUseCessationFeedbackObservation(1, patient_id, start_date, days)
    #BSeR_TobaccoUseCessationFeedbackObservation_2 = generate_BSeR_TobaccoUseCessationFeedbackObservation(2, patient_id, start_date, days)
    #BSeR_TobaccoUseCessationFeedbackObservation_3 = generate_BSeR_TobaccoUseCessationFeedbackObservation(3, patient_id, start_date, days)

    # Step ? - Add Resources to Composition
    rsrfs_section = generateCompositionSection({"system": CodeSystem_bser_codes, "code": "RSRFS"}, [activity_status], focus_reference=service_request)
    composition = addSection(composition, rsrfs_section)
    # Step ? - Add Resources to Bundle

    # FINAL - OUTPUT
    bundle = generate_BSeR_TobaccoUseCessationReferralFeedbackSupportingInformation

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