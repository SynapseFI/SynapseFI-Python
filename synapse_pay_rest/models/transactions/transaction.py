class Transaction():
    """Represents a transaction record with methods for constructing Transaction
    instances.

    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        node = '{0}(id={1})'.format(self.node.__class__, self.node.id)
        clean_dict = self.__dict__.copy()
        clean_dict['node'] = node
        return '{0}({1})'.format(self.__class__, clean_dict)

    @classmethod
    def from_response(cls, node, response):
        """Construct a Transaction from a response dict."""
        fee_amount = None
        fee_note = None
        fee_to_id = None
        if response.get('fees'):
            fee_amount = response['fees'][-1]['fee'],
            fee_note = response['fees'][-1]['note'],
            fee_to_id = response['fees'][-1]['to']['id']

        return cls(
            node=node,
            json=response,
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
            fees=response['fees'],
            recent_status=response['recent_status'],
            timeline=response['timeline'],
            from_info=response['from'],
            to_info=response['to'],
            to_type=response['to']['type'],
            to_id=response['to']['id'],
            fee_amount=fee_amount,
            fee_note=fee_note,
            fee_to_id=fee_to_id
        )

    @classmethod
    def multiple_from_response(cls, node, response):
        """Construct multiple Transactions from a response dict."""
        transactions = [cls.from_response(node, trans_data)
                        for trans_data in response]
        return transactions

    @staticmethod
    def payload_for_create(to_type, to_id, amount, currency, ip, **kwargs):
        """Build the API 'create transaction' payload from property values."""
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
                'supp_id': kwargs.get('supp_id') or '',
                'note': kwargs.get('note') or ''
            }
        }
        if 'process_in' in kwargs:
            payload['extra']['process_on'] = kwargs['process_in']
        fees = []
        # deprecated fee flow
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

        # new fee flow
        if 'fees' in kwargs:
            payload['fees'] = kwargs['fees']
        return payload

    @classmethod
    def create(cls, node=None, to_type=None, to_id=None, amount=None,
               currency=None, ip=None, idempotency_key=None, **kwargs):
        """Create a trans record in API and corresponding Transaction instance.

        Args:
            node (BaseNode): the node from which to send funds
            to_type (str): type of the 'to' node (e.g. 'ACH-US')
            to_id (id): id of the 'to' node
            amount (float): amount of currency
            currency (str): type of currency (e.g. 'USD')
            ip (str): ip of the sender
            idempotency_key (str): avoid accidentally performing the same operation twice
            process_in (int): delay in days until processing (default 1)
            note (str): a note to synapse
            supp_id (str): a supplementary id
            fees (list): fees associated with the transaction
            fee_amount (float): an additional fee to include (deprecated)
            fee_note (str): a note to go with the fee (deprecated)
            fee_to_id (str): the node id from which to take the fee (deprecated)

        Returns:
            Transaction: a new Transaction instance
        """
        payload = cls.payload_for_create(to_type, to_id, amount, currency, ip,
                                         **kwargs)
        response = node.user.client.trans.create(node.user.id, node.id,
                                                 payload, idempotency_key)
        return cls.from_response(node, response)

    @classmethod
    def by_id(cls, node=None, id=None):
        """Retrieve a trans record by id and create a Transaction instance from it.

        Args:
            node (BaseNode): the node from which to send funds
            id (str): id of the transaction to retrieve

        Returns:
            Transaction: a Transaction instance corresponding to the record
        """
        response = node.user.client.trans.get(node.user.id, node.id, id)
        return cls.from_response(node, response)

    @classmethod
    def all(cls, node=None, **kwargs):
        """Retrieve all trans records (limited by pagination) as Transactions.

        Args:
            node (BaseNode): the node from which to send funds
            per_page (int, str): (opt) number of records to retrieve
            page (int, str): (opt) page number to retrieve

        Returns:
            list: containing 0 or more Transaction instances
        """
        response = node.user.client.trans.get(node.user.id, node.id, **kwargs)
        return cls.multiple_from_response(node, response['trans'])

    def add_comment(self, comment):
        """Add a comment to the transaction's recent_status.

        Args:
            comment (str): text of the comment

        Returns:
            Transaction: a new instance representing the same record updated
        """
        payload = {'comment': comment}
        response = self.node.user.client.trans.update(self.node.user.id,
                                                      self.node.id,
                                                      self.id,
                                                      payload)
        if 'trans' in response:
            # API v3.1.0
            return self.from_response(self.node, response['trans'])
        else:
            # API v3.1.1
            return self.from_response(self.node, response)

    def cancel(self):
        """Cancel the transaction (will show in status).

        Returns:
            Transaction: a new instance representing the same record updated
        """
        response = self.node.user.client.trans.delete(self.node.user.id,
                                                      self.node.id,
                                                      self.id)
        return self.from_response(self.node, response)
