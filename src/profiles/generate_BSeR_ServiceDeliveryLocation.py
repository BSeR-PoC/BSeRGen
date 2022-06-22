import uuid
from src.helpers.reference import createReference
from bser.BSeR_ServiceDeliveryLocation import BSeR_ServiceDeliveryLocation
from fhirgenerator.resources.r4.location import generateLocation

def generate_BSeR_ServiceDeliveryLocation() -> dict:

    location = generateLocation()

    location = BSeR_ServiceDeliveryLocation(**location).dict()
    return location

