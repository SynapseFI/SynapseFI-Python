from .base_node import BaseNode


class TriumphSubaccountUsNode(BaseNode):
    """Represents a TRIUMPH-SUBACCOUNT-US node."""

    @classmethod
    def payload_for_create(cls, nickname, **kwargs):
        """Build the API 'create node' payload specific to TRIUMPH-SUBACCOUNT-US.
        """
        payload = super(TriumphSubaccountUsNode, cls).payload_for_create('TRIUMPH-SUBACCOUNT-US',
                                             nickname=nickname,
                                             **kwargs)
        return payload
