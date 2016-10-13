from .test_helpers import *


class ErrorsTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client

    def test_404_error(self):
        user_id = '11111111111111'
        with self.assertRaises(NotFoundError):
            self.client.users.get(user_id)
