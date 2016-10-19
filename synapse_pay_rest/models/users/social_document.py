from .document import Document


class SocialDocument(Document):
    """
    """

    @classmethod
    def create(cls, base_document=None, type=None, value=None):
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(social_documents=[payload])
        social_doc = [doc for doc in base_doc.social_documents
                      if doc.type == type][0]
        return social_doc
