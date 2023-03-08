#!/usr/bin/python3
"""Review Module Doc: Inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class Doc: Defines Review Object

    Attributes:
        place_id (str): empty string: Place.id
        user_id (str): empty string: User.id
        text (str): empty string: User Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review Instance
        """
        super().__init__(*args, **kwargs)
