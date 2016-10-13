import unittest
from .test_helpers import *


class ClientTestCases(unittest.TestCase):
    def setUp(self):
        self.client = Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            fingerprint=FINGERPRINT,
            ip_address=IP_ADDRESS,
            development_mode=True,
            logging=True
        )

    def test_attrs_are_set(self):
        self.assertIsInstance(self.client.http_client, HttpClient)
        self.assertIsInstance(self.client.users, Users)
        self.assertIsInstance(self.client.nodes, Nodes)
        self.assertIsInstance(self.client.transactions, Transactions)

    def test_passes_correct_base_url_to_http_client(self):
        sandbox = 'https://sandbox.synapsepay.com/api/3'
        production = 'https://synapsepay.com/api/3'
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
