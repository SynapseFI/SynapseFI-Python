import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models import BaseDocument
from synapse_pay_rest.models import PhysicalDocument
from synapse_pay_rest.models import SocialDocument
from synapse_pay_rest.models import VirtualDocument


class BaseDocumentTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)
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
        self.base_document = self.user.add_base_document(**args)

    def test_edit_base_document(self):
        base_document = self.base_document.update(entity_scope='Lawyer')
        self.assertIsInstance(base_document, BaseDocument)

    def test_add_physical_documents(self):
        type = 'GOVT_ID'
        value = 'data:text/csv;base64,SUQs=='
        physical_doc = self.base_document.add_physical_document(type=type,
                                                                value=value)
        self.assertIsInstance(physical_doc, PhysicalDocument)
        self.assertEqual(physical_doc.type, type)
        self.assertEqual(self.base_document.id, physical_doc.base_document.id)

        properties = ['type', 'id', 'status', 'last_updated']
        for prop in properties:
            self.assertIsNotNone(getattr(physical_doc, prop))

    def test_add_social_documents(self):
        type = 'FACEBOOK'
        value = 'facebook.com/barnabus'
        social_doc = self.base_document.add_social_document(type=type,
                                                            value=value)
        self.assertIsInstance(social_doc, SocialDocument)
        self.assertEqual(social_doc.type, type)
        self.assertEqual(self.base_document.id, social_doc.base_document.id)

        properties = ['type', 'id', 'status', 'last_updated']
        for prop in properties:
            self.assertIsNotNone(getattr(social_doc, prop))

    def test_add_virtual_documents(self):
        type = 'SSN'
        value = '2222'
        virtual_doc = self.base_document.add_virtual_document(type=type,
                                                              value=value)
        self.assertIsInstance(virtual_doc, VirtualDocument)
        self.assertEqual(virtual_doc.type, type)
        self.assertEqual(self.base_document.id, virtual_doc.base_document.id)

        properties = ['type', 'id', 'status', 'last_updated']
        for prop in properties:
            self.assertIsNotNone(getattr(virtual_doc, prop))
