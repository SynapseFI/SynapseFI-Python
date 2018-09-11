from .base_node import BaseNode


class IouNode(BaseNode):
    """Represents an IOU node."""

    @classmethod
    def payload_for_create(cls, nickname, currency, **kwargs):
        """Build the API 'create node' payload specific to IOU."""
        payload = super(IouNode, cls).payload_for_create('IOU',
                                             nickname=nickname,
                                             currency=currency, **kwargs)
        return payload
