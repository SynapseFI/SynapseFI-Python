from .http_client import HttpClient
from .api.users import Users
from .api.trans import Trans
from .api.nodes import Nodes
from .api.subnets import Subnets
from .api.subscriptions import Subscriptions
from .api.client import ClientEndpoint
from .api.atms import Atms

class Client():
    """Handles configuration and requests to the SynapsePay API.
    """

    def __init__(self, **kwargs):
        """Create a new API client.

        Args:
            client_id (str): your API client id
            client_secret (str): your API client secret
            fingerprint (str): the user's fingerprint
            ip_address (str): the user's IP address
            development_mode (bool): if True, requests sent to sandbox
            endpoints (else production)
            logging (bool): if True, requests logged to stdout

        Todo:
            Allow logging to file
        """
        self.base_url = 'https://api.synapsefi.com/v3.1'
        if kwargs.get('development_mode'):
            self.base_url = 'https://uat-api.synapsefi.com/v3.1'

        self.http_client = HttpClient(base_url=self.base_url, **kwargs)
        self.users = Users(self.http_client)
        self.nodes = Nodes(self.http_client)
        self.trans = Trans(self.http_client)
        self.subnets = Subnets(self.http_client)
        self.subscriptions = Subscriptions(self.http_client)
        self.client_endpoint = ClientEndpoint(self.http_client)
        self.atms = Atms(self.http_client)

    def __repr__(self):
        return '{0}(base_url={1})'.format(self.__class__, self.base_url)