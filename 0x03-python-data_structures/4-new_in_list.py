#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) > (len(my_list) - 1):
        return my_list.copy()
    else:
        listNew = my_list.copy()
        listNew[int(idx)] = element
        return listNew
