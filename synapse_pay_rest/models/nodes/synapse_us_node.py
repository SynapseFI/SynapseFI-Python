from .synapse_node import SynapseNode


class SynapseUsNode(SynapseNode):
    """Represents a SYNAPSE-US node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = super().payload_for_create('SYNAPSE-US', nickname,
                                             **kwargs)
        return payload
