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
