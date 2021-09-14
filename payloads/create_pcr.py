pcr_full_no_catalogue_items_auction_criteria =     {
        "tender": {
            "title": "PCR Title",
            "description": "PCR Description",
            "classification": {
                "id": "30230000-0",
                "scheme": "CPV"
            },
            "targets": [
                {
                    "id": "1",
                    "title": "target one title",
                    "relatesTo": "lot",
                    "relatedItem": "1",
                    "observations": [
                        {
                            "id": "1",
                            "period": {
                                "startDate": "2021-09-08T10:03:18Z",
                                "endDate": "2021-09-18T10:03:18Z"
                            },
                            "measure": "number",
                            "unit": {
                                "id": "10"
                            },
                            "dimensions": {
                                "requirementClassIdPR": "AAM372001"
                            },
                            "notes": "Diagonal",
                            "relatedRequirementId": "d8ec546d-4db0-4426-8808-97946b94c754"
                        }
                    ]
                }
            ],
            "criteria": [
                {
                    "id": "103",
                    "title": "Allowance of checks",
                    "source": "tenderer",
                    "relatesTo": "lot",
                    "relatedItem": "1",
                    "description": "For complex products or services to be supplied or, exceptionally, for products or services which are required for a special purpose: The economic operator will allow checks  to be conducted on the production capacities or the technical capacity of the economic operator and, where necessary, on the means of study and research which are available to it and on the quality control measures? The check is to be performed by the contracting authority or, in case the latter consents to this, on its behalf by a competent official body of the country in which the supplier or service provider is established.",
                    "classification": {
                        "id": "CRITERION.OTHER.OTHER",
                        "scheme": "ESPD-2.2.1"
                    },
                    "requirementGroups": [
                        {
                            "id": "67d76fbe-ff95-435c-964f-6c9fc30a1974",
                            "requirements": [
                                {
                                    "id": "d8ec546d-4db0-4426-8808-97946b94c754",
                                    "title": "Yes",
                                    "dataType": "boolean",
                                    "expectedValue": True
                                }
                            ]
                        },
                        {
                            "id": "ec20ab9e-00bd-402a-8116-f572b8011d4b",
                            "requirements": [
                                {
                                    "id": "910b0a20-0c64-40b6-a502-9edabbeb3aee",
                                    "title": "No",
                                    "dataType": "boolean",
                                    "expectedValue": False
                                }
                            ]
                        }
                    ]
                }
            ],
            "lots": [
                {
                    "id": "1",
                    "title": "lot one title",
                    "description": "lot one description",
                    "internalId": "lot one internalID",
                    "classification": {
                        "id": "30230000-0",
                        "scheme": "CPV"
                    }
                }
            ],
            "items": [
                {
                    "id": "1",
                    "classification": {
                        "id": "30230000-0",
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
            "electronicAuctions": {
                "details": [
                    {
                        "id": "1",
                        "relatedLot": "1",
                        "electronicAuctionModalities": [
                            {
                                "eligibleMinimumDifference": {
                                    "currency": "MDL"
                                }
                            }
                        ]
                    }
                ]
            },
            "procurementMethodModalities": [
                "electronicAuction"
            ],
            "conversions": [
                {
                    "id": "1",
                    "description": "conversion one description",
                    "rationale": "conversion one rationale",
                    "relatesTo": "requirement",
                    "relatedItem": "d8ec546d-4db0-4426-8808-97946b94c754",
                    "coefficients": [
                        {
                            "id": "1",
                            "value": True,
                            "coefficient": 0.7
                        }
                    ]
                },
                {
                    "id": "2",
                    "description": "conversion one description",
                    "rationale": "conversion one rationale",
                    "relatesTo": "requirement",
                    "relatedItem": "910b0a20-0c64-40b6-a502-9edabbeb3aee",
                    "coefficients": [
                        {
                            "id": "2",
                            "value": False,
                            "coefficient": 1.0
                        }
                    ]
                }
            ],
            "awardCriteria": "qualityOnly",
            "awardCriteriaDetails": "manual"
        }
    }