import uuid
from datetime import datetime
from bser.BSeR_ArthritisReferralSupportingInformation import BSeR_ArthritisReferralSupportingInformation

def generate_BSeR_ArthritisReferralSupportingInformation() -> dict:
    bundle = {}
    bundle["resourceType"] = "Bundle"
    bundle["id"] = str(uuid.uuid4())
    bundle["meta"] = {}
    bundle["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ArthritisReferralSupportingInformation" ]
    bundle["type"] = "collection"
    bundle["entry"] = []

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")
    bundle["timestamp"] = str(timestamp)

    bundle = BSeR_ArthritisReferralSupportingInformation(**bundle).dict()
    return bundle


