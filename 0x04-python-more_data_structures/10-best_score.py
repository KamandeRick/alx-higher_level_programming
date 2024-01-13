#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keyMax, valMax = "", float('-inf')
        for key, value in a_dictionary.items():
            if value > valMax:
                keyMax, valMax = key, value
        return keyMax
    else:
        return None
