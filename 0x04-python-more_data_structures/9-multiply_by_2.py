#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = {}
    for i in a_dictionary:
        copy_dictionary[i] = a_dictionary[i] * 2
    return copy_dictionary
