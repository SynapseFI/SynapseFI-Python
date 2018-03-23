import unittest
import pdb
import time
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.trans import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models.nodes.ach_us_node import AchUsNode
from synapse_pay_rest.models.nodes.synapse_us_node import SynapseUsNode
from synapse_pay_rest.models import Transaction
from synapse_pay_rest.errors import *


class TransactionTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)
        self.nodes = AchUsNode.create_via_bank_login(self.user,
                                                     'fake',
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
        self.assertEqual(self.from_node.id, transaction.node.id)

        other_props = ['node', 'amount', 'client_id', 'client_name',
                       'created_on', 'ip', 'latlon', 'note', 'process_on',
                       'supp_id', 'fees', 'recent_status',
                       'from_info', 'to_info', 'to_type', 'to_id', 'supp_id',
                       'currency']
        for prop in other_props:
            self.assertIsNotNone(getattr(transaction, prop))

    def test_create_with_idempotency_key(self):
        idempotency_key = str(time.time())
        transaction = Transaction.create(self.from_node,
                                         self.to_node.type,
                                         self.to_node.id,
                                         1.00,
                                         'USD',
                                         '127.0.0.1',
                                         idempotency_key=idempotency_key,
                                         supp_id='ABC123')
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(self.from_node.id, transaction.node.id)

        other_props = ['node', 'amount', 'client_id', 'client_name',
                       'created_on', 'ip', 'latlon', 'note', 'process_on',
                       'supp_id', 'fees', 'recent_status',
                       'from_info', 'to_info', 'to_type', 'to_id', 'supp_id',
                       'currency']
        for prop in other_props:
            self.assertIsNotNone(getattr(transaction, prop))

        with self.assertRaises(ConflictError):
            Transaction.create(self.from_node,
                               self.to_node.type,
                               self.to_node.id,
                               1.00,
                               'USD',
                               '127.0.0.1',
                               idempotency_key=idempotency_key,
                               supp_id='ABC123')

    def test_create_with_fees(self):
        fee_node = SynapseUsNode.create(self.user, 'Python Test SYNAPSE-US Node')
        fee_node2 = SynapseUsNode.create(self.user, 'Python Test SYNAPSE-US Node2')
        test_fees = [
            {
                'fee': 0.12,
                'note': 'Test Fee 1',
                'to': {'id': fee_node.id}
            }
        ]
        transaction_id = Transaction.create(self.from_node,
                                         self.to_node.type,
                                         self.to_node.id,
                                         1.00,
                                         'USD',
                                         '127.0.0.1',
                                         supp_id='ABC123',
                                         fees=test_fees).id
        transaction = Transaction.by_id(self.from_node, transaction_id)
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(self.from_node.id, transaction.node.id)
        self.assertEqual(transaction.fees[0]['fee'], 0.12)
        self.assertEqual(len(transaction.fees), 1)

    def test_by_id(self):
        transaction_id = Transaction.create(self.from_node,
                                            self.to_node.type,
                                            self.to_node.id,
                                            1.00,
                                            'USD',
                                            '127.0.0.1',
                                            supp_id='ABC123').id
        transaction = Transaction.by_id(self.from_node, transaction_id)
        self.assertEqual(self.from_node.id, transaction.node.id)
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(transaction_id, transaction.id)

    def test_all(self):
        Transaction.create(self.from_node, self.to_node.type, self.to_node.id,
                           1.00, 'USD', '127.0.0.1', supp_id='ABC123')
        Transaction.create(self.from_node, self.to_node.type, self.to_node.id,
                           1.00, 'USD', '127.0.0.1', supp_id='DEF456')
        Transaction.create(self.from_node, self.to_node.type, self.to_node.id,
                           1.00, 'USD', '127.0.0.1', supp_id='GHI789')
        Transaction.create(self.from_node, self.to_node.type, self.to_node.id,
                           1.00, 'USD', '127.0.0.1', supp_id='KLM000')
        transactions = Transaction.all(self.from_node)
        self.assertEqual(4, len(transactions))
        self.assertIsInstance(transactions[0], Transaction)
        self.assertEqual(self.from_node.id, transactions[0].node.id)
        # with params
        per_page = 2
        page1 = Transaction.all(self.from_node, page=1, per_page=per_page)
        page2 = Transaction.all(self.from_node, page=2, per_page=per_page)
        self.assertNotEqual(page1[0].id, page2[0].id)
        self.assertEqual(per_page, len(page1))

    def test_add_comment(self):
        transaction = Transaction.create(self.from_node,
                                         self.to_node.type,
                                         self.to_node.id,
                                         1.00,
                                         'USD',
                                         '127.0.0.1',
                                         supp_id='ABC123')
        comment = 'mocoso'
        transaction = transaction.add_comment(comment)
        self.assertIn(comment, transaction.recent_status['note'])

    def test_cancel(self):
        transaction = Transaction.create(self.from_node,
                                         self.to_node.type,
                                         self.to_node.id,
                                         1.00,
                                         'USD',
                                         '127.0.0.1',
                                         supp_id='ABC123')
        transaction = transaction.cancel()
        self.assertEqual('CANCELED', transaction.timeline[-1]['status'])
