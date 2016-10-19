import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.models import User
from synapse_pay_rest.models import BaseDocument
from synapse_pay_rest.models import PhysicalDocument
from synapse_pay_rest.models import SocialDocument
from synapse_pay_rest.models import VirtualDocument


class DocumentTestCases(unittest.TestCase):
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

    def test_physical_document_with_bytestream(self):
        type = 'GOVT_ID'
        file_path = ('/Users/Synapsepay/Documents/libraries/'
                     'SynapsePayRest-Python/synapse_pay_rest/'
                     'tests/fixtures/test.png')
        byte_stream = open(file_path, 'rb').read()
        doc = self.base_document.add_physical_document(type=type,
                                                       byte_stream=byte_stream,
                                                       mime_type='img/png')
        self.assertIsInstance(doc, PhysicalDocument)

    def test_physical_document_with_file_path(self):
        type = 'GOVT_ID'
        file_path = ('/Users/Synapsepay/Documents/libraries/'
                     'SynapsePayRest-Python/synapse_pay_rest/'
                     'tests/fixtures/test.png')
        doc = self.base_document.add_physical_document(type=type,
                                                       file_path=file_path)
        self.assertIsInstance(doc, PhysicalDocument)

    def test_physical_document_with_url(self):
        type = 'GOVT_ID'
        url = 'https://cdn.synapsepay.com/static_assets/logo@2x.png'
        doc = self.base_document.add_physical_document(type=type, url=url)
        self.assertIsInstance(doc, PhysicalDocument)

    # def test_virtual_document_with_valid_ssn(self):
    #     pass

    # def test_virtual_document_with_invalid_ssn(self):
    #     pass

    # def test_virtual_document_with_ssn_mfa(self):
    #     pass
