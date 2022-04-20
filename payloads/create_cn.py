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
