#!/usr/bin/python3
"""Simple class module."""


class BaseGeometry:
    """
    Basic BaseGeometry empty class.
    """
    def area(self):
        """
        Raises an exception with message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check the value.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Basic Rectangle inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        The instance constructor.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
