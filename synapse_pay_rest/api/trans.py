from synapse_pay_rest.http_client import HttpClient


class Trans():
    """Abstraction of the /trans endpoint.

    Used to make transaction-related calls to the API.
    https://docs.synapsepay.com/docs/trans-resources
    """

    def __init__(self, client):
        self.client = client

    def create_trans_path(self, user_id, node_id, trans_id=None):
        """Construct the correct URL for the request."""
        path = '/users/{0}/nodes/{1}/trans'.format(user_id, node_id)
        if trans_id:
            return path + '/' + trans_id
        else:
            return path

    def create(self, user_id, node_id, payload, idempotency_key=None):
        """Create a transaction record via POST request to the API.

        https://docs.synapsepay.com/docs/create-transaction

        Args:
            user_id (str): id of the user to whom the node will belong
            node_id (str): id of the from node
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: JSON data from response body (single node record)
        """
        path = self.create_trans_path(user_id, node_id)
        response = self.client.post(path, payload,
                                    idempotency_key=idempotency_key)
        return response

    def get(self, user_id, node_id, trans_id=None, **params):
        """Retrieve a single or multiple transaction records via GET request.

        https://docs.synapsepay.com/docs/transactions
        https://docs.synapsepay.com/docs/transaction

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the from node
            trans_id (str): if specified the method returns a single transaction
            **params: valid params are 'page', 'per_page'

        Returns:
            dict: response body (single or multiple transaction records)
        """
        path = self.create_trans_path(user_id, node_id, trans_id)
        response = self.client.get(path, **params)
        return response

    def update(self, user_id, node_id, trans_id, payload):
        """Updates a transaction record via PATCH request to the API.

        Used to edit transaction information (add status comment).

        https://docs.synapsepay.com/docs/update-transaction

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the from node
            trans_id (str): id of the transaction to update
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single transaction record)
        """
        path = self.create_trans_path(user_id, node_id, trans_id)
        response = self.client.patch(path, payload)
        return response

    def delete(self, user_id, node_id, trans_id):
        """Cancel a transaction.

        The transaction will still exist but the status will change to
        'CANCELED' if the call is successful.

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the from node
            trans_id (str): id of the transaction to cancel

        Returns:
            dict: response body (a single transaction record)
        """
        path = self.create_trans_path(user_id, node_id, trans_id)
        response = self.client.delete(path)
        return response
