#!/usr/bin/python3
"""
11-module
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

    def reload_from_json(self, json):
        for x in json:
            if x == "first_name":
                self.first_name = json[x]
            if x == "last_name":
                self.last_name = json[x]
            if x == "age":
                self.age = json[x]


