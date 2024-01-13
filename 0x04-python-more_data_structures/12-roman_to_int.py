#!/usr/bin/python3

def roman_to_int(roman_string):
    romDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if roman_string and isinstance(roman_string, str):
        total = 0
        keyLast = 0
        keyCurrent = 0
        for romSymbol in roman_string:
            keyCurrent = romDict.get(romSymbol, 0)
            if keyLast != 0 and keyLast >= keyCurrent:
                total += keyCurrent
            elif keyLast != 0 and keyLast < keyCurrent:
                total += (keyCurrent - (2 * keyLast))
            elif keyLast == 0:
                total += keyCurrent
            keyLast = keyCurrent
        return total
    else:
        return 0
