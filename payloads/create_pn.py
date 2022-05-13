pn_fa = {
  "planning": {
    "budget": {
      "budgetBreakdown": [
        {
          "id": "ocds-t1s2t3-MD-1643107017630-FS-1643107028795",
          "amount": {
            "amount": 100000,
            "currency": "MDL"
          }
        }
      ]
    }
  },
  "tender": {
    "title": "PN title",
    "description": "description of PN",
    "legalBasis": "DIRECTIVE_2009_81_EC",
    "tenderPeriod": {
      "startDate": "2022-01-01T00:00:00Z"
    }
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
