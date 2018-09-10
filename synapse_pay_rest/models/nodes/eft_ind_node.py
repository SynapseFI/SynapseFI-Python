from .base_node import BaseNode


class EftIndNode(BaseNode):
    """[DEPRECATED] Represents an EFT-IND node."""

    @classmethod
    def payload_for_create(cls, nickname, account_number, ifsc, **kwargs):
        """Build the API 'create node' payload specific to EFT-IND."""
        payload = super(EftIndNode, cls).payload_for_create('EFT-IND',
                                             nickname=nickname,
                                             account_number=account_number,
                                             ifsc=ifsc,
                                             **kwargs)
        return payload
