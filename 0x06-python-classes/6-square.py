#!/usr/bin/python3
"""Simple class again about square."""


class Square:
    """
    Continue to build the square class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor method.

        Parameters:
            size (int): the size of a square.
        """
        self.__size = size
        self.__pos = position
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

    def area(self):
        """
        Function that calc the area of a square.

        Returns:
            Square: the area of a square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        The getter func

        Returns:
            square: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The sitter func

        Parameters:
            value (int): The new value for the square.
        """
        self.__size = value
        self.check_size()

    def my_print(self):
        """
        Print a square of Hashtags.
        """
    
        if self.__size == 0:
            print()
        elif self.__pos[1] > 0 or self.__pos == (0, 0):
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            for i in range(self.__size):
                print(" " ,"#" * self.__size)

        
    @property
    def position(self):
        return self.__pos
    
    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__pos = value
