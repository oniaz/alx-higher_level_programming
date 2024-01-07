#!/usr/bin/python3
import unittest
from models.base import Base
""" Tests for Base module """

class TestBaseClass(unittest.TestCase):
    def test_no_id(self):
        """isntance created with no id provided (assigned automatically after
        incrementation)"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_given_id(self):
        """ isntance created with id provided """
        b2 = Base(22)
        self.assertEqual(b2.id, 22)