#!/usr/bin/python3
"""Simple module."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    data = json.dumps(my_obj)
    return (data)
