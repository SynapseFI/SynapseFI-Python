# Basic wrapper around the the requests library.
from http_client import *
# Assign all the api classes
from api.User import *
from api.Trans import *
from api.Node import *

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
		if options.has_key('development_mode'):
			if options['development_mode']:
				base_url = 'https://sandbox.synapsepay.com/api/3/users'

		self.client = HttpClient(options, user_id)
		self.User = User(self.client)
		self.Node = Node(self.client)
		self.Trans = Trans(self.client)
