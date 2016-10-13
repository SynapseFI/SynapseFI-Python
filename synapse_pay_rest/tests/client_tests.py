import unittest
from synapse_pay_rest.client import Client
from .test_helpers import *


# class ClientTestCases(unittest.TestCase):
#     def setUp(self):
#         self.http_client = HttpClient(
#             client_id=CLIENT_ID,
#             client_secret=CLIENT_SECRET,
#             fingerprint=FINGERPRINT,
#             ip_address=IP_ADDRESS,
#             base_url='https://sandbox.synapsepay.com/api/3',
#             log_requests=True
#         )

#     def test_attrs_are_set(self):
#         assertEqual('https://sandbox.synapsepay.com/api/3',
#                     self.http_client.base_url)
#         assertTrue(self.http_client.logging)

#     def test_headers_are_properly_formatted(self):
#         headers = self.http_client.headers
#         gateway = CLIENT_ID + '|' + CLIENT_SECRET
#         user = '|' + FINGERPRINT
#         self.assertEqual(gateway, headers['X-SP-GATEWAY'])
#         self.assertEqual(user, headers['X-SP-USER'])
#         self.assertEqual(IP_ADDRESS, headers['X-SP-USER-IP'])

    # def test_update_headers_updates_the_specified_kwargs(self):
    #     http_client = self.http_client
    #     new_oauth_key = 'oauth_key'
    #     http_client.update_headers(oauth_key=new_oauth_key)
    #     headers = http_client.generate_headers()
    #     gateway = CLIENT_ID + '|' + CLIENT_SECRET
    #     user = new_oauth_key + '|' + FINGERPRINT
    #     self.assertEqual(gateway, headers['X-SP-GATEWAY'])
    #     self.assertEqual(user, headers['X-SP-USER'])
    #     self.assertEqual(IP_ADDRESS, headers['X-SP-USER-IP'])
