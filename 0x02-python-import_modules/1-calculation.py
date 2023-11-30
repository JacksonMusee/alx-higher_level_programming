#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as xy
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, xy.add(a, b)))
    print("{} - {} = {}".format(a, b, xy.sub(a, b)))
    print("{} * {} = {}".format(a, b, xy.mul(a, b)))
    print("{} / {} = {}".format(a, b, xy.div(a, b)))
