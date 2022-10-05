#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for y in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """returns rectangle description"""
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height
        return ("[Rectangle] ({:d}) {}/{} - {:d}/{:d}".format(a, b, c, d, e))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for keyword in kwargs:
                if keyword == "id":
                    self.id = (kwargs[keyword])
                if keyword == "width":
                    self.width = (kwargs[keyword])
                if keyword == "height":
                    self.height = (kwargs[keyword])
                if keyword == "y":
                    self.y = (kwargs[keyword])
                if keyword == "x":
                    self.x = (kwargs[keyword])
