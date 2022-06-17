from fhir.resources.servicerequest import ServiceRequest
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralServiceRequest(ServiceRequest):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralServiceRequest"
    # TODO: Implement