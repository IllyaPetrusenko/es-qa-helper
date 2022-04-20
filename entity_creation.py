import datetime
import time

import requests, json
from payloads.create_ei import ei

# Create request class
from payloads.create_fs import fs


class CreateEntity:
    def __init__(self, host, credentials, lang, country, public_point):
        self.host = host
        self.lang = lang
        self.country = country
        self.credentials = credentials
        self.public_point = public_point

    def get_tokens(self):
        # get tokens from auth
        tokens = requests.get(url=f'{self.host}auth/signin', headers={
            'Authorization': f'{self.credentials}'
        }).json()
        # access token for the future requests
        access_token = tokens['data']['tokens']['access']
        # token to refresh old access token
        refresh_token = tokens['data']['tokens']['refresh']

        return access_token, refresh_token

    def get_x_operation_id(self):
        # get X-OPERATION-ID from operations
        request = requests.post(url=f'{self.host}operations', headers={
            'Authorization': f'Bearer {self.get_tokens()[0]}'
        }).json()
        # x_operation_id for the future requests
        x_operation_id = request['data']['operationId']

        return x_operation_id

    @staticmethod
    def get_message_from_kafka(operation_id):
        kafka_host = 'http://82.144.223.29:5000'
        kafka_message = requests.get(
            url=kafka_host + '/x-operation-id/' + operation_id
        )
        if kafka_message.status_code == 404:
            date = datetime.datetime.now()
            date_new = datetime.datetime.now() + datetime.timedelta(seconds=28)
            while date < date_new:
                kafka_message = requests.get(
                    url=kafka_host + '/x-operation-id/' + operation_id
                )
                date = datetime.datetime.now()
                if kafka_message.status_code == 200:
                    kafka_message = requests.get(
                        url=kafka_host + '/x-operation-id/' + operation_id
                    ).json()
                    del kafka_message['_id']
                    return kafka_message
            print('The message was not found in Kafka topic')
        if kafka_message.status_code == 200:
            kafka_message = requests.get(
                url=kafka_host + '/x-operation-id/' + operation_id
            ).json()
        del kafka_message['_id']

        return kafka_message

    @staticmethod
    def get_bpe_message_from_kafka(ocid, initiator):
        kafka_host = 'http://82.144.223.29:5000'
        if initiator == 'bpe':
            kafka_message = requests.get(
                url=f'{kafka_host}/ocid/{ocid}/bpe'
            )
            if kafka_message.status_code == 404:
                date = datetime.datetime.now()
                date_new = datetime.datetime.now() + datetime.timedelta(seconds=50)
                while date < date_new:
                    kafka_message = requests.get(
                        url=f'{kafka_host}/ocid/{ocid}/bpe'
                    )
                    date = datetime.datetime.now()
                    if kafka_message.status_code == 200:
                        kafka_message = requests.get(
                            url=f'{kafka_host}/ocid/{ocid}/bpe'
                        ).json()
                        del kafka_message[0]['_id']
                        return kafka_message
                print('The message was not found in Kafka topic')
            if kafka_message.status_code == 200:
                kafka_message = requests.get(
                    url=f'{kafka_host}/ocid/{ocid}/bpe'
                ).json()
            del kafka_message[0]['_id']
            return kafka_message
        elif initiator == 'platform':
            kafka_message = requests.get(
                url=f'{kafka_host}/ocid/{ocid}/platform'
            )
            if kafka_message.status_code == 404:
                date = datetime.datetime.now()
                date_new = datetime.datetime.now() + datetime.timedelta(seconds=35)
                while date < date_new:
                    kafka_message = requests.get(
                        url=f'{kafka_host}/ocid/{ocid}/platform'
                    )
                    date = datetime.datetime.now()
                    if kafka_message.status_code == 200:
                        kafka_message = requests.get(
                            url=f'{kafka_host}/ocid/{ocid}/platform'
                        ).json()
                        del kafka_message[0]['_id']
                        return kafka_message
                print('The message was not found in Kafka topic')
            if kafka_message.status_code == 200:
                kafka_message = requests.get(
                    url=f'{kafka_host}/ocid/{ocid}/platform'
                ).json()
            del kafka_message[0]['_id']
            return kafka_message

    @staticmethod
    def generate_periods():
        tender_period_end = datetime.datetime.now() - datetime.timedelta(hours=3)
        tender_period_end = tender_period_end + datetime.timedelta(seconds=15)
        tender_period_end = tender_period_end.strftime("%Y-%m-%dT%H:%M:%SZ")
        enq_period_end = datetime.datetime.now() - datetime.timedelta(hours=3)
        enq_period_end = enq_period_end + datetime.timedelta(seconds=5)
        enq_period_end = enq_period_end.strftime("%Y-%m-%dT%H:%M:%SZ")

        return str(tender_period_end), str(enq_period_end)

    def create_ei(self):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(url=f'{self.host}/do/ei?country={self.country}&lang={self.lang}&testMode=true', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'Content-Type': 'application/json'
        }, data=json.dumps(ei))
        kafka_message = self.get_message_from_kafka(operation_id)
        ei_ocid = kafka_message['data']['ocid']
        ei_x_token = kafka_message['data']['outcomes']['ei'][0]['X-TOKEN']

        return ei_ocid, ei_x_token

    def create_fs(self, ocid):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(url=f'{self.host}/do/fs/{ocid}', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'Content-Type': 'application/json'
        }, data=json.dumps(fs))
        kafka_message = self.get_message_from_kafka(operation_id)
        fs_cpid = kafka_message['data']['ocid']
        fs_ocid = kafka_message['data']['outcomes']['fs'][0]['id']
        fs_x_token = kafka_message['data']['outcomes']['fs'][0]['X-TOKEN']

        return fs_cpid, fs_ocid, fs_x_token

    def create_pn(self, pmd, payload, fs_ocid):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['planning']['budget']['budgetBreakdown'][0]['id'] = fs_ocid
        requests.post(url=f'{self.host}/do/pn?country={self.country}&lang={self.lang}&pmd={pmd}&testMode=true',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        pn_cpid = kafka_message['data']['ocid']
        pn_ocid = kafka_message['data']['outcomes']['pn'][0]['id']
        pn_x_token = kafka_message['data']['outcomes']['pn'][0]['X-TOKEN']

        return pn_cpid, pn_ocid, pn_x_token

    def create_cn_on_pn(self, cpid, ocid, x_token, payload, document, public_point):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['tender']['tenderPeriod']['endDate'] = self.generate_periods()[0]
        payload['tender']['enquiryPeriod']['endDate'] = self.generate_periods()[1]
        payload['tender']['documents'][0]['id'] = document
        requests.post(url=f'{self.host}/do/cn/{cpid}/{ocid}',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'X-TOKEN': x_token,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        cn_cpid = cpid
        cn_ocid = kafka_message['data']['outcomes']['ev'][0]['id']
        public_data = requests.get(url=f'{public_point}{cn_cpid}/{cn_ocid}').json()
        lot_id = public_data['releases'][0]['tender']['lots'][0]['id']

        return cn_cpid, cn_ocid, lot_id

    def create_bid(self, cpid, ocid, payload, document, lot_id):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['bid']['documents'][0]['id'] = document
        payload['bid']['relatedLots'][0] = lot_id
        payload['bid']['tenderers'][0]['identifier']['id'] = operation_id
        requests.post(url=f'{self.host}/do/bid/{cpid}/{ocid}',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        bid_id = kafka_message['data']['outcomes']['bids'][0]['id']
        bid_x_token = kafka_message['data']['outcomes']['bids'][0]['X-TOKEN']

        return bid_id, bid_x_token

    def get_awards(self, cpid, ocid):
        kafka_message = self.get_bpe_message_from_kafka(ocid, 'bpe')
        awards = kafka_message[0]['data']['outcomes']['awards']
        public_awards = requests.get(url=f'{self.public_point}/{cpid}/{ocid}').json()['releases'][0]['awards']
        for award in public_awards:
            if award['statusDetails'] == 'awaiting':
                award_1 = award['id']
                for i in awards:
                    if i['id'] == award_1:
                        return award_1, i['X-TOKEN']

    def do_consideration(self, award, award_token, cpid, ocid):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(
            url=f'{self.host}do/consideration/{cpid}/{ocid}/{award}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json',
                'X-TOKEN': award_token
            })
        kafka_message = self.get_message_from_kafka(operation_id)
        if kafka_message['data']['ocid'] == ocid:
            return "Consideration OK"

    def do_award_evaluation(self, award, award_token, cpid, ocid, payload):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(
            url=f'{self.host}do/award/{cpid}/{ocid}/{award}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json',
                'X-TOKEN': award_token}, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        if kafka_message['data']['ocid'] == ocid:
            return "Evaluation OK"

    def do_protocol(self, token, cpid, ocid, lot_id):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(
            url=f'{self.host}do/protocol/{cpid}/{ocid}/{lot_id}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json',
                'X-TOKEN': token
            })
        kafka_message = self.get_message_from_kafka(operation_id)
        can_id = kafka_message['data']['outcomes']['cans'][0]['id']
        can_x_token = kafka_message['data']['outcomes']['cans'][0]['X-TOKEN']
        return can_id, can_x_token

    def do_contract(self, token, cpid, ocid, can_id, payload):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['contracts'][0]['id'] = can_id
        print(payload)
        requests.post(
            url=f'{self.host}do/contract/{cpid}/{ocid}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json',
                'X-TOKEN': token
            }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        return kafka_message

