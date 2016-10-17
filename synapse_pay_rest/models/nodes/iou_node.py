from .base_node import BaseNode


class IouNode(BaseNode):
    """Represents an IOU node
    """

    @classmethod
    def payload_for_create(cls, nickname, currency, **kwargs):
        payload = {
            'type': 'IOU',
            'info': {
                'nickname': nickname,
                'balance': {
                    'currency': currency
                }
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
