import unittest
import pdb
import time
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.subnet import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models.nodes.synapse_us_node import SynapseUsNode
from synapse_pay_rest.models import Subnet
from synapse_pay_rest.errors import *


class SubnetTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)
        self.node = SynapseUsNode.create(self.user, 'Python Test SYNAPSE-US Node')

    def test_create(self):
        subnet = Subnet.create(self.node,
                            'test Subnet')
        self.assertIsInstance(subnet, Subnet)
        self.assertEqual(self.node.id, subnet.node.id)

        other_props = ['client_id', 'client_name', 'account_num', 'allowed',
                       'nickname', 'node_id', 'routing_num_ach', 'routing_num_wire',
                       'user_id']

        for prop in other_props:
            self.assertIsNotNone(getattr(subnet, prop))
  

    def test_by_id(self):
        subnet_id = Subnet.create(self.node,
                                  'ABC123').id
        subnet = Subnet.by_id(self.node, subnet_id)
        self.assertEqual(self.node.id, subnet.node.id)
        self.assertIsInstance(subnet, Subnet)
        self.assertEqual(subnet_id, subnet.id)

    def test_all(self):
        Subnet.create(self.node, 'ABC123')
        Subnet.create(self.node, 'DEF456')
        Subnet.create(self.node, 'testing')
        Subnet.create(self.node, 'test')

        subnets = Subnet.all(self.node)
        self.assertEqual(4, len(subnets))
        self.assertIsInstance(subnets[0], Subnet)
        self.assertEqual(self.node.id, subnets[0].node.id)
        # with params
        per_page = 2
        page1 = Subnet.all(self.node, page=1, per_page=per_page)
        page2 = Subnet.all(self.node, page=2, per_page=per_page)
        self.assertNotEqual(page1[0].id, page2[0].id)
        self.assertEqual(per_page, len(page1))

    def test_lock(self):
        subnet = Subnet.create(self.node,
                               'Test Subnet')
        response = subnet.lock()
        self.assertEqual('LOCKED', response.allowed )

