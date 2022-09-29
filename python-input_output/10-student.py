#!/usr/bin/python3
"""
10-module
"""

class Student:
    """
    class Student that defines a student 
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        new = {}
        if type(attrs) is list:
            for x in self.__dict__:
                for y in attrs:
                    if x == y:
                        new[x] = self.__dict__[x]
            return new
        else:
            return self.__dict__
