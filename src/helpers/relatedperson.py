from fhir.resources.relatedperson import RelatedPerson
import uuid
from src.helpers.reference import createReference


def generateRelatedPersonFromPatient(patient) -> dict:
    related_person = {}
    related_person["resourceType"] = "RelatedPerson"
    related_person["id"] = str(uuid.uuid4())
    related_person["patient"] = createReference(resource=patient)
    related_person["name"] = patient["name"]

    related_person = RelatedPerson(**related_person).dict()

    return related_person
