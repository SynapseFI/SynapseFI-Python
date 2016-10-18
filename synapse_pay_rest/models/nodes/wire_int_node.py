from .wire_node import WireNode


class WireIntNode(WireNode):
    """Represents a WIRE-INT node
    """

    @classmethod
    def payload_for_create(cls, nickname, bank_name, account_number, swift,
                           name_on_account, address, **kwargs):
        payload = super().payload_for_create('WIRE-INT', nickname, bank_name,
                                             account_number, name_on_account,
                                             address, **kwargs)
        payload['info']['swift'] = swift
        return payload
