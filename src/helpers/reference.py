from fhir.resources.reference import Reference

def createReference(resource_type: str = None, resource_id: str = None, resource: dict = None) -> dict:
    if resource is not None:
        resource_type = resource["resourceType"]
        resource_id = resource["id"]
    
    reference = {}
    reference = {"reference": f"{resource_type}/{resource_id}"}
    
    reference = Reference(**reference).dict()
    return reference