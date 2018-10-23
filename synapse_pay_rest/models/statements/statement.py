import copy
from synapse_pay_rest.client import Client


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
            _id = response['_id'],
            client_id = response['client_id'],
            date_end = response['date_end'],
            date_start = response['date_start'],
            ending_balance = response.get('ending_balance', None),
            is_active = response['is_active'],
            node_id = response['node_id'],
            opening_balance = response.get('opening_balance', None),
            status = response['status'],
            csv_url = response['urls']['csv'],
            json_url = response['urls'].get('json', None),
            pdf_url = response['urls']['pdf'],
            user_id = response['user_id']
        )

    @classmethod
    def multiple_from_response(cls, user, response):

        statements = [cls.from_response(user, statement_data)
                     for statement_data in response]
        return statements

    @classmethod
    def retrieve(cls, user, node_id=None, **kwargs):
        response = user.client.statements.retrieve(user.id, **kwargs)
        return cls.multiple_from_response(user, response['statements'])
