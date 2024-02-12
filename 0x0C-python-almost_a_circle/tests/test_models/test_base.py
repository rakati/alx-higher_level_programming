#!/usr/bin/python3
'''
This Module is for testing the Base class

classes:
--------
    - Base class
'''


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    '''
    A test Class that inherit from unittest TestCase
    for testing our Base class from Models package
    '''

    def test_class_attr(self):
        '''testing class attribute'''

        id = 0
        for i in range(10):
            b = Base()
            id += 1
            self.assertEqual(b.id, id)

    def test_inst_attr(self):
        '''testing instance attribute'''

        from random import randint

        for i in range(5):
            d = randint(0, 400)
            b = Base(d)
            self.assertEqual(b.id, d)


if __name__ == '__main__':
    unittest.main()
