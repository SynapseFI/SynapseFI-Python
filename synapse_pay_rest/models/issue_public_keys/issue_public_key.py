import copy
from synapse_pay_rest.client import Client

class PublicKey():
    """Represents a Public Key record with methods for constructing Public key
    instances.

    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        clean_dict = self.__dict__.copy()
        return '{0}({1})'.format(self.__class__, clean_dict)

    @classmethod
    def from_response(cls, client, response):
        """Construct a Public Key from a response dict."""
        return cls(
            client = client,
            json=response,
            client_obj_id=response['public_key_obj']['client_obj_id'],
            expires_at=response['public_key_obj']['expires_at'],
            expires_in=response['public_key_obj']['expires_in'],
            public_key=response['public_key_obj']['public_key'],
            scope=response['public_key_obj']['scope']
        )


    @classmethod
    def issue(cls,client=None, scope=None):
        """Issues a public key record and create a Public Key instance from it.

        Args:
            client (Client): an instance of the API Client
            scope (string): scope of the subscription

        Returns:
            Public Key: a PublicKey instance corresponding to the record
        """
        if scope is None:
            scope = "OAUTH|POST,USERS|POST,USERS|GET,USER|GET,USER|PATCH,SUBSCRIPTIONS|GET,SUBSCRIPTIONS|POST,SUBSCRIPTION|GET,SUBSCRIPTION|PATCH,CLIENT|REPORTS,CLIENT|CONTROLS"

        response = client.client_endpoint.issue_public_key(scope)
        return cls.from_response(client, response)

   