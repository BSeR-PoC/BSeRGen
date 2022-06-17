from venv import create
from fhir.resources.servicerequest import ServiceRequest
from fhir.resources.identifier import Identifier
import uuid
from src.helpers.reference import createReference
from fhir.resources.codeableconcept import CodeableConcept
from src.constants import use_case_arthritis, use_case_diabetes, use_case_ecn, use_case_hypertension, use_case_obesity, use_case_tobacco
from dateutil import parser

def generate_BSeR_ReferralServiceRequest(use_case, subject: dict, requester: dict, performer: dict, start_date) -> dict:
    service_request = {}
    service_request["resourceType"] = "ServiceRequest"
    service_request["id"] = str(uuid.uuid4())
    service_request["meta"] = {}
    service_request["meta"]["profile"] = ["http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralServiceRequest"]
    
    service_request["identifier"] = [__generateInitiatorServiceRequestIdentifier()]
    service_request["status"] = "active"
    service_request["intent"] = "order"

    service_request["subject"] = createReference(resource=subject)
    service_request["code"] = __setUseCase(use_case)

    service_request["requester"] = createReference(resource=requester)
    service_request["performer"] = [createReference(resource=performer)]
    service_request["occurrenceDateTime"] = parser.parse(start_date)

    service_request = ServiceRequest(**service_request).dict()

    return service_request


def __generateInitiatorServiceRequestIdentifier() -> dict:
    identifier = {
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "PLAC"
          }
        ]
      },
      "value" : str(uuid.uuid4())
    }

    identifier = Identifier(**identifier).dict()
    return identifier


def __setUseCase(use_case) -> dict:
    codeable_concept = { "text": use_case}
    codeable_concept = CodeableConcept(**codeable_concept).dict()
    return codeable_concept