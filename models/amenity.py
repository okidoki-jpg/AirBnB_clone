#!/usr/bin/python3
"""Amenity Module Doc: Inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class Doc: Defines Amenity Object

    Attributes:
        name (str): empty string: Amenity Name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity Instance
        """
        super().__init__(*args, **kwargs)
