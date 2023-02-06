#!/usr/bin/python3
"""The base model for all class"""
import uuid
import datetime


class BaseModel:
    """The base model for the project"""

    def __init__(self):
        """constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """the print out to stdout"""
        out = "[{}] ({}) {}".format(type(self).__name__,
                                    self.id,
                                    self.__dict__)
        return (out)

    def save(self):
        """save and update"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """change to dictionary"""
        dict_1 = self.__dict__.copy()
        dict_1['__class__'] = type(self).__name__
        for i, t in self.__dict__.items():
            if i in ["created_at", "updated_at"]:
                t = self.__dict__[i].isoformat()
                dict_1[i] = t
        return (dict_1)
