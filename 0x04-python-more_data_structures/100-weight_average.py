#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    note = 0
    nm_coef = 0
    for elements in my_list:
        note += elements[0] * elements[1]
        nm_coef += elements[1]
    res = note / nm_coef
    return res
