import uuid, datetime

from fhir.resources.bundle import Bundle

def generate_BSeR_TobaccoUseCessationReferralFeedbackSupportingInformation() -> dict:
    bundle = {}
    bundle["resourceType"] = "Bundle"
    bundle["id"] = str(uuid.uuid4())
    bundle["meta"] = {}
    bundle["meta"]["profile"] = [ "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-TobaccoUseCessationReferralFeedbackSupportingInformation" ]
    bundle["type"] = "collection"
    bundle["entry"] = []

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")
    bundle["timestamp"] = str(timestamp)

    bundle = Bundle(**bundle).dict()
    return bundle


def addEntry(bundle, entry):
    #bundle = dict(bundle)
    fullUrl = f"{entry['resourceType']}/{entry['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = entry
    if not "entry" in bundle.keys():
        bundle["entry"] = []
    bundle["entry"].append(bundle_entry)
    return bundle


def addEntries(bundle, entries):
    for entry in entries:
        addEntry(bundle, entry)
    return bundle