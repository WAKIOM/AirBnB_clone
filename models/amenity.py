#!/usr/bin/python3
"""
Module defines Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class defining Amenity entity
    Attributes:
        name (str): The amenity name
    """
    name = ""
