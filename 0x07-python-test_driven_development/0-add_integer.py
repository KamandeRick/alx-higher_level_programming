#!/usr/bin/python3

"""
Module defining a function that takes 2 arguments
returns the sum of the 2 arguments
"""


def add_integer(a, b=98):
    """
        function that takes 2 arguments of type int or float
        returns their sum
    """

    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")
    
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    
    result = a + b
    return result
