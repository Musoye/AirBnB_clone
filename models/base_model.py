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
