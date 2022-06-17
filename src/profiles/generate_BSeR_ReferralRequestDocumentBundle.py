import uuid
from datetime import datetime

from fhir.resources.bundle import Bundle

def generate_BSeR_ReferralRequestDocumentBundle() -> dict:
    bundle = {}
    bundle["resourceType"] = "Bundle"
    bundle["id"] = str(uuid.uuid4())
    bundle["meta"] = {}
    bundle["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRequestDocumentBundle" ]
    bundle["type"] = "document"
    bundle["entry"] = []

    bundle["timestamp"] = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00"))

    bundle = Bundle(**bundle).dict()
    return bundle


