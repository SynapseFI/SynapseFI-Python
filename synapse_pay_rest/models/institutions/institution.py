import copy
from synapse_pay_rest.client import Client

class Institution():
    """Respresents an institution location record with methods for constructing institution location
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
        """Construct an Institution location instance from a response dict."""
        return cls(
            client = client,
            json = response,
            bank_code = response['bank_code'],
            bank_name = response['bank_name'],
            features = response['features'],
            forgotten_password = response['forgotten_password'],
            is_active = response['is_active'],
            logo = response['logo'],
            tx_history_months = response['tx_history_months']
        )

    @classmethod
    def multiple_from_response(cls, client, response):
        """Construct multiple Institutions from a response dict."""
        institutions = [cls.from_response(client, institution_data)
                         for institution_data in response]
        return institutions

    @classmethod
    def find(cls, client=None, **kwargs):
        """Finds all institutions and creates an Institution instance from it.

        Args:
            client (Client): an instance of the API Client
        Returns:
            Institution: an Institution instance corresponding to the record
        """

        response = client.institutions.find(**kwargs)
        return cls.multiple_from_response(client, response['banks'])
