import requests


# Get access token
def get_access_token(host):
    token = requests.get(url=f'{host}auth/signin', headers={
        'Authorization': 'Basic dXNlcjpwYXNzd29yZA=='
    }).json()['data']['tokens']['access']
    return token


# Get x-operation-id
def get_x_operation_id(token, host):
    x_operation_id = requests.post(url=f'{host}operations', headers={
        'Authorization': f'Bearer {token}'
    }).json()['data']['operationId']
    return x_operation_id


def create_ei(host, token, x_operation_id):
    instant_response = requests.post(url=host, )