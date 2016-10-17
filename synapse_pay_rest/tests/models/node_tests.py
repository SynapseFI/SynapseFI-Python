import unittest
import pdb
from synapse_pay_rest.tests.fixtures.client import *
from synapse_pay_rest.tests.fixtures.user import *
from synapse_pay_rest.tests.fixtures.node import *
from synapse_pay_rest.models.user import User
from synapse_pay_rest.models.node import Node
from synapse_pay_rest.models.nodes.ach_us_node import AchUsNode
from synapse_pay_rest.models.nodes.eft_ind_node import EftIndNode
from synapse_pay_rest.models.nodes.eft_np_node import EftNpNode
from synapse_pay_rest.models.nodes.iou_node import IouNode
from synapse_pay_rest.models.nodes.reserve_us_node import ReserveUsNode
from synapse_pay_rest.models.nodes.synapse_ind_node import SynapseIndNode
from synapse_pay_rest.models.nodes.synapse_np_node import SynapseNpNode
from synapse_pay_rest.models.nodes.synapse_us_node import SynapseUsNode
from synapse_pay_rest.models.nodes.wire_int_node import WireIntNode
from synapse_pay_rest.models.nodes.wire_us_node import WireUsNode


class NodeTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = User.create(self.client, **user_create_args)

    # def test_by_id(self):
    #     pass

    # def test_all(self):
    #     pass

    # def test_deactivate(self):
    #     pass

    # def test_verify_node_mfa(self):
    #     pass

    # def test_verify_node_microdeposits(self):
    #     pass

    def test_create_ach_us_via_account_and_routing(self):
        kwargs = {
            'account_number': '2345654323456754323',
            'routing_number': '051000017',
            'account_type': 'PERSONAL',
            'account_class': 'CHECKING',
            'supp_id': 'ABC123'
        }
        node = AchUsNode.create(self.user, 'Python Test Ach-US via Acct/Rt', **kwargs)
        pdb.set_trace()
        for prop in kwargs:
            print(prop)
            print(node)
            self.assertIsNotNone(getattr(node, prop))

        other_props = ['user', 'nickname', 'id', 'type', 'is_active',
                       'bank_long_name', 'name_on_account', 'permission']
        for prop in other_props:
            self.assertIsNotNone(getattr(node, prop))
