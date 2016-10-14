from .test_helpers import *


class UserTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client

    def test_create(self):
        user = User.create(self.client, **user_create_args)
        properties = ['client', 'id', 'refresh_token', 'logins',
                      'phone_numbers', 'legal_names', 'permission',
                      'supp_id', 'is_business', 'cip_tag']
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(user, prop))

    def test_by_id(self):
        user_id = User.create(self.client, **user_create_args).id
        user = User.by_id(self.client, user_id)
        self.assertIsInstance(user, User)
        self.assertEqual(user_id, user.id)

    def test_all(self):
        users = User.all(self.client)
        self.assertIsInstance(users, list)
        self.assertIsInstance(users[0], User)
