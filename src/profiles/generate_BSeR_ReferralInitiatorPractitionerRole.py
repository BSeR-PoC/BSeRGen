import uuid
from fhir.resources.practitionerrole import PractitionerRole
from fhir.resources.reference import Reference

def generate_BSeR_ReferralInitiatorPractitionerRole(practitioner_id: str = None,
                                                    organization_id: str = None,
                                                    location_id: str = None) -> dict:
    practitioner_role = {}
    practitioner_role["resourceType"] = "PractitionerRole"
    
    practitioner_role["id"] = str(uuid.uuid4())
    practitioner_role["meta"] = {}
    practitioner_role["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-ReferralInitiatorPractitionerRole" ]
    
    if practitioner_id is not None:
        practitioner_reference = { "reference": f"Practitioner/{practitioner_id}"}
        practitioner_reference = Reference(**practitioner_reference).dict()
        practitioner_role["practitioner"] = practitioner_reference

    # TODO: Implement Organization and Location

    practitioner_role = PractitionerRole(**practitioner_role).dict()
    return practitioner_role

