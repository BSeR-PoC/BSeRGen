import orjson
from fhirgenerator.helpers.helpers import default
from fhir.resources.codeableconcept import CodeableConcept
from src.profiles.generate_BSeR_Organization import generate_BSeR_Organization

def test_generate_BSeR_Organization():
    resource = generate_BSeR_Organization()
    
    with open(f'tests/output/test_BSeR_Organization.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "Organization"
    assert isinstance(resource["meta"]["profile"], list)
    assert "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-Organization" in resource["meta"]["profile"]
    assert "type" in resource.keys()
    assert isinstance(resource["type"], list)
    for type in resource["type"]:
        assert isinstance(CodeableConcept(**type), CodeableConcept)

