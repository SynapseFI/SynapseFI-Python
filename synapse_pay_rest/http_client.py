import requests

import traceback
import logging
import json

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

NO_CLUE_ERROR = {
	"error": {
		"en": "An error has occured in this library."
	},
	"success": False
}

BASE_URL = 'https://synapsepay.com/api/3'

class HttpClient():

	def __init__(self, options, user_id=None):
		global BASE_URL
		self.session = requests.Session()
		if options.has_key('oauth_key'):
			initial_fingerprint = options['oauth_key'] + '|' + options['fingerprint']
		else:
			initial_fingerprint = '|' + options['fingerprint']
		gateway = options['client_id'] + '|' + options['client_secret']
		if options.has_key('development_mode'):
			if options['development_mode']:
				BASE_URL = 'https://sandbox.synapsepay.com/api/3'
		lang = 'en'
		if options.has_key('lang'):
			lang = options['lang']

		self.headers = {
			'Content-Type':'application/json',
			'X-SP-GATEWAY':gateway,
			'X-SP-USER':initial_fingerprint,
			'X-SP-USER-IP': options['ip_address'],
			'X-SP-LANG': lang
		}

		self.session.headers.update(self.headers)

		self.RESPONSE_HANDLERS = {
			200: self.success_handler,
			202: self.success_handler,
			400: self.bad_request_handler,
			401: self.unauthorized_handler,
			402: self.request_failed_handler,
			404: self.not_found_handler,
			409: self.incorrect_values_handler,
			500: self.server_error_handler
		}

		self.user_id = user_id

	def success_handler(self, r):
		print r.json()
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
		log_information(True)
		r = self.session.delete(BASE_URL + url)
		try:
			return self.RESPONSE_HANDLERS[r.status_code](r)
		except Exception, e:
			print str(e)
			return NO_CLUE_ERROR

	def get(self, url, params=None):
		log_information(True)
		print params
		r = self.session.get(BASE_URL + url, params=params)
		try:
			return self.RESPONSE_HANDLERS[r.status_code](r)
		except Exception, e:
			print str(e)
			return NO_CLUE_ERROR

	def post(self, url, payload):
		log_information(True)
		r = self.session.post(BASE_URL + url, data=json.dumps(payload))
		try:
			return self.RESPONSE_HANDLERS[r.status_code](r)
		except Exception, e:
			print str(e)
			return NO_CLUE_ERROR

	def patch(self, url, payload):
		log_information(True)
		r = self.session.patch(BASE_URL + url, data=json.dumps(payload))
		try:
			return self.RESPONSE_HANDLERS[r.status_code](r)
		except Exception, e:
			print str(e)
			return NO_CLUE_ERROR

	def update_oauth(self, oauth_key):
		self.headers['X-SP-USER'] = oauth_key + '|' + self.headers['X-SP-USER'].split('|')[1]
		self.session.headers.update(self.headers)

	def set_user_id(self, user_id):
		self.user_id = user_id