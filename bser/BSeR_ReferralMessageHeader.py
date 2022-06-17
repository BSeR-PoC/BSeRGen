from fhir.resources.messageheader import MessageHeader
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralMessageHeader(MessageHeader):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralMessageHeader"
    # TODO: Implement