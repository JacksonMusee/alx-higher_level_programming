#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8) and returns
the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
"""


def write_file(filename="", text=""):
    """
    Ths functon refers to the requirement listed in this module's documentation
    above.
    """

    with open(filename, "w", encoding="utf-8") as my_file:
        return (my_file.write(text))
