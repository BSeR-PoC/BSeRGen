from src.helpers.relatedperson import generateRelatedPersonFromPatient
from src.helpers.patient import generatePatient

import orjson
from fhirgenerator.helpers.helpers import default


def test_relatedperson():
    patient_config = { "ageMin": 18, "ageMax": 76, "genderMFOU": [ 47, 47, 1, 5]}
    start_date = '01-01-2022'

    patient = generatePatient(patient_config, start_date)
    resource = generateRelatedPersonFromPatient(patient)

    with open(f'tests/output/test_relatedperson.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))