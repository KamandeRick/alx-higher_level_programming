#!/usr/bin/python3
from sys stderr, import exc_info


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
    return isinstance(value, int)
