#!/usr/bin/python3

"""
This module defines a function that takes 2 args
Both args are type string
Returns a concatenated string of both args
Return value represents full name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that takes 2 args
    Args are both strings
    Returns concatenated string of both args
    Return value represetns full name
    """

    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    full_name = (first_name + " " + last_name).title()
    return full_name
