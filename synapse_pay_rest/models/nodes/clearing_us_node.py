from .base_node import BaseNode


class ClearingUsNode(BaseNode):
    """Represents a CLEARING-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to CLEARING-US."""
        payload = super(ClearingUsNode, cls).payload_for_create('CLEARING-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
