#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    with open("add_item.json" "w") as f:
        data = load_from_json_file(f)
        save_to_json_file(data, "add_item.json")
