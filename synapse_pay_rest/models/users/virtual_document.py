from .document import Document
from .question import Question


class VirtualDocument(Document):
    """Object representation of a supporting virtual document.

    Virtual documents are normally ID numbers that help verify the user's
    identity.
    https://docs.synapsepay.com/docs/user-resources#section-virtual-document-types
    """

    @classmethod
    def create(cls, base_document, type=None, value=None):
        """Add a VirtualDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-virtual-document-types
            value (str): SSN or TIN, for example

        Returns:
            VirtualDocument: a new VirtualDocument instance
        """
        payload = cls.payload_for_create(type, value)
        base_doc = base_document.update(virtual_documents=[payload])
        virtual_doc = [doc for doc in base_doc.virtual_documents
                       if doc.type == type][0]
        return virtual_doc

    @classmethod
    def from_response(cls, response):
        """Construct a VirtualDocument from a response dict."""
        doc = super(VirtualDocument, cls).from_response(response)
        if response.get('status') == 'SUBMITTED|MFA_PENDING':
            question_data = response['meta']['question_set']['questions']
            question_set = Question.multiple_from_response(question_data)
            doc.question_set = question_set
        return doc

    def submit_kba(self):
        """[DEPRECATED] Verify the VirtualDocument's MFA questions.

        If the VirtualDocument requires MFA, it will have a question_set
        property. This method takes the user's answers to those questions and
        submits them.

        Returns:
            VirtualDocument: a new instance representing the updated document
        """
        user = self.base_document.user
        response = user.client.users.update(user.id, self.payload_for_kba())
        user = user.from_response(user.client, response)
        base_doc = [base_doc for base_doc in user.base_documents
                    if base_doc.id == self.base_document.id][0]
        virtual_doc = [doc for doc in base_doc.virtual_documents if
                       doc.id == self.id][0]
        return virtual_doc

    def payload_for_kba(self):
        """[DEPRECATED] Build the API 'answer KBA' payload from property values."""
        answers = [{'question_id': question.id, 'answer_id': question.choice}
                   for question in self.question_set]
        payload = {
            'documents': [{
                'id': self.base_document.id,
                'virtual_docs': [{
                    'id': self.id,
                    'meta': {
                        'question_set': {
                            'answers': answers
                        }
                    }
                }]
            }]
        }
        return payload
