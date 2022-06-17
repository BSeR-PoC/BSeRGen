import orjson
from fhirgenerator.helpers.helpers import default
from fhir.resources.reference import Reference
from src.profiles.generate_BSeR_ReferralInitiatorPractitionerRole import generate_BSeR_ReferralInitiatorPractitionerRole
import uuid

def test_generate_BSeR_ReferralInitiatorPractitionerRole():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    practitioner = {'resourceType': 'Practitioner', 'id': str(uuid.uuid4())}
    resource = generate_BSeR_ReferralInitiatorPractitionerRole(practitioner, organization)
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralInitiatorPractitionerRole" in resource["meta"]["profile"]
    assert "organization" in resource.keys()
    # assert isinstance(Reference(**resource["organization"]), Reference)
    # assert isinstance(Reference(**resource["practitioner"]), Reference)


