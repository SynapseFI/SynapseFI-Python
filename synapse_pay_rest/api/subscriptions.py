from synapse_pay_rest.http_client import HttpClient


class Subscriptions():
    """Abstraction of the /subscriptions endpoint.

    Used to make subscription-related calls to the API. It should only ever be
    instantiated by the Client.
    https://docs.synapsepay.com/docs/subscriptions
    """

    def __init__(self, client):
        self.client = client

    def create_subscription_path(self, subscription_id=None):
        """Construct the correct URL for the request."""
        path = '/subscriptions'
        if subscription_id:
            return path + '/' + subscription_id
        else:
            return path

    def create(self, payload):
        """Create a subscription record via POST request to the API.

        https://docs.synapsepay.com/docs/create-subscription

        Args:
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single subscriton record)
        """
        path = self.create_subscription_path()
        response = self.client.post(path, payload)
        return response

    def get(self, subscription_id=None, **params):
        """Retrieve a single or multiple subscriptions records via GET request to the API.

        https://docs.synapsepay.com/docs/subscriptions-1
        https://docs.synapsepay.com/docs/subscription

        Args:
            subscription_id (str): if specified the method returns a single user
            **params: valid params are 'query', 'page', 'per_page', 'full_dehydrate'

        Returns:
            dict: response body (single or multiple subscription records)
        """
        path = self.create_subscription_path(subscription_id)
        response = self.client.get(path, **params)
        return response

    def update(self, subscription_id, payload):
        """Updates a subscription record via PATCH request to the API.

        Used to edit subscription information
        https://docs.synapsepay.com/docs/update-subscription

        Args:
            subscription_id (str): id of the subscription to update
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single subscription record)
        """
        path = self.create_subscription_path(subscription_id)
        response = self.client.patch(path, payload)
        return response


  
