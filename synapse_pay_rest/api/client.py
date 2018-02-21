from synapse_pay_rest.http_client import HttpClient


class ClientEndpoint():
    """Abstraction of the /client endpoint.

    Used to make public key-related calls to the API.
    https://docs.synapsepay.com/docs/issuing-public-key
    """

    def __init__(self, client):
        self.client = client

    def issue_public_key(self, scope):
        path = '/client?issue_public_key=YES&scope=' + scope
        response = self.client.get(path)
        return response