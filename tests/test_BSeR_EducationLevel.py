import orjson, uuid
from fhirgenerator.helpers.helpers import default
from src.profiles.generate_BSeR_EducationLevel import generateBSeR_EducationLevel

def test_generateBSeR_EducationLevel():
    patient_id = uuid.uuid4()
    start_date = '01-01-2022'
    days = 1

    resource = generateBSeR_EducationLevel(patient_id, start_date, days)
    
    with open(f'tests/output/test_BSeR_EducationLevel.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
