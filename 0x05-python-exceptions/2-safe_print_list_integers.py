from typing import Type


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for elements in range(0, x):
        try:
            print("{:d}".format(my_list[elements]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
