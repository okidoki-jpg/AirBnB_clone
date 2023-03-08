#!/usr/bin/python3
"""Place Module Doc: Inherits from BaseModel

Imports:
    moels.base_model.BaseModel (cls): Base Class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class Doc: Defines Place Object

    Attributes:
        city_id (str): empty string: City.id
        user_id (str): empty string: User.id
        name (str): empty string: Name of place
        description (str): empty string: Place description
        number_rooms (int): 0: Room count
        number_bathrooms (int): 0: Bathroom count
        max_guest (int): 0: Max guests permited
        price_by_night (int): 0: Price/night
        latitude (float): 0.0: GPS latitude
        longitude (float): 0.0: GPS longitude
        amenity_ids (list(str)): empty list: Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize Place Instance
        """
        super().__init__(*args, **kwargs)
