import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.subnet import *


class SubnetsTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = self.client.users.create(users_create_payload)
        refresh_payload = {'refresh_token': self.user['refresh_token']}
        self.client.users.refresh(self.user['_id'], refresh_payload)
        response = self.client.nodes.create(self.user['_id'],
                                            nodes_create_payload)
        self.node = response['nodes'][0]

    def test_create_a_new_subnet(self):
        subnet = self.client.subnets.create(self.user['_id'],
                                         self.node['_id'],
                                         subnet_create_payload)
        self.assertIsNotNone(subnet['_id'])

    def test_get_existing_subnet(self):
        subnet = self.client.subnets.create(self.user['_id'],
                                         self.node['_id'],
                                         subnet_create_payload)
        subnet = self.client.subnets.get(self.user['_id'],
                                      self.node['_id'],
                                      subnet['_id'])
        self.assertIsNotNone(subnet['_id'])

    def test_get_multiple_subnets(self):
        response = self.client.subnets.get(self.user['_id'],
                                         self.node['_id'])
        self.assertIsNotNone(response['subnets'])

    def test_lock_subnet(self):
        subnet = self.client.subnets.create(self.user['_id'],
                                         self.node['_id'],
                                         subnet_create_payload)
        subnet = self.client.subnets.update(self.user['_id'],
                                         self.node['_id'],
                                         subnet['_id'],
                                         subnet_update_payload)
        note = subnet['allowed']
        self.assertIsNotNone(subnet['_id'])
        self.assertIn(subnet_update_payload['allowed'], note)

