from .base_node import BaseNode


class SynapseNpNode(BaseNode):
    """[DEPRECATED] Represents a SYNAPSE-NP node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to SYNAPSE-NP."""
        payload = super(SynapseNpNode, cls).payload_for_create('SYNAPSE-NP',
                                             nickname=nickname,
                                             **kwargs)
        return payload
