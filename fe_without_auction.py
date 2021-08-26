

from functions import *
from config import host
from payloads.confirmation_response_invited_candidate import confirmation_response_invited_candidate
from payloads.confirmation_response import confirmation_response
from payloads.create_ei import ei
from payloads.create_fs import fs
from payloads.create_pn import pn
from payloads.create_ap import ap
from payloads.do_qualification import active_qualification
from payloads.issuing_fc import issuing
from payloads.update_ap import up_ap
from payloads.create_fe import fe
from payloads.create_submission import sub_1, sub_2, sub_3, sub_4

print('------  Start -------')
print('------  Create FS -------')
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

print(f'OCID: {fs_ocid}')

print('------  Create PN -------')
pn = create_pn(host=host,
               token=get_access_token(host),
               fs_ocid=fs_ocid,
               x_operation_id=get_x_operation_id(get_access_token(host), host),
               payload=pn)
print(f'CPID: {pn[0]}'
      f'  OCID: {pn[1]}'
      f'  X-TOKEN: {pn[2]}')

print('------  Create AP -------')
ap = create_ap(host=host,
               token=get_access_token(host),
               x_operation_id=get_x_operation_id(get_access_token(host), host),
               payload=ap)
print(f'CPID: {ap[0]}'
      f'  OCID: {ap[1]}'
      f'  X-TOKEN: {ap[2]}')


print('------  Do outsourcing PN -------')
do_outsourcing_pn = do_outsourcing_pn(host=host,
                                      token=get_access_token(host),
                                      x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                      pn_cpid=pn[0],
                                      pn_ocid=pn[1],
                                      pn_x_token=pn[2],
                                      ap_cpid=ap[0],
                                      ap_ocid=ap[1])
print(do_outsourcing_pn)

print('------  Do relation AP -------')
do_relation_ap_pn = do_relation_ap(host=host,
                                   token=get_access_token(host),
                                   x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                   pn_cpid=pn[0],
                                   pn_ocid=pn[1],
                                   ap_x_token=ap[2],
                                   ap_cpid=ap[0],
                                   ap_ocid=ap[1])
print(do_relation_ap_pn)


print('------  Update AP -------')
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

print('------  Create FE -------')
fe = create_fe(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    ap_ocid=ap[1],
    ap_x_token=ap[2],
    payload=fe
)
print(f'OCID:   {fe}')


time.sleep(1.5)

print('------  Create Submission 1 -------')
submission_1 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_1
)
print(f'ID:   {submission_1[0]}, X-TOKEN:  {submission_1[1]}')

print('------  Create Submission 2 -------')
submission_2 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_2
)
print(f'ID:   {submission_2[0]}, X-TOKEN:  {submission_2[1]}')

print('------  Create Submission 3 -------')
submission_3 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_3
)
print(f'ID:   {submission_3[0]}, X-TOKEN:  {submission_3[1]}')

print('------  Create Submission 4 -------')
submission_4 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_4
)
print(f'ID:   {submission_4[0]}, X-TOKEN:  {submission_4[1]}')

time.sleep(13)

print('------  QUALIFICATIONS -------')
qualifications = get_qualifications_from_public_point(fe)
print(qualifications)

print('------  DO CONSIDERATION AND QUALIFICATION 1 -------')
do_cons_1 = do_consideration_and_qualification(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    qualifications=qualifications,
    payload=active_qualification
)
print(do_cons_1)

print('------  DO CONSIDERATION AND QUALIFICATION 2 -------')
do_cons_2 = do_consideration_and_qualification(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    qualifications=qualifications,
    payload=active_qualification
)
print(do_cons_2)

print('------  DO CONSIDERATION AND QUALIFICATION 3 -------')
do_cons_3 = do_consideration_and_qualification(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    qualifications=qualifications,
    payload=active_qualification
)
print(do_cons_3)

print('------  DO CONSIDERATION AND QUALIFICATION 4 -------')
do_cons_4 = do_consideration_and_qualification(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    qualifications=qualifications,
    payload=active_qualification
)
print(do_cons_4)

time.sleep(2)

print('------  DO QUALIFICATION PROTOCOL -------')
qualification_protocol = do_qualification_protocol(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    ap_x_token=ap[2]
)
print(f'CONTRACT ID:  {qualification_protocol[0]}, CONTRACT TOKEN:  {qualification_protocol[1]}')


print('------  COMPLETE QUALIFICATION -------')
complete_qualification = complete_qualification(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    ap_x_token=ap[2]
)
print(complete_qualification)

print('------  ISSUING FC -------')
issuing_fc = issuing_fc(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    contract_id=qualification_protocol[0],
    ap_x_token=ap[2],
    payload=issuing
)
print(f'BUYER:   REQUEST ID: {issuing_fc[0]},     REQUEST TOKEN:  {issuing_fc[1]}')

time.sleep(2)

print('------  BUYER CONFIRMATION RESPONSE -------')
buyer_create_confirmation_response = create_confirmation_response(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    cpid=ap[0],
    ocid=fe,
    entity='contract',
    entity_id=qualification_protocol[0],
    response_id=issuing_fc[0],
    x_token=issuing_fc[1],
    role='buyer',
    payload=confirmation_response
)
print(f'BUYER CONFIRMATION REQUEST ID:  {buyer_create_confirmation_response}')

time.sleep(1)

print('------  BUYER NEXT CONFIRMATION STEP -------')
buyer_next_confirmation_step = next_confirmation_step(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    cpid=ap[0],
    ocid=fe,
    entity='contract',
    entity_id=qualification_protocol[0],
    x_token=qualification_protocol[1],
    role='buyer',
)
buyer_next_confirmation_step = buyer_next_confirmation_step['data']['outcomes']['requests']
print(f'INVITED CANDIDATES REQUESTS:  {buyer_next_confirmation_step}')


print('------  INVITED CANDIDATES CONFIRMATION RESPONSES -------')
num = 0
for i in buyer_next_confirmation_step:

    create_confirmation_response(
        host=host,
        token=get_access_token(host),
        x_operation_id=get_x_operation_id(get_access_token(host), host),
        cpid=ap[0],
        ocid=fe,
        entity='contract',
        entity_id=qualification_protocol[0],
        response_id=i['id'],
        x_token=i['X-TOKEN'],
        role='invitedCandidate',
        payload=confirmation_response_invited_candidate
    )
    num = num + 1
    print(f'PARTICIPANT {num} --- DONE')

time.sleep(1)

print('------  INVITED CANDIDATES NEXT CONFIRMATION STEP -------')
inv_cand_next_confirmation_step = next_confirmation_step(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    cpid=ap[0],
    ocid=fe,
    entity='contract',
    entity_id=qualification_protocol[0],
    x_token=qualification_protocol[1],
    role='invitedCandidate',
)
print("DONE")

print('------ Data for PCR ------')
print(f'LINK {host}/do/pcr/{ap[0]}/{fe}')
print(f'X-TOKEN:  {ap[2]}')




