users_create_payload = {
    'logins': [
        {
            'email': 'pythonTest@synapsepay.com',
            'password': 'test1234',
            'read_only': False
        }
    ],
    'phone_numbers': [
        '901.111.1111'
    ],
    'legal_names': [
        'PYTHON TEST USER'
    ],
    'extra': {
        'note': 'Interesting user',
        'supp_id': '122eddfgbeafrfvbbb',
        'is_business': False
    }
}

users_update_payload = {
    'update': {
        'login': {
            'email': 'test2python@email.com',
            'password': 'test1234',
            'read_only': True
        },
        'phone_number': '9019411111',
        'legal_name': 'Some new name'
    }
}

user_create_args = {
    'email': 'hello@synapsepay.com',
    'phone_number': '555-555-5555',
    'legal_name': 'Hello McHello',
    'note': ':)',
    'supp_id': '123abc',
    'is_business': False,
    'cip_tag': 1,
    'password': 'password'
}

user_base_doc = {
    'email': 'scoobie@doo.com',
    'phone_number': '707-555-5555',
    'ip': '127.0.0.1',
    'name': 'Doctor BaseDoc',
    'alias': 'Basey',
    'entity_type': 'F',
    'entity_scope': 'Arts & Entertainment',
    'birth_day': 28,
    'birth_month': 2,
    'birth_year': 1990,
    'address_street': '42 Base Blvd',
    'address_city': 'San Francisco',
    'address_subdivision': 'CA',
    'address_postal_code': '94114',
    'address_country_code': 'US'
}

base_doc_args = {
            "email":"test@test.com",
            "phone_number":"901.111.1111",
            "ip":"127.0.0.1",
            "name":"FirstName LastName",
            "alias":"Test",
            "entity_type":"M",
            "entity_scope":"Arts & Entertainment",
            "day":2,
            "month":5,
            "year":1989,
            "address_street":"1 Market St.",
            "address_city":"SF",
            "address_subdivision":"CA",
            "address_postal_code":"94114",
            "address_country_code":"US"
            }
