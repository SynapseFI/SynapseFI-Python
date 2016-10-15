from .errors import *
from .http_client import HttpClient
from .api.users import Users
from .api.trans import Trans
from .api.nodes import Nodes


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
        self.trans = Trans(self.http_client)
