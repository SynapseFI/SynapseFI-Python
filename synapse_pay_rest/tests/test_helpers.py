import unittest
import pdb
import os
from pprint import pprint
from synapse_pay_rest.client import Client
from synapse_pay_rest.http_client import HttpClient
from synapse_pay_rest.api.users import Users
from synapse_pay_rest.api.transactions import Transactions
from synapse_pay_rest.api.nodes import Nodes

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
FINGERPRINT = os.environ['FINGERPRINT']
IP_ADDRESS = '127.0.0.1'
USER_ID = '57d2055a86c27339ffdee4cc'
TO_NODE_ID = '57ec57be86c27345b3f8a159'
