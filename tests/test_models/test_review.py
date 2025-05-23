#!/usr/bin/python3
""" module to test Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test the Review class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ the place id should be a string """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ the user id should be a string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ The text should be a string """
        new = self.value()
        self.assertEqual(type(new.text), str)
