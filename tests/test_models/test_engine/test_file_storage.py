#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """setup"""
        cls.base = BaseModel()
        cls.base.name = 'Kevin'
        cls.base.num = 25

    @classmethod
    def teardown(cls):
        del cls.base

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertIsInstance(self.base, BaseModel)

    def test_save_BaseModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        baseDict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(baseDict['created_at'], str)
        self.assertIsInstance(baseDict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
