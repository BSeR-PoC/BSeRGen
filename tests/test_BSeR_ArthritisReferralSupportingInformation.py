import orjson, uuid
from fhirgenerator.helpers.helpers import default
from pydantic import MissingError
from src.profiles.generate_BSeR_ArthritisReferralSupportingInformation import generate_BSeR_ArthritisReferralSupportingInformation
from bser.BSeR_ArthritisReferralSupportingInformation import BSeR_ArthritisReferralSupportingInformation
import pytest

def test_generate_BSeR_ArthritisReferralSupportingInformation_1():
    resource = generate_BSeR_ArthritisReferralSupportingInformation()
    
    with open(f'tests/output/test_BSeR_ArthritisReferralSupportingInformation_1.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "Bundle"
    assert resource["type"] == "collection"
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ArthritisReferralSupportingInformation" in resource["meta"]["profile"]
    assert isinstance(BSeR_ArthritisReferralSupportingInformation(**resource), BSeR_ArthritisReferralSupportingInformation)

def test_generate_BSeR_ArthritisReferralSupportingInformation_2_bad_Type():
    resource = generate_BSeR_ArthritisReferralSupportingInformation()
    
    resource["type"] = "document"

    with pytest.raises(ValueError):
        BSeR_ArthritisReferralSupportingInformation(**resource)

def test_generate_BSeR_ArthritisReferralSupportingInformation_3_no_profile_url():
    resource = generate_BSeR_ArthritisReferralSupportingInformation()
    resource["meta"]["profile"] = [""]

    with pytest.raises(ValueError):
        BSeR_ArthritisReferralSupportingInformation(**resource)