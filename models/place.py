#!/usr/bin/python3
"""
Modules defines place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class representing a place entity.

    Attributes:
        city_id (str): The ID of the city to which the place belongs.
                       Defaults to an empty string.
        user_id (str): The ID of the user who owns the place.
                       Defaults to an empty string.
        name (str): The name of the place. Defaults to an empty string.
        description (str): description of place. Defaults to an empty string.
        number_rooms (int): The number of rooms in the place. Defaults to 0.
        number_bathrooms (int): number of bathrooms in place. Defaults to 0.
        max_guest (int): The maximum number of guests place can accommodate.
                         Defaults to 0.
        price_by_night (int): The price per night for the place. Defaults to 0.
        latitude (float): latitude coordinate of the place. Defaults to 0.0.
        longitude (float): longitude coordinate of the place. Defaults to 0.0.
        amenity_ids (list of str): list of Amenity IDs associated with place.
                                    Defaults to an empty list.
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
