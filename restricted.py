import time
from config import get_host
from entity_creation import CreateEntity
from payloads.create_ac import contract
from payloads.create_bid import bid
from payloads.create_pn import pn_open
from payloads.create_cn import cn_on_pn, cn_on_pn_rt
from payloads.create_submission import sub_1, sub_2, sub_3, sub_4
from payloads.do_qualification import active_qualification
from payloads.evaluate_award import evaluate_award
from sys import argv

script, env, country, lang, pn_pmd, auc = argv

host = get_host(env)

print(f'------  Start of {script} -------')
print(f'ENVIRONMENT: {env}')
print('------  Create EI -------')
system = CreateEntity(
    host=host[0],
    credentials=host[1],
    lang=lang,
    country=country,
    public_point=host[3]
)
create_ei = system.create_ei()
print(f'EI-OCID: {create_ei[0]}')
print(f'EI-X-TOKEN: {create_ei[1]}')

print('------  Create FS -------')
create_fs = system.create_fs(
    ocid=create_ei[0]
)
print(f'FS-CPID: {create_fs[0]}')
print(f'FS-OCID: {create_fs[1]}')
print(f'FS-X-TOKEN: {create_fs[2]}')

print('------  Create PN -------')
create_pn = system.create_pn(
    payload=pn_open,
    pmd=pn_pmd,
    fs_ocid=create_fs[1]
)
print(f'PN-CPID: {create_pn[0]}')
print(f'PN-OCID: {create_pn[1]}')
print(f'PN-X-TOKEN: {create_pn[2]}')

print('------  Create CNonPN -------')
create_cn = system.create_cn_on_pn(
    payload=cn_on_pn_rt,
    cpid=create_pn[0],
    ocid=create_pn[1],
    document=host[2],
    x_token=create_pn[2],
    public_point=host[3]
)
print(f'EV-CPID: {create_cn[0]}')
print(f'EV-OCID: {create_cn[1]}')
print(f'EV-LOT-ID: {create_cn[2]}')

print('------  Create Submission - 1 -------')
submission_1 = system.create_submission(
    cpid=create_cn[0],
    ocid=create_cn[1],
    payload=sub_1,
    document=host[2] )
print(f'SUB-ID: {submission_1[0]}')
print(f'SUB-TOKEN: {submission_1[1]}')

print('------  Create Submission - 2 -------')
submission_2 = system.create_submission(
    cpid=create_cn[0],
    ocid=create_cn[1],
    payload=sub_2,
    document=host[2]
)
print(f'SUB-ID: {submission_2[0]}')
print(f'SUB-TOKEN: {submission_2[1]}')

print('------  Create Submission - 3 -------')
submission_3 = system.create_submission(
    cpid=create_cn[0],
    ocid=create_cn[1],
    payload=sub_3,
    document=host[2]
)
print(f'SUB-ID: {submission_3[0]}')
print(f'SUB-TOKEN: {submission_3[1]}')

print('------  Create Submission - 4 -------')
submission_4 = system.create_submission(
    cpid=create_cn[0],
    ocid=create_cn[1],
    payload=sub_4,
    document=host[2]
)
print(f'SUB-ID: {submission_4[0]}')
print(f'SUB-TOKEN: {submission_4[1]}')

time.sleep(12)

print('------  GET QUALIFICATIONS -------')
qualifications = system.get_qualifications(
    ocid=create_cn[1]
)
print(f'QUALIFICATIONS: {qualifications}')


print('------  DO CONSIDERATION AND QUALIFICATION 1 -------')
do_cons_1 = system.do_consideration_and_qualification(
    cpid=create_cn[0],
    ocid=create_cn[1],
    qualifications=qualifications,
    payload=active_qualification,
    public_point=host[3],
    document=host[2]
)
print(do_cons_1)

time.sleep(2)

print('------  DO CONSIDERATION AND QUALIFICATION 2 -------')
do_cons_2 = system.do_consideration_and_qualification(
    cpid=create_cn[0],
    ocid=create_cn[1],
    qualifications=qualifications,
    payload=active_qualification,
    public_point=host[3],
    document=host[2]
)
print(do_cons_2)

time.sleep(2)

print('------  DO CONSIDERATION AND QUALIFICATION 3 -------')
do_cons_3 = system.do_consideration_and_qualification(
    cpid=create_cn[0],
    ocid=create_cn[1],
    qualifications=qualifications,
    payload=active_qualification,
    public_point=host[3],
    document=host[2]
)
print(do_cons_3)

time.sleep(2)

print('------  DO CONSIDERATION AND QUALIFICATION 4 -------')
do_cons_4 = system.do_consideration_and_qualification(
    cpid=create_cn[0],
    ocid=create_cn[1],
    qualifications=qualifications,
    payload=active_qualification,
    public_point=host[3],
    document=host[2]
)
print(do_cons_4)

print('------  START SECOND STAGE -------')
second_stage = system.start_second_stage(
    cpid=create_cn[0],
    ocid=create_cn[1]
)
print(f'STATUS: {second_stage}')

# print('------  Creaçte BID-1 -------')
# bid_1 = system.create_bid(
#     payload=bid,
#     cpid=create_cn[0],
#     ocid=create_cn[1],
#     document=host[2],
#     lot_id=create_cn[2]
# )
# print(f'BID-ID: {bid_1[0]}')
# print(f'BID-X-TOKEN: {bid_1[1]}')
#
#
# print('------  Create BID-2 -------')
# bid_2 = system.create_bid(
#     payload=bid,
#     cpid=create_cn[0],
#     ocid=create_cn[1],
#     document=host[2],
#     lot_id=create_cn[2]
# )
# print(f'BID-ID: {bid_2[0]}')
# print(f'BID-X-TOKEN: {bid_2[1]}')
#
# time.sleep(15)
#
# print('------  GET AWAITING AWARD -------')
# awards = system.get_awards(
#     ocid=create_cn[1],
#     cpid=create_cn[0]
# )
# print(f'Awards: {awards}')
#
#
# print('------  AWARD CONSIDERATION -------')
# consideration = system.do_consideration(
#     ocid=create_cn[1],
#     cpid=create_cn[0],
#     award=awards[0],
#     award_token=awards[1]
# )
# print(f'Status: {consideration}')
#
# print('------  AWARD EVALUATION -------')
# evaluation = system.do_award_evaluation(
#     ocid=create_cn[1],
#     cpid=create_cn[0],
#     award=awards[0],
#     award_token=awards[1],
#     payload=evaluate_award
# )
# print(f'Status: {evaluation}')
#
# print('------  DO LOT PROTOCOL -------')
# cans = system.do_protocol(
#     ocid=create_cn[1],
#     cpid=create_cn[0],
#     token=create_pn[2],
#     lot_id=create_cn[2]
# )
# print(f'CAN-ID: {cans[0]}')
# print(f'CAN-X-TOKEN: {cans[1]}')
#
# print('------  CREATE CONTRACT -------')
# ac = system.do_contract(
#     ocid=create_cn[1],
#     cpid=create_cn[0],
#     token=create_pn[2],
#     can_id=cans[0],
#     payload=contract
# )
# print(f'AC-ID: {ac[0]}')
# print(f'AC-TOKEN: {ac[1]}')
