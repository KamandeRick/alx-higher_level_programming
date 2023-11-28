#!/usr/bin/python3
for num in range(0, 99):
    print("{num:d} = {hexNumber}".format(
        num=int(num), hexNumber=hex(num)), end="\n")

