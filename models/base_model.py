#!/usr/bin/python3
"""This is the Base Model module.
Contains the BaseModel class which will be the
"base" of all other classes in this project.
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """The base model for the project"""

    def __init__(self, *arg, **kwargs):
        """constructor method"""
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k not in ['created_at', 'updated_at']:
                        setattr(self, k, v)
                    else:
                        setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))

    def __str__(self):
        """the print out to stdout"""
        out = "[{}] ({}) {}".format(type(self).__name__,
                                    self.id,
                                    self.__dict__)
        return (out)

    def save(self):
        """save and update"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """change to dictionary"""
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = type(self).__name__
        for i, t in self.__dict__.items():
            if i in ["created_at", "updated_at"]:
                t = self.__dict__[i].isoformat()
                dict_1[i] = t
        return (dict_1)
