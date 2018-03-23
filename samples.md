## Initialization

```python
import os
from synapse_pay_rest import Client

args = {
    'client_id': os.environ['TEST_CLIENT_ID'], # your client id
    'client_secret': os.environ['TEST_CLIENT_SECRET'], # your client secret
    'fingerprint': 'user_fingerprint',
    'ip_address': '127.0.0.1', # user's IP
    'development_mode': True, # (optional) default False
    'logging': False # (optional) logs to stdout if True
}

client = Client(**args)
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

optional:
user = User.by_id(client, '57e97ab786c2737f4ccd4dc1', full_dehydrate='yes')

Example of user response with full_dehydrate:
**Please note: if full_dehydrate='no', some fields will return as 'None'

user.base_documents[0] =

{
  'user': "<class 'synapse_pay_rest.models.users.user.User'>(id=592f1dfa8384540026e39a95)",
  'id': '189d2fc37c1ee5694aa62f302bcd7c0efaae2c0229f45bfc8bb3470f6f7ab92a',
  'name': 'Charlie Brown',
  'email': 'test@test.com',
  'phone_number': '111-111-1111',
  'ip': '::1',
  'alias': 'Woof Woof',
  'entity_type': 'M',
  'entity_scope': 'Arts & Entertainment',
  'birth_day': 2,
  'birth_month': 5,
  'birth_year': 1989,
  'address_street': '170 St Germain Ave',
  'address_city': 'SF',
  'address_subdivision': 'CA',
  'address_postal_code': '94114',
  'address_country_code': 'US',
  'screening_results': {
    '561': 'NO_MATCH',
    'aucl': 'NO_MATCH',
    'concern_location': 'NO_MATCH',
    'dpl': 'NO_MATCH',
    'dtc': 'NO_MATCH',
    'el': 'NO_MATCH',
    'eucl': 'NO_MATCH',
    'fatf_non_cooperative_jurisdiction': 'NO_MATCH',
    'fbi_bank_robbers': 'NO_MATCH',
    'fbi_counter_intelligence': 'NO_MATCH',
    'fbi_crimes_against_children': 'NO_MATCH',
    'fbi_criminal_enterprise_investigations': 'NO_MATCH',
    'fbi_cyber': 'NO_MATCH',
    'fbi_domestic_terrorism': 'NO_MATCH',
    'fbi_human_trafficking': 'NO_MATCH',
    'fbi_murders': 'NO_MATCH',
    'fbi_violent_crimes': 'NO_MATCH',
    'fbi_wanted_terrorists': 'NO_MATCH',
    'fbi_white_collar': 'NO_MATCH',
    'fincen_red_list': 'NO_MATCH',
    'fse': 'NO_MATCH',
    'fto_sanctions': 'NO_MATCH',
    'futures_sanctions': 'NO_MATCH',
    'hkma_sanctions': 'NO_MATCH',
    'hm_treasury_sanctions': 'NO_MATCH',
    'isn': 'NO_MATCH',
    'mas_sanctions': 'NO_MATCH',
    'monitored_location': 'NO_MATCH',
    'ns-isa': 'NO_MATCH',
    'ofac_561_list': 'NO_MATCH',
    'ofac_eo13645': 'NO_MATCH',
    'ofac_fse': 'NO_MATCH',
    'ofac_fse_ir': 'NO_MATCH',
    'ofac_fse_sy': 'NO_MATCH',
    'ofac_isa': 'NO_MATCH',
    'ofac_ns_isa': 'NO_MATCH',
    'ofac_plc': 'NO_MATCH',
    'ofac_sdn': 'NO_MATCH',
    'ofac_ssi': 'NO_MATCH',
    'ofac_syria': 'NO_MATCH',
    'ofac_ukraine_eo13662': 'NO_MATCH',
    'osfi': 'NO_MATCH',
    'pep': 'NO_MATCH',
    'plc': 'NO_MATCH',
    'primary_concern': 'NO_MATCH',
    'sdn': 'NO_MATCH',
    'ssi': 'NO_MATCH',
    'tel_sanctions': 'NO_MATCH',
    'ukcl': 'NO_MATCH',
    'uvl': 'NO_MATCH'
  },
  'permission_scope': 'SEND|RECEIVE|1000|DAILY',
  'physical_documents': 1,
  'social_documents': 4,
  'virtual_documents': 1
}
```

#### Create a User

