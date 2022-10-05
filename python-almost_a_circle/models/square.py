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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for keyword in kwargs:
                if keyword == "id":
                    self.id = (kwargs[keyword])
                if keyword == "size":
                    self.size = (kwargs[keyword])
                if keyword == "y":
                    self.y = (kwargs[keyword])
                if keyword == "x":
                    self.x = (kwargs[keyword])
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
