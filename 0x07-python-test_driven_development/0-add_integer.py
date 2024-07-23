#!/usr/bin/python3
"""
Module defining a function that takes 2 arguments and returns the sum of
the 2 arguments
"""
def add_integer(a, b=98):
    """
        function that takes 2 arguments of type int and returns their sum
    """
    if ((type(a) != int) and (type(a) != float)) or ((type(b) != int) and (type(b) != float)):
        raise TypeError 
    elif type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    
    result = a+b
    return result
