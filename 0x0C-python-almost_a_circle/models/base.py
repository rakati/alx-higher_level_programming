#!/usr/bin/python3
'''
Module with a Base class
classes:
--------
    - Base class
'''


class Base:
    '''
    A simple Class that will be used as Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Base class constructor

        Parameters:
        -----------
            - id: int
                A integer with default None
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
