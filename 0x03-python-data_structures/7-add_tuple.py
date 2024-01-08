#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = len(tuple_a)
    l_b = len(tuple_b)
    return ((tuple_a[0] if l_a > 0 else 0) +
            (tuple_b[0] if l_b > 0 else 0),
            (tuple_a[1] if l_a > 1 else 0) +
            (tuple_b[1] if l_b > 1 else 0))
