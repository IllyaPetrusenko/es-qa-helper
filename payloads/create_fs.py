fs = {
  	"tender": {
      "procuringEntity":
      {
        "name": "Procuring Entity in FS",
        "identifier":
        {
            "id": "PRCRNG",
            "scheme": "MD-IDNO",
            "legalName": "Legal Procuring Entity in FS",
            "uri": "PRCRNG.uri"
        },
        "address": {
            "streetAddress": "Street of Procuring Entity in FS",
            "postalCode": "Procuring Entity in FS postal code",
            "addressDetails": {
                "country": {
                  "id": "MD"
                },
                "region": {
                  "id": "6400000"
                },
                "locality": {
                  "scheme": "CUATM",
                  "id": "6413000",
                  "description": "description of 6413000"
                }
            }
        },
        "additionalIdentifiers":
        [{
            "id": "PE",
            "scheme": "MD",
            "legalName": "PE legalName",
            "uri": "PE.uri"
        }],
        "contactPoint":
        {
            "name": "PEntity",
            "email": "pentity@gmail.com",
            "telephone": "0989807866",
            "faxNumber": "0675675454",
            "url": "pentity.uri"
        }
      }
    },
    "planning":
	{
    	"budget":
		{
      		"id": "budget in FS",
      		"description": "description of budget in FS",
      		"period":
			{
        		"startDate": "2022-05-02T00:00:00Z",
        		"endDate": "2022-10-29T11:00:00Z"
      		},
      		"amount":
			{
        		"amount": 100000,
        		"currency": "MDL"
      		},
      		"isEuropeanUnionFunded": True,
			"europeanUnionFunding":
			{
      			"projectName": "name of project",
      			"projectIdentifier": "PRJCT-1",
      			"uri": "project.uri"
    		},
            "project": "PROJECT 1",
            "projectID": "PRJCT-1",
            "uri": "PRJCT-1.uri"
		},
		"rationale": "rationale for budget in FS"
	},
    "buyer":
    {
        "name": "buyer name in FS",
        "identifier":
        {
            "id": "FSBYR",
            "scheme": "MD-IDNO",
            "legalName": "legalName of FSBYR",
            "uri": "FSBYR.uri"
        },
        "address": {
            "streetAddress": "Street of FSBYR",
            "postalCode": "FSBYR postal code",
            "addressDetails": {
                "country": {
                  "id": "MD"
                },
                "region": {
                  "id": "0101000"
                },
                "locality": {
                  "scheme": "CUATM",
                  "id": "0121000",
                  "description": "description of 0121000"
                }
            }
        },
        "additionalIdentifiers":
        [{
            "id": "FSBYR",
            "scheme": "MD",
            "legalName": "additional legal Name",
            "uri": "fsbyr.uri"
        }],
        "contactPoint":
        {
            "name": "FS buyer",
            "email": "fsbuyer@gmail.com",
            "telephone": "0986786766",
            "faxNumber": "0673334323",
            "url": "fsbuyer.url"
        }
    }
}
