#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        length = 0
        for i in my_list:
            length += 1
        try:
            if x <= length:
                for i in range(x):
                    print(my_list[i], end="")
                print()
                return x
            else:
                for i in my_list:
                    print(i, end="")
                print()
                x = length
                return x
        except Exception:
            print("An error occured")
    else:
        return my_list
