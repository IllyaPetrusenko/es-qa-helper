import requests
from auth_operations.auth import Auth


class Operations:

    def __init__(self, host, credentials):
        self.host = host
        self.credentials = credentials

    def get_x_operation_id(self):
        # get X-OPERATION-ID from operations
        request = requests.post(url=f'{self.host}operations', headers={
            'Authorization': f'{self.credentials}'
        }).json()
        # x_operation_id for the future requests
        x_operation_id = request['data']['operationId']

        return x_operation_id

#
# token = Auth(host='http://10.0.20.126:8900/api/v1/', credentials='Basic dXNlcjpwYXNzd29yZA==')
# t = Operations(host='http://10.0.20.126:8900/api/v1/', credentials=f'Bearer {token.get_tokens()[0]}')
# print(t.get_x_operation_id())
# print(t.get_x_operation_id())
# print(t.get_x_operation_id())
# print(t.get_x_operation_id())
