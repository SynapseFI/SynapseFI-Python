# Basic wrapper around the the requests library.
from synapse_pay_rest.http_client import HttpClient
# Assign all the api classes
from synapse_pay_rest.api.users import Users
from synapse_pay_rest.api.transactions import Trans
from synapse_pay_rest.api.nodes import Nodes


class Client():
    """ Initialize the client to make SynapsePay v3 API calls.
    """

    def __init__(self, user_id=None, **kwargs):
        base_url = 'https://synapsepay.com/api/3'
        if kwargs.get('development_mode'):
            base_url = 'https://sandbox.synapsepay.com/api/3'

        self.http_client = HttpClient(user_id=user_id, base_url=base_url,
                                      **kwargs)
        self.users = Users(self.http_client)
        self.nodes = Nodes(self.http_client)
        self.transactions = Trans(self.http_client)