```python
args = {
    'email': 'hello@synapsepay.com',
    'phone_number': '555-555-5555',
    'legal_name': 'Hello McHello',
    'note': ':)',  # optional
    'supp_id': '123abc',  # optional
    'is_business': True,
    'cip_tag': 1
}

user = User.create(client, **args)
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

optional:
node = Node.by_id(user, '57ec57be86c27345b3f8a159', full_dehydrate='yes')

Example of node response with full_dehydrate:
**Please note: if full_dehydrate='no', some fields will return as 'None'

node =

<class'synapse_pay_rest.models.nodes.ach_us_node.AchUsNode'>({
  'user': "<class 'synapse_pay_rest.models.users.user.User'>(id=592f1dfa8384540026e39a95)",
  'type': 'ACH-US',
  'id': '592f1e2d603964002f1b07f7',
  'is_active': True,
  'permission': 'LOCKED',
  'nickname': 'SynapsePay Test Checking Account - 8901',
  'name_on_account': ' ',
  'bank_long_name': 'CAPITAL ONE N.A.',
  'bank_name': 'CAPITAL ONE N.A.',
  'account_type': 'PERSONAL',
  'account_class': 'CHECKING',
  'account_number': '12345678901',
  'routing_number': '031176110',
  'account_id': None,
  'address': 'PO BOX 85139, RICHMOND, VA, US',
  'swift': None,
  'ifsc': None,
  'user_info': {
    'account_id': 'fd52bf51f0354335e634940139a006ef91d7e789c665857e9821656d18e7d012',
    'addresses': [
      {
        'city': 'San Francisco',
        'state': 'CA',
        'street': '5315 Castro St.',
        'zipcode': '94110'
      }
    ],
    'dob': '',
    'emails': [
      'test@synapsepay.com'
    ],
    'names': [
      'Test User'
    ],
    'phone_numbers': [
      '1652545112',
      '1432656106',
      '1888321821',
      '6589100779'
    ]
  },
  'timeline': [
    {
      'date': 1496260140541,
      'note': 'Node created.'
    },
    {
      'date': 1496260142204,
      'note': 'Unable to send micro deposits as node allowed is not CREDIT.'
    },
    {
      'date': 1496260420927,
      'note': "User locked. Thus node 'allowed' changed to LOCKED."
    }
  ],
  'transactions': [
    {
      'amount': 8.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 8693.0,
      'date': 1470715200.0,
      'debit': False,
      'description': 'CAPITAL ONE MOBILE PMT PPD:32078173097005',
      'pending': False
    },
    {
      'amount': 249.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 827.0,
      'date': 1411358400.0,
      'debit': False,
      'description': 'WF Credit Card PPD:21164346914575',
      'pending': True
    },
    {
      'amount': 61.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 4284.0,
      'date': 1460779200.0,
      'debit': False,
      'description': 'AMEX EPAYMENT PPD:22042046432370',
      'pending': True
    },
    {
      'amount': 289.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 2039.0,
      'date': 1481432400.0,
      'debit': False,
      'description': 'BK OF AM CRD PPD:76067398573865',
      'pending': True
    },
    {
      'amount': 489.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1938.0,
      'date': 1397880000.0,
      'debit': True,
      'description': 'CAPITAL ONE MOBILE PMT PPD:12283074879351',
      'pending': True
    },
    {
      'amount': 306.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 4175.0,
      'date': 1436587200.0,
      'debit': False,
      'description': 'BK OF AM CRD PPD:36590769006391',
      'pending': False
    },
    {
      'amount': 162.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 2830.0,
      'date': 1480654800.0,
      'debit': True,
      'description': 'Payment to Chase card PPD:50214599701703',
      'pending': True
    },
    {
      'amount': 40.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1738.0,
      'date': 1425099600.0,
      'debit': False,
      'description': 'BK OF AM CRD PPD:51422971086988',
      'pending': False
    },
    {
      'amount': 126.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 8386.0,
      'date': 1393131600.0,
      'debit': False,
      'description': 'CAPITAL ONE MOBILE PMT PPD:83488871898117',
      'pending': False
    },
    {
      'amount': 18.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 5685.0,
      'date': 1439611200.0,
      'debit': True,
      'description': 'DISCOVER E-PAYMENT PPD:35631911243360',
      'pending': True
    },
    {
      'amount': 67.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 4634.0,
      'date': 1416027600.0,
      'debit': True,
      'description': 'DISCOVER E-PAYMENT PPD:52756385725550',
      'pending': True
    },
    {
      'amount': 228.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1321.0,
      'date': 1404532800.0,
      'debit': False,
      'description': 'Payment to Chase card PPD:18727859364976',
      'pending': True
    },
    {
      'amount': 107.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1065.0,
      'date': 1414296000.0,
      'debit': True,
      'description': 'CAPITAL ONE MOBILE PMT PPD:26468111647708',
      'pending': True
    },
    {
      'amount': 103.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 7907.0,
      'date': 1415336400.0,
      'debit': False,
      'description': 'DISCOVER E-PAYMENT PPD:82490497472711',
      'pending': True
    },
    {
      'amount': 106.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 7574.0,
      'date': 1468814400.0,
      'debit': True,
      'description': 'DISCOVER E-PAYMENT PPD:38032120832376',
      'pending': False
    },
    {
      'amount': 50.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 8876.0,
      'date': 1406433600.0,
      'debit': True,
      'description': 'Payment to Chase card PPD:35892567736339',
      'pending': True
    },
    {
      'amount': 61.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 9015.0,
      'date': 1435291200.0,
      'debit': False,
      'description': 'CITI CARDS PPD:28749452237576',
      'pending': True
    },
    {
      'amount': 445.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 9027.0,
      'date': 1447477200.0,
      'debit': True,
      'description': 'Payment to Chase card PPD:77434089827332',
      'pending': False
    },
    {
      'amount': 343.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1252.0,
      'date': 1428206400.0,
      'debit': True,
      'description': 'Payment to Chase card PPD:48935439759518',
      'pending': True
    },
    {
      'amount': 50.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 5973.0,
      'date': 1462766400.0,
      'debit': True,
      'description': 'WF Credit Card PPD:91101427763846',
      'pending': False
    },
    {
      'amount': 253.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 2814.0,
      'date': 1401854400.0,
      'debit': False,
      'description': 'CAPITAL ONE MOBILE PMT PPD:79516847131777',
      'pending': True
    },
    {
      'amount': 275.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 9891.0,
      'date': 1423112400.0,
      'debit': False,
      'description': 'WF Credit Card PPD:69798304985993',
      'pending': True
    },
    {
      'amount': 102.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1775.0,
      'date': 1421211600.0,
      'debit': True,
      'description': 'DISCOVER E-PAYMENT PPD:67858400658712',
      'pending': True
    },
    {
      'amount': 382.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 1585.0,
      'date': 1402632000.0,
      'debit': False,
      'description': 'BK OF AM CRD PPD:59371638589444',
      'pending': False
    },
    {
      'amount': 486.0,
      'category': {
        'primary': '',
        'subcategory': ''
      },
      'current_balance': 3946.0,
      'date': 1404187200.0,
      'debit': True,
      'description': 'WF Credit Card PPD:97364551261150',
      'pending': False
    }
  ],
  'balance': '800.00',
  'currency': 'USD',
  'supp_id': '',
  'gateway_restricted': None
})

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
args = {
    'to_type': 'ACH-US',
    'to_id': '57f4241d86c27331523e2f26',
    'amount': 5.50,
    'currency': 'USD',
    'ip': '127.0.0.1',
    'process_in': 0, # delay until processing (in days) [optional]
    'note': 'hi synapse', # a note to synapse [optional]
    'supp_id': 'ABC123', # optional
    'fees': [   # optional
        {
            'fee': 0.12, # Fee associated with the transaction
            'note': 'Test Fee 1', # Reason for the fee
            'to': {'id': fee_node.id} # Node ID where the fee would be credited when the transaction settles. Fee node has to be SYNAPSE-US type.
        }
    ]
}

transaction = Transaction.create(node, **args)
```

