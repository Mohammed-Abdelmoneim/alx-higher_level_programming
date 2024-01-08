#!/usr/bin/env python3
def no_c(my_string):
    x = ''
    a = ''
    z = "cC"
    ss = my_string.maketrans(x, a, z)
    return (my_string.translate(ss))
