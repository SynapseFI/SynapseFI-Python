import unittest
from synapse_pay_rest.http_client import HttpClient
from synapse_pay_rest.tests.fixtures.client import *


class HttpClientTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.http_client = HttpClient(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            fingerprint=FINGERPRINT,
            ip_address=IP_ADDRESS,
            base_url='https://uat-api.synapsefi.com/v3.1',
            logging=True
        )

    def test_properties_are_set(self):
        self.assertEqual('https://uat-api.synapsefi.com/v3.1',
                         self.http_client.base_url)
        self.assertTrue(self.http_client.logging)

    def test_headers_are_properly_formatted(self):
        headers = self.http_client.headers
        gateway = CLIENT_ID + '|' + CLIENT_SECRET
        user = '|' + FINGERPRINT
        self.assertEqual(gateway, headers['X-SP-GATEWAY'])
        self.assertEqual(user, headers['X-SP-USER'])
        self.assertEqual(IP_ADDRESS, headers['X-SP-USER-IP'])

    def test_update_headers_changes_the_specified_headers_and_props(self):
        new_oauth_key = 'oauth_key'
        self.http_client.update_headers(oauth_key=new_oauth_key)
        headers = self.http_client.headers
        gateway = CLIENT_ID + '|' + CLIENT_SECRET
        user = new_oauth_key + '|' + FINGERPRINT
        self.assertEqual(gateway, headers['X-SP-GATEWAY'])
        self.assertEqual(user, headers['X-SP-USER'])
        self.assertEqual(IP_ADDRESS, headers['X-SP-USER-IP'])
        self.assertEqual(new_oauth_key, self.http_client.oauth_key)
