from config import get_host
from functions import *
from payloads.confirmation_response_invited_candidate import confirmation_response_invited_candidate
from payloads.confirmation_response import confirmation_response
from payloads.create_ei import ei
from payloads.create_fs import fs
from payloads.create_pn import pn_fa
from payloads.create_ap import ap
from payloads.do_qualification import active_qualification
from payloads.evaluate_award import evaluate_award
from payloads.issuing_fc import issuing
from payloads.update_ap import up_ap
from payloads.create_fe import fe_auction
from payloads.create_submission import sub_1, sub_2, sub_3, sub_4
from payloads.create_pcr import pcr_full_no_catalogue_items_no_auction_no_criteria
from payloads.do_bid_pcr import bid_2, bid_1, bid_3, bid_4
from payloads.update_award_in_pcr import update_award
from sys import argv

script, env, pn_pmd_1, pn_pmd_2, pn_pmd_3, ap_pmd, auc = argv
host = get_host(env)[0]

print(f'------  Start of {script} -------')
print(f'ENVIRONMENT: {env}')
print('------  Create FS 1 -------')
fs_ocid_1 = create_fs(
    token=get_access_token(host),
    host=host,
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ocid=create_ei(
        token=get_access_token(host),
        host=host,
        x_operation_id=get_x_operation_id(get_access_token(host), host),
        payload=ei,
        idno='001'
    ),
    payload=fs)

print(f'OCID: {fs_ocid_1}')

print('------  Create FS 2 -------')
fs_ocid_2 = create_fs(
    token=get_access_token(host),
    host=host,
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ocid=create_ei(
        token=get_access_token(host),
        host=host,
        x_operation_id=get_x_operation_id(get_access_token(host), host),
        payload=ei,
        idno='001'
    ),
    payload=fs)

print(f'OCID: {fs_ocid_2}')

print('------  Create FS 3 -------')
fs_ocid_3 = create_fs(
    token=get_access_token(host),
    host=host,
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ocid=create_ei(
        token=get_access_token(host),
        host=host,
        x_operation_id=get_x_operation_id(get_access_token(host), host),
        payload=ei,
        idno='002'
    ),
    payload=fs)

print(f'OCID: {fs_ocid_3}')

print(f'------  Create PN with pmd {pn_pmd_1}  -------')
pn_1 = create_pn(host=host,
                 pmd=pn_pmd_1,
                 token=get_access_token(host),
                 fs_ocid=fs_ocid_1,
                 x_operation_id=get_x_operation_id(get_access_token(host), host),
                 payload=pn_fa)
print(f'CPID: {pn_1[0]}'
      f'  OCID: {pn_1[1]}'
      f'  X-TOKEN: {pn_1[2]}')

print(f'------  Create PN with pmd {pn_pmd_2}  -------')
pn_2 = create_pn(host=host,
                 pmd=pn_pmd_2,
                 token=get_access_token(host),
                 fs_ocid=fs_ocid_2,
                 x_operation_id=get_x_operation_id(get_access_token(host), host),
                 payload=pn_fa)
print(f'CPID: {pn_2[0]}'
      f'  OCID: {pn_2[1]}'
      f'  X-TOKEN: {pn_2[2]}')

print(f'------  Create PN with pmd {pn_pmd_3}  -------')
pn_3 = create_pn(host=host,
                 pmd=pn_pmd_3,
                 token=get_access_token(host),
                 fs_ocid=fs_ocid_3,
                 x_operation_id=get_x_operation_id(get_access_token(host), host),
                 payload=pn_fa)
print(f'CPID: {pn_3[0]}'
      f'  OCID: {pn_3[1]}'
      f'  X-TOKEN: {pn_3[2]}')

print('------  Create AP -------')
ap = create_ap(host=host,
               token=get_access_token(host),
               x_operation_id=get_x_operation_id(get_access_token(host), host),
               payload=ap,
               pmd=ap_pmd)
print(f'CPID: {ap[0]}'
      f'  OCID: {ap[1]}'
      f'  X-TOKEN: {ap[2]}')

