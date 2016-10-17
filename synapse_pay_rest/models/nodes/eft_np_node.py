from .eft_node import EftNode


class EftNpNode(EftNode):
    """Represents an EFT-NP node.
    """

    @classmethod
    def payload_for_create(cls, nickname, bank_name, account_number, **kwargs):
        payload = super().payload_for_create('EFT-NP', nickname, account_number, **kwargs)
        payload['info']['bank_name'] = bank_name
        return payload
