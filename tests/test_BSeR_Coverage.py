import orjson, uuid
from fhirgenerator.helpers.helpers import default
from src.profiles.generate_BSeR_Coverage import generate_BSeR_Coverage

def test_generate_BSeR_Coverage():
    subscriber_id = str(uuid.uuid4())
    beneficiary_id = str(uuid.uuid4())
    payor_id = str(uuid.uuid4())

    resource = generate_BSeR_Coverage(subscriber_id, beneficiary_id, payor_id)
    
    with open(f'tests/output/test_BSeR_Coverage.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))

    assert resource["resourceType"] == "Coverage"
    assert resource["subscriber"]["reference"] == f"RelatedPerson/{subscriber_id}"
    assert resource["beneficiary"]["reference"] == f"Patient/{beneficiary_id}"

    assert isinstance(resource["payor"], list)
    assert {"reference": f"Organization/{payor_id}"} in resource["payor"]
