"""This module contains models for objects tied to the /users endpoint.

Includes classes for user and documents that can be attached to the user.
"""


from .user import User
from .base_document import BaseDocument
from .physical_document import PhysicalDocument
from .social_document import SocialDocument
from .virtual_document import VirtualDocument
from .virtual_document import Question
