#!/usr/bin/python3
"""
11-module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle (9-rectangle.py)
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        calculates area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns description
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
