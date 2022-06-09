from fhir.resources.organization import Organization
from fhirgenerator.resources.uscore_r4.usCoreOrganization import generateUSCoreOrganization

def generate_BSeR_Organization() -> dict:
    resource = generateUSCoreOrganization()
    resource['meta'] = {'profile': ['http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-Organization']}
    resource['type'] = [
        {
        "coding" : [
            {
            "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
            "code" : "prov",
            "display" : "Healthcare Provider"
            }
        ]
        }
    ]
    resource = Organization(**resource).dict()
    return resource
