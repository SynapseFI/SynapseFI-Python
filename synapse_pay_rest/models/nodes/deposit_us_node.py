from .base_node import BaseNode


class DepositUsNode(BaseNode):
    """Represents a DEPOSIT-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to DEPOSIT-US."""
        payload = super(DepositUsNode, cls).payload_for_create('DEPOSIT-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
