#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for x, y in sorted(a_dictionary.items()):
            print("{}: {}".format(x, y))
    else:
        return a_dictionary
