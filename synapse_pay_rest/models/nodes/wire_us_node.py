from .base_node import BaseNode


class WireUsNode(BaseNode):
    """Represents a WIRE-US node."""

    @classmethod
    def payload_for_create(cls, nickname, account_number, routing_number,
                           name_on_account, address, **kwargs):
        """Build the API 'create node' payload specific to WIRE-US."""
        payload = super(WireUsNode, cls).payload_for_create('WIRE-US',
                                             nickname=nickname,
                                             account_number=account_number,
                                             routing_number=routing_number,
                                             name_on_account=name_on_account,
                                             address=address,
                                             **kwargs)
        return payload
