#!/usr/bin/python3
"""State Module Doc: Inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class Doc: Defines State Object

    Attributes:
        name (str): empty string: State Name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State Instance
        """
        super().__init__(*args, **kwargs)
