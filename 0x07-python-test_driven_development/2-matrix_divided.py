#!/usr/bin/python3

"""
This module defines a function that takes 2 arguments
argument 1 is a matrix, 2 is divisor an int
returns the matrix divided by the divisor
"""


def matrix_divided(matrix, div):
    """
    Function that takes 2 args
    Arg 1 is matrix, 2 is int
    returns the matrix result of dividing arg 1 by arg 2
    """
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        for column in row:
            if type(column) != int and type(column) != float:
                raise TypeError(
                    """matrix must be a matrix (list of lists)
                    of integers/floats"""
                    )
    if not all(len(row) == len(matrix[0])for row in matrix):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(column / div, 2) for column in row] for row in matrix]
