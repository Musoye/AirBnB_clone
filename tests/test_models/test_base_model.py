#!/usr/bin/python3
"""test base code"""
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseCase(unittest.TestCase):
    """test base model code"""
    maxDiff = None

    def test_instances(self):
        a = BaseModel();
        b = "[BaseModel] ({}) {}".format(a.id,
                                         a.__dict__)
        self.assertEqual(a.__str__(), b)

    def test_update_save(self):
        a = BaseModel()
        b, c = a.save(), datetime.datetime.now()
        self.assertEqual(a.updated_at.strftime('%H:%M:%S'), c.strftime('%H:%M:%S'))
