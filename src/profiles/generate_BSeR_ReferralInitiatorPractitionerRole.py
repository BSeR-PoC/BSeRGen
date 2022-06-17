import uuid
from src.helpers.reference import createReference
from bser.BSeR_ReferralInitiatorPractitionerRole import BSeR_ReferralInitiatorPractitionerRole

def generate_BSeR_ReferralInitiatorPractitionerRole(practitioner: dict,
                                                    organization: dict,
                                                    location: dict = None) -> dict:
    practitioner_role = {}
    practitioner_role["resourceType"] = "PractitionerRole"
    
    practitioner_role["id"] = str(uuid.uuid4())

    practitioner_role["practitioner"] = createReference(resource=practitioner)
    practitioner_role["organization"] = createReference(resource=organization)
    if location is not None:
        practitioner_role["location"] = [createReference(resource=location)]

    practitioner_role = BSeR_ReferralInitiatorPractitionerRole(**practitioner_role).dict()
    return practitioner_role

