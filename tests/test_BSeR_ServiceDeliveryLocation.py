import orjson
from fhirgenerator.helpers.helpers import default
from src.profiles.generate_BSeR_ServiceDeliveryLocation import generate_BSeR_ServiceDeliveryLocation
from bser.BSeR_ServiceDeliveryLocation import BSeR_ServiceDeliveryLocation
import pytest

def test_generate_BSeR_ServiceDeliveryLocation_1():
    resource = generate_BSeR_ServiceDeliveryLocation()
    
    with open(f'tests/output/test_BSeR_ServiceDeliveryLocation_1.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "Location"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ServiceDeliveryLocation" in resource["meta"]["profile"]
    assert "telecom" in resource.keys()
    assert "system" in resource["telecom"][0].keys()
    assert "value" in resource["telecom"][0].keys()
    assert "name" in resource.keys()
    assert isinstance(BSeR_ServiceDeliveryLocation(**resource), BSeR_ServiceDeliveryLocation)

def test_generate_BSeR_ServiceDeliveryLocation_2_missing_system_error():
    resource = generate_BSeR_ServiceDeliveryLocation()
    del resource["telecom"][0]["system"]

    with pytest.raises(ValueError):
        BSeR_ServiceDeliveryLocation(**resource)

def test_generate_BSeR_ServiceDeliveryLocation_3_missing_value_error():
    resource = generate_BSeR_ServiceDeliveryLocation()
    del resource["telecom"][0]["value"]

    with pytest.raises(ValueError):
        BSeR_ServiceDeliveryLocation(**resource)