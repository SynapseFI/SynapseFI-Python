from .document import Document


class SocialDocument(Document):
    """Object representation of a supporting social document.

    Social documents are normally URLs to social media profiles that help
    verify the user's identity.
    https://docs.synapsepay.com/docs/user-resources#section-social-document-types
    """

    @classmethod
    def create(cls, base_document, type=None, value=None):
        """Add a SocialDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-social-document-types
            value (str): url to social media profile, for example

        Returns:
            SocialDocument: a new SocialDocument instance
        """
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(social_documents=[payload])
        social_doc = [doc for doc in base_doc.social_documents
                      if doc.type == type][0]
        return social_doc
