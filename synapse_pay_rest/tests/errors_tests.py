import unittest
from synapse_pay_rest.errors import *
from synapse_pay_rest.tests.fixtures.client import *


class ErrorsTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_404_error(self):
        user_id = '11111111111111'
        with self.assertRaises(NotFoundError):
            self.client.users.get(user_id)
