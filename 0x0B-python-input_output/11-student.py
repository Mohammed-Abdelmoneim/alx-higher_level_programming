#!/usr/bin/python3
"""Simple module"""


class Student:
    """Simple class student."""
    def __init__(self, first_name, last_name, age):
        """The init func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {name: v for name, v in self.__dict__.items() if name in attrs}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for name, v in json.items():
            if hasattr(self, name):
                setattr(self, name, v)
