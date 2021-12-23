#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.base_model import BaseModel
import unittest


class test_review(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.Review = Review()
        cls.Review.place_id = "4321-dcba"
        cls.Review.user_id = "123-bca"
        cls.Review.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.Review

    def test_attributes_Review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.Review.__dict__)
        self.assertTrue('created_at' in self.Review.__dict__)
        self.assertTrue('updated_at' in self.Review.__dict__)
        self.assertTrue('place_id' in self.Review.__dict__)
        self.assertTrue('text' in self.Review.__dict__)
        self.assertTrue('user_id' in self.Review.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.Review.__class__, BaseModel))

    def test_attributes_type_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.Review.text), str)
        self.assertEqual(type(self.Review.place_id), str)
        self.assertEqual(type(self.Review.user_id), str)

    def test_save_Review(self):
        """test if the save works"""
        self.Review.save()
        self.assertNotEqual(self.Review.created_at, self.Review.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertTrue('to_dict' in dir(self.Review))


if __name__ == '__main__':
    unittest.main()
