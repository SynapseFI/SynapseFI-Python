import requests
import logging
import json
from .errors import ErrorFactory


class HttpClient():
    """Handles HTTP requests (including headers) and API errors.
    """
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

    def __repr__(self):
        return '{0}(base_url={1}, logging={2})'.format(self.__class__,
                                                       self.base_url,
                                                       self.logging)

    def update_headers(self, **kwargs):
        """Update the supplied properties on self and in the header dictionary.
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
        return self.session.headers

    def get_headers(self):
        return self.session.headers

    def get(self, url, **params):
        """Send a GET request to the API."""
        self.log_information(self.logging)
        valid_params = ['query', 'page', 'per_page', 'type', 'full_dehydrate', 'radius', 'lat', 'lon', 'zip']
        parameters = {}
        for param in valid_params:
            if param in params:
                parameters[param] = params[param]
        response = self.session.get(self.base_url + url, params=parameters)
        return self.parse_response(response)

    def post(self, url, payload, **kwargs):
        """Send a POST request to the API."""
        self.log_information(self.logging)
        headers = self.get_headers()
        if kwargs.get('idempotency_key'):
            headers['X-SP-IDEMPOTENCY-KEY'] = kwargs['idempotency_key']
        data = json.dumps(payload)
        response = self.session.post(self.base_url + url, data=data)
        return self.parse_response(response)

    def patch(self, url, payload):
        """Send a PATCH request to the API."""
        self.log_information(self.logging)
        data = json.dumps(payload)
        response = self.session.patch(self.base_url + url, data=data)
        return self.parse_response(response)

    def delete(self, url):
        """Send a DELETE request to the API."""
        self.log_information(self.logging)
        response = self.session.delete(self.base_url + url)
        return self.parse_response(response)

    def parse_response(self, response):
        """Convert successful response to dict or raise error."""
        if response.status_code >= 300:
            raise ErrorFactory.from_response(response)
        else:
            return response.json()

    def log_information(self, should_log):
        """Log requests to stdout."""
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
