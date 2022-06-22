import uuid
from src.helpers.reference import createReference
from bser.BSeR_ReferralInitiatorPractitionerRole import BSeR_ReferralInitiatorPractitionerRole

practitioner_type_error = "Practitioner must be a dict (representing a FHIR Practitioner resource)."
organization_type_error = "Organization must be a dict (representing a FHIR Practitioner resource)."
location_type_error = "Location must be either a dict (representing a FHIR Location resource) or a list of dicts."

def generate_BSeR_ReferralInitiatorPractitionerRole(practitioner: dict,
                                                    organization: dict,
                                                    location: dict | list = None) -> dict:
    practitioner_role = {}
    practitioner_role["resourceType"] = "PractitionerRole"
    practitioner_role["id"] = str(uuid.uuid4())

    if isinstance(practitioner, dict):
        practitioner_role["practitioner"] = createReference(resource=practitioner)
    else:
        raise TypeError(practitioner_type_error)
    
    if isinstance(organization, dict):
        practitioner_role["organization"] = createReference(resource=organization)
    else:
        raise TypeError(organization_type_error)
    
    if location is not None:
        if isinstance(location, dict):
            practitioner_role["location"] = [createReference(resource=location)]
        elif isinstance(location, list):
            practitioner_role["location"] = []
            for item in location:
                if isinstance(item, dict):
                    practitioner_role["location"].append(createReference(resource=item))
                else:
                    raise TypeError(location_type_error)
        else:
            raise TypeError(location_type_error)

    practitioner_role = BSeR_ReferralInitiatorPractitionerRole(**practitioner_role).dict()
    return practitioner_role

