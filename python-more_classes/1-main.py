#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

try:
    my_rectangle = Rectangle(2, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle("2", 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

"""my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)"""
