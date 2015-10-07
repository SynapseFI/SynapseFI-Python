import base64
import binascii
import mimetypes


def checkKwargs(keys, kwargs):
	for key in keys:
		if not key in kwargs:
			return False, create_custom_error_message('You are missing the "{0}" parameter'.format(key))
	return True, None

'''
	Converts a file object into a correctly padded base64 representation
	for the SynapsePay API.  Mimetype padding is done by file 
	extension not by content(for now).
'''
def convert_file_to_base64(file_object):
	encoded_string = base64.b64encode(file_object.read())
	mime_type = mimetypes.guess_type(file_object.name)[0]
	mime_padding = 'data:' + mime_type + ';base64,'
	base64_string = mime_padding + encoded_string
	return base64_string

'''
	Used to create JSON formatted error messages that occur at the
	library level.  This allows for no exceptions to ever be raised
	for the user.
'''
def create_custom_error_message(error_message):
	return {
		'success':False,
		'error':{
			'en':error_message
		}
	}

'''
	If we ever wanted to make a different response for the
	user(i.e. just the string message) we could change it here.
	However, for now it just forwards the json response.

	:param response 	The JSON response from the api call.

	:return response 	Returns the JSON response.
'''
def analyze_response(response):
	return response