USER_ID = '57d2055a86c27339ffdee4cc'

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
    'is_business': True,
    'cip_tag': 1,
    'password': 'password'
}
