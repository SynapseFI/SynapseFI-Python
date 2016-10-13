
## Initialization

```python
from synapse_pay_rest import Client

options = {
    'oauth_key':USER_OAUTH KEY, # Optional
    'fingerprint':USER_FINGERPRINT,
    'client_id': YOUR_CLIENT_ID,
    'client_secret': YOUR_CLIENT_SECRET,
    'ip_address': USER_IP_ADDRESS,
    'development_mode': True #True will ping sandbox.synapsepay.com while False will ping synapsepay.com
}

USER_ID = ID_OF_USER # Optional

client = Client(options, USER_ID)

```

## User API Calls

```python

# Get All Users

users_response = client.Users.get()


# Create a User

create_payload = {
    "logins": [
        {
            "email": "pythonTest@synapsepay.com",
            "password": "test1234",
            "read_only":False
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

create_response = client.Users.create(payload=create_payload)


# Get User

user_response = client.Users.get(user_id=USER_ID)

# Update User

update_payload = {
    "refresh_token": "REFRESH_TOKEN",
    "update":{
        "login": {
            "email": "test2python@email.com",
            "password": "test1234",
            "read_only": True
        },
        "phone_number": "9019411111",
        "legal_name": "Some new name"
    }
}

update_response = client.Users.update(payload=update_payload)


# Add Document

ssn_payload = {
        "doc":{
        "birth_day":4,
        "birth_month":2,
        "birth_year":1940,
        "name_first":"John",
        "name_last":"doe",
        "address_street1":"1 Infinite Loop",
        "address_postal_code":"95014",
        "address_country_code":"US",
        "document_value":"3333",
        "document_type":"SSN"
    }
}

ssn_response = client.Users.add_doc(payload=ssn_payload)


# Answer KBA Questions

kba_payload = {
    "doc":{
        "question_set_id":"557520ad343463000300005a",
        "answers":[
            { "question_id": 1, "answer_id": 1 },
            { "question_id": 2, "answer_id": 1 },
            { "question_id": 3, "answer_id": 1 },
            { "question_id": 4, "answer_id": 1 },
            { "question_id": 5, "answer_id": 1 }
        ]
    }
}

kba_response = client.Users.answer_kba(payload=kba_payload)


# Attach a File

file_response = client.Users.attach_file(file='https://s3.amazonaws.com/synapse_django/static_assets/marketing/images/synapse_dark.png')


# Get Oauth Key

oauth_payload = {
    "refresh_token": USER_REFRESH_TOKEN
}

oauth_response = client.Users.refresh(payload=oauth_payload)

```


## Node API Calls

```python


# Get All Nodes

nodes_response = client.Nodes.get()


# Add SYNAPSE-US Node

synapse_node_payload = {
    "type":"SYNAPSE-US",
    "info":{
        "nickname":"My Synapse Wallet"
    },
    "extra":{
        "supp_id":"123sa"
    }
}

synapse_node_response = client.Nodes.add(payload=synapse_node_payload)


# Add ACH-US node through account login

login_payload = {
    "type":"ACH-US",
    "info":{
        "bank_id":"synapse_good",
        "bank_pw":"test1234",
        "bank_name":"fake"
    }
}

login_response = client.Nodes.add(payload=login_payload)


# Verify ACH-US Node via MFA

mfa_payload = {
    "access_token":ACCESS_TOKEN_IN_LOGIN_RESPONSE,
    "mfa_answer":"test_answer"
}

mfa_response = client.Nodes.verify(payload=mfa_payload)


# Add ACH-US Node through Account and Routing Number Details

acct_rout_payload = {
    "type":"ACH-US",
    "info":{
        "nickname":"Python Library Savings Account",
        "name_on_account":"Python Library",
        "account_num":"72347235423",
        "routing_num":"051000017",
        "type":"PERSONAL",
        "class":"CHECKING"
    },
    "extra":{
        "supp_id":"123sa"
    }
}

acct_rout_response = client.Nodes.add(payload=acct_rout_payload)


# Verify ACH-US Node via Micro-Deposits

micro_payload = {
    "micro":[0.1,0.1]
}

micro_response = client.Nodes.verify(node_id=NODE_ID, payload=micro_payload)


# Delete a Node

delete_response = client.Nodes.delete(node_id=NODE_ID)

```

## Transaction API Calls

```python


# Get All Trans

transactions_response = client.Trans.get(node_id=NODE_ID)


#Create a Transaction

trans_payload = {
    "to":{
        "type":"SYNAPSE-US",
        "id":"560adb4e86c27331bb5ac86e"
    },
    "amount":{
        "amount":1.10,
        "currency":"USD"
    },
    "extra":{
        "supp_id":"1283764wqwsdd34wd13212",
        "note":"Deposit to bank account",
        "process_on":1,
        "ip":"192.168.0.1"
    },
    "fees":[{
        "fee":1.00,
        "note":"Facilitator Fee",
        "to":{
            "id":"55d9287486c27365fe3776fb"
        }
    }]
}

create_response = client.Trans.create(node_id=NODE_ID, payload=trans_payload)


# Get a Transaction

transaction_response = client.Trans.get(node_id=NODE_ID, trans_id=TRANS_ID)


# Update Transaction

update_payload = {
    "comment": "hi"
}

update_response = client.Trans.update(node_id=NODE_ID, trans_id=TRANS_ID, payload=update_payload)


# Delete Transaction

delete_trans_response = client.Trans.delete(node_id=NODE_ID, trans_id=TRANS_ID)

```