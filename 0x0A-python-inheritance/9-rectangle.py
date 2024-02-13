#!/usr/bin/python3
"""Simple class module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Basic Rectangle inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        The instance constructor.
        """
        self.__width = width
        self.integer_validator("width", self.__width)
        self.__height = height
        self.integer_validator("height", self.__height)

    def area(self):
        """
        returns the area of the rec
        """
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
