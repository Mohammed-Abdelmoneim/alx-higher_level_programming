#!/usr/bin/python3
"""Simple class again about square."""


class Square:
    """
    Continue to build the square class.
    """

    def __init__(self, size=0):
        """
        The constructor method.

        Parameters:
            size (int): the size of a square.
        """
        self.__size = size
        self.check_size()

    def check_size(self):
        """
        The function to check on the size.

        Returns:
            Square: raises an error on if statements.
        """
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
