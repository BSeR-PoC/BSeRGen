import orjson
from fhirgenerator.helpers.helpers import default
from fhir.resources.codeableconcept import CodeableConcept
from src.profiles.generate_BSeR_ReferralServiceRequest import generate_BSeR_ReferralServiceRequest
from src.constants import use_case_tobacco
import uuid

def test_generate_BSeR_ReferralServiceRequest():
    subject = { "resourceType": "Patient", "id": str(uuid.uuid4())}
    requester = { "resourceType": "PractitionerRole", "id": str(uuid.uuid4())}
    performer = { "resourceType": "PractitionerRole", "id": str(uuid.uuid4())}
    start_date = "01-01-2022"

    resource = generate_BSeR_ReferralServiceRequest(use_case_tobacco, subject, requester, performer, start_date)
    
    with open(f'tests/output/test_BSeR_ReferralServiceRequest.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "ServiceRequest"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralServiceRequest" in resource["meta"]["profile"]

