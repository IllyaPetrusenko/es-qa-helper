ei = {
	"tender":
	{
        "title": "Title of Expenditure Item",
    	 "description": "Expenditure Item description",
    	   "classification":
	    {
      		"id": "15100000-9"
    	  },
           "items": [{
              "id": "1",
              "description": "first item in EI",
              "classification": {
                  "id": "15110000-2"
               },
              "additionalClassifications": [{
                  "id": "BA43-8"
              }
            ],
              "deliveryAddress":{
                "streetAddress":"Street EI",
                "postalCode":"EI postal code",
                "addressDetails":{
                    "country":{
                        "id":"MD"
                        },
                    "region":{
                        "id":"3100000"
                    },
                    "locality":{
                        "id":"3110000",
                        "description":"description of locality",
                        "scheme":"CUATM",
                        "uri":"locality.uri in EI"
                    }
                }
              },
              "quantity": 100,
              "unit": {
                  "id": "166"
               }

      }
    ]
	},
  	"planning":
	{
    	   "budget":
		{
			"period":
			{
        		  "startDate": "2022-05-01T00:00:00Z",
        		  "endDate": "2022-10-30T00:00:00Z"
      		}
    	},
    	 "rationale": "Rationale for EI"
	},
        "buyer":
	{
      	  "name": "BUYER",
      	  "identifier":
		{
        	"id": "BYR",
        	"scheme": "MD-IDNO",
        	"legalName": "Bu Yer",
        	"uri": "buyer.uri in EI"
      	},
          "address": {
            "streetAddress": "Buyer street",
            "postalCode": "Buyer postal code",
            "addressDetails": {
                "country": {
                  "id": "MD"
                },
                "region": {
                  "id": "5700000"
                },
                "locality": {
                  "scheme": "other",
                  "id": "DNPRPTRVSK",
                  "description": "description of buyer locality"
                }
            }
        },
      	"additionalIdentifiers":
		[{
          	"id": "BY",
          	"scheme": "MD",
          	"legalName": "Yer Bu",
          	"uri": "yerbu.uri"
        }],
      	    "contactPoint":
		{
        	"name": "Anastasiia",
        	"email": "anastasiia@gmail.com",
        	"telephone": "0675667890",
        	"faxNumber": "0987667899",
        	"url": "contactPoint.buyer.url"
      	},
      	  "details":
		{
        	"typeOfBuyer": "BODY_PUBLIC",
        	"mainGeneralActivity": "PUBLIC_ORDER_AND_SAFETY",
        	"mainSectoralActivity": "WATER"
      	}
	}
}
