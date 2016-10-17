from .base_node import BaseNode


class SynapseNode(BaseNode):
    """Ancestor of Synapse node subclasses.
    """

    @classmethod
    def payload_for_create(cls, type, nickname, **kwargs):
        payload = {
            'type': type,
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
