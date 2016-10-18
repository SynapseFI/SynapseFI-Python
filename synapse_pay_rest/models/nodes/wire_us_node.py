from .wire_node import WireNode


class WireUsNode(WireNode):
    """Represents a WIRE-US node
    """

    @classmethod
    def payload_for_create(cls, nickname, bank_name, account_number,
                           name_on_account, address, **kwargs):
        payload = super().payload_for_create('WIRE-US', nickname, bank_name,
                                             account_number, name_on_account,
                                             address, **kwargs)
        return payload
