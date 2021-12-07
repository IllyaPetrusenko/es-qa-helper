bid_1 = {
    "bid": {
        "value": {
            "currency": "MDL",
            "amount": 150
        },
        "tenderers": [
            {
                "name": "tenderers name",
                "identifier": {
                    "id": "444-444",
                    "legalName": "tenderers legal name",
                    "scheme": "MD-IDNO",
                    "uri": "uri"
                },
                "additionalIdentifiers": [
                    {
                        "id": "additional",
                        "legalName": "legal name",
                        "scheme": "md",
                        "uri": "add uri"
                    }
                ],
                "address": {
                    "streetAddress": "street",
                    "postalCode": "code",
                    "addressDetails": {
                        "country": {
                            "id": "MD",
                            "description": "desc",
                            "scheme": "iso-alpha2"
                        },
                        "region": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        },
                        "locality": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        }
                    }
                },
                "contactPoint": {
                    "name": "contact point name",
                    "email": "mail",
                    "telephone": "telephone",
                    "faxNumber": "fax",
                    "url": "url"
                },
                "persones": [
                    {
                        "title": "Mr.",
                        "name": "person",
                        "identifier": {
                            "scheme": "string",
                            "id": "string",
                            "uri": "string"
                        },
                        "businessFunctions": [
                            {
                                "id": "string",
                                "type": "contactPoint",
                                "jobTitle": "job title",
                                "period": {
                                    "startDate": "2020-09-22T14:38:20Z"
                                },
                                ".documents": [
                                    {
                                        "documentType": "regulatoryDocument",
                                        "id": "{{doc_id}}",
                                        "title": "doc title",
                                        "description": "doc desc"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "details": {
                    "typeOfSupplier": "company",
                    "mainEconomicActivities": [
                        {
                            "id": "id",
                            "scheme": "MD-CAEM",
                            "description": "desc",
                            "uri": "uri"
                        }
                    ],
                    "scale": "micro",
                    "permits": [
                        {
                            "scheme": "string",
                            "id": "string",
                            "url": "string",
                            "permitDetails": {
                                "issuedBy": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "issuedThought": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "validityPeriod": {
                                    "startDate": "2020-11-26T11:07:00Z",
                                    "endDate": "2020-11-28T11:07:00Z"
                                }
                            }
                        }
                    ],
                    "bankAccounts": [
                        {
                            "description": "string",
                            "bankName": "string",
                            "address": {
                                "streetAddress": "bank street",
                                "postalCode": "bank code",
                                "addressDetails": {
                                    "country": {
                                        "id": "MD",
                                        "description": "string",
                                        "scheme": "iso-alpha2"
                                    },
                                    "region": {
                                        "id": "0301000",
                                        "description": "region desc",
                                        "scheme": "CUATM"
                                    },
                                    "locality": {
                                        "id": "0301000",
                                        "description": "string",
                                        "scheme": "CUATM"
                                    }
                                }
                            },
                            "identifier": {
                                "scheme": "UA-MFO",
                                "id": "string"
                            },
                            "accountIdentification": {
                                "scheme": "IBAN",
                                "id": "string"
                            },
                            "additionalAccountIdentifiers": [
                                {
                                    "scheme": "fiscal",
                                    "id": "string"
                                }
                            ]
                        }
                    ],
                    "legalForm": {
                        "scheme": "MD-CFOJ",
                        "id": "string",
                        "description": "string",
                        "uri": "string"
                    }
                }
            }
        ],
        "relatedLots": [
            "1"
        ],
        "documents": [
            {
                "id": "{{doc_id}}",
                "title": "doc title",
                "description": "doc desc",
                "documentType": "illustration"
            }
        ],
        "items": [
            {
                "id": "e287cc3a-d58e-4239-811f-d98e5b5afcda",
                "quantity": 10,
                "unit": {
                    "value": {
                        "amount": 15,
                        "currency": "MDL"
                    },
                    "id": "10"
                }
            }
        ]
    }
}

bid_2 = {
    "bid": {
        "value": {
            "currency": "MDL",
            "amount": 150
        },
        "tenderers": [
            {
                "name": "tenderers name",
                "identifier": {
                    "id": "444-333",
                    "legalName": "tenderers legal name",
                    "scheme": "MD-IDNO",
                    "uri": "uri"
                },
                "additionalIdentifiers": [
                    {
                        "id": "additional",
                        "legalName": "legal name",
                        "scheme": "md",
                        "uri": "add uri"
                    }
                ],
                "address": {
                    "streetAddress": "street",
                    "postalCode": "code",
                    "addressDetails": {
                        "country": {
                            "id": "MD",
                            "description": "desc",
                            "scheme": "iso-alpha2"
                        },
                        "region": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        },
                        "locality": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        }
                    }
                },
                "contactPoint": {
                    "name": "contact point name",
                    "email": "mail",
                    "telephone": "telephone",
                    "faxNumber": "fax",
                    "url": "url"
                },
                "persones": [
                    {
                        "title": "Mr.",
                        "name": "person",
                        "identifier": {
                            "scheme": "string",
                            "id": "string",
                            "uri": "string"
                        },
                        "businessFunctions": [
                            {
                                "id": "string",
                                "type": "contactPoint",
                                "jobTitle": "job title",
                                "period": {
                                    "startDate": "2020-09-22T14:38:20Z"
                                },
                                ".documents": [
                                    {
                                        "documentType": "regulatoryDocument",
                                        "id": "{{doc_id}}",
                                        "title": "doc title",
                                        "description": "doc desc"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "details": {
                    "typeOfSupplier": "company",
                    "mainEconomicActivities": [
                        {
                            "id": "id",
                            "scheme": "MD-CAEM",
                            "description": "desc",
                            "uri": "uri"
                        }
                    ],
                    "scale": "micro",
                    "permits": [
                        {
                            "scheme": "string",
                            "id": "string",
                            "url": "string",
                            "permitDetails": {
                                "issuedBy": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "issuedThought": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "validityPeriod": {
                                    "startDate": "2020-11-26T11:07:00Z",
                                    "endDate": "2020-11-28T11:07:00Z"
                                }
                            }
                        }
                    ],
                    "bankAccounts": [
                        {
                            "description": "string",
                            "bankName": "string",
                            "address": {
                                "streetAddress": "bank street",
                                "postalCode": "bank code",
                                "addressDetails": {
                                    "country": {
                                        "id": "MD",
                                        "description": "string",
                                        "scheme": "iso-alpha2"
                                    },
                                    "region": {
                                        "id": "0301000",
                                        "description": "region desc",
                                        "scheme": "CUATM"
                                    },
                                    "locality": {
                                        "id": "0301000",
                                        "description": "string",
                                        "scheme": "CUATM"
                                    }
                                }
                            },
                            "identifier": {
                                "scheme": "UA-MFO",
                                "id": "string"
                            },
                            "accountIdentification": {
                                "scheme": "IBAN",
                                "id": "string"
                            },
                            "additionalAccountIdentifiers": [
                                {
                                    "scheme": "fiscal",
                                    "id": "string"
                                }
                            ]
                        }
                    ],
                    "legalForm": {
                        "scheme": "MD-CFOJ",
                        "id": "string",
                        "description": "string",
                        "uri": "string"
                    }
                }
            }
        ],
        "relatedLots": [
            "1"
        ],
        "documents": [
            {
                "id": "{{doc_id}}",
                "title": "doc title",
                "description": "doc desc",
                "documentType": "illustration"
            }
        ],
        "items": [
            {
                "id": "e287cc3a-d58e-4239-811f-d98e5b5afcda",
                "quantity": 10,
                "unit": {
                    "value": {
                        "amount": 15,
                        "currency": "MDL"
                    },
                    "id": "10"
                }
            }
        ]
    }
}

bid_3 = {
    "bid": {
        "value": {
            "currency": "MDL",
            "amount": 120
        },
        "tenderers": [
            {
                "name": "tenderers name",
                "identifier": {
                    "id": "444-222",
                    "legalName": "tenderers legal name",
                    "scheme": "MD-IDNO",
                    "uri": "uri"
                },
                "additionalIdentifiers": [
                    {
                        "id": "additional",
                        "legalName": "legal name",
                        "scheme": "md",
                        "uri": "add uri"
                    }
                ],
                "address": {
                    "streetAddress": "street",
                    "postalCode": "code",
                    "addressDetails": {
                        "country": {
                            "id": "MD",
                            "description": "desc",
                            "scheme": "iso-alpha2"
                        },
                        "region": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        },
                        "locality": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        }
                    }
                },
                "contactPoint": {
                    "name": "contact point name",
                    "email": "mail",
                    "telephone": "telephone",
                    "faxNumber": "fax",
                    "url": "url"
                },
                "persones": [
                    {
                        "title": "Mr.",
                        "name": "person",
                        "identifier": {
                            "scheme": "string",
                            "id": "string",
                            "uri": "string"
                        },
                        "businessFunctions": [
                            {
                                "id": "string",
                                "type": "contactPoint",
                                "jobTitle": "job title",
                                "period": {
                                    "startDate": "2020-09-22T14:38:20Z"
                                },
                                ".documents": [
                                    {
                                        "documentType": "regulatoryDocument",
                                        "id": "{{doc_id}}",
                                        "title": "doc title",
                                        "description": "doc desc"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "details": {
                    "typeOfSupplier": "company",
                    "mainEconomicActivities": [
                        {
                            "id": "id",
                            "scheme": "MD-CAEM",
                            "description": "desc",
                            "uri": "uri"
                        }
                    ],
                    "scale": "micro",
                    "permits": [
                        {
                            "scheme": "string",
                            "id": "string",
                            "url": "string",
                            "permitDetails": {
                                "issuedBy": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "issuedThought": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "validityPeriod": {
                                    "startDate": "2020-11-26T11:07:00Z",
                                    "endDate": "2020-11-28T11:07:00Z"
                                }
                            }
                        }
                    ],
                    "bankAccounts": [
                        {
                            "description": "string",
                            "bankName": "string",
                            "address": {
                                "streetAddress": "bank street",
                                "postalCode": "bank code",
                                "addressDetails": {
                                    "country": {
                                        "id": "MD",
                                        "description": "string",
                                        "scheme": "iso-alpha2"
                                    },
                                    "region": {
                                        "id": "0301000",
                                        "description": "region desc",
                                        "scheme": "CUATM"
                                    },
                                    "locality": {
                                        "id": "0301000",
                                        "description": "string",
                                        "scheme": "CUATM"
                                    }
                                }
                            },
                            "identifier": {
                                "scheme": "UA-MFO",
                                "id": "string"
                            },
                            "accountIdentification": {
                                "scheme": "IBAN",
                                "id": "string"
                            },
                            "additionalAccountIdentifiers": [
                                {
                                    "scheme": "fiscal",
                                    "id": "string"
                                }
                            ]
                        }
                    ],
                    "legalForm": {
                        "scheme": "MD-CFOJ",
                        "id": "string",
                        "description": "string",
                        "uri": "string"
                    }
                }
            }
        ],
        "relatedLots": [
            "1"
        ],
        "documents": [
            {
                "id": "{{doc_id}}",
                "title": "doc title",
                "description": "doc desc",
                "documentType": "illustration"
            }
        ],
        "items": [
            {
                "id": "e287cc3a-d58e-4239-811f-d98e5b5afcda",
                "quantity": 10,
                "unit": {
                    "value": {
                        "amount": 15,
                        "currency": "MDL"
                    },
                    "id": "10"
                }
            }
        ]
    }
}

bid_4 = {
    "bid": {
        "value": {
            "currency": "MDL",
            "amount": 100
        },
        "tenderers": [
            {
                "name": "tenderers name",
                "identifier": {
                    "id": "444-111",
                    "legalName": "tenderers legal name",
                    "scheme": "MD-IDNO",
                    "uri": "uri"
                },
                "additionalIdentifiers": [
                    {
                        "id": "additional",
                        "legalName": "legal name",
                        "scheme": "md",
                        "uri": "add uri"
                    }
                ],
                "address": {
                    "streetAddress": "street",
                    "postalCode": "code",
                    "addressDetails": {
                        "country": {
                            "id": "MD",
                            "description": "desc",
                            "scheme": "iso-alpha2"
                        },
                        "region": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        },
                        "locality": {
                            "id": "0101000",
                            "description": "string",
                            "scheme": "CUATM"
                        }
                    }
                },
                "contactPoint": {
                    "name": "contact point name",
                    "email": "mail",
                    "telephone": "telephone",
                    "faxNumber": "fax",
                    "url": "url"
                },
                "persones": [
                    {
                        "title": "Mr.",
                        "name": "person",
                        "identifier": {
                            "scheme": "string",
                            "id": "string",
                            "uri": "string"
                        },
                        "businessFunctions": [
                            {
                                "id": "string",
                                "type": "contactPoint",
                                "jobTitle": "job title",
                                "period": {
                                    "startDate": "2020-09-22T14:38:20Z"
                                },
                                ".documents": [
                                    {
                                        "documentType": "regulatoryDocument",
                                        "id": "{{doc_id}}",
                                        "title": "doc title",
                                        "description": "doc desc"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "details": {
                    "typeOfSupplier": "company",
                    "mainEconomicActivities": [
                        {
                            "id": "id",
                            "scheme": "MD-CAEM",
                            "description": "desc",
                            "uri": "uri"
                        }
                    ],
                    "scale": "micro",
                    "permits": [
                        {
                            "scheme": "string",
                            "id": "string",
                            "url": "string",
                            "permitDetails": {
                                "issuedBy": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "issuedThought": {
                                    "id": "string",
                                    "name": "string"
                                },
                                "validityPeriod": {
                                    "startDate": "2020-11-26T11:07:00Z",
                                    "endDate": "2020-11-28T11:07:00Z"
                                }
                            }
                        }
                    ],
                    "bankAccounts": [
                        {
                            "description": "string",
                            "bankName": "string",
                            "address": {
                                "streetAddress": "bank street",
                                "postalCode": "bank code",
                                "addressDetails": {
                                    "country": {
                                        "id": "MD",
                                        "description": "string",
                                        "scheme": "iso-alpha2"
                                    },
                                    "region": {
                                        "id": "0301000",
                                        "description": "region desc",
                                        "scheme": "CUATM"
                                    },
                                    "locality": {
                                        "id": "0301000",
                                        "description": "string",
                                        "scheme": "CUATM"
                                    }
                                }
                            },
                            "identifier": {
                                "scheme": "UA-MFO",
                                "id": "string"
                            },
                            "accountIdentification": {
                                "scheme": "IBAN",
                                "id": "string"
                            },
                            "additionalAccountIdentifiers": [
                                {
                                    "scheme": "fiscal",
                                    "id": "string"
                                }
                            ]
                        }
                    ],
                    "legalForm": {
                        "scheme": "MD-CFOJ",
                        "id": "string",
                        "description": "string",
                        "uri": "string"
                    }
                }
            }
        ],
        "relatedLots": [
            "1"
        ],
        "documents": [
            {
                "id": "{{doc_id}}",
                "title": "doc title",
                "description": "doc desc",
                "documentType": "illustration"
            }
        ],
        "items": [
            {
                "id": "e287cc3a-d58e-4239-811f-d98e5b5afcda",
                "quantity": 10,
                "unit": {
                    "value": {
                        "amount": 15,
                        "currency": "MDL"
                    },
                    "id": "10"
                }
            }
        ]
    }
}

