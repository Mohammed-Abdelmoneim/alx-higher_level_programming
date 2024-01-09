#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list = []
    if len(tuple_a) == 1:
        list = [tuple_a[0], 0]
    else:
        list = [0, 0]
    for i in range(2):
        list[i] = tuple_a[i] + tuple_b[i]
        tup = tuple(list)
    return (tup)
 # input - processes - output
