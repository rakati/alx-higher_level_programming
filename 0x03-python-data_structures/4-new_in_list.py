#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0 or idx >= size:
        return my_list[:]
    new = my_list[:]
    new[idx] = element
    return new
