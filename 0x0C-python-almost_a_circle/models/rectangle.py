#!/usr/bin/python3
'''
Module with a Rectangle class
classes:
--------
    - Rectangle class
'''


from models.base import Base


class Rectangle(Base):
    '''
    A simple Class represent rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Rectangle class constructor

        Parameters:
        -----------
            - id: int
                A integer with default None
            - width: int
                A integer > 0 represent rectangle width
            - height: int
                A integer > 0 represent rectangle height
            - x: int
                A integer >= 0, default value is 0
            - y: int
                A integer >= 0, default value is 0
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width'''
        return self.__width

    @property
    def height(self):
        '''get height'''
        return self.__height

    @property
    def x(self):
        '''get x'''
        return self.__x

    @property
    def y(self):
        '''get y'''
        return self.__y

    @width.setter
    def width(self, width):
        '''Set width'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        '''Set height'''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        '''Set x'''
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        '''Set y'''
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
