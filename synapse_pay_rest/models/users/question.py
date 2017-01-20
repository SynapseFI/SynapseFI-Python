class Question():
    """[DEPRECATED] An MFA question caused by SSN partial match.
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        return '{0}({1})'.format(self.__class__, self.__dict__)

    @classmethod
    def from_response(cls, response):
        return cls(question=response['question'], answers=response['answers'],
                   id=response['id'])

    @classmethod
    def multiple_from_response(cls, response):
        return [cls.from_response(question) for question in response]
