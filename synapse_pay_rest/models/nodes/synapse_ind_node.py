from .synapse_node import SynapseNode


class SynapseIndNode(SynapseNode):
    """Represents a SYNAPSE-IND node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = {
            'type': 'SYNAPSE-IND',
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
