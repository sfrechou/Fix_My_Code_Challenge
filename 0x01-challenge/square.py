#!/usr/bin/python3
"""
Modules that defines a Square
"""


class Square():
    """Class that defines a Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instantiates a Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Area of a square"""
        return self.width * self.height

    def permiter(self):
        """Perimeter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String rep of a square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area())
    print(s.permiter())
