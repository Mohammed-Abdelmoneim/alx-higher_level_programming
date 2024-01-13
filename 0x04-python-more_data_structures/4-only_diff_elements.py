#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        diff_1 = set_1.symmetric_difference(set_2)
        return diff_1
    elif set_1 and not set_2:
        return set_1
    else:
        return set_2
