from .base_node import BaseNode


class EftNpNode(BaseNode):
    """[DEPRECATED] Represents an EFT-NP node."""

    @classmethod
    def payload_for_create(cls, nickname, bank_name, account_number, **kwargs):
        """Build the API 'create node' payload specific to EFT-NP."""
        payload = super(EftNpNode, cls).payload_for_create('EFT-NP',
                                             nickname=nickname,
                                             account_number=account_number,
                                             bank_name=bank_name, **kwargs)
        return payload
