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
               url=None, byte_stream=None, mime_type=None):
        if file_path:
            value = cls.file_to_base64(file_path)
        elif url:
            value = cls.url_to_base64(url)
        elif byte_stream:
            value = cls.byte_stream_to_base64(byte_stream, mime_type)
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(physical_documents=[payload])
        physical_doc = [doc for doc in base_doc.physical_documents
                        if doc.type == type][0]
        return physical_doc

    @staticmethod
    def byte_stream_to_base64(byte_stream, mime_type):
        encoded_string = str(base64.b64encode(byte_stream))
        mime_padding = 'data:{0};base64,'.format(mime_type)
        base64_string = mime_padding + encoded_string
        return base64_string

    @staticmethod
    def file_to_base64(file_path):
        """ Converts a file object into a correctly padded base64 representation
            for the SynapsePay API.  Mimetype padding is done by file
            extension not by content(for now).
        """
        with open(file_path, 'rb') as file_object:
            byte_stream = file_object.read()
            mime_type = mimetypes.guess_type(file_object.name)[0]
            return PhysicalDocument.byte_stream_to_base64(byte_stream,
                                                          mime_type)

    @staticmethod
    def url_to_base64(url):
        response = requests.get(url)
        mime_type = mimetypes.guess_type(url)[0]
        byte_stream = base64.b64encode(response.content)
        return PhysicalDocument.byte_stream_to_base64(byte_stream, mime_type)
