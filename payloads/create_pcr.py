pcr_full_no_catalogue_items_no_auction_no_criteria = {
        "tender": {
            "title": "PCR Title",
            "description": "PCR Description",
            "classification": {
                "id": "45200000-9",
                "scheme": "CPV"
            },
            "lots": [
                {
                    "id": "1",
                    "title": "lot one title",
                    "description": "lot one description",
                    "internalId": "lot one internalID",
                    "classification": {
                        "id": "45200000-9",
                        "scheme": "CPV"
                    }
                }
            ],
            "items": [
                {
                    "id": "1",
                    "classification": {
                        "id": "45200000-9",
                        "scheme": "CPV"
                    },
                    "description": "Item one description",
                    "quantity": 1000,
                    "unit": {
                        "id": "10"
                    },
                    "relatedLot": "1",
                    "internalId": "item one internalID"
                }
            ],
            "tenderPeriod": {
                "endDate": "2021-09-10T12:48:00Z"
            },
            "documents": [
                {
                    "id": "00bd3a80-40b9-45ab-817b-8d4fab887ea8-1631102709898",
                    "documentType": "tenderNotice",
                    "title": "document title",
                    "description": "document description",
                    "relatedLots": [
                        "1"
                    ]
                }
            ],
            "awardCriteria": "priceOnly",
            "awardCriteriaDetails": "automated"
        }
    }