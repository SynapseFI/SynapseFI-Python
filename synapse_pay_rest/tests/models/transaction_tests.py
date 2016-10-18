import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.tests.fixtures.trans import *
from synapse_pay_rest.models.user import User
from synapse_pay_rest.models.node import Node
from synapse_pay_rest.models.transaction import Transaction


class TransactionTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)

    def test_create(self):
        pass

    def test_by_id(self):
        pass

    def test_all(self):
        pass

    def test_add_comment(self):
        pass

    def test_cancel(self):
        pass
