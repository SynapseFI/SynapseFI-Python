from .base_node import BaseNode


class AchUsNode(BaseNode):
    """Represents an ACH-US node.
    """

    @classmethod
    def create_unverified_node(cls, user, response):
        return cls(user=user,
                   mfa_access_token=response['mfa']['access_token'],
                   mfa_message=response['mfa']['message'],
                   mfa_verified=False)

    @classmethod
    def create_via_bank_login(cls, user=None, bank_name=None, username=None,
                              password=None):
        payload = super().payload_for_create('ACH-US',
                                             bank_name=bank_name,
                                             username=username,
                                             password=password,
                                             mfa_verified=True)
        user.authenticate()
        response = user.client.nodes.create(user.id, payload)
        if 'mfa' in response:
            # create unverified node
            return cls.create_unverified_node(user, response)
        else:
            # no mfa needed
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

    def answer_mfa(self, answer):
        payload = {'access_token': self.mfa_access_token, 'mfa_answer': answer}
        response = self.user.client.nodes.create(self.user.id, payload)

        if response['error_code'] == '0':
            # correct answer
            self.mfa_verified = True
            return self.multiple_from_response(self.user, response['nodes'])
        elif response['error_code'] == '10':
            # incorrect answer or additional mfa answer required
            self.mfa_access_token = response['mfa']['access_token']
            self.mfa_message = response['mfa']['message']
            return self
