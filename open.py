import time
from config import get_host
from entity_creation import CreateEntity
from payloads.create_ac import contract
from payloads.create_bid import bid_1, bid_2
from payloads.create_cn import cn_on_pn
from payloads.create_pn import pn_md
from payloads.evaluate_award import evaluate_award
from sys import argv

script, env, country, lang, pn_pmd, auc = argv

host = get_host(env)

print(f'------  Start of {script} -------')
print(f'CREATE OBJECT ON  {env} ENVIRONMENT')
system = CreateEntity(
    host=host[0],
    credentials=host[1],
    lang=lang,
    country=country,
    public_point=host[3]
)

print(host[0])
print(host[1])
print(lang)
print(country)
print(host[3])

print('------  Create EI -------')
create_ei = system.create_ei()
print(f'EI-OCID: {create_ei[0]}')
print(f'EI-X-TOKEN: {create_ei[1]}')

if country == 'LT':
    print('-------Confirm EI------')
    confirm_ei = system.confirm_ei(
        cpid=create_ei[0],
        x_token=create_ei[1]
    )

if country == 'MD':
    print('------  Create FS -------')
    create_fs = system.create_fs(
        ocid=create_ei[0],
        country=country
    )
    print(f'FS-CPID: {create_fs[0]}')
    print(f'FS-OCID: {create_fs[1]}')
    print(f'FS-X-TOKEN: {create_fs[2]}')

print('------  Create PN -------')
if country == "MD":

    create_pn = system.create_pn(
        payload=pn_md,
        pmd=pn_pmd,
        ocid=create_fs[1]
    )
    print(f'PN-CPID: {create_pn[0]}')
    print(f'PN-OCID: {create_pn[1]}')
    print(f'PN-X-TOKEN: {create_pn[2]}')

if country == "LT":
    create_pn = system.create_pn(
        payload=pn_md,
        pmd=pn_pmd,
        ocid=create_ei[0]
    )
    print(f'PN-CPID: {create_pn[0]}')
    print(f'PN-OCID: {create_pn[1]}')
    print(f'PN-X-TOKEN: {create_pn[2]}')

# print('------  Create CNonPN -------')
# # create_cn = system.create_cn_on_pn(
# #     payload=cn_on_pn,
# #     cpid=create_pn[0],
# #     ocid=create_pn[1],
# #     document=host[2],
# #     x_token=create_pn[2],
# #     public_point=host[3]
# # )
# print(f'EV-CPID: {create_cn[0]}')
# print(f'EV-OCID: {create_cn[1]}')
# print(f'EV-LOT-ID: {create_cn[2]}')
#
# time.sleep(6)
#
# print('------  Create BID-1 -------')
# bid_1 = system.create_bid(
#     payload=bid_1,
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
#     payload=bid_2,
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
