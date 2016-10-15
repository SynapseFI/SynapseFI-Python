from .user import User
from .nodes import *


class Node():
    """Represents a Node record with methods for constructing node instances.

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

    @staticmethod
    def create():
        pass

    @staticmethod
    def by_id():
        pass

    @staticmethod
    def all():
        pass

    @staticmethod
    def init_from_response(user, response):
        pass

    @staticmethod
    def init_multiple_from_response(user, response):
        nodes = [Node.init_from_response(client, node_data)
                 for node_data in response]
        return nodes

    def __init__(self):
        pass

    def deactivate(self):
        pass
