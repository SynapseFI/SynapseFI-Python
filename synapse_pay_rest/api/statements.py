from synapse_pay_rest.http_client import HttpClient


class Statements():

    def __init__(self, client):
        self.client = client

    def create_path(self, user_id, node_id=None):
        path = '/users/{0}'.format(user_id)
        if node_id:
            return path + '/nodes/' + node_id + '/statements'
        else:
            return path + '/statements'

    def retrieve(self, user_id, node_id=None, **kwargs):

        path = self.create_path(user_id, node_id)
        response = self.client.get(path, **kwargs)
        return response
