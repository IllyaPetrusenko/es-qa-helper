import datetime

import json
import requests

from payloads.create_ei import ei_md, ei_lt, ei_ua
from payloads.create_pin import pin_ua, pin_lt
from payloads.create_fs import fs
from payloads.create_pn import pn_md, pn_lt


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
        enq_period_end = enq_period_end + datetime.timedelta(seconds=3)
        enq_period_end = enq_period_end.strftime("%Y-%m-%dT%H:%M:%SZ")

        return str(tender_period_end), str(enq_period_end)

    def create_ei(self):
        if self.country == 'MD':
            payload = ei_md
        elif self.country == 'LT':
            payload = ei_lt
        elif self.country == 'UA':
            payload = ei_ua
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(url=f'{self.host}/do/ei?country={self.country}&lang={self.lang}&testMode=true', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'Content-Type': 'application/json'
        }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)
        ei_ocid = kafka_message['data']['ocid']
        ei_x_token = kafka_message['data']['outcomes']['ei'][0]['X-TOKEN']

        return ei_ocid, ei_x_token

    def confirm_ei(self, cpid, x_token):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(url=f'{self.host}/do/confirmation/ei/{cpid}', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'X-TOKEN': x_token,
            'Content-Type': 'application/json'
        })
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)

    def create_fs(self, ocid, country):
        if country == 'MD':
            operation_id = self.get_x_operation_id()
            access_token = self.get_tokens()[0]
            requests.post(url=f'{self.host}/do/fs/{ocid}', headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json'
            }, data=json.dumps(fs))
            kafka_message = self.get_message_from_kafka(operation_id)
            print(kafka_message)
            fs_cpid = kafka_message['data']['ocid']
            fs_ocid = kafka_message['data']['outcomes']['fs'][0]['id']
            fs_x_token = kafka_message['data']['outcomes']['fs'][0]['X-TOKEN']

            return fs_cpid, fs_ocid, fs_x_token

        if country == 'LT':
            return '---'

    def create_pn(self, pmd, payload, ocid):
        if self.country == 'MD':
            payload = pn_md
            payload['planning']['budget']['budgetBreakdown'][0]['id'] = ocid
        elif self.country == 'LT':
            payload = pn_lt
            payload['planning']['budget']['budgetBreakdown'][0]['id'] = ocid
            payload['planning']['budget']['budgetBreakdown'][0]['classifications']['ei'] = ocid
        elif self.country == 'UA':
            payload = pn_ua
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]

        requests.post(url=f'{self.host}/do/pn?country={self.country}&lang={self.lang}&pmd={pmd}&testMode=true',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)
        pn_cpid = kafka_message['data']['ocid']
        pn_ocid = kafka_message['data']['outcomes']['pn'][0]['id']
        pn_x_token = kafka_message['data']['outcomes']['pn'][0]['X-TOKEN']

        return pn_cpid, pn_ocid, pn_x_token

    def create_pin(self, pmd, ei_ocid_1, ei_ocid_2):
        if self.country == 'MD':
            payload = pin_md
        elif self.country == 'LT':
            payload = pin_lt
        elif self.country == 'UA':
            payload = pin_ua
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['planning']['budget']['budgetBreakdown'][0]['id'] = ei_ocid_1
        payload['planning']['budget']['budgetBreakdown'][1]['id'] = ei_ocid_2
        payload['planning']['budget']['budgetBreakdown'][0]['classifications']['ei'] = ei_ocid_1
        payload['planning']['budget']['budgetBreakdown'][1]['classifications']['ei'] = ei_ocid_2
        requests.post(url=f'{self.host}/do/pin?country={self.country}&lang={self.lang}&pmd={pmd}&testMode=true',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        print(payload)
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)
        pn_cpid = kafka_message['data']['ocid']
        pn_ocid = kafka_message['data']['outcomes']['pin'][0]['id']
        pn_x_token = kafka_message['data']['outcomes']['pin'][0]['X-TOKEN']

        return pn_cpid, pn_ocid, pn_x_token

    def create_cn_on_pn(self, cpid, ocid, x_token, payload, document, public_point):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        if 'preQualification' in payload:
            payload['preQualification']['period']['endDate'] = self.generate_periods()[0]
        else:
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
        procedure_type = kafka_message['data']['outcomes']

        if 'ev' in procedure_type:
            cn_ocid = kafka_message['data']['outcomes']['ev'][0]['id']
            public_data = requests.get(url=f'{public_point}{cn_cpid}/{cn_ocid}').json()
            lot_id = public_data['releases'][0]['tender']['lots'][0]['id']
            return cn_cpid, cn_ocid, lot_id

        if 'tp' in procedure_type:
            cn_ocid = kafka_message['data']['outcomes']['tp'][0]['id']
            public_data = requests.get(url=f'{public_point}{cn_cpid}/{cn_ocid}').json()
            lot_id = public_data['releases'][0]['tender']['lots'][0]['id']
            return cn_cpid, cn_ocid, lot_id

    def create_bid(self, cpid, ocid, payload, document, lot_id):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['bid']['documents'][0]['id'] = document
        payload['bid']['relatedLots'][0] = lot_id
        requests.post(url=f'{self.host}/do/bid/{cpid}/{ocid}',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json'
                      }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)
        bid_id = kafka_message['data']['outcomes']['bids'][0]['id']
        bid_x_token = kafka_message['data']['outcomes']['bids'][0]['X-TOKEN']

        return bid_id, bid_x_token

    def get_awards(self, cpid, ocid):
        kafka_message = self.get_bpe_message_from_kafka(ocid, 'bpe')
        print(str(kafka_message))
        for i in kafka_message:
            outcomes = i['data']['outcomes']
            if 'awards' in outcomes:
                awards = i['data']['outcomes']['awards']
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
        requests.post(
            url=f'{self.host}do/contract/{cpid}/{ocid}',
            headers={
                'Authorization': f'Bearer {access_token}',
                'X-OPERATION-ID': operation_id,
                'Content-Type': 'application/json',
                'X-TOKEN': token
            },
            json=payload
        )
        kafka_message = self.get_message_from_kafka(operation_id)
        ac_id = kafka_message['data']['outcomes']['ac'][0]['id']
        ac_x_token = kafka_message['data']['outcomes']['ac'][0]['X-TOKEN']
        return ac_id, ac_x_token

    def create_submission(self, cpid, ocid, payload, document):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload['submission']['documents'][0]['id'] = document
        payload['submission']['candidates'][0]['persones'][0]['businessFunctions'][0]['documents'][0][
            'id'] = document
        requests.post(url=f'{self.host}/do/submission/{cpid}/{ocid}', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'Content-Type': 'application/json'
        }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        submission_id = kafka_message['data']['outcomes']['submissions'][0]['id']
        submission_token = kafka_message['data']['outcomes']['submissions'][0]['X-TOKEN']
        return submission_id, submission_token

    def get_qualifications(self, ocid):
        kafka_message = self.get_bpe_message_from_kafka(ocid, 'bpe')
        qualifications = kafka_message[0]['data']['outcomes']['qualifications']
        return qualifications

    def do_consideration_and_qualification(self, cpid, ocid, qualifications, payload, document, public_point):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        public_point = requests.get(url=f'{public_point}{cpid}/{ocid}').json()
        qualific = public_point['releases'][0]['qualifications']
        for i in qualific:
            if 'statusDetails' in i:
                if i['statusDetails'] == 'awaiting':
                    for a in qualifications:
                        if i['id'] == a['id']:
                            qualification_id = i['id']
                            requests.post(
                                url=f'{self.host}do/consideration/qualification/{cpid}/{ocid}/{qualification_id}',
                                headers={
                                    'Authorization': f'Bearer {access_token}',
                                    'X-OPERATION-ID': operation_id,
                                    'Content-Type': 'application/json',
                                    'X-TOKEN': a['X-TOKEN']
                                })
                            print('CONSIDERATION DONE')
                            x_operation_id_2 = self.get_x_operation_id()
                            payload['qualification']['documents'][0]['id'] = document
                            requests.post(url=f'{self.host}do/qualification/{cpid}/{ocid}/{qualification_id}',
                                          headers={
                                              'Authorization': f'Bearer {access_token}',
                                              'X-OPERATION-ID': x_operation_id_2,
                                              'Content-Type': 'application/json',
                                              'X-TOKEN': a['X-TOKEN']
                                          }, data=json.dumps(payload))
                            print('QUAL DONE')
            else:
                continue

        return 'Consideration and Qualification -- DONE'

    def do_qualification_protocol(self, token, cpid, ocid):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        requests.post(url=f'{self.host}/do/protocol/qualification/{cpid}/{ocid}',
                      headers={
                          'Authorization': f'Bearer {access_token}',
                          'X-OPERATION-ID': operation_id,
                          'Content-Type': 'application/json',
                          'X-TOKEN': token
                      })
        kafka_message = self.get_message_from_kafka(operation_id)
        print(kafka_message)
        return kafka_message

    def start_second_stage(self, cpid, ocid, token):
        operation_id = self.get_x_operation_id()
        access_token = self.get_tokens()[0]
        payload = {
            "tender": {
                "tenderPeriod": {
                    "endDate": "2021-02-11T19:25:00Z"
                }
            }
        }
        payload['tender']['tenderPeriod']['endDate'] = self.generate_periods()[0]
        requests.post(url=f'{self.host}/do/secondStage/{cpid}/{ocid}', headers={
            'Authorization': f'Bearer {access_token}',
            'X-OPERATION-ID': operation_id,
            'Content-Type': 'application/json',
            'X-TOKEN': token
        }, data=json.dumps(payload))
        kafka_message = self.get_message_from_kafka(operation_id)
        if kafka_message['data']['ocid'] == ocid:
            return "Second stage OK"
