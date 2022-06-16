ei = {
  "planning": {
    "budget": {
      "period": {
        "startDate": "2022-06-01T06:00:00Z",
        "endDate": "2022-12-16T06:00:01Z"
      },
      "!amount": {
        "amount": 10000,
        "currency": "MDL"
      }
    },
    "rationale": "rationale in EI"
  },
  "tender": {
    "title": "title in EI",
    "description": "desc in EI",
    "classification": {
      "id": "39200000-4",
      "scheme": "CPV"
    },
    "items": [
      {
        "id": "1",
        "description": "desc of first item",
        "classification": {
          "id": "39236000-5",
          "scheme": "CPV"
        },
        "additionalClassifications": [
          {
            "id": "LA22-6",
            "scheme": "CPVS"
          }
        ],
        "quantity": 1000,
        "unit": {
          "id": "20"
        },
        "deliveryAddress": {
          "streetAddress": "street in EI",
          "postalCode": "postal code in EI",
          "addressDetails": {
            "country": {
              "id": "MD",
              "description": "string",
              "scheme": "iso-alpha2"
            },
            "region": {
              "id": "7100000",
              "description": "string",
              "scheme": "CUATM"
            },
            "locality": {
              "id": "7135000",
              "description": "string",
              "scheme": "CUATM"
            }
          }
        }
      }
    ]
  },
  "buyer": {
    "name": "BUYEN in EI",
    "identifier": {
      "id": "1",
      "legalName": "legal name of buyer",
      "scheme": "MD-IDNO",
      "uri": "buyer.com"
    },
    "additionalIdentifiers": [
      {
        "id": "B1",
        "legalName": "string",
        "scheme": "MD",
        "uri": "b1.com"
      }
    ],
    "address": {
      "streetAddress": "street of buyer",
      "postalCode": "postal come of buyer",
      "addressDetails": {
        "country": {
          "id": "MD",
          "description": "string",
          "scheme": "iso-alpha2"
        },
        "region": {
          "id": "9600000",
          "description": "string",
          "scheme": "CUATM"
        },
        "locality": {
          "id": "9627002",
          "description": "string",
          "scheme": "CUATM"
        }
      }
    },
    "contactPoint": {
      "name": "name of CP",
      "email": "CP@gmail.com",
      "telephone": "0635330195",
      "faxNumber": "0956748373",
      "url": "CP.com"
    },
    "details": {
      "typeOfBuyer": "BODY_PUBLIC",
      "mainGeneralActivity": "DEFENCE",
      "mainSectoralActivity": "AIRPORT_RELATED_ACTIVITIES"
    }
  }
}
