def insertComposition(bundle, composition):
    fullUrl = f"{composition['resourceType']}/{composition['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = composition
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