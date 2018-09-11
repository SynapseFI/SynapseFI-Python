from .base_node import BaseNode


class SubaccountUsNode(BaseNode):
    """Represents a SUBACCOUNT-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to SUBACCOUNT-US."""
        payload = super(SubaccountUsNode, cls).payload_for_create('SUBACCOUNT-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
