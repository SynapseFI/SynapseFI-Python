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


user_from_response = {
    "_id": "5c09b6d84884002c47b53c27",
    "_links": {
        "self": {
            "href": "https://uat-api.synapsefi.com/v3.1/users/5c09b6d84884002c47b53c27"
        }
    },
    "client": {
        "id": "5be38afd6a785e6bddfffe68",
        "name": "Test User"
    },
    "doc_status": {
        "physical_doc": "MISSING|INVALID",
        "virtual_doc": "MISSING|INVALID"
    },
    "documents": [],
    "emails": [],
    "extra": {
        "cip_tag": 1,
        "date_joined": 1544140503244,
        "extra_security": False,
        "is_business": False,
        "last_updated": 1544140503244,
        "public_note": None,
        "supp_id": "122eddfgbeafrfvbbb"
    },
    "is_hidden": False,
    "legal_names": [
        "basic user"
    ],
    "logins": [
        {
            "email": "test@synapsefi.com",
            "scope": "READ_AND_WRITE"
        }
    ],
    "permission": "UNVERIFIED",
    "phone_numbers": [
        "901.111.1111",
        "test@synapsefi.com"
    ],
    "photos": [],
    "refresh_token": "refresh_R61lpOv9PtUHc2geAK4uifXyB5FodxCLhM0N78r3"
}

test_docs = {
        "email":"test@test.com",
        "phone_number":"901.111.1111",
        "ip":"::1",
        "name":"Test User",
        "alias":"Test",
        "entity_type":"M",
        "entity_scope":"Arts & Entertainment",
        "day":2,
        "month":5,
        "year":1989,
        "address_street":"1 Market St.",
        "address_city":"San Francisco",
        "address_subdivision":"CA",
        "address_postal_code":"94114",
        "address_country_code":"US",
        "virtual_docs":[{
            "document_value":"2222",
            "document_type":"SSN"
        }],
        "physical_docs":[{
            "document_value": "data:image/gif;base64,SUQs==",
            "document_type": "GOVT_ID"
        }],
        "social_docs":[{
            "document_value":"https://www.facebook.com/valid",
            "document_type":"FACEBOOK"
        }]
    }

docs_response = {
    "_id": "5c0abeb9970f8426abc8df67",
    "_links": {
        "self": {
            "href": "https://uat-api.synapsefi.com/v3.1/users/5c0abeb9970f8426abc8df67"
        }
    },
    "client": {
        "id": "5be38afd6a785e6bddfffe68",
        "name": "Test User"
    },
    "doc_status": {
        "physical_doc": "SUBMITTED|VALID",
        "virtual_doc": "SUBMITTED|VALID"
    },
    "documents": [
        {
            "entity_scope": "Arts & Entertainment",
            "entity_type": "M",
            "id": "2a4a5957a3a62aaac1a0dd0edcae96ea2cdee688ec6337b20745eed8869e3ac8",
            "name": "Test User",
            "permission_scope": "UNVERIFIED",
            "physical_docs": [
                {
                    "document_type": "GOVT_ID",
                    "id": "9afdc3b20c3880f506525e71b3ea7b6eb4fa4c9cfe46b3d70136cbf0e5e59ea9",
                    "last_updated": 1544478983941,
                    "status": "SUBMITTED|REVIEWING"
                }
            ],
            "social_docs": [
                {
                    "document_type": "EMAIL",
                    "id": "2c45158f6431ca874bbe82f63d5905567854dde4d8b81539944e5779e5eee741",
                    "last_updated": 1544478983973,
                    "status": "SUBMITTED|REVIEWING"
                },
                {
                    "document_type": "FACEBOOK",
                    "id": "8f314a6a53f36ee569455761e49a2a7fe790d251c5611c65255befdb303602b7",
                    "last_updated": 1544478983962,
                    "status": "SUBMITTED|REVIEWING"
                },
                {
                    "document_type": "PHONE_NUMBER",
                    "id": "fda60784d6375bc44edafaaeae149626c4c13dcb92e85a2a7a00eec2cdfd2b6f",
                    "last_updated": 1544478984012,
                    "status": "SUBMITTED|REVIEWING"
                },
                {
                    "document_type": "DATE",
                    "id": "2b52edae636ca2fbe12ab1b08a344d381dabc3d2b92844cf7a8d8b6052b26d8e",
                    "last_updated": 1544478984419,
                    "status": "SUBMITTED|REVIEWING"
                },
                {
                    "document_type": "ADDRESS",
                    "id": "9253436898627bc318ef39059558ccce8617ecab27dc1bb17d73caa8040f6980",
                    "last_updated": 1544478984308,
                    "status": "SUBMITTED|REVIEWING"
                },
                {
                    "document_type": "IP",
                    "id": "28d9177b22c127d9a51d8903893864accf6e553ac326704a4c0d585eaad2516a",
                    "last_updated": 1544478984052,
                    "status": "SUBMITTED|REVIEWING"
                }
            ],
            "virtual_docs": [
                {
                    "document_type": "SSN",
                    "id": "ee596c2896dddc19b76c07a184fe7d3cf5a04b8e94b9108190cac7890739017f",
                    "last_updated": 1544478983978,
                    "status": "SUBMITTED|REVIEWING"
                }
            ]
        }
    ],
    "emails": [],
    "extra": {
        "cip_tag": 1,
        "date_joined": 1544208044991,
        "extra_security": False,
        "is_business": False,
        "last_updated": 1544478982302,
        "public_note": None,
        "supp_id": "my_user_id"
    },
    "is_hidden": False,
    "legal_names": [
        "Test User"
    ],
    "logins": [
        {
            "email": "test2@synapsepay.com",
            "scope": "READ_AND_WRITE"
        }
    ],
    "permission": "SEND-AND-RECEIVE",
    "phone_numbers": [
        "901.111.1111"
    ],
    "photos": [],
    "refresh_token": "refresh_thaC1YjAMrWcQPm7gB5SqRe9kpDxTViOG62I0J8L"
}

test_good_2fa_device = {
    "error_code": "10",
    "http_code": "202",
    "message": {
        "en": "MFA sent to easak@synapsefi.com."
    },
    "success": True
}

test_bad_2fa_device = {
    "error_code": "20",
    "http_code": "202",
    "message": {
        "en": "bad response"
    },
    "success": False
}