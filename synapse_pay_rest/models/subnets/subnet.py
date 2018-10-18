class Subnet():
    """Represents a Subnet record with methods for constructing Subnet
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
        """Construct a Subnet from a response dict."""
        return cls(
            node=node,
            json=response,
            id=response['_id'],
            account_class=response['account_class'],
            account_num=response['account_num'],
            client_id=response['client']['id'],
            client_name=response['client']['name'],
            nickname=response['nickname'],
            node_id=response['node_id'],
            routing_num_ach=response['routing_num']['ach'],
            routing_num_wire=response['routing_num']['wire'],
            user_id=response['user_id']
        )

    @classmethod
    def multiple_from_response(cls, node, response):
        """Construct multiple Subnets from a response dict."""
        subnets = [cls.from_response(node, subnets_data)
                        for subnets_data in response ]
        return subnets

    @staticmethod
    def payload_for_create(nickname, **kwargs):
        """Build the API 'create subnet' payload from property values."""
        payload = {
            "nickname": nickname
        }
        return payload


    @classmethod
    def create(cls, node=None, nickname=None, **kwargs):
        """Create a subnets record in API and corresponding Subnet instance.

        Args:
            node (BaseNode): the node from which the subnet belongs
            nickname (str): nickname of subnet

        Returns:
            Subnet: a new Subnet instance
        """
        payload = cls.payload_for_create(nickname,
                                         **kwargs)
        response = node.user.client.subnets.create(node.user.id, node.id, payload)
        return cls.from_response(node, response)

    @classmethod
    def by_id(cls, node=None, id=None):
        """Retrieve a subnets record by id and create a Subnet instance from it.

        Args:
            node (BaseNode): the node from which the subnet belongs
            id (str): id of the subnet to retrieve

        Returns:
            Subnet: a Subnet instance corresponding to the record
        """
        response = node.user.client.subnets.get(node.user.id, node.id, id)
        return cls.from_response(node, response)

    @classmethod
    def all(cls, node=None, **kwargs):
        """Retrieve all subnets records (limited by pagination) as Subnets.

        Args:
            node (BaseNode): the node from which the subnet belongs
            per_page (int, str): (opt) number of records to retrieve
            page (int, str): (opt) page number to retrieve

        Returns:
            list: containing 0 or more Subnet instances
        """
        response = node.user.client.subnets.get(node.user.id, node.id, **kwargs)
        return cls.multiple_from_response(node, response['subnets'])

    def lock(self):
        """Lock subnet

        Args:
            allowed (str): Denotes the subnet standing. Currently you can only set allowed to

        Returns:
            Subnet: a new instance representing the same record updated
        """
        payload = {
            'allowed': 'LOCKED'
        }
        response = self.node.user.client.subnets.update(self.node.user.id,
                                                      self.node.id,
                                                      self.id,
                                                      payload)
        if 'subnets' in response:
            # API v3.1.0
            return self.from_response(self.node, response['subnets'])
        else:
            # API v3.1.1
            return self.from_response(self.node, response)
