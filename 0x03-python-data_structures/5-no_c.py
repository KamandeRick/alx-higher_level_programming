#!/usr/bin/python3
def no_c(my_string):
    strNew = ""
    if my_string:
        for n in my_string:
            if ord(n) != ord('c') and ord(n) != ord('C'):
                strNew += str(n)
    return strNew
