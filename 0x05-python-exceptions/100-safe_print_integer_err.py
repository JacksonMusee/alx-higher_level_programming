#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception:", err, file=sys.stderr)
        return False
    except TypeError as err1:
        print("Exception:", err1, file=sys.stderr)
        return False

    return True
