#!/usr/bin/python3
"""Simple module."""
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


with open("add_item.json" "w") as f:
    data = load_from_json_file(f)
    save_to_json_file(data, "add_item.json")
