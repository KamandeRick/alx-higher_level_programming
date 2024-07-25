#!/usr/bin/python3

"""
Module defining a function ''print_square''
print_square takes one argument size
prints a square of size 'size'
"""


def print_square(size):
    """
    Funtion that prints a square
    Takes one argument 'size' of type int
    Prints square of size size using the '#' sign
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
