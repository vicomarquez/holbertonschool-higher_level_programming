#!/usr/bin/python3
def add_integer(a, b=98):
    result = int(a) + int(b) 
    if type(a) != int and type(b) != int:
        raise TypeError("a must be an integer or b must be an integer")
    if type(a) != float and type(b) != float:
        raise TypeError("a must be an integer or b must be an integer")
    return result
