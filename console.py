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



"""
Hi, "Mustapha" I am just trying destroy task below you can right here the other staff her!
"""



    def do_destroy(self, arg):
        """
        Deletes an instance.
            usage: destroy <class_name> <id>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_all(self, arg):
        """
        Prints all string representation of all instances.
            usage: all [class_name]
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print([v.__str__() for v in models.storage.all().values()])
        elif args[0] in self.classes:
            print([v.__str__() for v in models.storage.all().values()
                   if type(v) is eval(args[0])])
        else:
            print(self.errors["wrongClass"])
