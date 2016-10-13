from .test_helpers import *


class TransactionsTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = self.client.users.create(users_create_payload)
        refresh_payload = {'refresh_token': self.user['refresh_token']}
        self.client.users.refresh(self.user['_id'], refresh_payload)
        response = self.client.nodes.create(self.user['_id'],
                                            ach_us_bank_login_payload)
        self.node = response['nodes'][0]

    def test_create_a_new_transaction(self):
        trans = self.client.transactions.create(self.user['_id'],
                                                self.node['_id'],
                                                trans_create_payload)
        self.assertIsNotNone(trans['_id'])

    def test_get_existing_transaction(self):
        trans = self.client.transactions.create(self.user['_id'],
                                                self.node['_id'],
                                                trans_create_payload)
        trans = self.client.transactions.get(self.user['_id'],
                                             self.node['_id'],
                                             trans['_id'])
        self.assertIsNotNone(trans['_id'])

    def test_get_multiple_transactions(self):
        response = self.client.transactions.get(self.user['_id'],
                                                self.node['_id'])
        self.assertIsNotNone(response['trans'])

    def test_update_transaction_with_comment(self):
        trans = self.client.transactions.create(self.user['_id'],
                                                self.node['_id'],
                                                trans_create_payload)
        response = self.client.transactions.update(self.user['_id'],
                                                   self.node['_id'],
                                                   trans['_id'],
                                                   trans_update_payload)
        trans = response['trans']
        note = trans['recent_status']['note']
        self.assertIsNotNone(trans['_id'])
        self.assertIn(trans_update_payload['comment'], note)

    def test_delete_transaction(self):
        trans = self.client.transactions.create(self.user['_id'],
                                                self.node['_id'],
                                                trans_create_payload)
        response = self.client.transactions.delete(self.user['_id'],
                                                   self.node['_id'],
                                                   trans['_id'])
        self.assertEqual('CANCELED', response['recent_status']['status'])
