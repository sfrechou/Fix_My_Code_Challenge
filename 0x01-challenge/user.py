#!/usr/bin/python3
"""
Module that defines a User class
"""


class User():
    """Class that defines a user"""

    def __init__(self):
        """Instantiates a user"""
        self.__email = None

    @property
    def email(self):
        """Getter for email"""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
