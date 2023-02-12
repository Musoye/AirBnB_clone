#!/usr/bin/python3
"""test for the engine"""
import models
from models.engine.file_storage import FileStorage
import unittest


class TestStorageinstate(unittest.TestCase):
    """Test for the file storage class"""

    def test_filepath_attribute(self):
        self.assertFalse(hasattr(FileStorage(), '__file_path'))

    def test_objects_attr(self):
        self.assertFalse(hasattr(FileStorage(), '__objects'))

    def test_for_instance(self):
        self.assertEqual(type(models.storage), FileStorage)
