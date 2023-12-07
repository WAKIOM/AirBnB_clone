#!/usr/bin/python3
"""
Defines the State class.

This module contains the definition of the State class, which is a child class
of the BaseModel. The State class represents a state entity and has an
attribute for the name of the state.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A class representing a state entity.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
