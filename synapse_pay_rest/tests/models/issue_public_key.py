import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.issue_public_key import *
from synapse_pay_rest.client import Client
from synapse_pay_rest.models import PublicKey


class PublicKeyTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_create(self):
        public_key = PublicKey.issue(self.client, **public_key_create_args)
        properties = ['client', 'client_obj_id', 'expires_at', 'expires_in',
                      'public_key', 'scope']
        self.assertEqual(self.client, public_key.client)
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(public_key, prop))
