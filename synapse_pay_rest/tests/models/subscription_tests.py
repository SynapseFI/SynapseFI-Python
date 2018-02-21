import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.subscription import *
from synapse_pay_rest.client import Client
from synapse_pay_rest.models import Subscription


class SubscriptionTestCases(unittest.TestCase):
    def setUp(self):
        print('\n{0}.{1}'.format(type(self).__name__, self._testMethodName))
        self.client = test_client

    def test_create(self):
        subscription = Subscription.create(self.client, **subscription_create_payload)
        properties = ['id', 'client_id', 'is_active',
                      'scope', 'url']
        self.assertEqual(self.client, subscription.client)
        # check properties assigned
        for prop in properties:
            self.assertIsNotNone(getattr(subscription, prop))

    def test_by_id(self):
        subscription_id = Subscription.create(self.client, **subscription_create_payload).id
        subscription = Subscription.by_id(self.client, subscription_id)
        self.assertIsInstance(subscription, Subscription)
        self.assertEqual(subscription_id, subscription.id)

    def test_all(self):
        subscriptions = Subscription.all(self.client)
        self.assertIsInstance(subscriptions, list)
        self.assertIsInstance(subscriptions[0], Subscription)
        self.assertIsInstance(subscriptions[0].client, Client)


    def test_update_is_active(self):
        subscription = Subscription.create(self.client, **subscription_create_payload)
        new_is_active = False
        subscription = subscription.update_is_active(new_is_active)
        self.assertEqual(new_is_active, subscription.is_active)


    def test_update_url(self):
        subscription = Subscription.create(self.client, **subscription_create_payload)
        new_url = 'test.com'
        subscription = subscription.update_url(new_url)
        self.assertEqual(new_url, subscription.url)

    def test_update_scope(self):
        subscription = Subscription.create(self.client, **subscription_create_payload)
        new_scope = ["USERS|POST"]
        subscription = subscription.update_scope(new_scope)
        self.assertEqual(new_scope, subscription.scope)



    