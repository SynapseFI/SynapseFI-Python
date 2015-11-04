# Basic wrapper around the the requests library.
from synapse_pay_rest.http_client import HttpClient
# Assign all the api classes
from synapse_pay_rest.api.Users import Users
from synapse_pay_rest.api.Trans import Trans
from synapse_pay_rest.api.Nodes import Nodes


class Client():
    '''
		Initialize the client to make SynapsePay v3 API calls.

		:param options	{
							'client':{
								'client_id':YOUR_CLIENT_ID,
								'client_secret':YOUR_CLIENT_SECRET
							},
							'user':{
								'fingerprint':USER_FINGERPRINT,
							},
							'oauth':{
								'oauth_key':USER_OAUTH_KEY,
								'refresh_token':USER_REFRESH_TOKEN
							}
						}
	'''

    def __init__(self, options, user_id=None):
        base_url = 'https://synapsepay.com/api/3/users'
        if options.get('development_mode', False):
            base_url = 'https://sandbox.synapsepay.com/api/3/users'

        self.client = HttpClient(options, user_id)
        self.Users = Users(self.client)
        self.Nodes = Nodes(self.client)
        self.Trans = Trans(self.client)
