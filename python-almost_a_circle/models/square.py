#!/usr/bin/python3
"""square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """innit"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns square description"""
        a = self.id
        b = self.x
        c = self.y
        d = self.size
        return ("[Square] ({:d}) {}/{} - {:d}".format(a, b, c, d))
