from synapse_pay_rest.http_client import HttpClient


class Nodes():
    """Abstraction of the /nodes endpoint.

    Used to make node-related calls to the API.
    https://docs.synapsepay.com/docs/node-resources
    """

    def __init__(self, client):
        self.client = client

    def create_node_path(self, user_id, node_id=None):
        """Construct the correct URL for the request."""
        path = '/users/{0}/nodes'.format(user_id)
        if node_id:
            return path + '/' + node_id
        else:
            return path

    def create(self, user_id, payload):
        """Create a node record via POST request to the API.

        There is a section in the docs describing the format of the request for
        each node type.

        Args:
            user_id (str): id of the user to whom the node will belong
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: JSON data from response body (single node record)
        """
        path = self.create_node_path(user_id)
        response = self.client.post(path, payload)
        return response

    def get(self, user_id, node_id=None, **params):
        """Retrieve a single or multiple node records via GET request to the API.

        https://docs.synapsepay.com/docs/nodes
        https://docs.synapsepay.com/docs/node

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): if specified the method returns a single node
            **params: valid params are 'type', 'page', 'per_page', 'full_dehydrate'

        Returns:
            dict: response body (single or multiple node records)
        """
        path = self.create_node_path(user_id, node_id)
        response = self.client.get(path, **params)
        return response

    def update(self, user_id, node_id, payload):
        """Updates a node record via PATCH request to the API.

        Used to edit node information (verify microdeposits).

        https://docs.synapsepay.com/docs/verify-micro-deposit

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the node to update
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single node record)
        """
        path = self.create_node_path(user_id, node_id)
        response = self.client.patch(path, payload)
        return response

    def verify(self, user_id, payload, node_id=None, **kwargs):
        """[DEPRECATED] Verify microdeposits or answer MFA, depending on args.

        Instead use update for verifying microdeposits or create/post to answer
        MFA.
        """
        if node_id:
            # PATCH to verify microdeposits
            self.update(user_id, payload, node_id, **kwargs)
        else:
            # POST to verify MFA
            path = self.create_node_path(user_id)
            response = self.client.post(path, payload)
        return response

    def delete(self, user_id, node_id):
        """Deactivate a node.

        The node will not appear in results and will not be available to create
        new transactions.

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the node to delete

        Returns:
            dict: response body (a confirmation message)
        """
        path = self.create_node_path(user_id, node_id)
        response = self.client.delete(path)
        return response
