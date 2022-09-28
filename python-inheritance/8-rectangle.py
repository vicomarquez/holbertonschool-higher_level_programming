#!/usr/bin/python3
"""
7-module
"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class BaseGeometry:
    """
    empty class BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
