import time
from config import get_host
from entity_creation import CreateEntity
from payloads.create_ac import contract
from payloads.create_bid import bid_1, bid_2
from payloads.create_cn import cn_on_pn_rt
from payloads.create_submission import sub_1, sub_2, sub_3, sub_4
from payloads.do_qualification import active_qualification
from payloads.evaluate_award import evaluate_award
from sys import argv

script, env, country, lang, pn_pmd, auc = argv

host = get_host(env)

print(f'------  Start of {script} -------')
print(f'ENVIRONMENT: {env}')
print('------  Create EI-1 -------')
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

print('------  Create EI-2 -------')
create_ei_2 = system.create_ei()
print(f'EI-OCID: {create_ei_2[0]}')
print(f'EI-X-TOKEN: {create_ei_2[1]}')

print('------  Confirm EI-1 -------')
system.confirm_ei(
    cpid=create_ei[0],
    x_token=create_ei[1]
)

print('------  Confirm EI-2 -------')
system.confirm_ei(
    cpid=create_ei_2[0],
    x_token=create_ei_2[1]
)

print('------  Create PIN -------')
create_pn = system.create_pin(
    pmd=pn_pmd,
    ei_ocid_1=create_ei[0],
    ei_ocid_2=create_ei_2[0]
)
print(f'PN-CPID: {create_pn[0]}')
print(f'PN-OCID: {create_pn[1]}')
print(f'PN-X-TOKEN: {create_pn[2]}')