#### Add a Comment to a Transaction's Status

```python
transaction = transaction.add_comment('this is my best transaction')
```

#### Cancel a Transaction

```python
transaction = transaction.cancel()
```

## Subnet Methods

#### Retrieve All Subnets Sent from a Node

```python
from synapse_pay_rest import Subnet

options = {
    'page': 1,
    'per_page': 20
}

subnets = Subnet.all(node, **options)
```

#### Retrieve Node's Subnet by Subnet ID

```python
subnet = Subnet.by_id(node, '57fc1a6886c2732e64a94c25')
```

#### Create a Subnet from a Node

```python
args = {
    'nickname': 'Test Subnet'
}

subnet = Subnet.create(node, **args)
```

#### Lock Subnet

```python
subnet = subnet.lock()
```

## Subscription Methods

#### Retrieve All Subscriptions

```python
from synapse_pay_rest import Subscription

options = {
    'page': 1,
    'per_page': 20
}

subscription = Subscription.all(client)
```

#### Retrieve Subscription by ID

```python
subscription = Subscription.by_id(client, '57fc1a6886c2732e64a94c25')
```

#### Create a Subscription

```python
args = {
  'scope': [
    'USERS|POST',
    'USER|PATCH',
    'NODES|POST',
    'NODE|PATCH',
    'TRANS|POST',
    'TRAN|PATCH'
  ],
  'url': 'https://requestb.in/1756g2g1'
}

subscription = Subscription.create(client, **args)
```

#### Update a Subscription's URL

```python
new_url = 'test.com'
subscription = subscription.update_url(new_url)
```

#### Update a Subscription's scope

```python
new_scope = ["USERS|POST"]
subscription = subscription.update_scope(new_scope)
```

