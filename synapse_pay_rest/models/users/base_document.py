from .physical_document import PhysicalDocument
from .social_document import SocialDocument
from .virtual_document import VirtualDocument


class BaseDocument():
    """
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    @classmethod
    def from_response(cls, user, response):
        physical_docs = PhysicalDocument.multiple_from_response(response['physical_docs'])
        social_docs = SocialDocument.multiple_from_response(response['social_docs'])
        virtual_docs = VirtualDocument.multiple_from_response(response['virtual_docs'])
        base_doc = cls(user=user,
                       id=response['id'],
                       name=response['name'],
                       permission_scope=response['permission_scope'],
                       physical_documents=physical_docs,
                       social_documents=social_docs,
                       virtual_documents=virtual_docs)

        for doc in physical_docs:
            doc.base_document = base_doc
        for doc in social_docs:
            doc.base_document = base_doc
        for doc in virtual_docs:
            doc.base_document = base_doc

        return base_doc

    @classmethod
    def multiple_from_response(cls, user, response):
        base_docs = [cls.from_response(user, base_doc_data)
                     for base_doc_data in response]
        return base_docs

    @classmethod
    def create(cls, user, **kwargs):
        payload = cls.payload_for_create(
            email=kwargs['email'],
            phone_number=kwargs['phone_number'],
            ip=kwargs['ip'],
            name=kwargs['name'],
            aka=kwargs['aka'],
            entity_type=kwargs['entity_type'],
            entity_scope=kwargs['entity_scope'],
            birth_day=kwargs['birth_day'],
            birth_month=kwargs['birth_month'],
            birth_year=kwargs['birth_year'],
            address_street=kwargs['address_street'],
            address_city=kwargs['address_city'],
            address_subdivision=kwargs['address_subdivision'],
            address_postal_code=kwargs['address_postal_code'],
            address_country_code=kwargs['address_country_code']
        )
        response = user.client.users.update(user.id, payload)
        user = user.from_response(user.client, response)
        base_document = user.base_documents[-1]
        return base_document

    @staticmethod
    def payload_for_create(email, phone_number, ip, name, aka,
                           entity_type, entity_scope, birth_day, birth_month,
                           birth_year, address_street, address_city,
                           address_subdivision, address_postal_code,
                           address_country_code):
        payload = {
            'documents': [{
                'email': email,
                'phone_number': phone_number,
                'ip': ip,
                'name': name,
                'alias': aka,
                'entity_type': entity_type,
                'entity_scope': entity_scope,
                'day': birth_day,
                'month': birth_month,
                'year': birth_year,
                'address_street': address_street,
                'address_city': address_city,
                'address_subdivision': address_subdivision,
                'address_postal_code': address_postal_code,
                'address_country_code': address_country_code
            }]
        }
        return payload
