from .base_node import BaseNode


class IbSubaccountUsNode(BaseNode):
    """Represents a IB-SUBACCOUNT-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to IB-SUBACCOUNT-US."""
        payload = super(IbSubaccountUsNode, cls).payload_for_create('IB-SUBACCOUNT-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
