from .base_node import BaseNode


class CheckUsNode(BaseNode):
    """Represents a CHECK-US node."""

    @classmethod
    def payload_for_create(cls, nickname, payee_name, address_street, address_city,
        address_subdivision, address_country_code, address_postal_code, **kwargs):
        """Build the API 'create node' payload specific to CHECK-US."""
        payload = super(CheckUsNode, cls).payload_for_create('CHECK-US',
                                             nickname=nickname,
                                             payee_name=payee_name,
                                             address_street=address_street,
                                             address_city=address_city,
                                             address_subdivision=address_subdivision,
                                             address_country_code=address_country_code,
                                             address_postal_code=address_postal_code,
                                             **kwargs)
        return payload
