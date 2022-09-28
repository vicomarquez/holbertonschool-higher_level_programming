#!/usr/bin/python3
"""
9-module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry (7-base_geometry.py)
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculates area
        """
        return self.__width * self.__height

    def str(self):
        """
        returns description
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
    def print(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
