

class Question():
    """
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    @classmethod
    def from_response(cls, response):
        return cls(question=response['question'], answers=response['answers'],
                   id=response['id'])

    @classmethod
    def multiple_from_response(cls, response):
        return [cls.from_response(question) for question in response]
