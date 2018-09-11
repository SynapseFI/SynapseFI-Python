from .base_node import BaseNode


class SynapseIndNode(BaseNode):
    """[DEPRECATED] Represents a SYNAPSE-IND node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to SYNAPSE-IND."""
        payload = super(SynapseIndNode, cls).payload_for_create('SYNAPSE-IND',
                                             nickname=nickname,
                                             **kwargs)
        return payload
