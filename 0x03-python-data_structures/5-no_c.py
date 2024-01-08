#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for e in my_string:
        if e not in "cC":
            s += e
    return s
