from .document import Document


class PhysicalDocument(Document):
    """
    """

    @classmethod
    def create(cls, base_document=None, type=None, value=None):
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(physical_documents=[payload])
        physical_doc = [doc for doc in base_doc.physical_documents
                        if doc.type == type][0]
        return physical_doc
