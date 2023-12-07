#!/usr/bin/python3
"""
Defines the Review class.

This module contains the definition of the Review class,
which represents a review entity.
The Review class is a child class of the BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review entity.

    Attributes:
        place_id (str): ID of the place to which the review is associated.
                        Defaults to an empty string.
        user_id (str): ID of the user who wrote the review.
                       Defaults to an empty string.
        text (str): The text content of the review.
                    Defaults to an empty string.
    """
    place_id = ""
    user_id = ""
    text = ""
