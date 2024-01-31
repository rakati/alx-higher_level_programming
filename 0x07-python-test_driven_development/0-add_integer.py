#!/usr/bin/python3
"""This is a module with function for adding integers

Functions:
    add_integer(int|float, int|float) -> int
"""

def add_integer(a, b=98):
    """Adding two number
    parameters:
        a(int or float): a number to be casted to int if it's float
        b(int or float): a number with default is 98, to be casted to int
            if it's float
    returns:
        the sum of a and b"""
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
