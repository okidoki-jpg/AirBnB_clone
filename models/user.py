#!/usr/bin/python3
"""User Module Doc: Inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class Doc: Defines User Object

    Attributes:
        email (str): empty string: User Email
        password (str): empty string: User Password
        first_name (str): empty string: User First Name
        last_name (str): empty string: User Last Name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User Instance
        """
        super().__init__(*args, **kwargs)
