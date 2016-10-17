from .base_node import BaseNode


class AchUsNode(BaseNode):
    """Represents an ACH-US node.
    """

    @staticmethod
    def payload_for_create(nickname, account_number, routing_number,
                           account_type, account_class, **kwargs):
        payload = {
            'type': 'ACH-US',
            'info': {
                'nickname': nickname,
                'account_num': account_number,
                'routing_num': routing_number,
                'type': account_type,
                'class': account_class
            }
        }
        options = ['supp_id', 'gateway_restricted']
        extra = {}
        for option in options:
            if option in kwargs:
                extra[option] = kwargs[option]
        if extra:
            payload['extra'] = extra
        return payload
