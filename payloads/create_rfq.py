create_rfq_data = {
  "tender": {
    "lots": [
      {
        "id": "1",
        "internalId": "l-1",
        "title": "first lot in RFQ",
        "description": "description of first lot in RFQ",
        "value": {
          "currency": "MDL"
        },
        "contractPeriod": {
          "startDate": "2021-08-29T09:28:18Z",
          "endDate": "2021-08-31T09:28:18Z"
        },
        "placeOfPerformance": {
          "description": "description of pOP first RFQ lot",
          "address": {
            "streetAddress": "streetAddress of first lot in RFQ",
            "postalCode": "postalCode of first lot in RFQ",
            "addressDetails": {
              "country": {
                "id": "MD",
                "description": "string coun",
                "scheme": "iso-alpha2"
              },
              "region": {
                "id": "2900000",
                "description": "string reg",
                "scheme": "CUATM"
              },
              "locality": {
                "id": "2912000",
                "description": "string loc",
                "scheme": "CUATM"
              }
            }
          }
        }
      }
    ],
    "items": [
      {
        "id": "3cd68298-b9ea-413e-b2ad-c7d3d02f170b",
        "internalId": "i-1",
        "description": "description of first RFQ item",
        "quantity": 1000,
        "unit": {
          "id": "911"
        },
        "relatedLot": "1"
      }
    ],
    "tenderPeriod": {
      "endDate": "2021-08-27T15:28:18Z"
    },
    "title": "title of RFQ tender",
    "description": "description of RFQ tender"
  }
}