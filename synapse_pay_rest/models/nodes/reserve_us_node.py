from .base_node import BaseNode


class ReserveUsNode(BaseNode):
    """Represents a RESERVE-US node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = {
            'type': 'RESERVE-US',
            'info': {
                'nickname': nickname,
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
