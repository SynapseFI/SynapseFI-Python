import os
from synapse_pay_rest.tests.test_helpers import *

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
FINGERPRINT = os.environ['FINGERPRINT']
IP_ADDRESS = '127.0.0.1'
USER_ID = '57d2055a86c27339ffdee4cc'
TO_NODE_ID = '57ec57be86c27345b3f8a159'

test_client = Client(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    fingerprint=FINGERPRINT,
    ip_address=IP_ADDRESS,
    development_mode=True,
    logging=False
)
