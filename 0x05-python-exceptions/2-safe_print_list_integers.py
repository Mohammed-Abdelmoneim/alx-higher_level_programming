#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = list(filter(lambda a: type(a) == int, my_list))

    length = 0
    for i in new_list:
        length += 1
    try:
        if x < length:
            for i in range(x):
                print("{:d}".format(new_list[i]), end="")
            print()
            return x
        else:
            for i in new_list:
                print("{:d}".format(i), end="")
            print()
            return x
    except Exception:
        print(Exception)
