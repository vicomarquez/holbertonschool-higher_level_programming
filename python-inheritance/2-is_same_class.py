#!/usr/bin/python3
"""
2-module
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is an instance of the specified class, or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
