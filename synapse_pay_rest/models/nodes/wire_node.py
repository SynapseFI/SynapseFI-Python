from .base_node import BaseNode


class WireNode(BaseNode):
    """Ancestor of Wire node subclasses.
    """

    @classmethod
    def payload_for_create(cls, type, nickname, bank_name, account_number,
                           address, name_on_account, **kwargs):
        payload = {
            'type': type,
            'info': {
                'nickname': nickname,
                'name_on_account': name_on_account,
                'account_num': account_number,
                'bank_name': bank_name,
                'address': address,
            }
        }

        if 'routing_number' in kwargs:
            payload['info']['routing_num'] = kwargs['routing_number']

        correspondent_info = {}
        if 'correspondent_routing_number' in kwargs:
            correspondent_info['routing_num'] = kwargs['correspondent_routing_number']
        if 'correspondent_bank_name' in kwargs:
            correspondent_info['bank_name'] = kwargs['correspondent_bank_name']
        if 'correspondent_address' in kwargs:
            correspondent_info['address'] = kwargs['correspondent_address']
        if 'correspondent_swift' in kwargs:
            correspondent_info['swift'] = kwargs['correspondent_swift']
        if correspondent_info:
            payload['info']['correspondent_info'] = correspondent_info

        options = ['supp_id', 'gateway_restricted']
        extra = {}
        for option in options:
            if option in kwargs:
                extra[option] = kwargs[option]
        if extra:
            payload['extra'] = extra

        return payload
