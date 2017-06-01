import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.client import Client
from synapse_pay_rest.models import User
from synapse_pay_rest.models import BaseDocument


class UserTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_create(self):
        user = User.create(self.client, **user_create_args)
        properties = ['client', 'id', 'refresh_token', 'logins',
                      'phone_numbers', 'legal_names', 'permission',
                      'supp_id', 'is_business', 'cip_tag']
        self.assertEqual(self.client, user.client)
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(user, prop))

    def test_create_with_add_base_doc(self):
        base_doc = User.build_base_doc(**user_base_doc)
        user_create_args['base_doc'] = base_doc
        user = User.create(self.client, **user_create_args)
        self.assertEqual(self.client, user.client)
        print(user.base_documents)
        self.assertEqual(len(user.base_documents), 1)

    def test_by_id(self):
        user_id = User.create(self.client, **user_create_args).id
        user = User.by_id(self.client, user_id)
        self.assertIsInstance(user, User)
        self.assertEqual(user_id, user.id)

    def test_all(self):
        users = User.all(self.client)
        self.assertIsInstance(users, list)
        self.assertIsInstance(users[0], User)
        self.assertIsInstance(users[0].client, Client)
        # no duplicate clients on different users
        self.assertNotEqual(users[0].client, users[1].client)
        # with params
        query = "test"
        per_page = 5
        page1 = User.all(self.client, query=query, page=1, per_page=per_page)
        page2 = User.all(self.client, query=query, page=2, per_page=per_page)
        self.assertNotEqual(page1[0].id, page2[0].id)
        self.assertEqual(per_page, len(page1))
        # TODO test that query is substring of legal names or emails

    def test_add_and_remove_legal_name(self):
        user = User.create(self.client, **user_create_args)
        new_name = "Barb Holland"
        self.assertNotIn(new_name, user.legal_names)
        # add legal name
        user = user.add_legal_name(new_name)
        self.assertIn(new_name, user.legal_names)
        # remove legal name
        user = user.remove_legal_name(new_name)
        self.assertNotIn(new_name, user.legal_names)

    def test_add_and_remove_login(self):
        user = User.create(self.client, **user_create_args)
        email = 'foo@foo.com'
        # add login
        user = user.add_login(email, password='letmein', read_only=True)
        self.assertEqual(email, user.logins[-1]['email'])
        self.assertEqual('READ', user.logins[-1]['scope'])
        # remove login
        user = user.remove_login(email)
        # TODO: update to loop through logins and check each dict for email
        self.assertEqual(1, len(user.logins))

    def test_add_and_remove_phone_number(self):
        user = User.create(self.client, **user_create_args)
        phone_number = '4155555555'
        # add phone number
        user = user.add_phone_number(phone_number)
        self.assertEqual(2, len(user.phone_numbers))
        self.assertIn(phone_number, user.phone_numbers)
        # remove phone number
        user = user.remove_phone_number(phone_number)
        self.assertNotIn(phone_number, user.phone_numbers)

    def test_update_cip_tag(self):
        user = User.create(self.client, **user_create_args)
        self.assertEqual(1, user.cip_tag)
        new_cip = 3
        user = user.change_cip_tag(new_cip)
        self.assertEqual(new_cip, user.cip_tag)

    def test_add_base_document(self):
        user = User.create(self.client, **user_create_args)
        self.assertFalse(user.base_documents)
        self.assertEqual('UNVERIFIED', user.permission)
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
        base_document = user.add_base_document(**args)
        user = base_document.user
        self.assertEqual(1, len(user.base_documents))
        self.assertIsInstance(user.base_documents[0], BaseDocument)
        self.assertEqual(user.base_documents[0], base_document)
        self.assertEqual(user, base_document.user)
        properties = ['id', 'user', 'name', 'permission_scope',
                      'physical_documents', 'social_documents',
                      'virtual_documents']
        for prop in properties:
            self.assertIsNotNone(getattr(base_document, prop))

    def test_fingerprint_registration(self):
        user = User.create(self.client, **user_create_args)

        devices = user.register_fingerprint('static_pin')
        self.assertIsInstance(devices, list)
        self.assertGreater(len(devices), 0)

        confirmation = user.select_2fa_device(devices[0])
        self.assertTrue(confirmation)

        confirmation = user.confirm_2fa_pin(device=devices[0], pin='123456')
        self.assertTrue(confirmation)
