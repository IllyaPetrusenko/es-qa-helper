from sys import argv
from config import get_host
from auth_operations.auth import Auth
from auth_operations.operations import Operations
from budgets.budgets import ExpenditureItem

script, env, state, pn_pmd_1, pn_pmd_2, pn_pmd_3, ap_pmd, auc = argv

host = get_host(env)[0]
credentials = get_host(env)[1]
access_token = Auth(host, credentials).get_tokens()[0]
x_operation_id = Operations(host, f'Bearer {access_token}').get_x_operation_id()

print(f'------  Start of {script} -------')
print(f'ENVIRONMENT: {env}')
print('------  Create EI 1 -------')
ei = ExpenditureItem(
        host=host,
        state=state,
        token=access_token,
        x_operation_id=x_operation_id
)
payload = ei.prepare_payload()
ocid_ei = ei.create_ei(payload=payload)

print(f'OCID: {ocid_ei}')
