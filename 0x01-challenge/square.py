#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square:
    """Class that defines a Square"""

    width = 0

    def __init__(self, width=0):
        """Instantiation attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculates the area of a Rectangle"""
        return self.__width * self.__width

    def perimeter(self):
        """Calculates the permiter of a rectangle"""
        if self.__width == 0:
            return 0
        else:
            return (self.__width * 4)

    def __str__(self):
        """Prints therep of a Square"""
        return "{}/{}".format(self.__width, self.__width)

if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.perimeter())
