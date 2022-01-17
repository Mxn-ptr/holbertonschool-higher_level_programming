#!/usr/bin/python3
from decimal import DivisionByZero
from re import T


def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, DivisionByZero):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
