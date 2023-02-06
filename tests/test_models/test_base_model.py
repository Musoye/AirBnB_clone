#!/usr/bin/python3
"""test base code"""
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseCase(unittest.TestCase):
    """test base model code"""
    maxDiff = None

    def test_id_attr(self):
        a = BaseModel()
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))

    def test_if_id_is_unique(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_id_is_str(self):
        a = BaseModel()
        self.assertEqual(type(a.id), str)

    def test_instances(self):
        a = BaseModel()
        b = "[BaseModel] ({}) {}".format(a.id,
                                         a.__dict__)
        self.assertEqual(a.__str__(), b)

    def test_update_save(self):
        a = BaseModel()
        b, c = a.save(), datetime.datetime.now()
        self.assertEqual(a.updated_at.strftime('%H:%M:%S'),
                         c.strftime('%H:%M:%S'))

    def test_for_class_dict(self):
        a = BaseModel()
        self.assertTrue('__class__' in a.to_dict())

    def test_for_added_instance(self):
        a = BaseModel()
        a.name = 'Musoye'
        self.assertTrue('name' in a.to_dict())

    def test_todict_is_dict(self):
        a = BaseModel()
        self.assertEqual(type(a.to_dict()), dict)

    def test_class_dict_name(self):
        a = BaseModel()
        b = a.to_dict()
        self.assertEqual('BaseModel', b['__class__'])

    def test_ioformat_date(self):
        a = BaseModel()
        b = a.to_dict()
        c = a.created_at.isoformat()
        self.assertEqual(c, b['created_at'])
