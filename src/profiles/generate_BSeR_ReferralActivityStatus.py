from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation
from src.cannonicalUrls import snomed
from enum import Enum


def generate_BSeR_ReferralActivityStatus(patient_id, start_date, days):
    resource_detail = {}
    resource_detail["codes"] = [{'code': '385641008', 'system': snomed, 'display': 'Action status'}]
    resource_detail["profile"] = ["http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralActivityStatus"]
    resource_detail["enumSetList"] = ["Referral accepted"]
    observation = generateObservation(resource_detail, patient_id, start_date, days)

    observation = Observation(**observation).dict()
    return observation