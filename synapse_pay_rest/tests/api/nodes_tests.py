import unittest
from synapse_pay_rest.errors import *
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *


class NodesTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = self.client.users.create(users_create_payload)
        refresh_payload = {'refresh_token': self.user['refresh_token']}
        self.client.users.refresh(self.user['_id'], refresh_payload)

    def test_create_a_new_node(self):
        response = self.client.nodes.create(self.user['_id'],
                                            nodes_create_payload)
        node = response['nodes'][0]
        self.assertIsNotNone(node['_id'])

    def test_get_existing_node(self):
        response = self.client.nodes.create(self.user['_id'],
                                            nodes_create_payload)
        node = response['nodes'][0]
        node = self.client.nodes.get(self.user['_id'], node['_id'])
        self.assertIsNotNone(node['_id'])

    def test_get_multiple_nodes(self):
        response = self.client.nodes.get(self.user['_id'])
        self.assertIsNotNone(response['nodes'])

    def test_update_node_with_microdeposits(self):
        response = self.client.nodes.create(self.user['_id'],
                                            ach_us_create_payload)
        node = response['nodes'][0]
        self.assertEqual('CREDIT', node['allowed'])
        node = self.client.nodes.update(self.user['_id'], node['_id'],
                                        ach_us_micro_payload)
        self.assertEqual('CREDIT-AND-DEBIT', node['allowed'])

    def test_delete_node(self):
        response = self.client.nodes.create(self.user['_id'],
                                            nodes_create_payload)
        node = response['nodes'][0]
        response = self.client.nodes.delete(self.user['_id'], node['_id'])
        self.assertIsNotNone(response['_id'])
