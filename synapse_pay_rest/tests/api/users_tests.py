import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *


class UsersTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_create_a_new_user(self):
        user = self.client.users.create(users_create_payload)
        self.assertIsNotNone(user['_id'])

    def test_get_existing_user(self):
        user = self.client.users.create(users_create_payload)
        user = self.client.users.get(user['_id'])
        self.assertIsNotNone(user['_id'])

    def test_get_multiple_users(self):
        users = self.client.users.get()['users']
        self.assertIsInstance(users, list)

    def test_update_user_info(self):
        user = self.client.users.create(users_create_payload)
        self.client.users.refresh(user['_id'],
                                  {'refresh_token': user['refresh_token']})
        payload = users_update_payload
        user = self.client.users.get(user['_id'])
        payload['refresh_token'] = user['refresh_token']
        new_login = payload['update']['login']['email']
        new_phone = payload['update']['phone_number']
        new_name = payload['update']['legal_name']
        user = self.client.users.update(user['_id'], payload)
        self.assertIsNotNone(user['_id'])
        self.assertEqual(new_login, user['logins'][-1]['email'])
        self.assertIn(new_phone, user['phone_numbers'])
        self.assertIn(new_name, user['legal_names'])
