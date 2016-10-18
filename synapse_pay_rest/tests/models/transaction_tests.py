import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.trans import *
from synapse_pay_rest.models.user import User
# from synapse_pay_rest.models.node import Node
from synapse_pay_rest.models.nodes.ach_us_node import AchUsNode
from synapse_pay_rest.models.transaction import Transaction


class TransactionTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)
        self.nodes = AchUsNode.create_via_bank_login(self.user,
                                                     'bofa',
                                                     'synapse_nomfa',
                                                     'test1234')
        self.from_node = self.nodes[0]
        self.to_node = self.nodes[1]

    def test_create(self):
        transaction = Transaction.create(self.from_node,
                                         self.to_node.type,
                                         self.to_node.id,
                                         1.00,
                                         'USD',
                                         '127.0.0.1',
                                         supp_id='ABC123')
        self.assertIsInstance(transaction, Transaction)
        # for prop in kwargs:
        #     self.assertIsNotNone(getattr(node, prop))

        other_props = ['node', 'amount', 'client_id', 'client_name',
                       'created_on', 'ip', 'latlon', 'note', 'process_on',
                       'supp_id', 'webhook', 'fees', 'recent_status',
                       'from_info', 'to_info', 'to_type', 'to_id']
        for prop in other_props:
            self.assertIsNotNone(getattr(transaction, prop))

    # def test_by_id(self):
    #     pass

    # def test_all(self):
    #     pass

    # def test_add_comment(self):
    #     pass

    # def test_cancel(self):
    #     pass
