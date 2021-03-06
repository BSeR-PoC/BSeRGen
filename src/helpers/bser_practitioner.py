from fhir.resources.practitioner import Practitioner

def get_BSeR_Initiator_Practitioner() -> dict:
    practitioner = {
        "resourceType" : "Practitioner",
        "id" : "bser-practitioner-intiator",
        "meta" : {
            "profile" : [
            "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-Practitioner"
            ]
        },
        "identifier" : [
            {
            "system" : "http://hl7.org.fhir/sid/us-npi",
            "value" : "9987654321"
            }
        ],
        "name" : [
            {
            "family" : "Initiator",
            "given" : [
                "BSeR"
            ],
            "prefix" : [
                "Dr"
            ]
            }
        ]
        }
    
    practitioner = Practitioner(**practitioner).dict()
    return practitioner


def get_BSeR_Recipient_Practitioner() -> dict:
    practitioner = {
        "resourceType" : "Practitioner",
        "id" : "bser-practitioner-recipient",
        "meta" : {
            "profile" : [
            "http://hl7.org/fhir/us/bser/StructureDefinition/BSeR-Practitioner"
            ]
        },
        "identifier" : [
            {
            "system" : "http://hl7.org.fhir/sid/us-npi",
            "value" : "9912345678"
            }
        ],
        "name" : [
            {
            "family" : "Recipient",
            "given" : [
                "BSeR"
            ],
            "prefix" : [
                "Dr"
            ]
            }
        ]
        }
    
    practitioner = Practitioner(**practitioner).dict()
    return practitioner

'''
{
  "resourceType": "Practitioner",
  "id": "practitioner-bser-hailey-eight",



  "telecom": [
    {
      "system": "email",
      "value": "hailey.eight@example.com"
    }
  ],
  "address": [
    {
      "line": [
        "BMass Doctors",
        "2100 North Ave"
      ],
      "city": "Burlington",
      "state": "MA",
      "postalCode": "02368",
      "country": "US"
    }
  ]
}

'''