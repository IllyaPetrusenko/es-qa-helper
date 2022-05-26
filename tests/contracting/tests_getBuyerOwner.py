import json
import uuid

import allure
import requests

from tests.db_functions.functions import CassandraSession
from tests.db_functions.json_data.issued_contract import issued_contract
from tests.contracting.payloads.get_buyer_owner import data


@allure.parent_suite('Contracting Integration Tests')
@allure.suite('Contracting')
@allure.sub_suite('Contracting : getBuyerOwner')
@allure.severity('Critical')
@allure.testcase(url='https://ustudio.atlassian.net/wiki/spaces/ES/pages/2658893825/R10.6.27+eContracting+'
                     'Get+Buyer+Owner',
                 name='VR.COM-6.27.2 Должна присутствовать запись о рекорде contract в сервисе по '
                      'cpid и ocid из запроса')
class Test1:
    @allure.title('Incorrect cpid')
    def test_check_service_response_with_incorrect_cpid(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_status_issued()

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244229'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
            data['id'] = f'{uuid.uuid4()}'
            payload = json.dumps(data)

        with allure.step(f'Send request'):
            r = requests.post(
                url='http://10.0.20.127:9151/command2',
                data=payload
            )

        with allure.step(f'See result'):
            assert r.status_code == 200
            assert r.json() == {'version': '2.0.0', 'id': data['id'],
                                'status': 'error', 'result': [{'code': 'VR.COM-6.27.2/9', 'description':
                                "There must be a record of the contract record in the service "
                    "by cpid 'ocds-t1s2t3-MD-1652879244229' and ocid 'ocds-t1s2t3-MD-1652879244220-AC-1652879488470'"
                    " from the request."}]}

    @allure.title('VR.COM-6.27.2 Должна присутствовать запись о рекорде contract в сервисе по cpid и ocid из запроса')
    def test_check_service_response_with_incorrect_ocid(self):

        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_status_issued()

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
            data['id'] = f'{uuid.uuid4()}'
            payload = json.dumps(data)

        with allure.step(f'Send request'):
            print(payload)
            r = requests.post(
                url='http://10.0.20.127:9151/command2',
                data=payload
            )

        with allure.step(f'See result'):
            assert r.status_code == 200
            print(r.json())
            assert r.json() == {'version': '2.0.0', 'id': data['id'],
                                'status': 'error', 'result': [{'code': 'VR.COM-6.27.2/9', 'description':
                                "There must be a record of the contract record in the service "
                    "by cpid 'ocds-t1s2t3-MD-1652879244220' and ocid 'ocds-t1s2t3-MD-1652879244229-AC-1652879488470'"
                    " from the request."}]}

    @allure.title('VR.COM-6.27.2 Должна присутствовать запись о рекорде contract в сервисе по cpid и ocid из запроса')
    def test_check_service_response_with_correct_data(self):

        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_status_issued()

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
            data['id'] = f'{uuid.uuid4()}'
            payload = json.dumps(data)

        with allure.step(f'Send request'):
            print(payload)
            r = requests.post(
                url='http://10.0.20.127:9151/command2',
                data=payload
            )

        with allure.step(f'See result'):
            assert r.status_code == 200
            print(r.json())
            assert r.json() == {'version': '2.0.0', 'id': data['id'],
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                'name': 'EI BUYER NAME', 'owner': '445f6851-c908-407d-9b45-14b92f3e964b'}}}