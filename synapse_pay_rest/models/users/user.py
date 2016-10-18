from synapse_pay_rest.client import Client
from .base_document import BaseDocument


class User():
    """Represents a user record with methods for constructing User instances.

    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    @classmethod
    def from_response(cls, client, response):
        user = cls(
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
        user.base_documents = BaseDocument.multiple_from_response(user,
                                                                  response['documents'])
        return user

    @classmethod
    def multiple_from_response(cls, client, response):
        users = [cls.from_response(client, user_data)
                 for user_data in response]
        return users

    @staticmethod
    def payload_for_create(email, phone_number, legal_name, **kwargs):
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
    def create(cls, client=None, email=None, phone_number=None,
               legal_name=None, **kwargs):
        """Create a user record in API and corresponding User instance.

        kwargs: password, read_only, note, supp_id, is_business
        """
        payload = cls.payload_for_create(email, phone_number, legal_name,
                                         **kwargs)
        response = client.users.create(payload)
        return cls.from_response(client, response)

    @classmethod
    def by_id(cls, client=None, id=None):
        response = client.users.get(id)
        return cls.from_response(client, response)

    @classmethod
    def all(cls, client=None, **kwargs):
        response = client.users.get(**kwargs)
        return cls.multiple_from_response(client, response['users'])

    def payload_for_refresh(self):
        return {'refresh_token': self.refresh_token}

    def authenticate(self):
        self.client.users.refresh(self.id, self.payload_for_refresh())
        return self

    def payload_for_update(self, **kwargs):
        payload = {
            'refresh_token': self.refresh_token,
            'update': {}
        }
        # TODO: Can simplify this when the API accepts null values w/o barfing
        if 'email' in kwargs:
            payload['update']['login'] = {'email': kwargs['email']}
            options = ['password', 'read_only']
            for option in options:
                if option in kwargs:
                    payload['update']['login'][option] = kwargs[option]
        if 'remove_login' in kwargs:
            payload['update']['remove_login'] = {'email': kwargs['remove_login']}
        options = ['legal_name', 'phone_number', 'remove_phone_number',
                   'cip_tag']
        for option in options:
            if option in kwargs:
                payload['update'][option] = kwargs[option]
        return payload

    def add_base_document(self, **kwargs):
        return BaseDocument.create(self, **kwargs)

    def edit_base_document(self, **kwargs):
        return BaseDocument.update(self, **kwargs)

    def add_legal_name(self, new_name):
        payload = self.payload_for_update(legal_name=new_name)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)

    def add_login(self, email, password=None, read_only=None):
        payload = self.payload_for_update(email=email, password=password,
                                          read_only=read_only)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)

    def remove_login(self, email):
        payload = self.payload_for_update(remove_login=email)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)

    def add_phone_number(self, phone_number):
        payload = self.payload_for_update(phone_number=phone_number)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)

    def remove_phone_number(self, phone_number):
        payload = self.payload_for_update(remove_phone_number=phone_number)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)

    def change_cip_tag(self, new_cip):
        payload = self.payload_for_update(cip_tag=new_cip)
        response = self.client.users.update(self.id, payload)
        return User.from_response(self.client, response)
