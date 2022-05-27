import json
import uuid

import allure
import requests

from tests.db_functions.functions import CassandraSession
from tests.db_functions.json_data.issued_contract import issued_contract, issued_contract_no_buyer
from tests.contracting.payloads.get_buyer_owner import data


@allure.parent_suite('Contracting Integration Tests')
@allure.suite('Contracting : getBuyerOwner')
@allure.sub_suite('VR.COM-6.27.2 Должна присутствовать запись о рекорде contract в сервисе по cpid и ocid из запроса')
@allure.severity('Critical')
@allure.testcase(url='https://ustudio.atlassian.net/wiki/spaces/ES/pages/2658893825/R10.6.27+eContracting+'
                     'Get+Buyer+Owner',
                 name='VR.COM-6.27.2 Должна присутствовать запись о рекорде contract в сервисе по '
                      'cpid и ocid из запроса')
class Test1:
    @allure.title('VR.COM-6.27.2 Проверить ответ от сервиса, если отправлен некорректный cpid')
    def test_1_negative(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

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

    @allure.title('VR.COM-6.27.2 Проверить ответ от сервиса, если отправлен некорректный ocid')
    def test_2_negative(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244229-AC-1652879488470'
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
                    "by cpid 'ocds-t1s2t3-MD-1652879244220' and ocid"
                    " 'ocds-t1s2t3-MD-1652879244229-AC-1652879488470'"
                    " from the request."}]}

    @allure.title('VR.COM-6.27.2 проверить ответ от сервиса при отправке корректных данных')
    def test_3_positive(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
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
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                                                          'name': 'EI BUYER NAME',
                                                                          'owner': '445f6851-c908-407d-9b45'
                                                                                   '-14b92f3e964b'}}}


@allure.parent_suite('Contracting Integration Tests')
@allure.suite('Contracting : getBuyerOwner')
@allure.sub_suite('VR.COM-6.27.1 Сервис должен работать только со списком допустимых этапов контрактного процесса.'
                  'допустимые stage = AC, PO')
@allure.severity('Critical')
@allure.testcase(url='https://ustudio.atlassian.net/wiki/spaces/ES/pages/2658893825/R10.6.27+eContracting+'
                     'Get+Buyer+Owner',
                 name='VR.COM-6.27.1 Сервис должен работать только со списком допустимых этапов контрактного процесса.')
class Test2:
    @allure.title('VR.COM-6.27.1 Проверить ответ от сервиса если stage == AC')
    def test_1_positive(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
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
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                                                          'name': 'EI BUYER NAME',
                                                                          'owner': '445f6851-c908-407d-9b45'
                                                                                   '-14b92f3e964b'}}}

    @allure.title('VR.COM-6.27.1 Проверить ответ от сервиса если stage == PO')
    def test_2_positive(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_po_status_issued(cpid='ocds-t1s2t3-MD-1652879244221',
                                                    ocid='ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244221'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
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
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                                                          'name': 'EI BUYER NAME',
                                                                          'owner': '445f6851-c908-407d-9b45'
                                                                                   '-14b92f3e964b'}}}

    @allure.title('VR.COM-6.27.1 Проверить ответ от сервиса если stage =! AC, PO')
    def test_3_negative(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-PN-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244220-PN-1652879488470'
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
                                'status': 'error',
                                'result': [{'code': 'VR.COM-6.27.1/9',
                                            'description': 'Service should work only with the list of allowable s'
                                                           'tages of the contract process.'}]}


@allure.parent_suite('Contracting Integration Tests')
@allure.suite('Contracting : getBuyerOwner')
@allure.sub_suite('VR.COM-6.27.3 Должна присутствовать запись '
                  'об организации с ролью buyer для рекорда contract '
                  'в сервисе по cpid и ocid из запроса.'
                  'Поиск организации с ролью buyer выполняется в массиве parties в сервисе')
@allure.severity('Critical')
@allure.testcase(url='https://ustudio.atlassian.net/wiki/spaces/ES/pages/2658893825/R10.6.27+eContracting+'
                     'Get+Buyer+Owner',
                 name='VR.COM-6.27.3 Должна присутствовать запись '
                      'об организации с ролью buyer для рекорда contract '
                      'в сервисе по cpid и ocid из запроса.')
class Test3:
    @allure.title('VR.COM-6.27.3 Проверить ответ от сервиса если в AC есть баер')
    def test_1_positive(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
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
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                                                          'name': 'EI BUYER NAME',
                                                                          'owner': '445f6851-c908-407d-9b45'
                                                                                   '-14b92f3e964b'}}}

    @allure.title('VR.COM-6.27.3 Проверить ответ от сервиса если в РО есть баер')
    def test_2_positive(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract
            )
            insert.insert_contract_po_status_issued(cpid='ocds-t1s2t3-MD-1652879244221',
                                                    ocid='ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244221'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
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
                                'status': 'success', 'result': {'buyer': {'id': 'MD-IDNO-BYR',
                                                                          'name': 'EI BUYER NAME',
                                                                          'owner': '445f6851-c908-407d-9b45'
                                                                                   '-14b92f3e964b'}}}

    @allure.title('VR.COM-6.27.3 Проверить ответ от сервиса если в AC нет баера')
    def test_1_negative(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract_no_buyer
            )
            insert.insert_contract_ac_status_issued(cpid='ocds-t1s2t3-MD-1652879244220',
                                                    ocid='ocds-t1s2t3-MD-1652879244220-AC-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244220'
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
                                'status': 'error', 'result': [{'code': 'VR.COM-6.27.3/9',
                                'description': 'There must be a record of the organization with the buyer role'
                                            ' for the contract record in the service by cpid and ocid from'
                                                                            ' the request.'}]}

    @allure.title('VR.COM-6.27.3 Проверить ответ от сервиса если в РО нет баера')
    def test_2_negative(self):
        with allure.step(f'Insert data into DB'):
            insert = CassandraSession(
                cassandra_username='caclient',
                cassandra_password='6AH7vbrkMWnfK',
                cassandra_cluster='10.0.20.106',
                json_data=issued_contract_no_buyer
            )
            insert.insert_contract_po_status_issued(cpid='ocds-t1s2t3-MD-1652879244221',
                                                    ocid='ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
                                                    )

        with allure.step(f'Prepare request for service'):
            data['params']['cpid'] = 'ocds-t1s2t3-MD-1652879244221'
            data['params']['ocid'] = 'ocds-t1s2t3-MD-1652879244221-PO-1652879488470'
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
                                'status': 'error', 'result': [{'code': 'VR.COM-6.27.3/9',
                                'description': 'There must be a record of the organization with the buyer role'
                                            ' for the contract record in the service by cpid and ocid from'
                                                                            ' the request.'}]}
