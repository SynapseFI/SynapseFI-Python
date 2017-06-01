from .physical_document import PhysicalDocument
from .social_document import SocialDocument
from .virtual_document import VirtualDocument


class BaseDocument():
    """Object representation of a user's CIP base document.

    Contains various constructors (instances from existing API records or de
    novo) as well as methods for modifying base documents and attaching
    physical/social/virtual documents. Please check your organization's
    specific CIP agreement to learn the exact requirements for the exact number
    and types of documents that are required, which may also vary by user type
    (business/personal) or spending limit (10,000/day vs 1,000,000/day).
    """

    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __repr__(self):
        user = '{0}(id={1})'.format(self.user.__class__, self.user.id)
        clean_dict = self.__dict__.copy()
        clean_dict['user'] = user
        clean_dict['physical_documents'] = len(self.physical_documents)
        clean_dict['social_documents'] = len(self.social_documents)
        clean_dict['virtual_documents'] = len(self.virtual_documents)
        return '{0}({1})'.format(self.__class__, clean_dict)

    @classmethod
    def from_response(cls, user, response):
        """Construct a BaseDocument from a response dict."""
        physical_docs = PhysicalDocument.multiple_from_response(response['physical_docs'])
        social_docs = SocialDocument.multiple_from_response(response['social_docs'])
        virtual_docs = VirtualDocument.multiple_from_response(response['virtual_docs'])
        base_doc = cls(user=user,
                       id=response['id'],
                       name=response['name'],
                       email=response.get('email',None),
                       phone_number=response.get('phone_number',None),
                       ip=response.get('ip',None),
                       alias=response.get('alias',None),
                       entity_type=response.get('entity_type',None),
                       entity_scope=response.get('entity_scope',None),
                       birth_day=response.get('day',None),
                       birth_month=response.get('month',None),
                       birth_year=response.get('year',None),
                       address_street=response.get('address_street',None),
                       address_city=response.get('address_city',None),
                       address_subdivision=response.get('address_subdivision',None),
                       address_postal_code=response.get('address_postal_code',None),
                       address_country_code=response.get('address_country_code',None),
                       screening_results=response.get('screening_results',None),
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
        """Construct multiple BaseDocuments from a response dict."""
        base_docs = [cls.from_response(user, base_doc_data)
                     for base_doc_data in response]
        return base_docs

    @classmethod
    def create(cls, user, **kwargs):
        """Add a BaseDocument to the User.

        Args:
            email (str): user's email
            phone_number (str): user's phone number
            ip (str): user's IP address
            name (str): user's name
            alias (str): user's alias or DBA (use name if no alias)
            entity_type (str): https://docs.synapsepay.com/docs/user-resources#section-supported-entity-types
            entity_scope (str): https://docs.synapsepay.com/docs/user-resources#section-supported-entity-scope
            day (int): day of birth
            month (int): month of birth
            year (int): year of birth
            address_street (str): street address (as '123 Maple Street')
            address_city (str): address city
            address_subdivision (str): state, province, or other division
            address_postal_code (str): postal code
            address_country_code (str): country code (as 'US')

        Returns:
            BaseDocument: a new BaseDocument instance
        """
        payload = cls.payload_for_create(
            email=kwargs['email'],
            phone_number=kwargs['phone_number'],
            ip=kwargs['ip'],
            name=kwargs['name'],
            alias=kwargs['alias'],
            entity_type=kwargs['entity_type'],
            entity_scope=kwargs['entity_scope'],
            birth_day=kwargs['day'],
            birth_month=kwargs['month'],
            birth_year=kwargs['year'],
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
    def payload_for_create(email, phone_number, ip, name, alias,
                           entity_type, entity_scope, birth_day, birth_month,
                           birth_year, address_street, address_city,
                           address_subdivision, address_postal_code,
                           address_country_code):
        """Build the API 'add documents' payload from property values."""
        payload = {
            'documents': [{
                'email': email,
                'phone_number': phone_number,
                'ip': ip,
                'name': name,
                'alias': alias,
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

    def update(self, **kwargs):
        """Change the value of the supplied fields in the BaseDocument.

        Args:
            email (str): user's email
            phone_number (str): user's phone number
            ip (str): user's IP address
            name (str): user's name
            alias (str): user's alias or DBA (use name if no alias)
            entity_type (str): https://docs.synapsepay.com/docs/user-resources#section-supported-entity-types
            entity_scope (str): https://docs.synapsepay.com/docs/user-resources#section-supported-entity-scope
            day (int): day of birth
            month (int): month of birth
            year (int): year of birth
            address_street (str): street address (as '123 Maple Street')
            address_city (str): address city
            address_subdivision (str): state, province, or other division
            address_postal_code (str): postal code
            address_country_code (str): country code (as 'US')

        Returns:
            BaseDocument: a new instance representing the same API record
        """
        payload = self.payload_for_update(**kwargs)
        response = self.user.client.users.update(self.user.id, payload)
        user = self.user.from_response(self.user.client, response)
        base_doc = [base_doc for base_doc in user.base_documents
                    if base_doc.id == self.id]
        if base_doc:
            # id match found
            base_doc = base_doc[0]
        else:
            # id not found so assume the most recent one is correct
            base_doc = user.base_documents[-1]
        return base_doc

    def payload_for_update(self, **kwargs):
        """Build the API 'edit existing docs' payload from property values."""
        payload = {
            'documents': [{
                'id': self.id
            }]
        }
        for kwarg in kwargs:
            if kwarg == 'physical_documents':
                physical_docs = kwargs['physical_documents']
                payload['documents'][0]['physical_docs'] = physical_docs
            elif kwarg == 'social_documents':
                social_docs = kwargs['social_documents']
                payload['documents'][0]['social_docs'] = social_docs
            elif kwarg == 'virtual_documents':
                virtual_docs = kwargs['virtual_documents']
                payload['documents'][0]['virtual_docs'] = virtual_docs
            else:
                payload['documents'][0][kwarg] = kwargs[kwarg]
        return payload

    def add_physical_document(self, type=None, **kwargs):
        """Add a PhysicalDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-physical-document-types
            value (str): (opt) padded Base64 encoded image string
            file_path (str): path to image file (instead of value)
            url (str): url to image file (instead of value)
            byte_stream (str): byte array (instead of value)

        Returns:
            PhysicalDocument: a new PhysicalDocument instance
        """
        return PhysicalDocument.create(base_document=self, type=type,
                                       **kwargs)

    def add_social_document(self, type=None, value=None):
        """Add a SocialDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-social-document-types
            value (str): url to social media profile, for example

        Returns:
            SocialDocument: a new SocialDocument instance
        """
        return SocialDocument.create(base_document=self, type=type,
                                     value=value)

    def add_virtual_document(self, type=None, value=None):
        """Add a VirtualDocument to the BaseDocument.

        Args:
            type (str): https://docs.synapsepay.com/docs/user-resources#section-virtual-document-types
            value (str): SSN or TIN, for example

        Returns:
            VirtualDocument: a new VirtualDocument instance
        """
        return VirtualDocument.create(base_document=self, type=type,
                                      value=value)
