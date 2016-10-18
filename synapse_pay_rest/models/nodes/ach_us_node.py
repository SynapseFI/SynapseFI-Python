from .base_node import BaseNode


class AchUsNode(BaseNode):
    """Represents an ACH-US node.
    """

    @classmethod
    def payload_for_create(cls, nickname, account_number, routing_number,
                           account_type, account_class, **kwargs):
        payload = super().payload_for_create('ACH-US', nickname,
                                             account_number=account_number,
                                             routing_number=routing_number,
                                             account_type=account_type,
                                             account_class=account_class,
                                             **kwargs)
        return payload
