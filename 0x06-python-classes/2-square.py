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
    '''
    def __init__(self, size=0):
        self.__size = 0

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        '''

        Private instance attribute: size
        inatantiation with optional size
        Ascertain size is int
        ascertain size is > 0
        '''
