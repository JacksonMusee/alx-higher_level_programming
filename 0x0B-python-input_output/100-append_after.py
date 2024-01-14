#!/usr/bin/python3

"""
Write a function that inserts a line of text to a file, after each line
containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        lines = my_file.readlines()

    with open(filename, "w", encoding="utf-8") as my_file:
        for line in lines:
            my_file.write(line)
            if search_string in line:
                my_file.write(new_string)
