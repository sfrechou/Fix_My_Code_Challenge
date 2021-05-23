#!/usr/bin/python3
"""
Module that defines a square
"""


class Square():
    """Defines a square"""
    width = 0

    def __init__(self, *args, **kwargs):
        """Instantiates a Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Area of a square"""
        return self.width ** 2

    def perimeter(self):
        """Perimeter of a square"""
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area())
    print(s.perimeter())
