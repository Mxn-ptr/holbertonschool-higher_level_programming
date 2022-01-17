#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for elements in range(0, x):
        try:
            print("{:d}".format(my_list[elements]), end="")
            count += 1
        except: 
            pass
    print(" ")
    return count
