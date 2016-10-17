from .eft_node import EftNode


class EftIndNode(EftNode):
    """Represents an EFT-IND node
    """

    @classmethod
    def payload_for_create(cls, nickname, account_number, ifsc, **kwargs):
        payload = super().payload_for_create('EFT-IND', nickname, account_number, **kwargs)
        payload['info']['ifsc'] = ifsc
        return payload
