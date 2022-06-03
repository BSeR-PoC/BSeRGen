from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation

def generateBSeR_EducationLevel(patient_id, start_date, days):
    resource_detail = {}
    resource_detail["codes"] = [{'code': '80913-7', 'system': 'http://loinc.org'}]
    resource_detail["profile"] = ["http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-EducationLevel"]
    resource_detail["enumSetList"] = [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'ASSOC', 'display': "Associate's or technical degree complete"}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'BD', 'display': 'College or baccalaureate degree complete'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'ELEM', 'display': 'Elementary School'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'GD', 'display': 'Graduate or professional Degree complete'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'HS', 'display': 'High School or secondary school degree complete'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'PB', 'display': 'Some post-baccalaureate education'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'POSTG', 'display': 'Doctoral or post graduate education'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'SCOL', 'display': 'Some College education'}]}, {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-EducationLevel', 'code': 'SEC', 'display': 'Some secondary or high school education'}]}]
    observation = generateObservation(resource_detail, patient_id, start_date, days)

    observation = Observation(**observation).dict()
    return observation
