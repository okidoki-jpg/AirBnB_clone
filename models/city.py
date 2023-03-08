#!/usr/bin/python3
"""City Module Doc: inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class Doc: Defines a City Object

    Attributes:
        state_id (str): empty string: State.id
        name (str): empty string: City Name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City Instance
        """
        super().__init__(*args, **kwargs)
