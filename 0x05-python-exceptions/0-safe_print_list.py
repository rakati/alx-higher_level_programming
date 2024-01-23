#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for e in range(x):
        try:
            print(my_list[e], end='')
        except:
            print()
            return e
    print()
    return x
