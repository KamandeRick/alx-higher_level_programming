#!/usr/bin/python3

"""
Module defining a text indentation function
The function takes in a string argument
Inserts 2 newline characters after '?', '.', or ':'
Prints new result text
"""


def text_indentation(text):
    """
    The function takes in a string argument
    Inserts 2 newline characters after '?', '.', or ':'
    Prints new result text
    """

    if type(text) != str:
        raise TypeError("text must be a string")