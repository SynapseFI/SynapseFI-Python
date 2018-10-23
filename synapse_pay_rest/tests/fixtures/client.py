import os
import sys
from synapse_pay_rest.client import Client

if sys.version_info[0] >= 3:
  try:
    CLIENT_ID = os.environ['TEST_CLIENT_ID']
    CLIENT_SECRET = os.environ['TEST_CLIENT_SECRET']
  except KeyError:
    CLIENT_ID = input("Please enter client ID: ")
    CLIENT_SECRET = input("Please enter client secret: ")
else:
    try:
      CLIENT_ID = os.environ['TEST_CLIENT_ID']
      CLIENT_SECRET = os.environ['TEST_CLIENT_SECRET']
    except KeyError:
      CLIENT_ID = raw_input("Please enter client ID: ")
      CLIENT_SECRET = raw_input("Please enter client secret: ")

FINGERPRINT = 'INPUT_USER_FINGERPRINT_HERE'

IP_ADDRESS = '127.0.0.1'

test_client = Client(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    fingerprint=FINGERPRINT,
    ip_address=IP_ADDRESS,
    development_mode=True,
    logging=False
)
