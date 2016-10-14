from synapse_pay_rest.http_client import HttpClient


class Users():
    def __init__(self, client):
        self.client = client

    def create_user_path(self, user_id=None):
        path = '/users'
        if user_id:
            return path + '/' + user_id
        else:
            return path

    def create(self, payload, **kwargs):
        """ Creates a SynapsePay user and updates the client with the new oauth
            key.

            :api add_doc        http://api.synapsepay.com/docs/attach-document

            :param user_id        The id of the user to add SSN info to.
            :param options        The body of the API response.

            :return response     The JSON response
        """
        path = self.create_user_path()
        response = self.client.post(path, payload)
        if '_id' in response:
            self.client.user_id = response['_id']
        return response

    def get(self, user_id=None, **kwargs):
        path = self.create_user_path(user_id)
        params = {}
        if 'query' in kwargs:
            params['query'] = kwargs.get('query')
        if 'page' in kwargs:
            params['page'] = kwargs.get('page')
        if 'page_count' in kwargs:
            params['per_page'] = kwargs.get('per_page')
        response = self.client.get(path, params)
        if '_id' in response:
            self.client.user_id = response['_id']
        return response

    def update(self, user_id, payload, **kwargs):
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        if '_id' in response:
            self.client.user_id = response['_id']
        return response

    def refresh(self, user_id, payload, **kwargs):
        path = '/oauth/' + self.client.user_id
        response = self.client.post(path, payload)
        if 'oauth_key' in response:
            self.client.update_headers(oauth_key=response['oauth_key'])
        return response

    def add_doc(self, user_id, payload, **kwargs):
        """ Adds the SSN information for the specific user. See
            http://api.synapsepay.com/docs/attach-document for more
            detailed explanation of this api and more example payloads.

            :param user_id    The id of the user to add SSN info to.
            :param options    The body of the API response.

            :return response     The JSON response
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def verify(self, user_id, payload, **kwargs):
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def attach_file(self, user_id, payload, **kwargs):
        """ Uploads a file for the user to help verify their identity. Can be an
            image, pdf, etc.
        """
        path = self.create_user_path(user_id)
        base64_image = convert_file_to_base64(kwargs['file'])
        if base64_image:
            payload = {
                'doc': {
                    'attachment': base64_image
                }
            }
            response = self.client.patch(path, payload)
        return response

    def answer_kba(self, user_id, payload, **kwargs):
        """ Adds the SSN information for the specific user. See
            http://api.synapsepay.com/docs/attach-document for more
            detailed explanation of this api and more example payloads.

            :param user_id    The id of the user to add SSN info to.
            :param options    The body of the API response.

            :return response     The JSON response
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response
