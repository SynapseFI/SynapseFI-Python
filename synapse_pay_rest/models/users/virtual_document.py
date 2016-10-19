from .document import Document
from .question import Question


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

    @classmethod
    def from_response(cls, response):
        doc = super().from_response(response)
        if response.get('meta') and response['meta'].get('question_set'):
            question_data = response['meta']['question_set']['questions']
            question_set = Question.multiple_from_response(question_data)
            doc.question_set = question_set
        return doc

    def submit_kba(self):
        user = self.base_document.user
        response = user.client.users.update(user.id, self.payload_for_kba())
        user = user.from_response(user.client, response)
        base_doc = [base_doc for base_doc in user.base_documents
                    if base_doc.id == self.base_document.id][0]
        virtual_doc = [doc for doc in base_doc.virtual_documents if
                       doc.id == self.id][0]
        return virtual_doc

    def payload_for_kba(self):
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
