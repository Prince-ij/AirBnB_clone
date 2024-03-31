#!/usr/bin/python3
"""
Unittest for Base Model class
"""
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                '..')))

from models.base_model import BaseModel  # noqa
from datetime import datetime  # noqa


class TestBaseModel(unittest.TestCase):
    """
    Test case for BaseModel class
    """

    def test_attributes(self):
        """
        Test baseModel attributes
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_method(self):
        """
        Test the save method
        """

        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method of BaseModel class
        """

        my_model = BaseModel()
        my_model.name = 'Test Model'
        my_model.number = 42
        my_model_dict = my_model.to_dict()
        expected_keys = ['id', 'name', 'created_at', 'updated_at',
                         'number', '__class__']
        self.assertCountEqual(my_model_dict.keys(), expected_keys)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'Test Model')
        self.assertEqual(my_model_dict['number'], 42)
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],
                         my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
