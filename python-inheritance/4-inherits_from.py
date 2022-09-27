#!/usr/bin/python3
"""
4-module
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
