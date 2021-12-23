#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    count = len(sys.argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
