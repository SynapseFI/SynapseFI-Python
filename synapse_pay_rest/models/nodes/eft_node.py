from .base_node import BaseNode


class EftNode(BaseNode):
    """Ancestor of EFT node subclasses.
    """

    @classmethod
    def payload_for_create(cls, type, nickname, account_number, **kwargs):
        payload = {
            'type': type,
            'info': {
                'nickname': nickname,
                'account_num': account_number
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
