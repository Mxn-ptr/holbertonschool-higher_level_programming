#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_i = len(my_list)
    for i in range(0, len_i):
        print("{:d}".format(my_list[i]))
