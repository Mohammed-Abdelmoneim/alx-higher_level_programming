#!/usr/bin/python3
"""Simple module"""


def class_to_json(obj):
    """returns the dictionary description"""
    return obj.__dict__
