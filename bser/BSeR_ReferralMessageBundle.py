from fhir.resources.bundle import Bundle
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralMessageBundle(Bundle):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralMessageBundle"
    # TODO: Implement