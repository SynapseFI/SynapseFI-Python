from synapse_pay_rest.models.users.user import User
from .base_node import BaseNode
from .ach_us_node import AchUsNode
from .eft_ind_node import EftIndNode
from .eft_np_node import EftNpNode
from .iou_node import IouNode
from .reserve_us_node import ReserveUsNode
from .synapse_ind_node import SynapseIndNode
from .synapse_np_node import SynapseNpNode
from .synapse_us_node import SynapseUsNode
from .triumph_subaccount_us_node import TriumphSubaccountUsNode
from .wire_int_node import WireIntNode
from .wire_us_node import WireUsNode
from .deposit_us_node import DepositUsNode
from .check_us_node import CheckUsNode
from .interchange_us_node import InterchangeUsNode
from .ib_deposit_us_node import IbDepositUsNode
from .ib_subaccount_us_node import IbSubaccountUsNode
from .clearing_us_node import ClearingUsNode
from .subaccount_us_node import SubaccountUsNode
from .card_us_node import CardUsNode
from .subcard_us_node import SubcardUsNode


class Node():
    """Factory for producing the various node types.

    The actual node subclasses descend from BaseNode, but the factory is named
    Node to be consistent with User and Transaction.
    """

    NODE_TYPES_TO_CLASSES = {
      'ACH-US': AchUsNode,
      'EFT-NP': EftNpNode,
      'EFT-IND': EftIndNode,
      'IOU': IouNode,
      'RESERVE-US': ReserveUsNode,
      'SYNAPSE-IND': SynapseIndNode,
      'SYNAPSE-NP': SynapseNpNode,
      'SYNAPSE-US': SynapseUsNode,
      'TRIUMPH-SUBACCOUNT-US': TriumphSubaccountUsNode,
      'WIRE-INT': WireIntNode,
      'WIRE-US': WireUsNode,
      'DEPOSIT-US': DepositUsNode,
      'CHECK-US': CheckUsNode,
      'INTERCHANGE-US': InterchangeUsNode,
      'IB-DEPOSIT-US': IbDepositUsNode,
      'IB-SUBACCOUNT-US': IbSubaccountUsNode,
      'CLEARING-US': ClearingUsNode,
      'SUBACCOUNT-US': SubaccountUsNode,
      'CARD-US': CardUsNode,
      'SUBCARD-US': SubcardUsNode
    }

    @classmethod
    def from_response(cls, user, response):
        """Construct a BaseNode subclass instance from a response dict."""
        args = {
          'user': user,
          'json': response,
          'type': response.get('type'),
          'id': response.get('_id'),
          'is_active': response.get('is_active'),
          'permission': response.get('allowed'),
          'nickname': response['info'].get('nickname'),
          'name_on_account': response['info'].get('name_on_account'),
          'bank_long_name': response['info'].get('bank_long_name'),
          'bank_name': response['info'].get('bank_name'),
          'account_type': response['info'].get('type'),
          'account_class': response['info'].get('class'),
          'account_number': response['info'].get('account_num'),
          'routing_number': response['info'].get('routing_num'),
          'account_id': response['info'].get('account_id'),
          'address': response['info'].get('address'),
          'swift': response['info'].get('swift'),
          'ifsc': response['info'].get('ifsc'),
          'user_info': response['extra']['other'].get('info',None),
          'timeline': response.get('timeline',None),
          'transactions': response['extra']['other'].get('transactions',None),
          'billpay_info': response['extra']['other'].get('billpay_info',None),
          'transaction_analysis': response['extra']['other'].get('transaction_analysis',None),
          'payee_name': response['info'].get('payee_name'),
          'document_id': response['info'].get('document_id'),
          'network': response['info'].get('network'),
          'card_type': response['info'].get('type'),
        }

        # correspondent info (optional)
        if response['info'].get('correspondent_info'):
            info = response['info']['correspondent_info']
            args['correspondent_swift'] = info.get('swift')
            args['correspondent_bank_name'] = info.get('bank_name')
            args['correspondent_routing_number'] = info.get('routing_num')
            args['correspondent_address'] = info.get('address')
            args['correspondent_swift'] = info.get('swift')

        # balance info (optional)
        if response['info'].get('balance'):
            info = response['info']['balance']
            args['balance'] = info.get('amount')
            args['currency'] = info.get('currency')

        # extra info (optional)
        if response.get('extra'):
            info = response['extra']
            args['supp_id'] = info.get('supp_id')
            args['gateway_restricted'] = info.get('gateway_restricted')

        #check info(optional)
        if response['info'].get('payee_address'):
            info = response['info']['payee_address']
            args['address_street'] = info.get('address_street')
            args['address_city'] = info.get('address_city')
            args['address_subdivision'] = info.get('address_subdivision')
            args['address_country_code'] = info.get('address_country_code')
            args['address_postal_code'] = info.get('address_postal_code')

        #cards info(optional)
        if response['info'].get('preferences'):
            info = response['info']['preferences']
            args['allow_foreign_transactions'] = info.get('allow_foreign_transactions')
            args['atm_withdrawal_limit'] = info.get('atm_withdrawal_limit')
            args['max_pin_attempts'] = info.get('max_pin_attempts')
            args['pos_withdrawal_limit'] = info.get('pos_withdrawal_limit')
            args['security_alerts'] = info.get('security_alerts')

        klass = cls.NODE_TYPES_TO_CLASSES.get(response['type'], BaseNode)
        return klass(**args)

    @classmethod
    def multiple_from_response(cls, user, response):
        """Construct multiple BaseNode subclass instances from a response dict.
        """
        nodes = [cls.from_response(user, node_data)
                 for node_data in response]
        return nodes

    @classmethod
    def by_id(cls, user=None, id=None, full_dehydrate='no'):
        """Retrieve a node record by id and create a BaseNode instance from it.

        Args:
            user (User): the  User that the node belongs to
            id (str): id of the node to retrieve
            full_dehydrate(optional, str): if 'yes', returns transaction data on node

        Returns:
            BaseNode: a BaseNode instance corresponding to the record
        """
        response = user.client.nodes.get(user.id, id, full_dehydrate=full_dehydrate)
        return cls.from_response(user, response)

    @classmethod
    def all(cls, user=None, **kwargs):
        """Retrieve all node records (limited by pagination) as BaseNodes.

        Args:
            user (User): the  User that the node belongs to
            per_page (int, str): (opt) number of records to retrieve
            page (int, str): (opt) page number to retrieve
            type (str): (opt) node type to filter by (as 'ACH-US')

        Returns:
            list: containing 0 or more BaseNode instances
        """
        response = user.client.nodes.get(user.id, **kwargs)
        return cls.multiple_from_response(user, response['nodes'])
