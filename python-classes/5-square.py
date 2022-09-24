#!/usr/bin/python3
"""
Python excercise 1
"""


class Square:
    """
    size
    """
    def __init__(self, size=0):
        """
        size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()

        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()

