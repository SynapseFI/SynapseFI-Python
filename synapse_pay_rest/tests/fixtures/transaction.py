from synapse_pay_rest.tests.test_helpers import *

TO_NODE_ID = '57ec57be86c27345b3f8a159'

trans_create_payload = {
    "to": {
        "type": "ACH-US",
        "id": TO_NODE_ID
    },
    "amount": {
        "amount": 1.10,
        "currency": "USD"
    },
    "extra": {
        "supp_id": "1283764wqwsdd34wd13212",
        "note": "Python test transaction... huehueh...",
        "process_on": 1,
        "ip": "192.168.0.1"
    }
}

trans_update_payload = {
    "comment": "hiyeee"
}
