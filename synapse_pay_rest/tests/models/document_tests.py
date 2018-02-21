import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models import BaseDocument
from synapse_pay_rest.models import PhysicalDocument
from synapse_pay_rest.models import SocialDocument
from synapse_pay_rest.models import VirtualDocument
from synapse_pay_rest.models import Question
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../fixtures/test.png')


class DocumentTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)
        args = {
            'email': 'scoobie@doo.com',
            'phone_number': '707-555-5555',
            'ip': '127.0.0.1',
            'name': 'Doctor BaseDoc',
            'alias': 'Basey',
            'entity_type': 'F',
            'entity_scope': 'Arts & Entertainment',
            'day': 28,
            'month': 2,
            'year': 1990,
            'address_street': '42 Base Blvd',
            'address_city': 'San Francisco',
            'address_subdivision': 'CA',
            'address_postal_code': '94114',
            'address_country_code': 'US'
        }
        self.base_document = self.user.add_base_document(**args)

    def test_physical_document_with_bytestream(self):
        type = 'GOVT_ID'
        file_path = filename
        byte_stream = open(file_path, 'rb').read()
        doc = self.base_document.add_physical_document(type=type,
                                                       byte_stream=byte_stream,
                                                       mime_type='img/png')
        self.assertIsInstance(doc, PhysicalDocument)

    def test_physical_document_with_file_path(self):
        type = 'GOVT_ID'
        file_path = filename
        doc = self.base_document.add_physical_document(type=type,
                                                       file_path=file_path)
        self.assertIsInstance(doc, PhysicalDocument)

    def test_physical_document_with_url(self):
        type = 'GOVT_ID'
        url = 'https://cdn.synapsepay.com/static_assets/logo@2x.png'
        doc = self.base_document.add_physical_document(type=type, url=url)
        self.assertIsInstance(doc, PhysicalDocument)

    def test_physical_doc_with_url_and_query_params(self):
        type = 'GOVT_ID'
        url = 'https://cdn.synapsepay.com/static_assets/logo@2x.png?testinh=1234'
        doc = self.base_document.add_physical_document(type=type, url=url)
        self.assertEqual(doc.type, type)

    def test_virtual_document_with_valid_ssn(self):
        type = 'SSN'
        value = '2222'
        doc = self.base_document.add_virtual_document(type=type, value=value)
        self.assertIsInstance(doc, VirtualDocument)
        self.assertEqual(doc.type, type)
        self.assertEqual(self.base_document.id, doc.base_document.id)

    def test_virtual_document_with_invalid_ssn(self):
        type = 'SSN'
        value = '1111'
        doc = self.base_document.add_virtual_document(type=type, value=value)
        self.assertIsInstance(doc, VirtualDocument)
        self.assertEqual(doc.type, type)
        self.assertEqual(self.base_document.id, doc.base_document.id)

    @unittest.skip("deprecated")
    def test_virtual_document_with_ssn_mfa(self):
        type = 'SSN'
        value = '3333'
        doc = self.base_document.add_virtual_document(type=type, value=value)
        self.assertIsInstance(doc, VirtualDocument)
        self.assertEqual(doc.type, type)
        self.assertEqual(self.base_document.id, doc.base_document.id)
        self.assertEqual('SUBMITTED|MFA_PENDING', doc.status)
        self.assertIsNotNone(doc.question_set)
        self.assertIsInstance(doc.question_set[0], Question)

        # answer the MFA questions
        for question in doc.question_set:
            question.choice = 1
        doc = doc.submit_kba()
        self.assertIsInstance(doc, VirtualDocument)
        self.assertEqual('SUBMITTED|VALID', doc.status)
