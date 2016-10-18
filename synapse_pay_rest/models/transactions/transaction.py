

class Transaction():
    """Represents a transaction record with methods for constructing Transaction
    instances.

    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    @classmethod
    def from_response(cls, node, response):
        return cls(
            node=node,
            id=response['_id'],
            amount=response['amount']['amount'],
            currency=response['amount']['currency'],
            client_id=response['client']['id'],
            client_name=response['client']['name'],
            created_on=response['extra']['created_on'],
            ip=response['extra']['ip'],
            latlon=response['extra']['latlon'],
            note=response['extra']['note'],
            process_on=response['extra']['process_on'],
            supp_id=response['extra']['supp_id'],
            webhook=response['extra']['webhook'],
            fees=response['fees'],
            recent_status=response['recent_status'],
            timeline=response['timeline'],
            from_info=response['from'],
            to_info=response['to'],
            to_type=response['to']['type'],
            to_id=response['to']['id'],
            fee_amount=response['fees'][-1]['fee'],
            fee_note=response['fees'][-1]['note'],
            fee_to_id=response['fees'][-1]['to']['id'],
        )

    @classmethod
    def multiple_from_response(cls, node, response):
        nodes = [cls.from_response(node, trans_data)
                 for trans_data in response]
        return nodes

    @staticmethod
    def payload_for_create(to_type, to_id, amount, currency, ip, **kwargs):
        payload = {
            'to': {
                'type': to_type,
                'id': to_id
            },
            'amount': {
                'amount': amount,
                'currency': currency
            },
            'extra': {
                'ip': ip,
                'supp_id': kwargs.get('supp_id'),
                'note': kwargs.get('note')
            }
        }
        if 'process_in' in kwargs:
            payload['extra']['process_on'] = kwargs['process_in']
        fees = []
        if 'fee_amount' in kwargs:
            fee = {
                'fee': kwargs['fee_amount'],
                'note': kwargs.get('fee_note'),
                'to': {
                    'id': kwargs['fee_to_id']
                }
            }
            fees.append(fee)
        if fees:
            payload['fees'] = fees
        return payload

    @classmethod
    def create(cls, node=None, to_type=None, to_id=None, amount=None,
               currency=None, ip=None, **kwargs):
        # TODO allow multiple fees
        # TODO idempotency key
        payload = cls.payload_for_create(to_type, to_id, amount, currency, ip,
                                         **kwargs)
        node.user.authenticate()
        response = node.user.client.trans.create(node.user.id, node.id,
                                                 payload)
        return cls.from_response(node, response)

    @classmethod
    def by_id(cls, node=None, id=None):
        response = node.user.client.trans.get(node.user.id, node.id, id)
        return cls.from_response(node, response)

    @classmethod
    def all(cls, node=None, **kwargs):
        response = node.user.client.trans.get(node.user.id, node.id, **kwargs)
        return cls.multiple_from_response(node, response['trans'])

    def add_comment(self, comment):
        payload = {'comment': comment}
        response = self.node.user.client.trans.update(self.node.user.id,
                                                      self.node.id,
                                                      self.id,
                                                      payload)
        return self.from_response(self.node, response['trans'])

    def cancel(self):
        response = self.node.user.client.trans.delete(self.node.user.id,
                                                      self.node.id,
                                                      self.id)
        return self.from_response(self.node, response)
