import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models import BaseDocument


class UserTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)

    def test_edit_base_document(self):
        args = {
            'email': 'scoobie@doo.com',
            'phone_number': '707-555-5555',
            'ip': '127.0.0.1',
            'name': 'Doctor BaseDoc',
            'aka': 'Basey',
            'entity_type': 'F',
            'entity_scope': 'Arts & Entertainment',
            'birth_day': 28,
            'birth_month': 2,
            'birth_year': 1990,
            'address_street': '42 Base Blvd',
            'address_city': 'San Francisco',
            'address_subdivision': 'CA',
            'address_postal_code': '94114',
            'address_country_code': 'US'
        }
        base_document = self.user.add_base_document(**args)
        base_document = base_document.update(entity_scope='Lawyer')
        self.assertIsInstance(base_document, BaseDocument)
