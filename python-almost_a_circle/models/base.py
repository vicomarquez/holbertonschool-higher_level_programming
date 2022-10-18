#!/usr/bin/python3
"""1 - module"""


class Base:
    """base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        Base.__nb_objects = __nb_objects + 1
        self.id = __nb_objects
