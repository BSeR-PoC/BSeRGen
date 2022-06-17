import uuid
from fhirgenerator.helpers.helpers import makeRandomDate
from fhir.resources.composition import Composition, CompositionSection
from src.cannonicalUrls import loinc
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from datetime import datetime


def generate_BSeR_ReferralRequestComposition(patient_id: str, practitioner_role_id: str) -> dict:
    composition = {}
    composition["resourceType"] = "Composition"
    
    composition["id"] = str(uuid.uuid4())
    composition["meta"] = {}
    composition["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRequestComposition" ]
    composition["status"] = "final"
    
    composition["subject"] = { "reference": f"Patient/{patient_id}"}
    composition["author"] = [{ "reference": f"PractitionerRole/{practitioner_role_id}"}]
    composition["title"] = "BSeR Referral Request Composition"
    
    composition["type"] = {}
    composition["type"]["coding"] = []
    composition["type"]["coding"].append({ "system": loinc, "code": "57133-1", "display": "Referral note"})

    composition["date"] = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00"))

    composition = Composition(**composition).dict()
    return composition