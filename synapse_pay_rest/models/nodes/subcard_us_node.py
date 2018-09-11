from .base_node import BaseNode


class SubcardUsNode(BaseNode):
    """Represents a SUBCARD-US node."""

    @classmethod
    def payload_for_create(cls, nickname, document_id, card_type, **kwargs):
        """Build the API 'create node' payload specific to SUBCARD-US."""
        payload = super(SubcardUsNode, cls).payload_for_create('SUBCARD-US',
                                             nickname=nickname,
                                             document_id=document_id,
                                             card_type=card_type,
                                             **kwargs)
        return payload

    def update_preferences(self, **kwargs):
        """Update SUBCARD-US preferences

        Returns:
            SubcardUsNode: a new instance representing the same API record
        """
        payload = self.payload_for_preferences(**kwargs)
        response = self.user.client.nodes.update(self.user.id, self.id, payload)
        return self.from_response(self.user, response)

    def update_allowed(self, allowed):
        """Update SUBCARD-US allowed. Change to INACTIVE if card is misplaced. LOCKED if lost.

        Returns:
            SubcardUsNode: a new instance representing the same API record
        """
        payload = {'allowed': allowed}
        response = self.user.client.nodes.update(self.user.id, self.id, payload)
        return self.from_response(self.user, response)

    def payload_for_preferences(self, **kwargs):
        payload = {
            'preferences': {}
        }

        if 'allow_foreign_transactions' in kwargs:
            payload['preferences']['allow_foreign_transactions'] = kwargs['allow_foreign_transactions']
        if 'atm_withdrawal_limit' in kwargs:
            payload['preferences']['atm_withdrawal_limit'] = kwargs['atm_withdrawal_limit']
        if 'max_pin_attempts' in kwargs:
            payload['preferences']['max_pin_attempts'] = kwargs['max_pin_attempts']
        if 'pos_withdrawal_limit' in kwargs:
            payload['preferences']['pos_withdrawal_limit'] = kwargs['pos_withdrawal_limit']
        if 'security_alerts' in kwargs:
            payload['preferences']['security_alerts'] = kwargs['security_alerts']
        return payload
