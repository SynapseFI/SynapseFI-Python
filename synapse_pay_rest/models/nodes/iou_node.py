from .base_node import BaseNode


class IouNode(BaseNode):
    """Represents an IOU node
    """

    @classmethod
    def payload_for_create(cls, nickname, currency, **kwargs):
        payload = super().payload_for_create('IOU', nickname,
                                             currency=currency, **kwargs)
        return payload
