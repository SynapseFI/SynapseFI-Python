from .helper_functions import *


class Nodes():
    def __init__(self, client):
        self.client = client

    def create_node_path(self, user_id, node_id=None):
        path = '/users/{0}/nodes'.format(user_id)
        if node_id:
            return path + '/' + node_id
        else:
            return path

    def create(self, user_id, payload, **kwargs):
        path = self.create_node_path(user_id)
        response = self.client.post(path, payload)
        return response

    def get(self, user_id, node_id=None, **kwargs):
        path = self.create_node_path(user_id, node_id)
        response = self.client.get(path)
        return response

    def update(self, user_id, node_id, payload, **kwargs):
        path = self.create_node_path(user_id, node_id)
        response = self.client.patch(path, payload)
        return response

    def verify(self, user_id, payload, node_id=None, **kwargs):
        # TODO deprecate
        if node_id:
            # PATCH to verify microdeposits
            self.update(user_id, payload, node_id, **kwargs)
        else:
            # POST to verify MFA
            path = self.create_node_path(user_id)
            response = self.client.post(path, payload)
        return response

    def delete(self, user_id, node_id, **kwargs):
        path = self.create_node_path(user_id, node_id)
        response = self.client.delete(path)
        return response
