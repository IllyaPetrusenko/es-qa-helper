pcr_full_no_catalogue_items_no_auction_no_criteria = {
  "tender": {
    "title": "PCR tender title",
    "description": "PCR tender description",
    "classification": {
      "id": "37410000-5",
      "scheme": "CPV"
    },
    "lots": [
     {
        "id": "1",
        "title": "personal computer",
        "description": "description of personal computer",
        "internalId": "lot internal id1",
        "classification": {
          "id": "37410000-5",
          "scheme": "CPV"
        }
      }
    ],
    "items": [
      {
        "id": "1",
        "classification": {
          "id": "37410000-5",
          "scheme": "CPV"
        },
         "additionalClassification": {
          "id": "AA10-8",
          "scheme": "CPVs"
        },
        "description": "description of PCR item1",
        "quantity": 200,
        "unit": {
          "id": "794"
        },
        "relatedLot": "1",
        "internalId": "item internalId1"
      }
    ],
    "tenderPeriod": {
      "endDate": "2021-10-04T14:05:00Z"
    },
    "documents": [
      {
        "id": "5c78f85e-c4e7-464a-a4a9-3951520922a8-1652163224146",
        "documentType": "tenderNotice",
        "title": "title of PCR document",
        "description": "description of PCR document",
        "relatedLots": [
          "1"
        ]
      }
    ],
    "awardCriteria": "priceOnly",
    "awardCriteriaDetails": "automated"
  }
}