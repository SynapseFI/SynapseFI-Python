import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.client import Client
from synapse_pay_rest.models import Institution


class InstitutionTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_find_institutions(self):
        institutions = Institution.find(self.client)
        institution = institutions[0]
        properties = ['client', 'bank_code', 'bank_name', 'features', 'forgotten_password', 'is_active', 'logo', 'tx_history_months']
        self.assertIsInstance(institution, Institution)

        for prop in properties:
            self.assertIsNotNone(getattr(institution, prop))
