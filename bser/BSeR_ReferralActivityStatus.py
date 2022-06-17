from fhir.resources.observation import Observation
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralActivityStatus(Observation):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralActivityStatus"
    # TODO: Implement