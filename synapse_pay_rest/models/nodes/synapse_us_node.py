from .base_node import BaseNode


class SynapseUsNode(BaseNode, object):
    """Represents a SYNAPSE-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to SYNAPSE-US."""
        payload = super(SynapseUsNode, cls).payload_for_create('SYNAPSE-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
