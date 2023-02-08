#!/usr/bin/python3
"""This is the Console module."""
import cmd
import shlex
import models
import ast

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """The Console class of our HBNB project."""
    prompt = "(hbnb) "

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **",
        "missingAttr": "** attribute name missing **",
        "missingValue": "** value missing **"
    }


    classes = [
        "BaseModel", "Amenity", "City", "Place", "Review", "State", "User"
    ]
