from fhir.resources.task import Task
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralTask(Task):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralTask"
    # TODO: Implement