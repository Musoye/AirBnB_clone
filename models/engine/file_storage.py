#!/usr/bin/python3
"""The storage Module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """The file stoage class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the __objects"""
        return (self.__objects)

    def new(self, obj):
        """
          sets in __objects the obj with key
          <obj class name>.id
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
           serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as s_file:
            dict_form = {}
            for k, v in self.__objects.items():
                dict_form[k] = v.to_dict()
            json.dump(dict_form, s_file)

    def reload(self):
        """
          deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as r_file:
                for obj in json.load(r_file).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
