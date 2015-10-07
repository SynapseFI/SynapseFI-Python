from HelperFunctions import *

NODES_PATH = '/users/{0}/nodes/{1}'

class Node():

	def __init__(self, client):
		self.client = client


	def create_node_path(self, node_id=None):
		if node_id:
			return NODES_PATH.format(self.client.user_id, node_id)
		else:
			return NODES_PATH.replace('/{1}','').format(self.client.user_id)


	def add(self, **kwargs):
		if not 'payload' in kwargs:
			return create_custom_error(message='Set the user id before making this API call.')
		path = self.create_node_path()
		response = self.client.post(path, kwargs['payload'])
		return analyze_response(response)


	def verify(self, **kwargs):
		micro_keys = ['payload', 'node_id']
		ok_micro, error_micro = checkKwargs(micro_keys, kwargs)
		mfa_keys = ['payload']
		ok_mfa, error_mfa = checkKwargs(mfa_keys, kwargs)
		response = None
		if ok_micro:
			path = self.create_node_path(kwargs['node_id'])
			response = self.client.patch(path, kwargs['payload'])
		elif ok_mfa:
			path = self.create_node_path()
			response = self.client.post(path, kwargs['payload'])
		else:
			return error_micro
		return analyze_response(response)	


	def delete(self, **kwargs):
		if not 'node_id' in kwargs:
			return create_custom_error(message='Missing "node_id" argument')
		path = self.create_node_path(kwargs['node_id'])
		response = self.client.delete(path)
		return analyze_response(response)


	def get(self, **kwargs):
		path = None
		if 'node_id' in kwargs:
			path = self.create_node_path(kwargs['node_id'])
		elif self.client.user_id:
			path = self.create_node_path()
		else:
			return create_custom_error(message='Set the user id before making this API call.')
		response = self.client.get(path)
		return analyze_response(response)