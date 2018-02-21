import copy
from synapse_pay_rest.client import Client


class Subscription():
    """Object representation of a subscription record.

    Contains various constructors (instances from existing API records) as well as methods for modifying subscription records 
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        clean_dict = self.__dict__.copy()
        return '{0}({1})'.format(self.__class__, clean_dict)

    @classmethod
    def from_response(cls, client, response):
        """Construct a Subscription from a response dict."""
        return cls(
          client=client,
          json=response,
          id=response['_id'],
          client_id=response['client_id'],
          is_active=response['is_active'],
          scope=response['scope'],
          url=response['url']
        )


    @classmethod
    def multiple_from_response(cls, client, response):
        """Construct multiple Subscriptions from a response dict."""
        subscriptions = [cls.from_response(copy.copy(client), subscription_data)
                 for subscription_data in response]
        return subscriptions

    @staticmethod
    def payload_for_create(scope, url, **kwargs):
        """Build the API 'create subscription' payload from property values."""
        payload = {
            "scope": scope,
            "url": url
        }
        return payload

    @classmethod
    def create(cls, client=None, scope=None, url=None, **kwargs):
        """Create a subscription record in API and corresponding Subscription instance.

        Args:
            client (Client): an instance of the API Client
            scope (arr): scope of the subscription
            url (str) webhook URL

        Returns:
            Subscription: a new Subscription instance
        """
        payload = cls.payload_for_create(scope, url,
                                         **kwargs)
        response = client.subscriptions.create(payload)
        return cls.from_response(client, response)

    @classmethod
    def by_id(cls, client=None, id=None):
        """Retrieve a subscription record by id and create a Subscription instance from it.

        Args:
            client (Client): an instance of the API Client
            id (str): id of the subscription to retrieve

        Returns:
            Subscription: a new Subscription instance
        """
        response = client.subscriptions.get(id)
        return cls.from_response(client, response)

    @classmethod
    def all(cls, client=None, **kwargs):
        """Retrieve all subscription records (limited by pagination) as Subscriptions.

        Args:
            client (Client): an instance of the API Client
            per_page (int, str): (opt) number of records to retrieve
            page (int, str): (opt) page number to retrieve
            query (str): (opt) substring to filter for in user names/emails

        Returns:
            list: containing 0 or more Subscription instances
        """
        response = client.subscriptions.get(**kwargs)
        return cls.multiple_from_response(client, response['subscriptions'])


    # def update(self, **kwargs):
    #     """Build the API 'update subscription' payload from property values."""
    #     payload = {}

    #     if 'is_active' in kwargs:
    #         payload['is_active'] = kwargs['is_active']
    #     if 'url' in kwargs:
    #         payload['url'] = kwargs['url']
    #     if 'scope' in kwargs:
    #         payload['scope'] = kwargs['scope']

    #     response = self.client.subscriptions.update(self.id, payload)
    #     return cls.from_response(client, response)


    def payload_for_update(self, **kwargs):
        payload = {}

        if 'is_active' in kwargs:
            payload['is_active'] = kwargs['is_active']
        if 'url' in kwargs:
            payload['url'] = kwargs['url']
        if 'scope' in kwargs:
            payload['scope'] = kwargs['scope']
        return payload

    def update_url(self, new_url):
        """Update subscription's url

        Args:
            new_url (str): new url

        Returns:
            Subscription: a new Subscription instance
        """
        payload = self.payload_for_update(url=new_url)
        response = self.client.subscriptions.update(self.id, payload)
        return Subscription.from_response(self.client, response)


    def update_scope(self, new_scope):
        """Update subscription's scope

        Args:
            new_scope (str): updated scope

        Returns:
            Subscription: a new Subscription instance
        """
        payload = self.payload_for_update(scope=new_scope)
        response = self.client.subscriptions.update(self.id, payload)
        return Subscription.from_response(self.client, response)

    def update_is_active(self, is_active):
        """Update subscription's url

        Args:
            is_active (bool): active or inactive (T/F)

        Returns:
            Subscription: a new Subscription instance
        """
        payload = self.payload_for_update(is_active= is_active)
        response = self.client.subscriptions.update(self.id, payload)
        return Subscription.from_response(self.client, response)



