import unittest
from synapse_pay_rest.errors import *
from synapse_pay_rest.tests.fixtures.client import *


class ErrorsTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    # TODO. Build an actual Response object manually?
    # def test_400_error(self):
    #     response = {
    #         'error': {
    #             'en': "Unable to verify document information. Please submit a valid copy of passport/driver's license."
    #         },
    #         'error_code': '400',
    #         'http_code': '409',
    #         'success': False
    #     }
    #     error = ErrorFactory.from_response(response)
    #     self.assertEqual(response['error']['en'], error.message)
    #     self.assertEqual(response['error_code'], error.code)
    #     self.assertIsInstance(error, NotFoundError)

    def test_not_found_error(self):
        user_id = '11111111111111'
        with self.assertRaises(NotFoundError):
            self.client.users.get(user_id)
