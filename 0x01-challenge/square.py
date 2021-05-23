#!/usr/bin/python3
"""Module that defines a Square"""


class Square():
    """Defines class Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instantiates Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_square(self):
        """Area of the Square"""
        return self.width * self.height

    def perim_square(self):
        """Perimeter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String rep of Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_square())
    print(s.perim_square())
