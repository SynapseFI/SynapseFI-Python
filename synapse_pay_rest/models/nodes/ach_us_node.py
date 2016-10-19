from .base_node import BaseNode


class AchUsNode(BaseNode):
    """Represents an ACH-US node.
    """

    @classmethod
    def create_via_bank_login(cls, user=None, bank_name=None, username=None,
                              password=None):
        payload = super().payload_for_create('ACH-US',
                                             bank_name=bank_name,
                                             username=username,
                                             password=password)
        user.authenticate()
        response = user.client.nodes.create(user.id, payload)
        return cls.multiple_from_response(user, response['nodes'])

    @classmethod
    def payload_for_create(cls, nickname, account_number, routing_number,
                           account_type, account_class, **kwargs):
        payload = super().payload_for_create('ACH-US',
                                             nickname=nickname,
                                             account_number=account_number,
                                             routing_number=routing_number,
                                             account_type=account_type,
                                             account_class=account_class,
                                             **kwargs)
        return payload

    def verify_microdeposits(self, amount1, amount2):
        payload = {'micro': [amount1, amount2]}
        response = self.user.client.nodes.update(self.user.id, self.id, payload)
        return self.from_response(self.user, response)
