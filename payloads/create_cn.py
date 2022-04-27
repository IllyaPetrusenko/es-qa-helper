cn_on_pn = {
    "tender": {
        "procurementMethodRationale": "procurement Method Rationale in CN",
        "procurementMethodAdditionalInfo": "procurement Method Additional Info in CN",
        "awardCriteria": "priceOnly",
        "awardCriteriaDetails": "automated",
        "tenderPeriod": {
            "endDate": "2022-01-28T21:05:00Z"
        },
        "enquiryPeriod": {
            "endDate": "2022-01-28T20:59:00Z"
        },
        ".procurementMethodModalities": [
            "electronicAuction"
        ],
        ".electronicAuctions": {
            "details": [{
                "id": "1",
                "relatedLot": "1",
                "electronicAuctionModalities": [{
                    "eligibleMinimumDifference": {
                        "amount": 100,
                        "currency": "MDL"
                    }
                }]
            }]
        },
        "procuringEntity": {
            "id": "MD-IDNO-1007601009820",
        },
        "lots": [{
            "id": "1",
            "internalId": "L-1-1",
            "title": "first lot",
            "description": "description of first lot",
            "value": {
                "amount": 50000,
                "currency": "MDL"
            },
            "contractPeriod": {
                "startDate": "2022-12-20T09:56:39Z",
                "endDate": "2022-12-28T09:56:39Z"
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
            "options": [{
                "description": "string",
                "period": {
                    "durationInDays": 30,
                    "startDate": "2021-07-05T09:56:39Z",
                    "endDate": "2021-07-15T09:56:39Z",
                    "maxExtentDate": "2021-07-20T09:56:39Z"
                }
            }],
            "hasRecurrence": True,
            "recurrence": {
                "dates": [{
                    "startDate": "2021-07-05T09:56:39Z"
                }],
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
        }],
        "items": [{
            "id": "1",
            "internalId": "I-1-1",
            "classification": {
                "id": "45200000-9"
            },
            "additionalClassifications": [{
                "id": "RA13-5"
            }],
            "quantity": 50,
            "unit": {
                "id": "170"
            },
            "description": "description of first item",
            "relatedLot": "1"
        }

        ],
        "documents": [{
            "documentType": "billOfQuantity",
            "id": "2f4c5cc8-8918-4f42-844c-c923e3e76c07-1643403155020",
            "title": "documents.title",
            "description": "documents.description",
            "relatedLots": [
                "1"
            ]
        }]
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
            "endDate": "2021-11-18T10:43:00Z"
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
            "qualificationSystemMethods": [
                "automated"
            ]
        },
        "!procurementMethodModalities": [
            "electronicAuction"
        ],
        "!electronicAuctions": {
            "details": [
                {
                    "id": "",
                    "relatedLot": "",
                    "electronicAuctionModalities": [
                        {
                            "eligibleMinimumDifference": {
                                "amount": 150.00,
                                "currency": "MDL"
                            }
                        }
                    ]
                }
            ]
        },
        "procurementMethodRationale": "pmr",
        "procurementMethodAdditionalInfo": "pmai",
        "awardCriteria": "priceOnly",
        "awardCriteriaDetails": "automated",
        "procuringEntity": {
            "id": "MD-IDNO-1007601009820",
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
                            },
                            ".documents": [
                                {
                                    "id": "efb260fb-cbfb-4f17-8831-b17aa5179e0d-1637231815593",
                                    "documentType": "regulatoryDocument",
                                    "title": "doc",
                                    "description": "doc 1"
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
                "internalId": "1-1",
                "title": "lot kate",
                "description": "looooooo1",
                "value": {
                    "amount": 10000,
                    "currency": "MDL"
                },
                "contractPeriod": {
                    "startDate": "2022-11-26T16:00:00Z",
                    "endDate": "2022-11-27T16:00:00Z"
                },
                "placeOfPerformance": {
                    "address": {
                        "streetAddress": "Street",
                        "postalCode": "123321",
                        "addressDetails": {
                            "country": {
                                "id": "MD"
                            },
                            "region": {
                                "id": "4100000"
                            },
                            "locality": {
                                "scheme": "CUATM",
                                "id": "4102000",
                                "description": "1"
                            }
                        }
                    },
                    "description": "place"
                }
            }
        ],
        "items": [
            {
                "id": "1",
                "quantity": 10,
                "classification": {
                    "id": "45200000-9"
                },
                "unit": {
                    "id": "120"
                },
                "description": "item",
                "relatedLot": "1"
            }
        ],
        "documents": [
            {
                "documentType": "illustration",
                "id": "efb260fb-cbfb-4f17-8831-b17aa5179e0d-1637231815593",
                "title": "doc",
                "description": "doc1",
                "relatedLots": [
                    "1"
                ]
            }
        ]
    }
}
