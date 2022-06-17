from email import message
from fhir.resources.messageheader import MessageHeader
import uuid
from src.helpers.reference import createReference

def generate_BSeR_ReferralMessageHeader(recipient: dict, sender: dict, task: dict, destination_endpoint = "http://fakedestinationurl.org/fhir", source_endpoint = "http://fakesourceurl.org/fhir") -> dict:
    message_header = {}
    message_header["resourceType"] = "MessageHeader"
    message_header["id"] = str(uuid.uuid4())
    message_header["meta"] = {}
    message_header["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralMessageHeader" ]
    
    message_header["eventCoding"] = { "system" : "http://terminology.hl7.org/CodeSystem/v2-0003", "code" : "I12", "display" : "REF/RRI - Patient referral"}
    message_header["destination"] = [
        {
            "endpoint": destination_endpoint,
            "receiver": createReference(resource = recipient)
        }
    ]
    message_header["source"] = {
        "endpoint": source_endpoint
    }
    message_header["sender"] = createReference(resource = sender)
    message_header["focus"] = [createReference(resource = task)]

    message_header = MessageHeader(**message_header).dict()
    return message_header