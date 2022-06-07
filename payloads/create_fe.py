fe_auction = {
  "preQualification": {
    "period": {
      "endDate": "2022-01-18T15:25:00Z"
    }
  },
  "tender": {
    "procurementMethodModalities": "",
    "title": "FE tender title",
    "description": "FE tender description",
    "electronicAuctions": [],
    "secondStage": {
      "minimumCandidates": 1,
      "maximumCandidates": 10
    },
    "!procurementMethodModalities": [
      "electronicAuction"
    ],
    "procurementMethodRationale": "PMR in FE",
    "procuringEntity": {
      "id": "MD-IDNO-231",
      "persones": [
        {
          "title": "Mr.",
          "id": "Twister",
          "name": "Person 1",
          "identifier": {
            "scheme": "MD-IDNO",
            "id": "FE-person",
            "uri": "twister.uri"
          },
          "businessFunctions": [
            {
              "id": "1",
              "type": "chairman",
              "jobTitle": "boss",
              "period": {
                "startDate": "2021-01-29T10:58:32Z"
              },
              ".documents": [
                {
                  "id": "2502466e-ff8e-4918-be08-8defb0eac5d6-1642531155701",
                  "documentType": "regulatoryDocument",
                  "title": "fe reg doc",
                  "description": "regulatory fe"
                },
                 {
                  "id": "d8382187-4041-4cc6-ab16-d8d3a1a3dd06-1642531156087",
                  "documentType": "regulatoryDocument",
                  "title": "fe reg doc",
                  "description": "regulatory fe"
                },
                 {
                  "id": "269df4ef-aebe-4b16-b03f-d83991ab60ed-1642531156782",
                  "documentType": "regulatoryDocument",
                  "title": "fe reg doc",
                  "description": "regulatory fe"
                },
                 {
                  "id": "bbba1740-42ad-4477-a300-09cf70a48a3c-1642531157122",
                  "documentType": "regulatoryDocument",
                  "title": "fe reg doc",
                  "description": "regulatory fe"
                }
              ]
            }
          ]
        }
      ]
    },
    "!criteria": [
      {
        "id": "1",
        "title": "Criteria 1",
        "description": "first criteria",
        "relatesTo": "tenderer",
        "requirementGroups": [
          {
            "id": "1",
            "description": "group 1",
            "requirements": [
              {
                "id": "1",
                "title": "requirement 1",
                "description": "first req",
                "dataType": "number",
                "period": {
                  "startDate": "2021-01-29T10:58:32Z",
                  "endDate": "2021-01-29T10:58:33Z"
                },
                "minValue": 1.0,
                "maxValue": 5.0,
                "eligibleEvidences": [
                  {
                    "id": "1",
                    "title": "evidence 1",
                    "description": "first evidence",
                    "type": "document",
                    "relatedDocument": {
                      "id": "{{doc1}}"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "classification": {
          "id": "CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION",
          "scheme": "ESPD"
        }
      },
      {
        "id": "2",
        "title": "Criteria 2",
        "description": "first criteria",
        "relatesTo": "tenderer",
        "requirementGroups": [
          {
            "id": "2",
            "description": "group 1",
            "requirements": [
              {
                "id": "2",
                "title": "requirement 1",
                "description": "first req",
                "dataType": "number",
                "period": {
                  "startDate": "2021-01-29T10:58:32Z",
                  "endDate": "2021-01-29T10:58:33Z"
                },
                "minValue": 6.0,
                "maxValue": 9.0,
                "eligibleEvidences": [
                  {
                    "id": "2",
                    "title": "evidence 1",
                    "description": "first evidence",
                    "type": "document",
                    "relatedDocument": {
                      "id": "{{doc1}}"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "classification": {
          "id": "CRITERION.EXCLUSION.NATIONAL.OTHER",
          "scheme": "ESPD"
        }
      },{
        "id": "3",
        "title": "Criteria 5",
        "description": "first criteria",
        "relatesTo": "tenderer",
        "requirementGroups": [
          {
            "id": "5",
            "description": "group 1",
            "requirements": [
              {
                "id": "5",
                "title": "requirement 1",
                "description": "first req",
                "dataType": "number",
                "period": {
                  "startDate": "2021-01-29T10:58:32Z",
                  "endDate": "2021-01-29T10:58:33Z"
                },
                "minValue": 21.0,
                "maxValue": 25.0,
                "eligibleEvidences": [
                  {
                    "id": "5",
                    "title": "evidence 1",
                    "description": "first evidence",
                    "type": "document",
                    "relatedDocument": {
                      "id": "{{doc1}}"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "classification": {
          "id": "CRITERION.SELECTION.ECONOMIC_FINANCIAL_STANDING.TURNOVER.GENERAL_YEARLY",
          "scheme": "ESPD"
        }
      }
    ],
    "otherCriteria": {
      "qualificationSystemMethods": [
        "automated"
      ],
      "reductionCriteria": "scoring"
    },
    "documents": [
      {
        "documentType": "evaluationCriteria",
        "id": "16009246-c02d-42a1-bfe2-cc4ad6752cac-1642510769694",
        "title": "FE document",
        "description": "description of FE document",
        "!relatedLots": [
          "6714a3d7-afcd-4d33-94cc-71f72255975f"
        ]
      }
    ]
  }
}