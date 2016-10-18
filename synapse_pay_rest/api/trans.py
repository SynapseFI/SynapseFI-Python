from synapse_pay_rest.http_client import HttpClient


class Trans():
    def __init__(self, client):
        self.client = client

    def create_trans_path(self, user_id, node_id, trans_id=None):
        path = '/users/{0}/nodes/{1}/trans'.format(user_id, node_id)
        if trans_id:
            return path + '/' + trans_id
        else:
            return path

    def create(self, user_id, node_id, payload, **kwargs):
        path = self.create_trans_path(user_id, node_id)
        response = self.client.post(path, payload)
        return response

    def get(self, user_id, node_id, trans_id=None, **kwargs):
        path = self.create_trans_path(user_id, node_id, trans_id)
        response = self.client.get(path, **kwargs)
        return response

    def update(self, user_id, node_id, trans_id, payload, **kwargs):
        """ Updates a transaction with a comment.

            :param user_id               The id of the user whose transaction is going to be deleted.
            :param node_id               The id of the node that initiated the transaction to be deleted.
            :param trans_id              The id the transaction to be deleted.
            :param transaction_object    The object returned when the transaction was created.

            :return response     The JSON response
        """
        path = self.create_trans_path(user_id, node_id, trans_id, **kwargs)
        response = self.client.patch(path, payload)
        return response

    def delete(self, user_id, node_id, trans_id, **kwargs):
        """ Cancels a specific transaction.

            :param user_id                The id of the user whose transaction is going to be deleted.
            :param node_id                The id of the node that initiated the transaction to be deleted.
            :param trans_id                The id the transaction to be deleted.
            :param transaction_object    The object returned when the transaction was created.

            :return response     The JSON response
        """
        path = self.create_trans_path(user_id, node_id, trans_id)
        response = self.client.delete(path)
        return response
