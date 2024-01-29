#!/usr/bin/python3
"""Simple module."""


class Rectangle:
    """Basic rec class."""
    def __init__(self, width=0, height=0):
        """
        The constructor method.

        Parameters:
            value (int): the size of a Rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        The getter func

        Returns:
            square: The size of the rectungle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The sitter func

        Parameters:
            value (int): The new value for the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        The sitter func

        Parameters:
            value (int): The new value for the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
