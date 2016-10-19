import base64
import mimetypes
import io
import requests
from .document import Document


class PhysicalDocument(Document):
    """
    """

    @classmethod
    def create(cls, base_document=None, value=None, type=None, file_path=None,
               url=None, byte_stream=None):
        if file_path:
            value = cls.file_to_base64(file_path)
        elif url:
            value = cls.url_to_base64(url)
        elif byte_stream:
            value = cls.byte_stream_to_bas64(byte_stream)
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(physical_documents=[payload])
        physical_doc = [doc for doc in base_doc.physical_documents
                        if doc.type == type][0]
        return physical_doc

    @staticmethod
    def file_to_base64(file_path):
        """ Converts a file object into a correctly padded base64 representation
            for the SynapsePay API.  Mimetype padding is done by file
            extension not by content(for now).
        """
        with open(file_path, 'wb') as file_object:
            encoded_string = base64.b64encode(file_object.read())
            mime_type = mimetypes.guess_type(file_object.name)[0]
            mime_padding = 'data:' + mime_type + ';base64,'
            base64_string = mime_padding + encoded_string
            return base64_string

    @staticmethod
    def url_to_base64(url):
        response = requests.get(url)
        mime_type = mimetypes.guess_type(url)[0]
        uri = ("data:" + mime_type + ";" + "base64," +
               base64.b64encode(response.content).decode('ascii'))
        return uri

    @staticmethod
    def byte_stream_to_bas64(byte_stream):
        pass
