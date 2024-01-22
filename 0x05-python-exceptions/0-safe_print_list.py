def safe_print_list(my_list=[], x=0):
    if my_list:
        len = 0
        for i in my_list:
            len += 1
        try:
            if x <= len:
                for i in range(x):
                    print(my_list[i], end="")
                print()
                return x
            else:
                for i in my_list:
                    print(i, end="")
                print()
                x = len
                return x
        except Exception:
            print("An error occured")
