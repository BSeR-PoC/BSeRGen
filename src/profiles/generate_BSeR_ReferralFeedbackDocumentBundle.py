import uuid
from datetime import datetime

from fhir.resources.bundle import Bundle

def generate_BSeR_ReferralFeedbackDocumentBundle() -> dict:
    bundle = {}
    bundle["resourceType"] = "Bundle"
    bundle["id"] = str(uuid.uuid4())
    bundle["meta"] = {}
    bundle["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralFeedbackDocumentBundle" ]
    bundle["type"] = "document"
    bundle["entry"] = []

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")
    bundle["timestamp"] = str(timestamp)

    bundle = Bundle(**bundle).dict()
    return bundle