print(f'------  Do outsourcing PN with {pn_pmd_1}  -------')
do_outsourcing_pn_1 = do_outsourcing_pn(host=host,
                                        token=get_access_token(host),
                                        x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                        pn_cpid=pn_1[0],
                                        pn_ocid=pn_1[1],
                                        pn_x_token=pn_1[2],
                                        ap_cpid=ap[0],
                                        ap_ocid=ap[1])
print(do_outsourcing_pn)

print(f'------  Do outsourcing PN with {pn_pmd_2}  -------')
do_outsourcing_pn_2 = do_outsourcing_pn(host=host,
                                        token=get_access_token(host),
                                        x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                        pn_cpid=pn_2[0],
                                        pn_ocid=pn_2[1],
                                        pn_x_token=pn_2[2],
                                        ap_cpid=ap[0],
                                        ap_ocid=ap[1])
print(do_outsourcing_pn_2)

print(f'------  Do outsourcing PN with {pn_pmd_3}  -------')
do_outsourcing_pn_3 = do_outsourcing_pn(host=host,
                                        token=get_access_token(host),
                                        x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                        pn_cpid=pn_3[0],
                                        pn_ocid=pn_3[1],
                                        pn_x_token=pn_3[2],
                                        ap_cpid=ap[0],
                                        ap_ocid=ap[1])
print(do_outsourcing_pn_3)

print(f'------  Do relation AP with pmd: {pn_pmd_1}  -------')
do_relation_ap_pn_1 = do_relation_ap(host=host,
                                     token=get_access_token(host),
                                     x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                     pn_cpid=pn_1[0],
                                     pn_ocid=pn_1[1],
                                     ap_x_token=ap[2],
                                     ap_cpid=ap[0],
                                     ap_ocid=ap[1])
print(do_relation_ap_pn_1)

print(f'------  Do relation AP with pmd: {pn_pmd_2}  -------')
do_relation_ap_pn_2 = do_relation_ap(host=host,
                                     token=get_access_token(host),
                                     x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                     pn_cpid=pn_2[0],
                                     pn_ocid=pn_2[1],
                                     ap_x_token=ap[2],
                                     ap_cpid=ap[0],
                                     ap_ocid=ap[1])
print(do_relation_ap_pn_2)

print(f'------  Do relation AP with pmd: {pn_pmd_3}  -------')
do_relation_ap_pn_3 = do_relation_ap(host=host,
                                     token=get_access_token(host),
                                     x_operation_id=get_x_operation_id(token=get_access_token(host), host=host),
                                     pn_cpid=pn_3[0],
                                     pn_ocid=pn_3[1],
                                     ap_x_token=ap[2],
                                     ap_cpid=ap[0],
                                     ap_ocid=ap[1])
print(do_relation_ap_pn_3)

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
    payload=fe_auction,
    auction=auc
)
print(f'OCID:   {fe}')

time.sleep(2)
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

time.sleep(20)

print('------  QUALIFICATIONS -------')
qualifications = get_qualifications_from_public_point(fe)
print(qualifications)

time.sleep(2)


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
time.sleep(2)
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
time.sleep(2)
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
time.sleep(2)
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

time.sleep(5)

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

