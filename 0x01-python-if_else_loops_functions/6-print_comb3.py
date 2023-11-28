#!/usr/bin/python3
for numFirst in range(10):
    for numSecond in range(10):
        if numFirst == 8 and numSecond == 9:
            print("{one}{two}".format(one=numFirst,
                                      two=numSecond), end="\n")
        elif numFirst < numSecond and numFirst != numSecond:
            print("{one}{two}".format(one=numFirst,
                                      two=numSecond), end=", ")
