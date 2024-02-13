#!/usr/bin/python3
"""Simple class module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Basic Square inherits from Rectangle.
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
        returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
