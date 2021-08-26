fe = {
  "preQualification": {
    "period": {
      "endDate": "2021-08-24T08:19:00Z"
    }
  },
  "tender": {
    "title": "creation of FE",
    "description": "description of FE creation",
    "otherCriteria": {
      "qualificationSystemMethods": [
        "automated"
      ],
      "reductionCriteria": "scoring"
    },
    "documents": [
      {
        "documentType": "evaluationCriteria",
        "id": "b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555",
        "title": "evaluationCriteria of FE",
        "description": "Criteria of evaluationCriteria evaluationCriteria"
      }
    ]
  }
}

fe_auction = {
    "preQualification": {
        "period": {
            "endDate": "2021-07-30T11:37:00Z"
        }
    },
    "tender": {
        "title": "Xnew",
        "description": "Ynew",
        "secondStage": {
            "minimumCandidates": 1,
            "maximumCandidates": 3
        },
        "procurementMethodModalities": [
            "electronicAuction"
        ],
        "electronicAuctions": {
            "details": [
                {
                    "id": "1",
                    "relatedLot": "{{lot-id-1}}",
                    "electronicAuctionModalities": [
                        {
                            "eligibleMinimumDifference": {
                                "amount": 0.1,
                                "currency": "EUR"
                            }
                        }
                    ]
                }
            ]
        },
        "otherCriteria": {
            "qualificationSystemMethods": [
                "automated"
            ],
            "reductionCriteria": "scoring"
        },
        "documents": [
            {
                "documentType": "evaluationCriteria",
                "id": "b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555",
                "title": "doctitle`",
                "description": "docdesc`"
            }
        ]
    }
}