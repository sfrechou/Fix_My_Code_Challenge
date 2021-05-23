#!/usr/bin/python3
"""
Module that defines a Square
"""


class square:
    """Defines class Square"""
    side = 0

    def __init__(self, *args, **kwargs):
        """Init sequence."""
        for key, value in kwargs.items():
            if type(value) is int and value > 0:
                setattr(self, key, value)
            else:
                raise TypeError("Type Error")

    def area(self):
        """Area of the Square"""
        return self.side * 2

    def perim(self):
        """Perimeter of the Square"""
        return self.side * 4

    def __str__(self):
        """String rep of Square"""
        return "{}/{}".format(self.side, self.side)

if __name__ == "__main__":
    s = square(side=9, height=9)
    print(s)
    print(s.area())
    print(s.perim())
