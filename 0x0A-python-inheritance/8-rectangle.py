#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Simple class module."""


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
