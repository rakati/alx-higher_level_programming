#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    print("\n".join('{:d}'.format(e) for e in my_list[::-1]))
