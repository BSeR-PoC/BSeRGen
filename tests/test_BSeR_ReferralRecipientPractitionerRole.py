import orjson
from fhirgenerator.helpers.helpers import default
from fhir.resources.reference import Reference
from src.profiles.generate_BSeR_ReferralRecipientPractitionerRole import generate_BSeR_ReferralRecipientPractitionerRole
from bser.BSeR_ReferralRecipientPractitionerRole import BSeR_ReferralRecipientPractitionerRole
import uuid

'''
Test for both organization and practitioner reference included.
'''
def test_generate_BSeR_ReferralRecipientPractitionerRole_1():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    practitioner = {'resourceType': 'Practitioner', 'id': str(uuid.uuid4())}
    resource = generate_BSeR_ReferralRecipientPractitionerRole(practitioner, organization)
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole_1.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRecipientPractitionerRole" in resource["meta"]["profile"]
    assert "organization" in resource.keys()
    assert "practitioner" in resource.keys()
    assert "location" not in resource.keys()
    assert isinstance(Reference(**resource["organization"]), Reference)
    assert isinstance(Reference(**resource["practitioner"]), Reference)
    assert isinstance(BSeR_ReferralRecipientPractitionerRole(**resource), BSeR_ReferralRecipientPractitionerRole)

'''
Test for just organization included.
'''
def test_generate_BSeR_ReferralRecipientPractitionerRole_2():
    organization = {'resourceType': 'Organization', 'id': str(uuid.uuid4())}
    resource = generate_BSeR_ReferralRecipientPractitionerRole(organization=organization)
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole_2.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRecipientPractitionerRole" in resource["meta"]["profile"]
    assert "practitioner" not in resource.keys()
    assert "organization" in resource.keys()
    assert "location" not in resource.keys()
    assert isinstance(Reference(**resource["organization"]), Reference)
    assert isinstance(BSeR_ReferralRecipientPractitionerRole(**resource), BSeR_ReferralRecipientPractitionerRole)

'''
Test for no references provided.
'''
def test_generate_BSeR_ReferralRecipientPractitionerRole_3():
    resource = generate_BSeR_ReferralRecipientPractitionerRole()
    
    with open(f'tests/output/test_BSeR_ReferralInitiatorPractitionerRole_3.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "PractitionerRole"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRecipientPractitionerRole" in resource["meta"]["profile"]
    assert "practitioner" not in resource.keys()
    assert "organization" not in resource.keys()
    assert "location" not in resource.keys()
    assert isinstance(BSeR_ReferralRecipientPractitionerRole(**resource), BSeR_ReferralRecipientPractitionerRole)