from .base_node import BaseNode


class AchUsNode(BaseNode):
    """Represents an ACH-US node."""

    @classmethod
    def unverified_from_response(cls, user, response):
        """Create an AchUsNode instance for an ACH-US node that needs MFA.

        The API record is not actually created until the MFA has been correctly
        answered.
        """
        return cls(user=user,
                   mfa_access_token=response['mfa']['access_token'],
                   mfa_message=response['mfa']['message'],
                   mfa_verified=False)

    @classmethod
    def create_via_bank_login(cls, user=None, bank_name=None, username=None,
                              password=None):
        """Create a ACH-US node record in API via bank login.

        Args:
            user (User): user the node belongs to
            bank_name (str): https://synapsepay.com/api/v3/institutions/show
            username (str): the user's username with the bank
            password (str): the user's password with the bank

        Returns:
            list: if no MFA, returns a list of AchUsNodes
            AchUsNode: if MFA, returns an AchUsNode with mfa_verified=False
        """
        payload = super(AchUsNode, cls).payload_for_create('ACH-US',
                                             bank_name=bank_name,
                                             username=username,
                                             password=password,
                                             mfa_verified=True)
        response = user.client.nodes.create(user.id, payload)
        if 'mfa' in response:
            # create unverified node
            return cls.unverified_from_response(user, response)
        else:
            # no mfa needed
            return cls.multiple_from_response(user, response['nodes'])

    @classmethod
    def payload_for_create(cls, nickname, account_number, routing_number,
                           account_type, account_class, **kwargs):
        """Build the API 'create node' payload specific to ACH-US."""
        payload = super(AchUsNode, cls).payload_for_create('ACH-US',
                                             nickname=nickname,
                                             account_number=account_number,
                                             routing_number=routing_number,
                                             account_type=account_type,
                                             account_class=account_class,
                                             **kwargs)
        return payload

    def verify_microdeposits(self, amount1, amount2):
        """Verify the microdeposits to activate ACH-US added by acct/routing.

        After adding an ACH-US nodes via account and routing number
        the user will receive two microdeposits to their account within a
        a couple days. The node will not have the ability to send funds until
        microdeposits are verified.

        Args:
            amount1 (float): the first microdeposit amount
            amount2 (float): the second microdeposit amount

        Returns:
            AchUsNode: a new instance representing the same API record
        """
        payload = {'micro': [amount1, amount2]}
        response = self.user.client.nodes.update(self.user.id, self.id, payload)
        return self.from_response(self.user, response)

    def answer_mfa(self, answer):
        """Answer the MFA questions presented during bank login attempt.

        This step is only necessary if the node's mfa_verified property is
        False. Present the value of the node's mfa_message property to the user
        and pass their answer to this method.

        If the user answers incorrectly, the node will remain unverified and
        the question will remain the same. If the bank requires an additional
        MFA question, the node will remain unverified but the question
        property will have a new value. Otherwise, if the user satisfies MFA,
        the method will retrieve their ACH-US node data.

        Args:
            answer (str): the user's response to the MFA question

        Returns:
            AchUsNode: (self) if still unverified, returns self
            list: if verification complete, returns a list of AchUsNodes
        """
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
            self.json = response
            return self
