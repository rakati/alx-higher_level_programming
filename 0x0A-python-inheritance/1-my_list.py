#!/usr/bin/python3
'''This Module contain mylist class that inherit from python list
classes:
    MyList
'''


class MyList(list):
    '''Simple class for handling list inherited from Python list class'''
    def print_sorted(self):
        '''Print list element in sorted order'''
        c = self.copy()
        c.sort()
        print(c)
