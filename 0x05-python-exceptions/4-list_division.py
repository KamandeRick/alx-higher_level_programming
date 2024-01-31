#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    vals = []
    errResult = 0
    for i in range(0, list_length):
        try:
            value = (my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            value = errResult
        except ZeroDivisionError:
            print("division by 0")
            value = errResult
        except IndexError:
            print("out of range")
            value = errResult
        finally:
            vals.append(value)
    return vals
