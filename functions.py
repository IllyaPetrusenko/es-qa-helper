import datetime
import json
import requests
from config import host
from payloads.create_ei import ei
from payloads.create_fs import fs
from payloads.create_pn import pn
from payloads.create_ap import ap
from payloads.update_ap import up_ap


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
    requests.post(url=f'{host}/do/ei?country=MD&lang=ro', headers={
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
def create_pn(host, token, x_operation_id, fs_ocid, payload):
    payload['planning']['budget']['budgetBreakdown'][0]['id'] = fs_ocid
    requests.post(url=f'{host}/do/pn?country=MD&lang=ro&pmd=TEST_RFQ', headers={
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
def create_ap(host, token, x_operation_id, payload):
    requests.post(url=f'{host}/do/ap?country=MD&pmd=TEST_CF&lang=ro', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
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
    requests.post(url=f'{host}/do/ap/{ap_cpid}/{ap_ocid}', headers={
        'Authorization': f'Bearer {token}',
        'X-OPERATION-ID': x_operation_id,
        'Content-Type': 'application/json',
        'X-TOKEN':ap_x_token
    }, data=json.dumps(payload))
    kafka_message = get_message_from_kafka(x_operation_id)
    return kafka_message


fs_ocid = create_fs(
    token=get_access_token(host),
    host=host,
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ocid=create_ei(
        token=get_access_token(host),
        host=host,
        x_operation_id=get_x_operation_id(get_access_token(host), host),
        payload=ei
    ),
    payload=fs)

pn = create_pn(host=host,
               token=get_access_token(host),
               fs_ocid=fs_ocid,
               x_operation_id=get_x_operation_id(get_access_token(host), host),
               payload=pn)

ap = create_ap(host=host,
               token=get_access_token(host),
               x_operation_id=get_x_operation_id(get_access_token(host), host),
               payload=ap)

do_outsourcing_pn = do_outsourcing_pn(host=host,
                                      token=get_access_token(host),
                                      x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                      pn_cpid=pn[0],
                                      pn_ocid=pn[1],
                                      pn_x_token=pn[2],
                                      ap_cpid=ap[0],
                                      ap_ocid=ap[1])


do_relation_ap_pn = do_relation_ap(host=host,
                                   token=get_access_token(host),
                                   x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                   pn_cpid=pn[0],
                                   pn_ocid=pn[1],
                                   ap_x_token=ap[2],
                                   ap_cpid=ap[0],
                                   ap_ocid=ap[1])

update_ap_after_relation = update_ap(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    ap_ocid=ap[1],
    ap_x_token=ap[2],
    payload=up_ap
)

print(update_ap_after_relation)
