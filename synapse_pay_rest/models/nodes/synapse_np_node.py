from .base_node import BaseNode


class SynapseNpNode(BaseNode):
    """Represents a SYNAPSE-NP node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = super().payload_for_create('SYNAPSE-NP', nickname,
                                             **kwargs)
        return payload
