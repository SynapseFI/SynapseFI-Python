from synapse_pay_rest.http_client import HttpClient


class Atms():
    """Abstraction of the /nodes/atm endpoint.

    Used to make atm location-related calls to the API.
    https://docs.synapsefi.com/docs/locate-atms
    """

    def __init__(self, client):
        self.client = client

    def locate(self, **kwargs):
        
        path = '/nodes/atms?'
        response = self.client.get(path, **kwargs)
        return response