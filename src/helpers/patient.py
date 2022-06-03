from fhirgenerator.resources.uscore_r4.usCorePatient import generateUSCorePatient
import random

def generatePatient(config: dict, start_date: str):
    gender = (random.choices(["M", "F", "O", "U"], weights=tuple(config["genderMFOU"])))[0]
    patient_config = {
        "age": random.randint(config["ageMin"], config["ageMax"]),
        "gender": gender,
        "startDate": start_date
    }
    resource = generateUSCorePatient(patient_config)
    return resource