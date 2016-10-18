from .base_node import BaseNode


class SynapseUsNode(BaseNode):
    """Represents a SYNAPSE-US node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = super().payload_for_create('SYNAPSE-US', nickname,
                                             **kwargs)
        return payload
