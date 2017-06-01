import base64
import mimetypes
from synapse_pay_rest.http_client import HttpClient


class Users():
    """Abstraction of the /users endpoint.

    Used to make user-related calls to the API. It should only ever be
    instantiated by the Client.
    https://docs.synapsepay.com/docs/user-resources
    """

    def __init__(self, client):
        self.client = client

    def create_user_path(self, user_id=None):
        """Construct the correct URL for the request."""
        path = '/users'
        if user_id:
            return path + '/' + user_id
        else:
            return path

    def create(self, payload):
        """Create a user record via POST request to the API.

        https://docs.synapsepay.com/docs/create-a-user

        Args:
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single user record)
        """
        path = self.create_user_path()
        response = self.client.post(path, payload)
        return response

    def get(self, user_id=None, **params):
        """Retrieve a single or multiple user records via GET request to the API.

        https://docs.synapsepay.com/docs/get-user
        https://docs.synapsepay.com/docs/create-a-usercustomer

        Args:
            user_id (str): if specified the method returns a single user
            **params: valid params are 'query', 'page', 'per_page', 'full_dehydrate'

        Returns:
            dict: response body (single or multiple user records)
        """
        path = self.create_user_path(user_id)
        response = self.client.get(path, **params)
        return response

    def update(self, user_id, payload):
        """Updates a user record via PATCH request to the API.

        Used to edit user information, including CIP documents.
        https://docs.synapsepay.com/docs/update-user
        https://docs.synapsepay.com/docs/adding-documents
        https://docs.synapsepay.com/docs/updating-existing-document

        Args:
            user_id (str): id of the user to update
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (single user record)
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def refresh(self, user_id, payload):
        """Refreshes a user's oauth token via POST request to the API.

        This is actually a different endpoint from /users but stored here for
        convenience.

        https://docs.synapsepay.com/docs/get-oauth_key-refresh-token

        Args:
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body (containing oauth token and expiry info)
        """
        path = '/oauth/' + user_id
        response = self.client.post(path, payload)
        if 'oauth_key' in response:
            self.client.update_headers(oauth_key=response['oauth_key'])
        return response

    def add_doc(self, user_id, payload):
        """[DEPRECATED] Add the SSN virtual doc for the specified user.

        Deprecated for using KYC 1.0 format.

        https://docs.synapsepay.com/docs/add-virtual-doc

        Args:
            user_id (str): id of the user to whom the SSN belongs
            payload (dict): See the docs for exact payload structure

        Returns:
            dict: response body
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def verify(self, user_id, payload):
        """[DEPRECATED] Duplicate of the update method.
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def attach_file(self, user_id, payload, **kwargs):
        """[DEPRECATED] Upload a physical doc for the specified user.

        Deprecated for using KYC 1.0 format.

        https://docs.synapsepay.com/docs/add-physical-doc
        """
        path = self.create_user_path(user_id)
        base64_image = self.convert_file_to_base64(kwargs['file'])
        if base64_image:
            payload = {
                'doc': {
                    'attachment': base64_image
                }
            }
            response = self.client.patch(path, payload)
        return response

    def answer_kba(self, user_id, payload):
        """[DEPRECATED] Answer KBA questions for a virtual doc.

        Deprecated for using KYC 1.0 format.

        https://docs.synapsepay.com/docs/answer-kba
        """
        path = self.create_user_path(user_id)
        response = self.client.patch(path, payload)
        return response

    def convert_file_to_base64(file_path):
        """Convert a file object into padded base64 format (required by API).

        Mimetype padding is done by file extension, not by content.
        """

        file_object = None
        try:
            with open(file_path, 'wb') as file_object:
                encoded_string = base64.b64encode(file_object.read())
                mime_type = mimetypes.guess_type(file_object.name)[0]
                mime_padding = 'data:' + mime_type + ';base64,'
                base64_string = mime_padding + encoded_string
                return base64_string
        except Exception:
            response = requests.get(file_path)
            mime_type = mimetypes.guess_type(file_path)[0]
            uri = ("data:" + mime_type + ";" + "base64," + base64.b64encode(response.content).decode('ascii'))
            return uri
