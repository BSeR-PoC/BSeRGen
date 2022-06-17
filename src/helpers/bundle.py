from fhir.resources.composition import Composition
from fhir.resources.messageheader import MessageHeader

def insertComposition(bundle, composition):
    composition = Composition(**composition).dict() # Confirm valid Composition
    if bundle["type"] != "document":
        raise Exception("Bundle is not type 'document'.")
    fullUrl = f"{composition['resourceType']}/{composition['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = composition
    if not "entry" in bundle.keys():
        bundle["entry"] = []
    bundle["entry"].insert(0, bundle_entry)
    return bundle


def insertMessageHeader(bundle, message_header):
    message_header = MessageHeader(**message_header).dict() # Confirm valid Composition
    if bundle["type"] != "message":
        raise Exception("Bundle is not type 'message'.")
    fullUrl = f"{message_header['resourceType']}/{message_header['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = message_header
    if not "entry" in bundle.keys():
        bundle["entry"] = []
    bundle["entry"].insert(0, bundle_entry)
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