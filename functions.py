import datetime
import json
import requests
import time


# Get access token
def get_access_token(host):
    token = requests.get(url=f'{host}/auth/signin', headers={
        'Authorization': 'Basic dXNlcjpwYXNzd29yZA=='
    }).json()['data']['tokens']['access']
    return token


# Get x-operation-id
def get_x_operation_id(token, host):
    x_operation_id = requests.post(url=f'{host}/operations', headers={
        'Authorization': f'Bearer {token}'
    }).json()['data']['operationId']
    return x_operation_id


# Get message from Kafka
def get_message_from_kafka(operation_id):
    kafka_host = 'http://82.144.223.29:5000'
    kafka_message = requests.get(
        url=kafka_host + '/x-operation-id/' + operation_id
    )
    if kafka_message.status_code == 404:
        date = datetime.datetime.now()
        date_new = datetime.datetime.now() + datetime.timedelta(seconds=25)
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


# Create EI
def create_ei(host, token, x_operation_id, payload):
    payload['buyer']['identifier']['id'] = x_operation_id
    requests.post(url=f'{host}/do/ei?country=MD&lang=ro&testMode=true', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    ei_ocid = kafka_message['data']['ocid']
    return ei_ocid


# Create FS
def create_fs(host, token, x_operation_id, ocid, payload):
    requests.post(url=f'{host}/do/fs/{ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    fs_ocid = kafka_message['data']['outcomes']['fs'][0]['id']
    return fs_ocid


# Create PN
def create_pn(host, token, x_operation_id, fs_ocid, payload, pmd):
    payload['planning']['budget']['budgetBreakdown'][0]['id'] = fs_ocid
    requests.post(url=f'{host}/do/pn?country=MD&lang=ro&pmd={pmd}&testMode=true', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    pn_cpid = kafka_message['data']['ocid']
    pn_ocid = kafka_message['data']['outcomes']['pn'][0]['id']
    pn_x_token = kafka_message['data']['outcomes']['pn'][0]['X-TOKEN']

    return pn_cpid, pn_ocid, pn_x_token


# Create AP
def create_ap(host, token, x_operation_id, payload, pmd):
    document = ''
    if host == 'http://10.0.20.126:8900/api/v1/':
        document = 'b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555'
    if host == 'http://10.0.10.116:8900/api/v1/':
        document = '21a5d5ef-84c0-4730-892c-338db4e3e98d-1631521816681'
    payload['tender']['documents'][0]['id'] = document
    requests.post(url=f'{host}/do/ap?country=MD&pmd={pmd}&lang=ro&testMode=true', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    print(kafka_message)
    ap_cpid = kafka_message['data']['ocid']
    ap_ocid = kafka_message['data']['outcomes']['ap'][0]['id']
    ap_x_token = kafka_message['data']['outcomes']['ap'][0]['X-TOKEN']

    return ap_cpid, ap_ocid, ap_x_token


# Do outsourcing
def do_outsourcing_pn(host, token, x_operation_id, pn_cpid, pn_ocid, pn_x_token, ap_cpid, ap_ocid):
    requests.post(url=f'{host}/do/outsourcing/{pn_cpid}/{pn_ocid}?FA={ap_cpid}&AP={ap_ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json',
        'X-TOKEN': pn_x_token
    })
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message


# Do relation
def do_relation_ap(host, token, x_operation_id, pn_cpid, pn_ocid, ap_x_token, ap_cpid, ap_ocid):
    requests.post(url=f'{host}/do/relation/{ap_cpid}/{ap_ocid}?CP={pn_cpid}&PN={pn_ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json',
        'X-TOKEN': ap_x_token
    })
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message


# Update AP
def update_ap(host, token, x_operation_id, ap_x_token, ap_cpid, ap_ocid, payload):
    document = ''
    if host == 'http://10.0.20.126:8900/api/v1/':
        document = 'b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555'
    if host == 'http://10.0.10.116:8900/api/v1/':
        document = '21a5d5ef-84c0-4730-892c-338db4e3e98d-1631521816681'
    payload['tender']['documents'][0]['id'] = document
    requests.post(url=f'{host}/do/ap/{ap_cpid}/{ap_ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json',
        'X-TOKEN': ap_x_token
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message


# Generate periods
def generate_period():
    prequalification_period_end = datetime.datetime.now() - datetime.timedelta(hours=3)
    prequalification_period_end = prequalification_period_end + datetime.timedelta(seconds=15)
    prequalification_period_end = prequalification_period_end.strftime("%Y-%m-%dT%H:%M:%SZ")
    return str(prequalification_period_end)


# Create FE
def create_fe(host, token, x_operation_id, ap_x_token, ap_cpid, ap_ocid, payload, auction):
    print(auction)
    if auction == 'auction':
        payload['preQualification']['period']['endDate'] = generate_period()
    if auction == 'no_auction':
        del payload['tender']['procurementMethodModalities']
        del payload['tender']['electronicAuctions']
        payload['preQualification']['period']['endDate'] = generate_period()
    
    document = ''
    if host == 'http://10.0.20.126:8900/api/v1/':
        document = 'b5802bf4-b838-431e-831b-7d0ef5ed9437-1593170692555'
    if host == 'http://10.0.10.116:8900/api/v1/':
        document = '21a5d5ef-84c0-4730-892c-338db4e3e98d-1631521816681'
    payload['tender']['documents'][0]['id'] = document
    requests.post(url=f'{host}/do/fe/{ap_cpid}/{ap_ocid}?&testMode=true', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json',
        'X-TOKEN': ap_x_token
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    print(kafka_message)
    fe_ocid = kafka_message['data']['outcomes']['fe'][0]['id']
    return fe_ocid


# Create submission
def create_submission(host, token, x_operation_id, ap_cpid, fe_ocid, payload):
    r = requests.post(url=f'{host}/do/submission/{ap_cpid}/{fe_ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    submission_id = kafka_message['data']['outcomes']['submissions'][0]['id']
    submission_token = kafka_message['data']['outcomes']['submissions'][0]['X-TOKEN']
    return submission_id, submission_token


# Get qualification from Kafka
def get_bpe_message_from_kafka(ocid, initiator):
    kafka_host = 'http://82.144.223.29:5000'
    if initiator == 'bpe':
        kafka_message = requests.get(
            url=f'{kafka_host}/ocid/{ocid}/bpe'
        )
        if kafka_message.status_code == 404:
            date = datetime.datetime.now()
            date_new = datetime.datetime.now() + datetime.timedelta(seconds=25)
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
            print(kafka_message)
        del kafka_message[0]['_id']
        return kafka_message
    elif initiator == 'platform':
        kafka_message = requests.get(
            url=f'{kafka_host}/ocid/{ocid}/platform'
        )
        if kafka_message.status_code == 404:
            date = datetime.datetime.now()
            date_new = datetime.datetime.now() + datetime.timedelta(seconds=25)
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


# Get qualifications from public point
def get_qualifications_from_public_point(ocid):
    kafka_message = get_bpe_message_from_kafka(ocid, 'bpe')
    qualifications = kafka_message[0]['data']['outcomes']['qualifications']
    return qualifications


# Do consideration and qualification
def do_consideration_and_qualification(host, token, x_operation_id, ap_cpid, fe_ocid, qualifications, payload):
    public_point = ''
    if host == 'http://10.0.20.126:8900/api/v1/':
        public_point = 'http://dev.public.eprocurement.systems/tenders/'
    if host == 'http://10.0.10.116:8900/api/v1/':
        public_point = 'http://public.eprocurement.systems/tenders/'
    public_point = requests.get(url=f'{public_point}{ap_cpid}/{fe_ocid}').json()
    qualific = public_point['releases'][0]['qualifications']
    for i in qualific:
        if 'statusDetails' in i:
            if i['statusDetails'] == 'awaiting':
                for a in qualifications:
                    if i['id'] == a['id']:
                        qualification_id = i['id']
                        requests.post(
                            url=f'{host}do/consideration/qualification/{ap_cpid}/{fe_ocid}/{qualification_id}',
                            headers={
                                'Authorization': f'Bearer {token}',
                                'X-OPERATION-ID': x_operation_id,
                                'Content-Type': 'application/json',
                                'X-TOKEN': a['X-TOKEN']
                            })
                        x_operation_id_2 = get_x_operation_id(get_access_token(host), host)
                        requests.post(url=f'{host}do/qualification/{ap_cpid}/{fe_ocid}/{qualification_id}',
                                      headers={
                                          'Authorization': f'Bearer {token}',
                                          'X-OPERATION-ID': x_operation_id_2,
                                          'Content-Type': 'application/json',
                                          'X-TOKEN': a['X-TOKEN']
                                      }, data=json.dumps(payload))
        else:
            continue

    return 'Consideration and Qualification -- DONE'


# Do qualification protocol
def do_qualification_protocol(host, token, x_operation_id, ap_cpid, fe_ocid, ap_x_token):
    requests.post(url=f'{host}/do/protocol/qualification/{ap_cpid}/{fe_ocid}',
                  headers={
                      'Authorization': f'Bearer {token}',
                      'X-OPERATION-ID': x_operation_id,
                      'Content-Type': 'application/json',
                      'X-TOKEN': ap_x_token
                  })
    kafka_message = get_message_from_kafka(x_operation_id)
    contract_id = kafka_message['data']['outcomes']['contracts'][0]['id']
    contract_token = kafka_message['data']['outcomes']['contracts'][0]['X-TOKEN']
    return contract_id, contract_token


# Complete qualification
def complete_qualification(host, token, x_operation_id, ap_cpid, fe_ocid, ap_x_token):
    requests.post(url=f'{host}/complete/qualification/{ap_cpid}/{fe_ocid}',
                  headers={
                      'Authorization': f'Bearer {token}',
                      'X-OPERATION-ID': x_operation_id,
                      'Content-Type': 'application/json',
                      'X-TOKEN': ap_x_token
                  })
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message


# Issuing FC
def issuing_fc(host, token, x_operation_id, ap_cpid, fe_ocid, contract_id, ap_x_token, payload=None):
    if payload:
            payload['contract']['internalId'] = x_operation_id
            requests.post(url=f'{host}/issue/fc/{ap_cpid}/{fe_ocid}/{contract_id}',
                    headers={
                        'Authorization': f'Bearer {token}',
                        'X-OPERATION-ID': x_operation_id,
                        'Content-Type': 'application/json',
                        'X-TOKEN': ap_x_token
                    }, data=json.dumps(payload))
            time.sleep(3)
            bpe_message = get_bpe_message_from_kafka(fe_ocid, 'bpe')[1]
            del bpe_message['_id']
            request_id = bpe_message['data']['outcomes']['requests'][0]['id']
            request_token = bpe_message['data']['outcomes']['requests'][0]['X-TOKEN']
    else:
            requests.post(url=f'{host}/issue/fc/{ap_cpid}/{fe_ocid}/{contract_id}',
                  headers={
                      'Authorization': f'Bearer {token}',
                      'X-OPERATION-ID': x_operation_id,
                      'Content-Type': 'application/json',
                      'X-TOKEN': ap_x_token
                  })
            time.sleep(3)
            bpe_message = get_bpe_message_from_kafka(fe_ocid, 'bpe')[1]
            del bpe_message['_id']
            request_id = bpe_message['data']['outcomes']['requests'][0]['id']
            request_token = bpe_message['data']['outcomes']['requests'][0]['X-TOKEN']


    return request_id, request_token


# Confirmation response
def create_confirmation_response(host, token, x_operation_id, x_token, entity, cpid, ocid, entity_id, role,
                                 payload, response_id):
    payload['confirmationResponse']['requestId'] = f'{response_id}'
    requests.post(url=f'{host}/do/confirmation/{entity}/{cpid}/{ocid}/{entity_id}?role={role}',
                  headers={
                      'Authorization': f'Bearer {token}',
                      'X-OPERATION-ID': x_operation_id,
                      'Content-Type': 'application/json',
                      'X-TOKEN': x_token
                  }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message['data']['outcomes']['confirmationResponses'][0]['id']


# Next confirmation step
def next_confirmation_step(host, token, x_operation_id, x_token, entity, cpid, ocid, entity_id, role):
    requests.post(url=f'{host}/complete/confirmationStage/{entity}/{cpid}/{ocid}/{entity_id}?role={role}',
                  headers={
                      'Authorization': f'Bearer {token}',
                      'X-OPERATION-ID': x_operation_id,
                      'Content-Type': 'application/json',
                      'X-TOKEN': x_token
                  })
    get_message_from_kafka(x_operation_id)
    print(get_message_from_kafka(x_operation_id))
    bpe_message = get_bpe_message_from_kafka(ocid, 'platform')
    bpe_message = bpe_message[16]
    return bpe_message
