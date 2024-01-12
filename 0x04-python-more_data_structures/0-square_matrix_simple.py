#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_list = [list(map(lambda x: x ** 2, x)) for x in matrix]
    return new_list
