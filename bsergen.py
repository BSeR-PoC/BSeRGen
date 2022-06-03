from src.profiles.generate_BSeR_EducationLevel import generateBSeR_EducationLevel
from src.helpers.patient import generatePatient
import orjson, os, json, random
from fhirgenerator.helpers.helpers import default

def main():
    config = openConfig()
    record_count = config["recordCount"]
    start_date = config["startDate"]
    days = 1

    # Step 1 - Generate New Bundle
    ## TODO: Implement Bundle

    # Step 2 - Generate Patient (US Core Patient)
    patient = generatePatient(config["patient"], start_date) # The Patient helper class provides a means to manage BSER specific considerations of the US Core Patient.
    patient_id = patient["id"]
    patient_name = getPatientName(patient)

    # Step ? - TESTING
    BSeREducationLevel = generateBSeR_EducationLevel(patient_id, start_date, days)


    # FINAL - OUTPUT
    writeFile(BSeREducationLevel, patient_name)


def getPatientName(patient: dict) -> str:
    family = patient["name"][0]["family"]
    given = patient["name"][0]["given"][0]
    return f"{family}, {given}"


def openConfig() -> dict:
    file = open('config.json')
    file_contents = json.load(file)
    file.close()
    return file_contents


def writeFile(resource, patient_name: str):
    output_path = "output/"
    output_path_exists = os.path.isdir(output_path)
    if not output_path_exists:
        os.makedirs(output_path)
    
    file_name = f"{patient_name} - {resource['id']}"
    with open(f'{output_path}{file_name}.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))


if __name__ == "__main__":
    main()