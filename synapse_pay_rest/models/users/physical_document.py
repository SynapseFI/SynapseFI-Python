import base64
import mimetypes
import requests
from .document import Document


class PhysicalDocument(Document):
    """Object representation of a supporting physical document.

    Physical documents are images or pdfs that help verify the user's identity.
    https://docs.synapsepay.com/docs/user-resources#section-physical-document-types

    jpg and png are preferred. Base64 values should be padded like this:
    jpg - data:image/jpeg;base64,...
    png - data:image/png;base64,...
    """

    @classmethod
    def create(cls, base_document, value=None, type=None, file_path=None,
               url=None, byte_stream=None, mime_type=None):
        """Add a PhysicalDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-physical-document-types
            value (str): (opt) padded Base64 encoded image string
            file_path (str): path to image file (instead of value)
            url (str): url to image file (instead of value)
            byte_stream (str): byte array (instead of value)

        Returns:
            PhysicalDocument: a new PhysicalDocument instance
        """
        if file_path:
            value = cls.file_to_base64(file_path)
        elif url:
            has_query = url.find('?') > 0
            url = url[:url.find('?')] if has_query else url
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
        """Convert a byte stream / array to a properly padded base64 string.
        """
        base64_string = base64.b64encode(byte_stream).decode("utf-8")
        mime_padding = 'data:{0};base64,'.format(mime_type)
        padded_base64 = mime_padding + base64_string
        return padded_base64

    @staticmethod
    def file_to_base64(file_path):
        """Convert the specified img/pdf file to a properly padded base64 string.
        """
        with open(file_path, 'rb') as file_object:
            byte_stream = file_object.read()
            mime_type = mimetypes.guess_type(file_object.name)[0]
            return PhysicalDocument.byte_stream_to_base64(byte_stream,
                                                          mime_type)

    @staticmethod
    def url_to_base64(url):
        """Convert the specified img/pdf url to a properly padded base64 string.
        """
        response = requests.get(url)
        mime_type = mimetypes.guess_type(url)[0]
        return PhysicalDocument.byte_stream_to_base64(response.content,
                                                      mime_type)