time.sleep(2)

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
# print(f'BUYER:   REQUEST ID: {issuing_fc[0]},     REQUEST TOKEN:  {issuing_fc[1]}')
# time.sleep(2)
#
# print('------  BUYER CONFIRMATION RESPONSE -------')
# buyer_create_confirmation_response = create_confirmation_response(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=fe,
#     entity='contract',
#     entity_id=qualification_protocol[0],
#     response_id=issuing_fc[0],
#     x_token=issuing_fc[1],
#     role='buyer',
#     payload=confirmation_response
# )
# print(f'BUYER CONFIRMATION REQUEST ID:  {buyer_create_confirmation_response}')
#
# time.sleep(1)
#
# print('------  BUYER NEXT CONFIRMATION STEP -------')
# buyer_next_confirmation_step = next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=fe,
#     entity='contract',
#     entity_id=qualification_protocol[0],
#     x_token=qualification_protocol[1],
#     role='buyer',
# )
# buyer_next_confirmation_step = buyer_next_confirmation_step['data']['outcomes']['requests']
# print(f'INVITED CANDIDATES REQUESTS:  {buyer_next_confirmation_step}')
#
# print('------  INVITED CANDIDATES CONFIRMATION RESPONSES -------')
# num = 0
# for i in buyer_next_confirmation_step:
#     if num == 3:
#         break
#     else:
#         create_confirmation_response(
#             host=host,
#             token=get_access_token(host),
#             x_operation_id=get_x_operation_id(get_access_token(host), host),
#             cpid=ap[0],
#             ocid=fe,
#             entity='contract',
#             entity_id=qualification_protocol[0],
#             response_id=i['id'],
#             x_token=i['X-TOKEN'],
#             role='invitedCandidate',
#             payload=confirmation_response_invited_candidate
#         )
#         num = num + 1
#         print(f'PARTICIPANT {num} --- DONE')
#
# time.sleep(1)
#
# print('------  INVITED CANDIDATES NEXT CONFIRMATION STEP -------')
# inv_cand_next_confirmation_step = next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=fe,
#     entity='contract',
#     entity_id=qualification_protocol[0],
#     x_token=qualification_protocol[1],
#     role='invitedCandidate',
# )

time.sleep(1)

