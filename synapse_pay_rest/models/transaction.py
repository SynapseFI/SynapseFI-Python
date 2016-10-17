from .user import User
from .node import Node


class Transaction():
    """Represents a Node record with methods for constructing node instances.

    """

    @classmethod
    def create(node):
        pass

    @classmethod
    def by_id(node):
        pass

    @classmethod
    def all(node):
        pass

    @staticmethod
    def init_from_response(node, response):
        pass

    @staticmethod
    def init_multiple_from_response(node, response):
        nodes = [Node.init_from_response(node, node_data)
                 for node_data in response]
        return nodes

    def __init__(self):
        pass

    def add_comment(self, comment):
        pass

    def cancel(self):
        pass
