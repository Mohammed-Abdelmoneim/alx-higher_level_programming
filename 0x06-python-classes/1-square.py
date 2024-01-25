#!/usr/bin/python3
"""Again simple class about square."""

class Square:
    """Square class with size atrr.
    
    Attributes:
        size (int): The square size.
    """

    def __init__(self, size):
        """
        The constructor for the square class.

        Parameters:
            size (int): The square size.
        """
        self.__size = size
