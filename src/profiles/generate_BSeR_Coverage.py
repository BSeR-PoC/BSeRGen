from fhir.resources.coverage import Coverage
import uuid

def generate_BSeR_Coverage(subscriber_id: str, beneficiary_id: str, payor_id: str) -> dict:
    coverage = {}
    coverage["resourceType"] = "Coverage"

    coverage["id"] = str(uuid.uuid4())
    coverage["meta"] = {}
    coverage["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-Coverage" ]
    coverage["status"] = "active"
    coverage["type"] = { "coding": [{ "system" : "http://terminology.hl7.org/CodeSystem/v3-ActCode", "code" : "EHCPOL", "display" : "extended healthcare" }]}

    coverage["subscriber"] = { "reference": f"RelatedPerson/{subscriber_id}"}
    coverage["beneficiary"] = { "reference": f"Patient/{beneficiary_id}"}
    coverage["relationship"] = { "coding" : [{"system" : "http://terminology.hl7.org/CodeSystem/subscriber-relationship", "code" : "self"}]}

    coverage["payor"] = [{ "reference": f"Organization/{payor_id}"}]

    coverage = Coverage(**coverage).dict()
    return coverage