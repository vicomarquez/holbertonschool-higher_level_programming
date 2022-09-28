#!/usr/bin/python3
"""
10-module
"""


Rectangle = __import__('9-rectangle.py').Rectangle


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
        return self.__width * self.__height 
