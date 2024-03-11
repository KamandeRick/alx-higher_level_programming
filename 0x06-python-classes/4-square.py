#!/usr/bin/python3
'''
Square Module to write a Square class
which defines a square based on 1-square.py
Author Fredrick Kamande
'''


class Square:
    '''Definition of square class
    Attributes:
    __size

    Methods:
    __init__
    area- Returns current square area
    '''
    def __init__(self, size=0):
        '''
        __init__ method to initialize square instances
        Args:
        size(int): Integer value for first parameter
        '''
        self.__size = 0
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
         Note:

         Args:

         Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Note:

        Args:

        Returns:
            Area
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        '''
        Note:

        Args:

        Returns:
            Area
        '''
        return self.__size ** 2

        '''

        Private instance attribute: size
        inatantiation with optional size
        Ascertain size is int
        ascertain size is > 0
        '''
