#!/usr/bin/python3
"""Simple module."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
