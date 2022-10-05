#!/usr/bin/python3
""" 1-module"""


import json


class Base:
    """ base """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs is None:
            list_objs = []

        for i in list_objs:
            new_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", "w", encoding="utf=8") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        nm = cls.__name__
        if nm == "Rectangle":
            dummy = cls(1, 1)
        if nm == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_n = cls.__name__ + ".json"
        new_list = []
        if file_n is None:
            return new_list
        with open(file_n, "r", encoding="utf=8") as f:
            x = cls.from_json_string(f.read())
        return  [cls.create(**y) for y in x]
