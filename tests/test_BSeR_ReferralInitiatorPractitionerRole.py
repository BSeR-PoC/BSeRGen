import orjson
from fhirgenerator.helpers.helpers import default
from fhir.resources.reference import Reference
from src.profiles.generate_BSeR_ReferralInitiatorPractitionerRole import generate_BSeR_ReferralInitiatorPractitionerRole
from bser.BSeR_ReferralInitiatorPractitionerRole import BSeR_ReferralInitiatorPractitionerRole
import uuid
import pytest

def test_generate_BSeR_ReferralInitiatorPractitionerRole_1():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    practitioner = {'resourceType': 'Practitioner', 'id': str(uuid.uuid4())}
    resource = generate_BSeR_ReferralInitiatorPractitionerRole(practitioner, organization)
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole_1.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralInitiatorPractitionerRole" in resource["meta"]["profile"]
    assert "organization" in resource.keys()
    assert "practitioner" in resource.keys()
    assert "location" not in resource.keys()
    assert isinstance(Reference(**resource["organization"]), Reference)
    assert isinstance(Reference(**resource["practitioner"]), Reference)
    assert isinstance(BSeR_ReferralInitiatorPractitionerRole(**resource), BSeR_ReferralInitiatorPractitionerRole)

def test_generate_BSeR_ReferralInitiatorPractitionerRole_2():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    practitioner = {'resourceType': 'Practitioner', 'id': str(uuid.uuid4())}
    location = {'resourceType': 'Location', 'id': str(uuid.uuid4())}

    resource = generate_BSeR_ReferralInitiatorPractitionerRole(practitioner, organization, location)
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole_1.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralInitiatorPractitionerRole" in resource["meta"]["profile"]
    assert "organization" in resource.keys()
    assert "practitioner" in resource.keys()
    assert "location" in resource.keys()
    assert isinstance(Reference(**resource["organization"]), Reference)
    assert isinstance(Reference(**resource["practitioner"]), Reference)
    assert isinstance(Reference(**resource["location"][0]), Reference)
    assert isinstance(BSeR_ReferralInitiatorPractitionerRole(**resource), BSeR_ReferralInitiatorPractitionerRole)


def test_generate_BSeR_ReferralInitiatorPractitionerRole_Exception_1():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    practitioner = {'resourceType': 'Practitioner', 'id': str(uuid.uuid4())}
    location = "String is a Bad Type for location"
    
    with pytest.raises(TypeError):
        generate_BSeR_ReferralInitiatorPractitionerRole(practitioner, organization, location)
    