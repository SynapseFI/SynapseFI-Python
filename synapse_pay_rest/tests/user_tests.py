import unittest
from unittest import TestCase, mock

from synapse_pay_rest.tests.fixtures.test_client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.models.users.user import User
from synapse_pay_rest.api.users import Users

class UserTests(TestCase):

	def setUp(self):
		self.user = User.from_response(test_client, user_from_response, oauth=False)

	@mock.patch('synapse_pay_rest.api.Users.update', autospec=True)
	def test_add_documents(self, mock_update):
		mock_update.return_value = docs_response
		user = self.user.add_documents(test_docs)
		self.assertIsInstance(user, User)

	@mock.patch('synapse_pay_rest.api.Users.refresh', autospec=True)
	def test_select_2fa_device(self, mock_refresh):
		pass

	@mock.patch('synapse_pay_rest.api.Users.refresh', autospec=True)
	def test_confirm_2fa_pin(self, mock_refresh):
		pass

if __name__ == '__main__':
	unittest.main()