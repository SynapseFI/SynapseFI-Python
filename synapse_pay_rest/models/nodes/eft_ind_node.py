from .base_node import BaseNode


class EftIndNode(BaseNode):
    """Represents an EFT-IND node
    """

    @classmethod
    def payload_for_create(cls, nickname, account_number, ifsc, **kwargs):
        payload = super().payload_for_create('EFT-IND', nickname,
                                             account_number=account_number,
                                             ifsc=ifsc,
                                             **kwargs)
        return payload
