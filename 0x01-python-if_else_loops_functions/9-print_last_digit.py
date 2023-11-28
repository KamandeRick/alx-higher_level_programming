#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        lastDigit = 0
    else:
        lastDigit = int(str(number)[-1])
    print("{:d}".format(lastDigit), end="")
    return lastDigit
