from fhir.resources.task import Task
import uuid
from datetime import datetime

from src.helpers.reference import createReference

def generate_BSeR_ReferralTask(service_request: dict) -> dict:
    task = {}
    task["resourceType"] = "Task"
    task["id"] = str(uuid.uuid4())
    task["meta"] = {}
    task["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralTask" ]
    
    task["status"] = "requested"
    task["businessStatus"] = {
        "coding" : [
            {
                "system" : "http://hl7.org/fhir/us/bser/CodeSystem/TaskBusinessStatusCS",
                "code" : "2.0",
                "display" : "Service Request Created"
            }
        ]
    }
    task["identifier"] = service_request["identifier"]
    task["intent"] = "order"
    task["focus"] = createReference(resource=service_request)
    task["authoredOn"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")

    task["requester"] = service_request["requester"]
    task["owner"] = service_request["performer"][0]

    task = Task(**task).dict()
    return task