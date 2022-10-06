#!/usr/bin/python3
"""rectangle tests"""


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRect(unittest.TestCase):
    """rectangle tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

    def test_area(self):
        r1 = Rectangle(4, 3)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(85, 3)
        self.assertEqual(r2.area(), 255)
        r3 = Rectangle(6, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 42)
