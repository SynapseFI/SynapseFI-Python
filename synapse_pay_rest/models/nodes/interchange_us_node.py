from .base_node import BaseNode


class InterchangeUsNode(BaseNode):
    """Represents a INTERCHANGE-US node."""

    @classmethod
    def payload_for_create(cls, nickname, card_number, exp_date, document_id, **kwargs):
        """Build the API 'create node' payload specific to INTERCHANGE-US."""
        payload = super(InterchangeUsNode, cls).payload_for_create('INTERCHANGE-US',
                                             nickname=nickname,
                                             card_number=card_number,
                                             exp_date=exp_date,
                                             document_id=document_id,
                                             **kwargs)
        return payload
