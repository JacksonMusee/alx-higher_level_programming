#!/usr/bin/python3

"""
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""

def read_file(filename=""):
    """
    This function does exectly as required in the module
    Documentation above.
    That must be clear
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        print(read(my_file))
