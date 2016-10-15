from .test_helpers import *


class UserTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client

    # def test_create(self):
    #     user = User.create(self.client, **user_create_args)
    #     properties = ['client', 'id', 'refresh_token', 'logins',
    #                   'phone_numbers', 'legal_names', 'permission',
    #                   'supp_id', 'is_business', 'cip_tag']
    #     # check properties assigned
    #     for prop in properties:
    #         self.assertIsNotNone(getattr(user, prop))

    # def test_by_id(self):
    #     user_id = User.create(self.client, **user_create_args).id
    #     user = User.by_id(self.client, user_id)
    #     self.assertIsInstance(user, User)
    #     self.assertEqual(user_id, user.id)

    # def test_all(self):
    #     users = User.all(self.client)
    #     self.assertIsInstance(users, list)
    #     self.assertIsInstance(users[0], User)
    #     # with params
    #     query = "test"
    #     per_page = 5
    #     page1 = User.all(self.client, query=query, page=1, per_page=per_page)
    #     page2 = User.all(self.client, query=query, page=2, per_page=per_page)
    #     self.assertNotEqual(page1[0].id, page2[0].id)
    #     self.assertEqual(per_page, len(page1))
    #     # TODO should test query in legal names or emails

    # def test_add_legal_name(self):
    #     user = User.create(self.client, **user_create_args)
    #     new_name = "Barb Holland"
    #     self.assertNotIn(new_name, user.legal_names)
    #     user = user.add_legal_name(new_name)
    #     self.assertIn(new_name, user.legal_names)

    # def test_add_and_remove_login(self):
    #     user = User.create(self.client, **user_create_args)
    #     email = 'foo@foo.com'
    #     # add login
    #     user = user.add_login(email, password='letmein', read_only=True)
    #     self.assertEqual(2, len(user.logins))
    #     self.assertEqual(email, user.logins[-1]['email'])
    #     self.assertEqual('READ', user.logins[-1]['scope'])
    #     # remove login
    #     user = user.remove_login(email)
    #     self.assertEqual(1, len(user.logins))

    def test_add_and_remove_phone_number(self):
        user = User.create(self.client, **user_create_args)
        phone_number = '4155555555'
        # add phone number
        user = user.add_phone_number(phone_number)
        self.assertEqual(2, len(user.phone_numbers))
        self.assertEqual(phone_number, user.phone_numbers[-1])
        # remove phone number
        user = user.remove_phone_number(phone_number)
        self.assertNotIn(phone_number, user.phone_numbers)
