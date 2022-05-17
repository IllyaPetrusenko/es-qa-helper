cn_on_pn = {
  "tender": {
    "procurementMethodRationale": "procurement Method Rationale in CN",
    "procurementMethodAdditionalInfo": "procurement Method Additional Info in CN",
    "awardCriteria": "priceOnly",
    "awardCriteriaDetails": "automated",
    "tenderPeriod": {
      "endDate": "2022-05-17T05:20:00Z"
    },
    "enquiryPeriod": {
      "endDate": "2022-05-17T05:15:00Z"
    },
    "procuringEntity": {
      "id": "MD-IDNO-PEPN",
      "persones": [
        {
          "title": "Mr.",
          "name": "name of CN Person",
          "identifier": {
            "id": "CN-PRSN",
            "scheme": "MD-IDNO",
            "uri": "CN-PRSN.uri"
          },
          "businessFunctions": [
            {
              "id": "1",
              "type": "chairman",
              "jobTitle": "jobTitle of CN-PRSN",
              "period": {
                "startDate": "2021-07-05T09:56:39Z"
              },
              "documents": [
                {
                  "id": "157822d5-e88f-478f-abb6-0ed547f8d8b9-1652083954576",
                  "title": "title of business document",
                  "documentType": "regulatoryDocument",
                  "description": "description of business document"
                }
              ]
            }
          ]
        }
      ]
    },
    "lots": [
      {
        "id": "1",
        "internalId": "L-1-1",
        "title": "first lot",
        "description": "description of first lot",
        "value": {
          "amount": 50000,
          "currency": "MDL"
        },
        "contractPeriod": {
          "startDate": "2022-05-19T10:00:00Z",
          "endDate": "2022-05-25T10:00:00Z"
        },
        "placeOfPerformance": {
          "address": {
            "streetAddress": "Street of LOT",
            "postalCode": "LOT postal Code",
            "addressDetails": {
              "country": {
                "id": "MD"
              },
              "region": {
                "id": "8700000"
              },
              "locality": {
                "id": "8710000",
                "scheme": "CUATM",
                "description": "description of 8710000"
              }
            }
          },
          "description": "description of LOT placeOfPerformance"
        },
        "hasOptions": True,
        "options": [
          {
            "description": "string",
            "period": {
              "durationInDays": 30,
              "startDate": "2021-07-05T09:56:39Z",
              "endDate": "2021-07-15T09:56:39Z",
              "maxExtentDate": "2021-07-20T09:56:39Z"
            }
          }
        ],
        "hasRecurrence": True,
        "recurrence": {
          "dates": [
            {
              "startDate": "2021-07-05T09:56:39Z"
            }
          ],
          "description": "description of LOT recurrence"
        },
        "hasRenewal": True,
        "renewal": {
          "description": "description of LOT renewal",
          "minimumRenewals": 1,
          "maximumRenewals": 10,
          "period": {
            "durationInDays": 60,
            "startDate": "2021-07-05T09:56:39Z",
            "endDate": "2021-08-05T09:56:39Z",
            "maxExtentDate": "2021-09-05T09:56:39Z"
          }
        }
      }
    ],
    "items": [
      {
        "id": "1",
        "internalId": "I-1-1",
        "classification": {
          "id": "37400000-2"
        },
        "additionalClassifications": [
          {
            "id": "RA13-5"
          }
        ],
        "quantity": 50,
        "unit": {
          "id": "170"
        },
        "description": "description of first item",
        "relatedLot": "1"
      }

    ],
    "documents": [
      {
        "id": "b7032fe9-100d-4a42-86f8-f2df9ef09bc8-1652083076593",
        "title": "PN document 1",
        "documentType": "procurementPlan",
        "description": "description of PN document 1",
        "relatedLots": [
          "1"
        ]
      },
      {
        "id": "a524910a-8728-4939-8562-7f3f2161b7e2-1652083532134",
        "title": "CN document 2",
        "documentType": "illustration",
        "description": "description of CN document 2",
        "relatedLots": [
          "1"
        ]
      }
    ]
  }
}
cn_on_pn_rt = {
  "planning": {
    "rationale": "reason",
    "budget": {
      "description": "fs budget"
    }
  },
  "preQualification": {
    "period": {
       "endDate": "2021-06-30T10:14:00Z"
    }
  },
  "tender": {
    "title": "cn on pn",
    "description": "tenderrrrr",
    "secondStage": {
      "minimumCandidates": 2,
      "maximumCandidates": 5
    },
    "otherCriteria": {
        "reductionCriteria": "scoring",
        "qualificationSystemMethods":["manual"]
    },
    "procurementMethodRationale": "pmr",
    "procurementMethodAdditionalInfo": "pmai",
    "awardCriteria": "priceOnly",
    "awardCriteriaDetails": "automated",
    "procuringEntity": {
      "id": "MD-IDNO-PEPN",
      "persones": [
        {
          "title": "Mr.",
          "name": "ira",
          "identifier": {
            "scheme": "MD-IDNO",
            "id": "123",
            "uri": ".uri"
          },
          "businessFunctions": [
            {
              "id": "1",
              "type": "chairman",
              "jobTitle": "Chief Executive Officer",
              "period": {
                "startDate": "2021-01-02T16:00:00Z"
              }
            }
          ]
        }
      ]
    },
    "lots": [
     {
            "id":"1",
            "internalId":"1-1",
            "title":"lot 1",
            "description":"first lot",
            "value":{
               "amount":10000,
               "currency":"MDL"
            },
            "contractPeriod":{
               "startDate":"2022-05-20T00:00:00Z",
               "endDate":"2022-05-22T00:00:00Z"
            },
            "placeOfPerformance":{
               "address":{
                  "streetAddress":"Lesnaya",
                  "postalCode":"100200",
                  "addressDetails":{
                     "country":{
                        "id":"MD"
                     },
                     "region":{
                        "id":"6700000"
                     },
                     "locality":{
                        "scheme":"CUATM",
                        "id":"6701002",
                        "description":"loc"
                     }
                  }
               },
               "description":"description of locality"
            }
             }
    ],
      "items":[
         {
            "id":"1",
            "quantity":10,
            "classification":{
               "id":"37400000-2"},
            "unit":{
               "id":"120"
            },
            "description":"item",
            "relatedLot":"1"
         }
      ],
    "documents": [
      {
        "documentType": "illustration",
        "id": "377ca816-c7c9-4d38-bd83-c70f99a113ab-1652163991404",
        "title": "doc",
        "description": "doc1",
        "relatedLots": [
          "1"
        ]
      }
    ]
  }
}
