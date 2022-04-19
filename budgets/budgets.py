import json
import requests


class ExpenditureItem:
    def __init__(self, host, state, token, x_operation_id):
        self.host = host
        self.state = state
        self.token = token
        self.x_operation_id = x_operation_id

    def prepare_payload(self):
        if self.state == 'obligatory':
            payload = json.loads(open('budgets/ei_obligatory.json', 'r').read())
            return payload
        if self.state == 'full_data_model':
            payload = 'There is no payload'
            return payload

    def create_ei(self, payload):
        r = requests.post(url=f'{self.host}/do/ei?country=MD&lang=ro&testMode=true', headers={
            'Authorization': f'Bearer {self.token}',
            'X-OPERATION-ID': self.x_operation_id,
            'Content-Type': 'application/json'
        }, data=json.dumps(payload))

        return r.status_code, self.x_operation_id


