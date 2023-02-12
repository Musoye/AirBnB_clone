#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


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
        b, c = a.save(), datetime.now()
        self.assertEqual(a.updated_at.strftime('%H:%M:%S'),
                         c.strftime('%H:%M:%S'))

    def test_update_save_a(self):
        a = BaseModel()
        sleep(0.05)
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)

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

    def test_dict_arg(self):
        a = BaseModel()
        with self.assertRaises(TypeError):
            a.to_dict(None)

    def test_dunder_ne_todict(self):
        a = BaseModel()
        self.assertNotEqual(a.__dict__, a.to_dict())

    def test_class_dict_name(self):
        a = BaseModel()
        b = a.to_dict()
        self.assertEqual('BaseModel', b['__class__'])

    def test_ioformat_date(self):
        a = BaseModel()
        b = a.to_dict()
        c = a.created_at.isoformat()
        self.assertEqual(c, b['created_at'])

    def test_instance_with_kwargs(self):
        a = BaseModel()
        b = a.to_dict()
        c = BaseModel(**b)
        self.assertEqual(b, c.to_dict())
        self.assertEqual(b.get('id'), c.id)
        self.assertEqual(a.created_at, c.created_at)

    def testno_class_attribute(self):
        a = BaseModel()
        a.save()
        b = a.to_dict()
        c = BaseModel(**b)
        self.assertNotEqual(c.created_at, c.updated_at)
        self.assertEqual(c.updated_at, a.updated_at)
