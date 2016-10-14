
class User():
    """Represents a User record with methods for constructing user instances.

    """

    @classmethod
    def create(cls, client, email, phone_number, legal_name, **kwargs):
        """Create a user record in API and corresponding User instance.

        kwargs: password, readonly, note, supp_id, is_business
        """
        payload = cls.payload_for_create(email, phone_number, legal_name,
                                         **kwargs)
        response = client.users.create(payload)
        return cls.init_from_response(client, response)

    @classmethod
    def by_id(cls, client, id):
        response = client.users.get(id)
        return cls.init_from_response(client, response)

    @classmethod
    def all(cls, client, **kwargs):
        response = client.users.get(**kwargs)
        return cls.init_multiple_from_response(client, response['users'])

    @classmethod
    def payload_for_create(cls, email, phone_number, legal_name, **kwargs):
        payload = {
          'logins': [{'email': email}],
          'phone_numbers': [phone_number],
          'legal_names': [legal_name],
          'extra': {
            'supp_id': kwargs.get('supp_id'),
            'note': kwargs.get('note'),
            'is_business': kwargs.get('is_business'),
            'cip_tag': kwargs.get('cip_tag')
          }
        }
        return payload

    @classmethod
    def init_from_response(cls, client, response):
        return cls(
          client=client,
          id=response['_id'],
          refresh_token=response['refresh_token'],
          logins=response['logins'],
          phone_numbers=response['phone_numbers'],
          legal_names=response['legal_names'],
          permission=response['permission'],
          note=response.get('extra').get('note'),
          supp_id=response.get('extra').get('supp_id'),
          is_business=response.get('extra').get('is_business'),
          cip_tag=response.get('extra').get('cip_tag')
        )

    @classmethod
    def init_multiple_from_response(cls, client, response):
        users = []
        for user_data in response:
            user = cls.init_from_response(client, user_data)
            users.append(user)
        return users

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def authenticate(self):
        pass

    def update(self):
        pass

    def create_base_document(self):
        pass

    def add_login(self):
        pass

    def remove_login(self):
        pass

    def add_phone_number(self):
        pass

    def remove_phone_number(self):
        pass

    def nodes(self):
        pass

    def node_by_id(self):
        pass

    def create_ach_us_node(self):
        pass

    def create_ach_us_nodes_via_bank_login(self):
        pass

    def create_eft_ind_node(self):
        pass

    def create_eft_np_node(self):
        pass

    def create_iou_node(self):
        pass

    def create_reserve_us_node(self):
        pass

    def create_synapse_ind_node(self):
        pass

    def create_synapse_np_node(self):
        pass

    def create_synapse_us_node(self):
        pass

    def create_wire_int_node(self):
        pass

    def create_wire_us_node(self):
        pass
