import requests
import traceback
import logging
import json
from synapse_pay_rest.errors import *


class HttpClient():
    def __init__(self, **kwargs):
        self.update_headers(
            client_id=kwargs['client_id'],
            client_secret=kwargs['client_secret'],
            fingerprint=kwargs['fingerprint'],
            ip_address=kwargs['ip_address'],
            oauth_key=''
        )

        self.base_url = kwargs['base_url']
        self.logging = kwargs.get('logging', False)
        self.user_id = kwargs.get('user_id')

    def update_headers(self, **kwargs):
        """ Updates the supplied properties on self and in the header dictionary.

        Args:
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        header_options = ['client_id', 'client_secret', 'fingerprint',
                          'ip_address', 'oauth_key']
        for prop in header_options:
            if kwargs.get(prop) is not None:
                setattr(self, prop, kwargs.get(prop))

        self.headers = {
            'Content-Type': 'application/json',
            'X-SP-LANG': 'en',
            'X-SP-GATEWAY': self.client_id + '|' + self.client_secret,
            'X-SP-USER': self.oauth_key + '|' + self.fingerprint,
            'X-SP-USER-IP': self.ip_address
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get(self, url, params=None):
        self.log_information(self.logging)
        response = self.session.get(self.base_url + url, params=params)
        return self.parse_response(response)

    def post(self, url, payload):
        self.log_information(self.logging)
        response = self.session.post(self.base_url + url, data=json.dumps(payload))
        return self.parse_response(response)

    def patch(self, url, payload):
        self.log_information(self.logging)
        response = self.session.patch(self.base_url + url, data=json.dumps(payload))
        return self.parse_response(response)

    def delete(self, url):
        self.log_information(self.logging)
        response = self.session.delete(self.base_url + url)
        return self.parse_response(response)

    def parse_response(self, response):
        if response.status_code >= 300:
            raise ErrorFactory.from_response(ErrorFactory, response)
        else:
            return response.json()

    def log_information(self, should_log):
        if should_log:
            try:
                import http.client as http_client
            except ImportError:
                # Python 2
                import httplib as http_client
            http_client.HTTPConnection.debuglevel = 1

            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
