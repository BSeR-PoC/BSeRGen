from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.composition import CompositionSection

def generateCompositionSection(coding: Coding, resources: list, focus_reference: Reference = None):
    section = {}
    section["code"] = { "coding": [coding] }
    if resources:
        section["entry"] = []
        for resource in resources:
            section["entry"].append({ "reference": f"{resource['resourceType']}/{resource['id']}"})
    else:
        section["text"] = { "status": "empty", "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\">Records Unavailable</div>" }
        section["emptyReason"] = {
            "coding": [
                {
                    "system" : "http://terminology.hl7.org/CodeSystem/list-empty-reason",
                    "code" : "unavailable",
                    "display" : "Unavailable"
                }
            ]
        }

    if focus_reference is not None:
        section["focus"] = focus_reference

    section = CompositionSection(**section).dict()
    return section

def addSection(composition, section) -> dict:
    if not "section" in composition.keys():
        composition["section"] = []
    composition["section"].append(section)
    return composition