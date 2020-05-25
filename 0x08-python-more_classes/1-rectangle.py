#!/usr/bin/python3
"""Define a rectangle
    """


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter

        Arguments:
            value {int} -- value of the width

        Raises:
            TypeError: if width isn't an integer print error
            ValueError: if width its less than 0 print error
        """
        if type(value) not in [int]:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter

        Arguments:
            value {int} -- value of the height<

        Raises:
            TypeError: if height isn't an integer print error
            ValueError: if height its less than 0 print error
        """
        if type(value) not in [int]:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('heigt must be >= 0')

        self.__height = value
