from .synapse_node import SynapseNode


class SynapseNpNode(SynapseNode):
    """Represents a SYNAPSE-NP node
    """

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        payload = super().payload_for_create('SYNAPSE-NP', nickname,
                                             **kwargs)
        return payload
