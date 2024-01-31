#!/usr/bin/python3
"""This Module for rectangle data structure
classes:
    Rectangle
"""


class Rectangle:
    """
    A class to represent Rectangle.
    ...
    Attributes
    ----------
        width : int, optional
            rectangle width
            Its default value is [0]
        height : int, optional
            rectangle height
            Its default value is [0]

    Methods
    -------
        area():
            returns area of the Rectangle
        perimeter()):
            returns perimeter of the Rectangle

    """

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object

        Parameters
        ----------
            width : int, optional
                rectangle width
                Its default value is [0]
            height : int, optional
                rectangle height
                Its default value is [0]
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width attribute"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """Get rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Get rectangle perimeter"""
        return (self.width + self.height) * 2
