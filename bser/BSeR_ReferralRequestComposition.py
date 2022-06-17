from fhir.resources.composition import Composition
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ReferralRequestComposition(Composition):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralRequestComposition"
    # TODO: Implement