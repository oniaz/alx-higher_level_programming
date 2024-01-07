#!/usr/bin/python3
""" Tests for Base module """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Testing the base class """

    def test_no_id(self):
        """instance created with no id provided (assigned automatically after
        incrementation)"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_given_id(self):
        """ isntance created with id provided """
        b = Base(22)
        self.assertEqual(b.id, 22)

    def test_no_id_inc(self):
        """2 isntance created with no id provided (assigned automatically after
        incrementation) b1.id == b1.id + 1 ?"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)
