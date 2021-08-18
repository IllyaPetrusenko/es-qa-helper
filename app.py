import time

from functions import *
from config import host
from payloads.create_ei import ei
from payloads.create_fs import fs
from payloads.create_pn import pn
from payloads.create_ap import ap
from payloads.update_ap import up_ap
from payloads.create_fe import fe
from payloads.create_submission import sub_1, sub_2, sub_3, sub_4


# Create FS
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

# Create PN
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

fe = create_fe(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    ap_ocid=ap[1],
    ap_x_token=ap[2],
    payload=fe
)

submission_1 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_1
)

submission_2 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_2
)

submission_3 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_3
)

submission_4 = create_submission(
    host=host,
    token=get_access_token(host),
    x_operation_id=get_x_operation_id(get_access_token(host), host),
    ap_cpid=ap[0],
    fe_ocid=fe,
    payload=sub_4
)

time.sleep(15)

qualifications = get_qualifications_from_public_point(fe)


print(qualifications)

