#!/usr/bin/python3
"""Simple module."""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)."""
    data = json.loads(my_str)
    return (data)
