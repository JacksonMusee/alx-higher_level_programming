#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    arg_count = len(sys.argv) - 1

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == "+":
        rslt = calculator_1.add(a, b)
    elif op == "-":
        rslt = calculator_1.sub(a, b)
    elif op == "*":
        rslt = calculator_1.mul(a, b)
    elif op == "/":
        rslt = calculator_1.div(a, b)

    print("{} {} {} = {}".format(a, op, b, rslt))
