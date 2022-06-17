import uuid
from fhirgenerator.helpers.helpers import makeRandomDate
from fhir.resources.composition import Composition, CompositionSection
from src.cannonicalUrls import loinc
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from datetime import datetime

def generate_BSeR_ReferralFeedbackComposition(patient_id: str, practitioner_role_id: str, start_date: str) -> dict:
    composition = {}
    composition["resourceType"] = "Composition"
    
    composition["id"] = str(uuid.uuid4())
    composition["meta"] = {}
    composition["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralFeedbackComposition" ]
    composition["status"] = "final"
    
    composition["subject"] = { "reference": f"Patient/{patient_id}"}
    composition["author"] = [{ "reference": f"PractitionerRole/{practitioner_role_id}"}]
    composition["title"] = "BSeR Referral Feedback Composition"
    
    composition["type"] = {}
    composition["type"]["coding"] = []
    composition["type"]["coding"].append({ "system": loinc, "code": "57133-1", "display": "Referral note"})

    composition["date"] = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00"))

    composition = Composition(**composition).dict()
    return composition


def generateCompositionSection(coding: Coding, resources: list, focus_reference: Reference = None):
    section = {}
    section["code"] = { "coding": [coding] }
    if resources:
        section["entry"] = []
        for resource in resources:
            section["entry"].append({ "reference": f"{resource['resourceType']}/{resource['id']}"})
    else:
        section["text"] = { "status": "empty", "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Records Unavailable</div>" }
        section["emptyReason"] = {
            "coding": [
                {
                    "system" : "http://terminology.hl7.org/CodeSystem/list-empty-reason",
                    "code" : "unavailable",
                    "display" : "Unavailable"
                }
            ]
        }

    if focus_reference is not None:
        section["focus"] = focus_reference

    section = CompositionSection(**section).dict()
    return section

def addSection(composition, section) -> dict:
    if not "section" in composition.keys():
        composition["section"] = []
    composition["section"].append(section)
    return composition