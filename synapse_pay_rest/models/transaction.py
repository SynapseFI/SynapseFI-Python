from .user import User
from .node import Node


class Transaction():
    """Represents a Node record with methods for constructing node instances.

    """

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

    def add_comment(self):
        pass

    def cancel(self):
        pass
