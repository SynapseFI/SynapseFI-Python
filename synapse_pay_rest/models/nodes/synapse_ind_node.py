from .base_node import BaseNode


class SynapseIndNode(BaseNode):
    """Represents a SYNAPSE-IND node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = super().payload_for_create('SYNAPSE-IND', nickname,
                                             **kwargs)
        return payload
