#!/usr/bin/python3
def no_c(my_string):
    sl = list(my_string)
    for e in sl:
        if e in 'cC':
            sl.remove(e)
    return "".join(sl)
