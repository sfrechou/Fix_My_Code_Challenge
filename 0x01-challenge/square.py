#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square():
    """Class that defines a Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instantiate a Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of a square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Perimeter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String repr of a Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
