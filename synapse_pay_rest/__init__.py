"""SynapsePay client library for the SynapsePay platform.

This client library is designed to support the SynapsePay API for creating
users, linking nodes (accounts), and creating transactions between users. Read
more at https://docs.synapsepay.com
"""

from .client import Client
from .api import Users, Nodes, Trans
from .models import User, Node, Transaction
