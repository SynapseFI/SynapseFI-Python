import unittest
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.subscription import *


class SubscriptionsTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_create_a_new_subscription(self):
        subscription = self.client.subscriptions.create(subscription_create_payload)
        self.assertIsNotNone(subscription['_id'])

    def test_get_existing_subscription(self):
        subscription = self.client.subscriptions.create(subscription_create_payload)
        subscription = self.client.subscriptions.get(subscription['_id'])
        self.assertIsNotNone(subscription['_id'])

    def test_get_multiple_subscriptions(self):
        subscriptions = self.client.subscriptions.get()['subscriptions']
        self.assertIsInstance(subscriptions, list)

    def test_update_subscription_info(self):
        subscription = self.client.subscriptions.create(subscription_create_payload)
        payload = subscription_update_payload
        subscription = self.client.subscriptions.get(subscription['_id'])
        subscription = self.client.subscriptions.update(subscription['_id'], payload)
        self.assertIsNotNone(subscription['_id'])
        self.assertEqual(['USERS|POST'], subscription['scope'])