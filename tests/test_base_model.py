#!/usr/bin/python3
"""
Unittest for Base Model class
"""
import unittest
import os
import sys

sys.path.insert(0, '/AirBnB_clone/models')
from base_model import BaseModel # noqa
from datetime import datetime # noqa
from __init__ import storage # noqa


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

    def test_recreate_instance_from_dict(self):
        """
        Recreate Instance from dictionary
        """

        my_model = BaseModel()
        my_model.name = 'My_First_Model'
        my_model.my_number = 89
        my_model.save()

        my_model_dict = my_model.to_dict()

        my_new_model = BaseModel(**my_model_dict)

        # check if attributes match
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

        # check if created_at & updated_at are datetime objects
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)

        # next we check if they match
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
