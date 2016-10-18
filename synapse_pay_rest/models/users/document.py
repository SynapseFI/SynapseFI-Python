

class Document():
    """
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    @classmethod
    def from_response(cls, response):
        return cls(type=response['document_type'],
                   id=response['id'],
                   status=response['status'],
                   last_updated=response['last_updated'])

    @classmethod
    def multiple_from_response(cls, response):
        base_docs = [cls.from_response(doc_data)
                     for doc_data in response]
        return base_docs
