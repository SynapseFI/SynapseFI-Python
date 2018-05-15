import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.atm import *
from synapse_pay_rest.client import Client
from synapse_pay_rest.models import Atm


class AtmTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_locate_zip(self):
        atms = Atm.locate(self.client, **atm_args)
        atm = atms[0]
        properties = ['client', 'address_city', 'address_country', 'address_postal_code', 'address_state', 'address_street',
                      'latitude', 'longitude', 'id', 'isAvailable24Hours', 'isDepositAvailable', 'isHandicappedAccessible', 'isOffPremise',
                      'isSeasonal','locationDescription', 'logoName', 'name', 'distance']
        self.assertIsInstance(atms[0], Atm)
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(atm, prop))

    def test_locate_lat_lon(self):
        atms = Atm.locate(self.client, **atm_args2)
        atm = atms[0]
        properties = ['client', 'address_city', 'address_country', 'address_postal_code', 'address_state', 'address_street',
                      'latitude', 'longitude', 'id', 'isAvailable24Hours', 'isDepositAvailable', 'isHandicappedAccessible', 'isOffPremise',
                      'isSeasonal','locationDescription', 'logoName', 'name', 'distance']
        self.assertIsInstance(atms[0], Atm)
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(atm, prop))
