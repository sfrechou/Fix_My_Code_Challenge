#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square():
    """Defines class Square"""

    width = 0
    height = 0

    def __init__(self, width, height):
        """Instantiates Square"""
        if type(width) is int:
            self.width = width
        if type(height) is int:
            self.height = height

    def areasquare(self):
        """Area of the Square"""
        return self.width * self.height

    def perimsquare(self):
        """Perimeter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String rep of Square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=9, height=9)
    print(s)
    print(s.areasquare())
    print(s.perimsquare())
