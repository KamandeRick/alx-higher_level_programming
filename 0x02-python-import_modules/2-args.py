#!/usr/bin/python3

from sys import argv

zero_args = "arguments."
one_arg = "argument:"
n_args = "arguments:"
arg_count = len(argv) - 1

def arg_counter():
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))

if __name__ == "__main__":
    if (arg_count == 0):
        print("{:d} {}".format(arg_count, zero_args))
    elif (arg_count == 1):
        print("{:d} {}".format(arg_count, one_args))
        arg_counter()
    else:
        print("{:d} {}".format(arg_count, n_args))
        arg_counter()
