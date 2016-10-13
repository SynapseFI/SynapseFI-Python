import requests
import traceback
import logging
import json


# TODO: this is so bad
NO_CLUE_ERROR = {
    "error": {
        "en": "An error has occured in this library."
    },
    "success": False
}


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

        # TODO: move this
        # self.RESPONSE_HANDLERS = {
        #     200: self.success_handler,
        #     202: self.success_handler,
        #     400: self.bad_request_handler,
        #     401: self.unauthorized_handler,
        #     402: self.request_failed_handler,
        #     404: self.not_found_handler,
        #     409: self.incorrect_values_handler,
        #     500: self.server_error_handler
        # }

    def update_headers(self, **kwargs):
        """Summary

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

    def success_handler(self, r):
        return r.json()

    def bad_request_handler(self, r):
        return r.json()

    def unauthorized_handler(self, r):
        return r.json()

    def request_failed_handler(self, r):
        return {
            "error": {
                "en": "An error has occured in this library."
            },
            "success": False
        }

    def not_found_handler(self, r):
        return {
            "error": {
                "en": "The url is not found."
            },
            "success": False
        }

    def incorrect_values_handler(self, r):
        return r.json()

    def server_error_handler(self, r):
        try:
            return r.json()
        except:
            return {
                "error": {
                    "en": "Unknown sever error has occurred."
                },
                "success": False
            }

    def delete(self, url):
        self.log_information(self.logging)
        r = self.session.delete(self.base_url + url)
        try:
            return self.RESPONSE_HANDLERS[r.status_code](r)
        except Exception as e:
            return NO_CLUE_ERROR

    def get(self, url, params=None):
        self.log_information(self.logging)
        r = self.session.get(self.base_url + url, params=params)
        try:
            return self.RESPONSE_HANDLERS[r.status_code](r)
        except Exception as e:
            print(str(e))
            return NO_CLUE_ERROR

    def post(self, url, payload):
        self.log_information(self.logging)
        r = self.session.post(self.base_url + url, data=json.dumps(payload))
        try:
            return self.RESPONSE_HANDLERS[r.status_code](r)
        except Exception as e:
            print(str(e))
            return NO_CLUE_ERROR

    def patch(self, url, payload):
        self.log_information(self.logging)
        r = self.session.patch(self.base_url + url, data=json.dumps(payload))
        try:
            return self.RESPONSE_HANDLERS[r.status_code](r)
        except Exception as e:
            print(str(e))
            return NO_CLUE_ERROR

    def update_oauth(self, oauth_key):
        self.headers['X-SP-USER'] = oauth_key + '|' + self.headers['X-SP-USER'].split('|')[1]
        self.session.headers.update(self.headers)

    def set_user_id(self, user_id):
        self.user_id = user_id

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
