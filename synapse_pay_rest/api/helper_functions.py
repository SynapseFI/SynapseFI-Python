import base64
import binascii
import mimetypes
import requests


def convert_file_to_base64(file_path):
    """ Converts a file object into a correctly padded base64 representation
        for the SynapsePay API.  Mimetype padding is done by file 
        extension not by content(for now).
    """
    file_object = None
    # TODO raise custom exception
    try:
        with open(file_path, 'wb') as file_object:
            encoded_string = base64.b64encode(file_object.read())
            mime_type = mimetypes.guess_type(file_object.name)[0]
            mime_padding = 'data:' + mime_type + ';base64,'
            base64_string = mime_padding + encoded_string
            return base64_string
    except Exception:
        try:
            response = requests.get(file_path)
            mime_type = mimetypes.guess_type(file_path)[0]
            uri = ("data:" + mime_type + ";" + "base64," + base64.b64encode(response.content).decode('ascii'))
            return uri
        except Exception as e:
            print(str(e))
            return None
