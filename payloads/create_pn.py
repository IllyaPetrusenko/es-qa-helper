pn_fa = {
    "planning": {
        "rationale": "Необходимо выделить деньги для покупки ноутбуков",
        "budget": {
            "description": "Средства на покупку ноутбуков для школы №1 города Кишинев",
            "budgetBreakdown": [
                {
                    "id": "{{fs-id}}",
                    "amount": {
                        "amount": 315620.34,
                        "currency": "MDL"
                    }
                }
            ]
        }
    },
    "tender": {
        "title": "Закупка компьютерной техники для школы №1 города Кишинев",
        "description": "Закупка компьютерной техники для школы №1 города Кишинев. Необходимо закупить ноутбуки.",
        "legalBasis": "NATIONAL_PROCUREMENT_LAW",
        "procurementMethodRationale": "Рамочное соглашение",
        "procurementMethodAdditionalInfo": "Дополнительная информация будет указана в документации ",
        "tenderPeriod": {
            "startDate": "2021-09-01T00:00:00Z"
        },
        ".lots": [
            {
                "id": "1",
                "internalId": "16000-22/44",
                "title": "Ноутбуки",
                "description": "Список ноутбуков, которые хоелось бы закупить",
                "value": {
                    "amount": 315620.34,
                    "currency": "MDL"
                },
                "contractPeriod": {
                    "startDate": "2021-12-15T00:00:00Z",
                    "endDate": "2021-12-31T00:00:00Z"
                },
                "placeOfPerformance":
                    {
                        "address": {
                            "streetAddress": "Piaţa Marii Adunări Naţionale, 1",
                            "postalCode": "MD-2033",
                            "addressDetails": {
                                "country": {
                                    "id": "MD"
                                },
                                "region": {
                                    "id": "0101000"
                                },
                                "locality": {
                                    "scheme": "CUATM",
                                    "id": "0142000",
                                    "description": "mun. Chişinău"
                                }
                            }
                        },
                        "description": "Место поставки товаров"
                    }
            }
        ],
        ".items": [
            {
                "id": "1",
                "internalId": "1",
                "classification": {
                    "id": "09100000-0"
                },
                "quantity": 10,
                "unit": {
                    "id": "10"
                },
                "description": "Ноутбуки",
                "relatedLot": "1"
            }
        ]
    }
}
pn_open = {
    "planning":
    {
        "rationale": "rationale for PN",
        "budget":
        {
            "description": "description of budget in PN",
            "budgetBreakdown":
            [{
                "id": "ocds-t1s2t3-MD-1629100833045-FS-1629100840747",
                "amount":
                {
                    "amount": 100000,
                    "currency": "MDL"
                }
            }]
        }
    },
    "tender":
    {
        "title": "tender title in PN",
        "description": "description of tender in PN",
        "legalBasis": "DIRECTIVE_2014_23_EU",
        "procurementMethodRationale": "procurement Method Rationale of PN",
        "procurementMethodAdditionalInfo": "procurement Method Additional Info of PN",
        "tenderPeriod":
        {
            "startDate": "2022-05-01T00:00:00Z"
        },
        "procuringEntity":
        {
            "name": "PE in PN",
            "identifier":
            {
                "scheme": "MD-IDNO",
                "id": "PEPN",
                "legalName": "legalName PEPN",
                "uri": "PEPN.uri"
            },
            "additionalIdentifiers":
            [{
                "scheme": "MD",
                "id": "PP",
                "legalName": "legalName PP",
                "uri": "PP.uri"
            }],
            "address": {
                "streetAddress": "Street of PEPN",
                "postalCode": "PEPN postal code",
                "addressDetails": {
                    "country": {
                      "id": "MD"
                    },
                    "region": {
                      "id": "0501000"
                    },
                    "locality": {
                      "scheme": "CUATM",
                      "id": "0510000",
                      "description": "description of 0510000"
                    }
                }
            },
            "contactPoint":
            {
                "name": "PEPN contact point",
                "email": "pepncp@gmail.com",
                "telephone": "0989878776",
                "faxNumber": "0677656554",
                "url": "pepncp.url"
            }
        }
    }
}
