#!/usr/bin/python3
for characterNumber in range(97, 123):
    if characterNumber != 101 and characterNumber != 113:
        print("{character}".format(character=chr(characterNumber)), end="")
