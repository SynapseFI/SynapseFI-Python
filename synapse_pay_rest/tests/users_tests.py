from .test_helpers import *
from .payloads.user_payloads import *


class UsersTestCases(unittest.TestCase):
    def setUp(self):
        self.client = Client(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            fingerprint=FINGERPRINT,
            ip_address=IP_ADDRESS,
            development_mode=True,
            logging=False
        )

    def test_create_a_new_user(self):
        user = self.client.users.create(users_create_payload)
        self.assertIsNotNone(user['_id'])

    def test_get_existing_user(self):
        user = self.client.users.get(USER_ID)
        self.assertIsNotNone(user['_id'])

    def test_get_multiple_users(self):
        users = self.client.users.get()['users']
        self.assertIsInstance(users, list)

    def test_update_user_info(self):
        payload = users_update_payload
        user = self.client.users.get(USER_ID)
        payload['refresh_token'] = user['refresh_token']
        new_login = payload['update']['login']['email']
        user = self.client.users.update(USER_ID, payload)
        self.assertIsNotNone(user['_id'])
        self.assertEqual(new_login, user['logins'][-1]['email'])
