create_rfq_data = {
  "tender": {
    "lots": [
      {
        "id": "1",
        "internalId": "Lot 1",
        "title": "lot 1 title",
        "description": "lot 1 description",
        "value": {
          "currency": "MDL"
        },
        "contractPeriod": {
          "startDate": "2022-12-30T20:39:24Z",
          "endDate": "2022-12-31T20:39:24Z"
        },
        "placeOfPerformance": {
          "description": "placeOfPerformance.description",
          "address": {
            "streetAddress": "address.streetAddress",
            "postalCode": "02217",
            "addressDetails": {
              "country": {
                "id": "MD",
                "description": "string",
                "scheme": "iso-alpha2"
              },
              "region": {
                "id": "0101000",
                "description": "string",
                "scheme": "CUATM"
              },
              "locality": {
                "id": "0101000",
                "description": "string",
                "scheme": "CUATM"
              }
            }
          }
        }
      }
    ],
    "items": [
      {
        "id": "1",
        "internalId": "item 1 internal id",
        "description": "item 1 description",
        "quantity": 100,
        "unit": {
          "id": "10"
        },
        "relatedLot": "1"
      }
    ],
    "tenderPeriod": {
      "endDate": "2021-12-08T20:39:24.991Z"
    },
    ".electronicAuctions": {
      "details": [
        {
          "id": "string",
          "relatedLot": "string",
          "electronicAuctionModalities": [
            {
              "eligibleMinimumDifference": {
                "amount": 0,
                "currency": "string"
              }
            }
          ]
        }
      ]
    },
    ".procurementMethodModalities": [
      "electronicAuction"
    ],
    "title": "RFQ",
    "description": "RFQ description"
  }
}