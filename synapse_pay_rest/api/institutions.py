from synapse_pay_rest.http_client import HttpClient


class Institutions():
    """Abstraction of the /institutions endpoint.

    Used to make insitution location-related calls to the API.
    https://docs.synapsefi.com/docs/institutions
    """

    def __init__(self, client):
        self.client = client

    def find(self, **kwargs):

        path = '/institutions'
        response = self.client.get(path, **kwargs)
        return response
