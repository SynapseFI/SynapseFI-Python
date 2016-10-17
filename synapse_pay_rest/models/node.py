from .user import User
from .nodes.ach_us_node import AchUsNode
from .nodes.eft_ind_node import EftIndNode
from .nodes.eft_np_node import EftNpNode
from .nodes.iou_node import IouNode
from .nodes.reserve_us_node import ReserveUsNode
from .nodes.synapse_ind_node import SynapseIndNode
from .nodes.synapse_np_node import SynapseNpNode
from .nodes.synapse_us_node import SynapseUsNode
from .nodes.wire_int_node import WireIntNode
from .nodes.wire_us_node import WireUsNode


class Node():
    """ Factory for producing the various node types, which descend from
    BaseNode.
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
      'WIRE-INT': WireIntNode,
      'WIRE-US': WireUsNode
    }

    @classmethod
    def create(user):
        pass

    @classmethod
    def by_id(user):
        pass

    @classmethod
    def all(user):
        pass

    @staticmethod
    def init_from_response(user, response):
        pass

    @staticmethod
    def init_multiple_from_response(user, response):
        nodes = [Node.init_from_response(user, node_data)
                 for node_data in response]
        return nodes
