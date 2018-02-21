from synapse_pay_rest.http_client import HttpClient


class Subnets():
    """Abstraction of the /subnets endpoint.

    Used to make subnets-related calls to the API.
    https://docs.synapsepay.com/docs/subnets
    """

    def __init__(self, client):
        self.client = client

    def create_subnet_path(self, user_id, node_id, subnet_id=None):
        """Construct the correct URL for the request."""
        path = '/users/{0}/nodes/{1}/subnets'.format(user_id, node_id)
        if subnet_id:
            return path + '/' + subnet_id
        else:
            return path

    def create(self, user_id, node_id, payload):
        """Create a subnet record via POST request to the API.

        https://docs.synapsepay.com/docs/create-subnet

        Args:
            user_id (str): id of the user to whom the node will belong
            node_id (str): id of the node the subnet belongs to
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: JSON data from response body (single node record)
        """
        path = self.create_subnet_path(user_id, node_id)
        response = self.client.post(path, payload)
        return response

    def get(self, user_id, node_id, subnet_id=None, **params):
        """Retrieve a single or multiple subnet records via GET request.

        https://docs.synapsepay.com/docs/subnets
        https://docs.synapsepay.com/docs/subnet

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the node the subnet belongs to
            subnet_id (str): if specified the method returns a single subnet
            **params: valid params are 'page', 'per_page'

        Returns:
            dict: response body (single or multiple subnet records)
        """
        path = self.create_subnet_path(user_id, node_id, subnet_id)
        response = self.client.get(path, **params)
        return response

    def update(self, user_id, node_id, subnet_id, payload):
        """Updates a subnet record via PATCH request to the API.

        Used to edit subnet information (lock subnet).

        https://docs.synapsepay.com/docs/subnet-1

        Args:
            user_id (str): id of the user the node belongs to
            node_id (str): id of the from node
            subnet_id (str): id of the subnet to update
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single subnet record)
        """
        path = self.create_subnet_path(user_id, node_id, subnet_id)
        response = self.client.patch(path, payload)
        return response
