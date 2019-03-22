import copy

class Statement():


    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        clean_dict = self.__dict__.copy()
        return '{0}({1})'.format(self.__class__, clean_dict)

    @classmethod
    def from_response(cls, user, response):
        return cls(
            user = user,
            json = response,
            **response
        )

    @classmethod
    def multiple_from_response(cls, user, response):

        statements = [cls.from_response(user, statement_data)
                     for statement_data in response]
        return statements

    @classmethod
    def retrieve(cls, user, node_id=None, **kwargs):
        response = None
        if not node_id:
            response = user.client.statements.retrieve(user.id, **kwargs)
        else:
            response = user.client.statements.retrieve(user.id, node_id, **kwargs)
        return cls.multiple_from_response(user, response['statements'])
