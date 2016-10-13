from synapse_pay_rest.tests.test_helpers import *

nodes_create_payload = {
    "type": "SYNAPSE-US",
    "info": {
        "nickname": "Python Test SYNAPSE-US"
    },
    "extra": {
        "supp_id": "123sa"
    }
}

ach_us_create_payload = {
    "type": "ACH-US",
    "info": {
        "nickname": "Python Library Savings Account",
        "name_on_account": "Python Library",
        "account_num": "72347235423",
        "routing_num": "051000017",
        "type": "PERSONAL",
        "class": "CHECKING"
    },
    "extra": {
        "supp_id": "123sa"
    }
}

ach_us_micro_payload = {"micro": [0.1, 0.1]}
