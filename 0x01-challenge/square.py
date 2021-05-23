#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square():
    """Defines class Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Init sequence."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Area of the Square"""
        return self.width * self.height

    def perim(self):
        """Perimeter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String rep of Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=10, height=9)
    print(s)
    print(s.area())
    print(s.perim())
