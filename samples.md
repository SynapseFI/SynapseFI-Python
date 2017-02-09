## Initialization

```python
import os
from synapse_pay_rest import Client

required = {
    'client_id': os.environ['CLIENT_ID'], # your client id
    'client_secret': os.environ['CLIENT_SECRET'], # your client secret
    'fingerprint': 'user_fingerprint',
    'ip_address': '127.0.0.1', # user's IP
}

options = {
    'development_mode': True, # default False
    'logging': False # logs to stdout if True
}

client = Client(**required, **options)
```


## User Methods

#### Retrieve All Users

```python
from synapse_pay_rest import User

options = {
    'page': 1,
    'per_page': 20,
    'query': 'Steven' # name/email substring
}

users = User.all(client, **options)
```

#### Retrieve User by ID

```python
user = User.by_id(client, '57e97ab786c2737f4ccd4dc1')
```

#### Create a User

```python
required = {
    'email': 'hello@synapsepay.com',
    'phone_number': '555-555-5555',
    'legal_name': 'Hello McHello'
}

options = {
    'note': ':)',
    'supp_id': '123abc',
    'is_business': True,
    'cip_tag': 1
}

user = User.create(client, **required, **options)
```

#### Update a User's Personal Info
```python
user = user.add_legal_name('Sam Iam')
user = user.add_login('sam@iam.com')
user = user.remove_login('sam@iam.com')
user = user.add_phone_number('415-555-5555')
user = user.remove_phone_number('415-555-5555')
user = user.change_cip_tag(1)
```


## Adding Documents to Users

#### Add a CIP Base Document to a User
```python
options = {
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

base_document = user.add_base_document(**options)
user = base_document.user
```

#### Update an Existing CIP Base Document

```python
options = {
    'email': 'boop@doo.com',
    'phone_number': '415-555-5555',
    'ip': '127.0.0.2',
    'name': 'Doctor Boop',
    'alias': 'Boopsie',
    'entity_type': 'M',
    'entity_scope': 'Education',
    'birth_day': 21,
    'birth_month': 3,
    'birth_year': 1986,
    'address_street': '42 Boop Blvd',
    'address_city': 'Frisco',
    'address_subdivision': 'TX',
    'address_postal_code': '75034',
    'address_country_code': 'UK'
}

base_document = base_document.update(**options)
```

#### Add a Physical Document to a CIP Base Document

##### using a padded base64 string
```python
value = 'data:image/png;base64,SUQs=='
physical_document = base_document.add_physical_document(type='GOVT_ID',
                                                        value=value)
base_document = physical_document.base_document
```

##### using a file path
```python
file_path = 'path/to/file.png'
physical_document = base_document.add_physical_document(type='GOVT_ID',
                                                        file_path=file_path)
base_document = physical_document.base_document
```

##### using a URL
```python
url = 'https://cdn.synapsepay.com/static_assets/logo@2x.png'
physical_document = base_document.add_physical_document(type='GOVT_ID', url=url)
base_document = physical_document.base_document
```

##### using a byte stream
```python
byte_stream = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00...'
physical_document = base_document.add_physical_document(type='GOVT_ID',
                                                        mime_type='image/jpeg',
                                                        byte_stream=byte_stream)
base_document = physical_document.base_document
```

#### Add a Social Document to a CIP Base Document

```python
value = 'facebook.com/sankaet'
social_document = base_document.add_social_document(type= 'FACEBOOK',
                                                    value=value)
base_document = social_document.base_document
```

#### Add a Virtual Document to a CIP Base Document

```python
virtual_document = base_document.add_virtual_document(type='SSN', value='3333')

base_document = virtual_document.base_document
```

##### Answer KBA Questions for Virtual Document
If a Virtual Document is returned with status **SUBMITTED|MFA_PENDING**, you will need to have the user answer some questions:

```python
# check for any virtual docs with SUBMITTED|MFA_PENDING status
pending_doc = [doc for doc in base_document.virtual_documents 
               if doc.status == 'SUBMITTED|MFA_PENDING'][0]

for question in pending_doc.question_set:
    print(question.question)
    # => "Which one of the following zip codes is associated with you?"
    print(question.answers)
    # => {1=>"49230", 2=>"49209", 3=>"49268", 4=>"49532", 5=>"None Of The Above"}
    question.choice = 1 # this should be based on user input

# submit after finished answering all questions in question_set
pending_doc = pending_doc.submit_kba()

# assign the variable to the updated base doc if needed
base_document = pending_doc.base_document
```


## Node Methods

#### Retrieve All Nodes of a User

```python
from synapse_pay_rest import Node

options = {
    'page': 1,
    'per_page': 20,
    'type': 'ACH-US'
}

nodes = Node.all(user, **options)
```

#### Retrieve User's Node by Node ID

```python
node = Node.by_id(user, '57ec57be86c27345b3f8a159')
```

#### Create ACH-US Node(s) via Bank Login


Returns a list of nodes unless the bank requires MFA.
```python
from synapse_pay_rest.models.nodes import AchUsNode

required = {
    'bank_name': 'fake',
    'username': 'synapse_good',
    'password': 'test1234'
}

ach_us = AchUsNode.create_via_bank_login(user, **required)

ach_us.mfa_verified
# => False (requires MFA)
```

##### Verify Bank Login MFA

If the bank requires MFA, you will need to resolve the MFA question(s):
```python

ach_us.mfa_message
# => "Enter the code we texted to your phone number."

nodes = ach_us.answer_mfa('test_answer')
# => returns list of nodes if successful
# => returns self if incorrect answer or if there is a new MFA question

ach_us.mfa_verified
# => True
```

#### Create ACH-US Node via Account/Routing Number

```python
required = {
    'nickname': 'Primary Joint Checking',
    'account_number': '2222222222',
    'routing_number': '051000017',
    'account_type': 'PERSONAL',
    'account_class': 'CHECKING'
}

node = AchUsNode.create(user, **required)
```

##### Verify Microdeposits

ACH-US nodes added by account/routing must be verified with microdeposits:

```python
required = {
    'amount1': 0.1,
    'amount2': 0.1
}

node = node.verify_microdeposits(**required)
```

#### Deactivate a Node

```python
node.deactivate()
```


## Transaction Methods

#### Retrieve All Transactions Sent from a Node

```python
from synapse_pay_rest import Transaction

options = {
    'page': 1,
    'per_page': 20
}

transactions = Transaction.all(node, **options)
```

#### Retrieve Node's Transaction by Transaction ID

```python
transaction = Transaction.by_id(node, '57fc1a6886c2732e64a94c25')
```

#### Create a Transaction from a Node

```python
required = {
    'to_type': 'ACH-US',
    'to_id': '57f4241d86c27331523e2f26',
    'amount': 5.50,
    'currency': 'USD',
    'ip': '127.0.0.1'
}

options = {
    'process_in': 1, # delay until processing (in days)
    'note': 'hi synapse', # a note to synapse
    'supp_id': 'ABC123',
    'fees': [
        {
            'fee': 0.12, # Fee associated with the transaction
            'note': 'Test Fee 1', # Reason for the fee
            'to': {'id': fee_node.id} # Node ID where the fee would be credited when the transaction settles. Fee node has to be SYNAPSE-US type.
        }
    ]
}

transaction = Transaction.create(node, **required, **options)
```

#### Add a Comment to a Transaction's Status

```python
transaction = transaction.add_comment('this is my best transaction')
```

#### Cancel a Transaction

```python
transaction = transaction.cancel()
```
