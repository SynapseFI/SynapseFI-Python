import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.trans import *


class TransTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = self.client.users.create(users_create_payload)
        refresh_payload = {'refresh_token': self.user['refresh_token']}
        self.client.users.refresh(self.user['_id'], refresh_payload)
        response = self.client.nodes.create(self.user['_id'],
                                            ach_us_bank_login_payload)
        self.node = response['nodes'][0]
        self.to_node = response['nodes'][1]
        trans_create_payload['to']['id'] = self.to_node['_id']

    def test_create_a_new_transaction(self):
        trans = self.client.trans.create(self.user['_id'],
                                         self.node['_id'],
                                         trans_create_payload)
        self.assertIsNotNone(trans['_id'])

    def test_get_existing_transaction(self):
        trans = self.client.trans.create(self.user['_id'],
                                         self.node['_id'],
                                         trans_create_payload)
        trans = self.client.trans.get(self.user['_id'],
                                      self.node['_id'],
                                      trans['_id'])
        self.assertIsNotNone(trans['_id'])

    def test_get_multiple_trans(self):
        response = self.client.trans.get(self.user['_id'],
                                         self.node['_id'])
        self.assertIsNotNone(response['trans'])

    def test_update_transaction_with_comment(self):
        trans = self.client.trans.create(self.user['_id'],
                                         self.node['_id'],
                                         trans_create_payload)
        trans = self.client.trans.update(self.user['_id'],
                                         self.node['_id'],
                                         trans['_id'],
                                         trans_update_payload)
        note = trans['recent_status']['note']
        self.assertIsNotNone(trans['_id'])
        self.assertIn(trans_update_payload['comment'], note)

    def test_delete_transaction(self):
        trans = self.client.trans.create(self.user['_id'],
                                         self.node['_id'],
                                         trans_create_payload)
        response = self.client.trans.delete(self.user['_id'],
                                            self.node['_id'],
                                            trans['_id'])
        self.assertEqual('CANCELED', response['recent_status']['status'])
