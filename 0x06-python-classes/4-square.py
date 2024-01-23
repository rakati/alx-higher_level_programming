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
        self.size = size

    def area(self):
        '''Return Area of the square'''
        return self._Square__size * self._Square__size

    @property
    def size(self):
        '''return size of square side'''
        return self._Square__size

    @size.setter
    def size(self, value):
        '''size setter method'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
