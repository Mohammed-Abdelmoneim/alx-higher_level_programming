#!/usr/bin/python3
"""Simple module"""


class MyInt(int):
    """A rebel class"""
    def __eq__(self, number):
        """Equal func"""
        return self.real != number

    def __ne__(self, number):
        """Not equal func"""
        return self.real == number
