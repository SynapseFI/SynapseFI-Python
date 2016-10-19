from .document import Document


class VirtualDocument(Document):
    """
    """

    @classmethod
    def create(cls, base_document=None, type=None, value=None):
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(virtual_documents=[payload])
        virtual_doc = [doc for doc in base_doc.virtual_documents
                       if doc.type == type][0]
        return virtual_doc
