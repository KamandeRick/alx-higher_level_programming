#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    upper = 0
    lower = 0
    for high, low in my_list:
        upper += (high * low)
        lower += low
    return upper / lower
