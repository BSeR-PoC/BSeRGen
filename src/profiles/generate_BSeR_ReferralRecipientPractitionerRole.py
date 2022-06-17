import uuid
from bser.BSeR_ReferralRecipientPractitionerRole import BSeR_ReferralRecipientPractitionerRole
from src.helpers.reference import createReference

def generate_BSeR_ReferralRecipientPractitionerRole(practitioner: dict = None,
                                                    organization: dict = None,
                                                    location: dict = None) -> dict:
    practitioner_role = {}
    practitioner_role["resourceType"] = "PractitionerRole"
    
    practitioner_role["id"] = str(uuid.uuid4())

    if practitioner is not None:
        practitioner_role["practitioner"] = createReference(resource=practitioner)
    if organization is not None:
        practitioner_role["organization"] = createReference(resource=organization)
    if location is not None:
        practitioner_role["location"] = [createReference(resource=location)]

    practitioner_role = BSeR_ReferralRecipientPractitionerRole(**practitioner_role).dict()
    return practitioner_role

