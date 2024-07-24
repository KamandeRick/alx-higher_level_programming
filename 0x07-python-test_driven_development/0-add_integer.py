#!/usr/bin/python3

"""
Module defining a function that takes 2 arguments
returns the sum of the 2 arguments
a + b
"""


def add_integer(a, b=98):
    """
        function that takes 2 arguments of type int or float
        returns their sum
        sum = a+b
    """

    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
