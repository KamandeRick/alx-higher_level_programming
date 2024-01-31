#!/usr/bin/python3
from sys import stderr

def safe_function(*args, fct):
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
    return None
