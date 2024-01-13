#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortkeys = list(a_dictionary)
    sortkeys.sort()
    for i in sortkeys:
        print("{}: {}".format(i, a_dictionary.get(i)))
