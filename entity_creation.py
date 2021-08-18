import requests
# TODO прописать механику для создания разных сущностей

# Create request class
class PrepareRequest:
    def __init__(self, host, api_version, endpoint, lang=None, country=None, cpid=None, ocid=None):
        self.host = host
        self.api_version = api_version
        self.endpoint = endpoint
        self.lang = lang
        self.country = country
        self.cpid = cpid
        self.ocid = ocid


    def prepare_request_for_create_ei(self):
        request = requests.post(url=f'{self.host}/{self.api_version}/{self.endpoint}')


# Create Expenditure Item
class ExpenditureItem:

    def __init__(self):
