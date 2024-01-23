#!/usr/bin/python3
'''Module for Square class
'''


class Square:
    '''Class represent square
    Args:
        size (int): size of the square side
    Attributes:
        _Square__size (int): private attribute represent size of the square
    '''
    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
