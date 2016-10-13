import requests
import traceback
import logging
import json


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
        self.logging = kwargs['logging']

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def update_headers(self, **kwargs):
        """Updates the supplied properties on self and in the header dictionary.

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

    def get(self, url, params=None):
        self.log_information(self.logging)
        return self.session.get(self.base_url + url, params=params)

    def post(self, url, payload):
        self.log_information(self.logging)
        return self.session.post(self.base_url + url, data=json.dumps(payload))

    def patch(self, url, payload):
        self.log_information(self.logging)
        return self.session.patch(self.base_url + url, data=json.dumps(payload))

    def delete(self, url):
        self.log_information(self.logging)
        return self.session.delete(self.base_url + url)

    def log_information(should_log):
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
