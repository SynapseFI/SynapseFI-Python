"""SynapsePay client library for the SynapsePay platform.

This client library is designed to support the SynapsePay API for creating
users, linking nodes (accounts), and creating transactions between users. Read
more at https://docs.synapsepay.com

"""

from synapse_pay_rest.client import Client
from synapse_pay_rest.api import Users, Nodes, Trans
from synapse_pay_rest.models import User, Node, Transaction
