#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        new_set = set(my_list)
        result = sum(new_set)
        return result
    else:
        return my_list
