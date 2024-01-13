#!/usr/bin/python3

def squareList(N):
    return (N**2)


def square_matrix_simple(matrix=[]):
    return [list(map(squareList, matrix[i])) for i in range(len(matrix))]
