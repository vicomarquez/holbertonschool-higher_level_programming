#!/usr/bin/python3
"""
8-module
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """
    return obj.__dict__
