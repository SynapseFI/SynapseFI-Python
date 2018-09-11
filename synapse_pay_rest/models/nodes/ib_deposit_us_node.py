from .base_node import BaseNode


class IbDepositUsNode(BaseNode):
    """Represents a IB-DEPOSIT-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to IB-DEPOSIT-US."""
        payload = super(IbDepositUsNode, cls).payload_for_create('IB-DEPOSIT-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
