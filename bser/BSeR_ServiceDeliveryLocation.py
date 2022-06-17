from fhir.resources.location import Location
import typing
from fhir.resources import fhirtypes
from pydantic import Field, validator

class BSeR_ServiceDeliveryLocation(Location):
    profile_url = "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ServiceDeliveryLocation"
    # TODO: Implement