users_create_payload = {
    "logins": [
        {
            "email": "pythonTest@synapsepay.com",
            "password": "test1234",
            "read_only": False
        }
    ],
    "phone_numbers": [
        "901.111.1111"
    ],
    "legal_names": [
        "PYTHON TEST USER"
    ],
    "extra": {
        "note": "Interesting user",
        "supp_id": "122eddfgbeafrfvbbb",
        "is_business": False
    }
}

users_update_payload = {
    "update": {
        "login": {
            "email": "test2python@email.com",
            "password": "test1234",
            "read_only": True
        },
        "phone_number": "9019411111",
        "legal_name": "Some new name"
    }
}
