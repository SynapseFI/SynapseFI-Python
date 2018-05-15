import copy
from synapse_pay_rest.client import Client

class Atm():
    """Represents an atm location record with methods for constructing atm location methods
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
        """Construct an Atm location instance from a response dict."""
        return cls(
            client = client,
            json=response,
            address_city=response['atmLocation'].get('address').get('city'),
            address_country=response['atmLocation'].get('address').get('country'),
            address_postal_code=response['atmLocation'].get('address').get('postalCode'),
            address_state=response['atmLocation'].get('address').get('state'),
            address_street=response['atmLocation'].get('address').get('street'),
            latitude=response['atmLocation'].get('coordinates').get('latitude'),
            longitude=response['atmLocation'].get('coordinates').get('longitude'),
            id=response['atmLocation']['id'],
            isAvailable24Hours=response['atmLocation']['isAvailable24Hours'],
            isDepositAvailable=response['atmLocation']['isDepositAvailable'],
            isHandicappedAccessible=response['atmLocation']['isHandicappedAccessible'],
            isOffPremise=response['atmLocation']['isOffPremise'],
            isSeasonal=response['atmLocation']['isSeasonal'],
            languageType=response['atmLocation']['languageType'],
            locationDescription=response['atmLocation']['locationDescription'],
            logoName=response['atmLocation']['logoName'],
            name=response['atmLocation']['name'],
            distance=response['distance']
        )

    @classmethod
    def multiple_from_response(cls, client, response):
        """Construct multiple Atms from a response dict."""
        atms = [cls.from_response(client, atm_data)
                 for atm_data in response]
        return atms


    @classmethod
    def locate(cls,client=None, **kwargs):
        """Locates nearby atms and create an Atm instance from it.

        Args:
            client (Client): an instance of the API Client
            zip(string): Zip code for ATM locator
            radius(string): radius in miles
            page(integer): Page number
            per_page(integer): Number of atms per page
        Returns:
            Atm: an ATM instance corresponding to the record
        """

        response = client.atms.locate(**kwargs)
        return cls.multiple_from_response(client, response['atms'])

   