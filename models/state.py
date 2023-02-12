#!/usr/bin/python3
"""This is the State Model module.
Contains the State class that inherits from BaseModel.
"""
from models.base_model import BaseModel
import pep8

class State(BaseModel):
    """This class defines a State.
    Attributes:
        name (str): the state's name.
    """

    name = ""
