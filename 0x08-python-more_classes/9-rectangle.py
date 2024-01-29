#!/usr/bin/python3
"""Simple rec module."""


class Rectangle:
    """
    Basic rec class.
    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The constructor method.

        Parameters:
            value (int): the size of a Rectangle.
        """
        self.__height = height
        self.check_h()
        self.__width = width
        self.check_w()
        Rectangle.number_of_instances += 1

    def check_h(self):
        """
        The function to check on the height.

        Returns:
            Rectangle: raises an error on if statements.
        """
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")

    def check_w(self):
        """
        The function to check on the width.

        Returns:
            Rectangle: raises an error on if statements.
        """
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """
        The getter func

        Returns:
            Rectangle: The size of the rectungle.
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
            Rectangle: The size of the rec.
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

    def area(self):
        """
        Rec area.

        Returns:
            Rectangle: returns the area of the rec
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Rec perimeter.

        Returns:
            Rectangle: returns the area of the rec
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join([str(self.print_symbol)
                          * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
