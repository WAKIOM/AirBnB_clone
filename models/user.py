#!/usr/bin/python3
"""
Defines the User class.

This module contains the definition of the User class, which is a child class
of the BaseModel. The User class represents user entities with attributes
such as email, password, first name, and last name.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class representing user entities.

    Attributes:
        email (str): The email address associated with the user.
        password (str): The password for user authentication.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
