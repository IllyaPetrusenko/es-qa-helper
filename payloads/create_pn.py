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
    "planning": {
        "rationale": "rationale is an optional field",
        "budget": {
            "description": "description",
            "budgetBreakdown": [
                {
                    "id": "test-b3wdp1-MD-1643396534456-FS-1643398052236",
                    "amount": {
                        "amount": 315620.00,
                        "currency": "MDL"
                    }
                }
            ]
        }
    },
    "tender": {
        "title": "TITLE of sighsosldnv PUBLIC PORTAL 22222",
        "description": "descr",
        "legalBasis": "NATIONAL_PROCUREMENT_LAW",
        "procurementMethodRationale": "null",
        "procurementMethodAdditionalInfo": "procurementMethodAdditionalInfo ",
        "tenderPeriod": {
            "startDate": "2021-11-01T00:00:00Z"
        },
        "procuringEntity": {
            "name": "Direcția Agricultura, Relații Funciare și Cadastru a Consiliului Raional Edineț",
            "identifier": {
                "id": "1007601009820",
                "scheme": "MD-IDNO",
                "legalName": "Direcția Agricultura, Relații Funciare și Cadastru a Consiliului Raional Edineț",
                "uri": "http://reference.iatistandard.org"
            },
            "address": {
                "streetAddress": "str. Șoseaua Bucovinei 37",
                "postalCode": "MD4601",
                "addressDetails": {
                    "country": {
                        "id": "MD"
                    },
                    "region": {
                        "id": "4100000"
                    },
                    "locality": {
                        "scheme": "CUATM",
                        "id": "4101000",
                        "description": "mun.Chişinău"
                    }
                }
            },
            "additionalIdentifiers": [
                {
                    "id": "1003600152606",
                    "scheme": "MD-IDNO",
                    "legalName": "IMSP Institutul de Medicina Urgenta",
                    "uri": "http://hrystynivka.miskrada.org.ua/"
                }
            ],
            "contactPoint": {
                "name": "Serviciul achizitii publice",
                "email": "achizitii@urgenta.md",
                "telephone": "022250809, 022250707",
                "faxNumber": "022250809, 022250707",
                "url": "http://hrystynivka.miskrada.org.ua/"
            }
        }
    }
}
