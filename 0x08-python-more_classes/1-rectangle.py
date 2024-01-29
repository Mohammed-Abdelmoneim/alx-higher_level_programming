#!/usr/bin/python3
"""Simple rec module."""


class Rectangle:
    """
    Basic rec class.
    """

    def __init__(self, width=0, height=0):
        """
        The constructor method.

        Parameters:
            value (int): the size of a Rectangle.
        """
        self.__height = height
        self.__width = width

    def check_h(self):
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise TypeError("height must be >= 0")

    def check_w(self):
        if type(self.__width) != int:
            raise TypeError("height must be an integer")
        elif self.__width < 0:
            raise TypeError("height must be >= 0")

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
        The setter func

        Parameters:
            value (int): The new value for the Rectangle.
        """
        self.__width = value
        self.check_w()

    @property
    def height(self):
        """
        The getter func

        Returns:
            square: The size of the rec.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter func

        Parameters:
            value (int): The new value for the Rectangle.
        """
        self.__height = value
        self.check_h()