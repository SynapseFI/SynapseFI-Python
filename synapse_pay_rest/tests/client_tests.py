import unittest
from synapse_pay_rest.client import Client
from synapse_pay_rest.http_client import HttpClient
from synapse_pay_rest.api.users import Users
from synapse_pay_rest.api.nodes import Nodes
from synapse_pay_rest.api.trans import Trans
from synapse_pay_rest.api.subnets import Subnets
from synapse_pay_rest.tests.fixtures.client import *


class ClientTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            fingerprint=FINGERPRINT,
            ip_address=IP_ADDRESS,
            development_mode=True,
            logging=True
        )

    def test_properties(self):
        self.assertIsInstance(self.client.http_client, HttpClient)
        self.assertIsInstance(self.client.users, Users)
        self.assertIsInstance(self.client.nodes, Nodes)
        self.assertIsInstance(self.client.trans, Trans)
        self.assertIsInstance(self.client.subnets, Subnets)

    def test_passes_correct_base_url_to_http_client(self):
        sandbox = 'https://uat-api.synapsefi.com/v3.1'
        production = 'https://api.synapsefi.com/v3.1'
        self.assertEqual(sandbox, self.client.http_client.base_url)

        prod_client = Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            fingerprint=FINGERPRINT,
            ip_address=IP_ADDRESS,
            development_mode=False,
            logging=True
        )
        self.assertEqual(production, prod_client.http_client.base_url)

    def test_passes_header_info_to_http_client(self):
        headers = self.client.http_client.headers
        gateway = CLIENT_ID + '|' + CLIENT_SECRET
        user = '|' + FINGERPRINT
        self.assertEqual(gateway, headers['X-SP-GATEWAY'])
        self.assertEqual(user, headers['X-SP-USER'])
        self.assertEqual(IP_ADDRESS, headers['X-SP-USER-IP'])
