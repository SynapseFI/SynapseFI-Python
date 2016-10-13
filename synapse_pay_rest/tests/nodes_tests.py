from .test_helpers import *


class NodesTestCases(unittest.TestCase):
    def setUp(self):
        self.client = test_client
        self.user = self.client.users.create(users_create_payload)
        refresh_payload = {'refresh_token': self.user['refresh_token']}
        self.client.users.refresh(self.user['_id'], refresh_payload)

    def test_create_a_new_node(self):
        node = self.client.nodes.add(self.user['_id'], nodes_create_payload)
        self.assertIsNotNone(node['nodes'][0]['_id'])

    def test_get_existing_node(self):
        pass

    # def test_get_multiple_nodes(self):
    #     pass
    #     # self.client.nodes.get()

    # def test_update_node_info(self):
    #     pass

    # def test_delete_node(self):
    #     pass
