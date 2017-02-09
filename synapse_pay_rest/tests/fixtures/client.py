import os
from synapse_pay_rest.client import Client

CLIENT_ID = os.environ['TEST_CLIENT_ID']
CLIENT_SECRET = os.environ['TEST_CLIENT_SECRET']
FINGERPRINT = 'test_fp'
IP_ADDRESS = '127.0.0.1'

test_client = Client(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    fingerprint=FINGERPRINT,
    ip_address=IP_ADDRESS,
    development_mode=True,
    logging=False
)
