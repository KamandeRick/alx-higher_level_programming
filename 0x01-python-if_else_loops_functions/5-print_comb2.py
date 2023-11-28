#!/usr/bin/python3
for n in range(100):
    if n != 99:
        print("{num:02d}".format(num=n), end=", ")
    else:
        print("{num:02d}".format(num=n), end="\n")
