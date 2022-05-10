up_ap = {
  "tender": {
    "title": "AP tender title",
    "description": "AP tender description",
    "procurementMethodRationale": "AP PMR",
    "tenderPeriod": {
      "startDate": "2021-05-01T16:00:00Z"
    },
    "lots": [
      {
        "id": "1",
        "internalId": "lot 1",
        "title": "first lot in AP",
        "description": "description of first lot in AP",
        "placeOfPerformance": {
          "address": {
            "streetAddress": "Peremogi",
            "postalCode": "10040",
            "addressDetails": {
              "country": {
                "id": "MD"
              },
              "region": {
                "id": "7800000"
              },
              "locality": {
                "id": "7811000",
                "scheme": "CUATM",
                "description": "string"
              }
            }
          }
        }
      }
    ],
    "items": [
      {
        "id": "1",
        "internalId": "item 1",
        "classification": {
          "id": "37411110-6"
        },
        "additionalClassifications": [
          {
            "id": "QA04-7"
          }
        ],
        "quantity": 100,
        "unit": {
          "id": "120"
        },
        "description": "description of first item in AP",
        "relatedLot": "1",
        "deliveryAddress": {
          "streetAddress": "Franka",
          "postalCode": "20010",
          "addressDetails": {
            "country": {
              "id": "MD"
            },
            "region": {
              "id": "7800000"
            },
            "locality": {
              "id": "7812000",
              "description": "string",
              "scheme": "CUATM"
            }
          }
        }
      }
    ],
    "documents": [
      {
        "documentType": "procurementPlan",
        "id": "377ca816-c7c9-4d38-bd83-c70f99a113ab-1652163991404",
        "title": "title of AP document",
        "description": "description of AP document",
        "relatedLots": [
          "1"
        ]
      }
    ],
    "!value": {
      "currency": "MDL"
    }
  }
}