# print('------  CREATE PCR  ------')
# pcr = create_pcr(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     x_token=ap[2],
#     cpid=ap[0],
#     ocid=fe,
#     payload=pcr_full_no_catalogue_items_no_auction_no_criteria
# )
#
# print('------  CREATE BID IN PCR - 1  ------')
# bid_1 = create_bid(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     lot_id=pcr[1],
#     item_id=pcr[2],
#     payload=bid_1
# )
#
# print('------  CREATE BID IN PCR - 2  ------')
# bid_2 = create_bid(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     lot_id=pcr[1],
#     item_id=pcr[2],
#     payload=bid_2
# )
#
# print('------  CREATE BID IN PCR - 3  ------')
# bid_3 = create_bid(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     lot_id=pcr[1],
#     item_id=pcr[2],
#     payload=bid_3
# )
#
# print('------  CREATE BID IN PCR - 4  ------')
# bid_4 = create_bid(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     lot_id=pcr[1],
#     item_id=pcr[2],
#     payload=bid_4
# )
#
#
# print('------  AWARDS -------')
# time.sleep(25)
# awards = get_awards_for_pcr(pcr[0])
# print('AWARD 1 :', awards[0])
# print('AWARD 2 :', awards[1])
# print('AWARD 3 :', awards[2])
# print('AWARD 4 :', awards[3])
#
#
# print('------  AWARD CONSIDERATION  ------')
# awards_consideration(
#     host=host,
#     token=get_access_token(host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     awards=awards
# )
#
# print('-------  UPDATE AWARD  ------')
# update_award_pcr(
#     host=host,
#     token=get_access_token(host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     awards=awards,
#     payload=update_award
# )
#
#
# print('-------  EVALUATE AWARD  ------')
# evaluate_award_pcr(
#     host=host,
#     token=get_access_token(host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     awards=awards,
#     payload=evaluate_award
# )
#
# print('------   PCR PROTOCOL   ------')
# contracts = pcr_protocol_do(
#     host=host,
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     token=get_access_token(host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     lot_id=pcr[1],
#     x_token=pcr[3]
# )
#
# print('------ CONTRACTS ------')
# print(contracts[0])
# print(contracts[1])
# print(contracts[2])
# print(contracts[3])
#
# print('------   GET REQUESTS   ------')
# requests = get_contract_response_id_x_token(
#     ocid=pcr[0]
# )
# print(requests)
#
# print('------   CREATE CONFIRMATION RESPONSE USER 1 ------')
# create_confirmation_response(
#             host=host,
#             token=get_access_token(host),
#             x_operation_id=get_x_operation_id(get_access_token(host), host),
#             cpid=ap[0],
#             ocid=pcr[0],
#             entity='contract',
#             entity_id=contracts[0]['id'],
#             response_id=requests[0]['data']['outcomes']['requests'][0]['id'],
#             x_token=requests[0]['data']['outcomes']['requests'][0]['X-TOKEN'],
#             role='supplier',
#             payload=confirmation_response_invited_candidate
#         )
#
# print('------   CREATE CONFIRMATION RESPONSE USER 2 ------')
# create_confirmation_response(
#             host=host,
#             token=get_access_token(host),
#             x_operation_id=get_x_operation_id(get_access_token(host), host),
#             cpid=ap[0],
#             ocid=pcr[0],
#             entity='contract',
#             entity_id=contracts[1]['id'],
#             response_id=requests[1]['data']['outcomes']['requests'][0]['id'],
#             x_token=requests[1]['data']['outcomes']['requests'][0]['X-TOKEN'],
#             role='supplier',
#             payload=confirmation_response_invited_candidate
#         )
#
# print('------   CREATE CONFIRMATION RESPONSE USER 3 ------')
# create_confirmation_response(
#             host=host,
#             token=get_access_token(host),
#             x_operation_id=get_x_operation_id(get_access_token(host), host),
#             cpid=ap[0],
#             ocid=pcr[0],
#             entity='contract',
#             entity_id=contracts[2]['id'],
#             response_id=requests[2]['data']['outcomes']['requests'][0]['id'],
#             x_token=requests[2]['data']['outcomes']['requests'][0]['X-TOKEN'],
#             role='supplier',
#             payload=confirmation_response_invited_candidate
#         )
#
# print('------   CREATE CONFIRMATION RESPONSE USER 4 ------')
# create_confirmation_response(
#             host=host,
#             token=get_access_token(host),
#             x_operation_id=get_x_operation_id(get_access_token(host), host),
#             cpid=ap[0],
#             ocid=pcr[0],
#             entity='contract',
#             entity_id=contracts[3]['id'],
#             response_id=requests[3]['data']['outcomes']['requests'][0]['id'],
#             x_token=requests[3]['data']['outcomes']['requests'][0]['X-TOKEN'],
#             role='supplier',
#             payload=confirmation_response_invited_candidate
#         )
#
#
# print('------   NEXT CONFIRMATION STEP -1  -------')
# next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[0]['id'],
#     x_token=contracts[0]['X-TOKEN'],
#     role='supplier',
# )
#
#
# print('------   NEXT CONFIRMATION STEP -2  -------')
# next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[1]['id'],
#     x_token=contracts[1]['X-TOKEN'],
#     role='supplier',
# )
#
# print('------   NEXT CONFIRMATION STEP -3  -------')
# next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[2]['id'],
#     x_token=contracts[2]['X-TOKEN'],
#     role='supplier',
# )
#
# print('------   NEXT CONFIRMATION STEP -4  -------')
# next_confirmation_step(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[3]['id'],
#     x_token=contracts[3]['X-TOKEN'],
#     role='supplier',
# )
#
#
# print('------   APPLY CONFIRMATION - 1 -------')
# apply_confirmation(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[0]['id'],
#     x_token=contracts[0]['X-TOKEN']
# )
#
# print('------   APPLY CONFIRMATION - 2 -------')
# apply_confirmation(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[1]['id'],
#     x_token=contracts[1]['X-TOKEN']
# )
#
# print('------   APPLY CONFIRMATION - 3 -------')
# apply_confirmation(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[2]['id'],
#     x_token=contracts[2]['X-TOKEN']
# )
#
# print('------   APPLY CONFIRMATION - 4 -------')
# apply_confirmation(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     cpid=ap[0],
#     ocid=pcr[0],
#     entity='contract',
#     entity_id=contracts[3]['id'],
#     x_token=contracts[3]['X-TOKEN']
# )


# print('------   CREATE RFQ -------')
# rfq = create_rfq(
#     host=host,
#     token=get_access_token(host),
#     x_operation_id=get_x_operation_id(get_access_token(host), host),
#     x_token=pn_1[2],
#     ap_cpid=ap[0],
#     cpid=pn_1[0],
#     ocid=pn_1[1],
#     pcr_ocid=pcr[0],
#     payload=create_rfq_data,
#     lot_id=pcr[1],
#     item_id=pcr[2]
# )

print('DONE')


