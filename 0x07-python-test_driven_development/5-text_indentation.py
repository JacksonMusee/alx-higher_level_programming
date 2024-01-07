#!/usr/bin/python3
"""
This module le wll only have one function
Should I repeat?
No
See function code for details
"""


def text_indentation(text):
    """
    Print  text
    Print two lines whenevwe you encount . or ? or :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i, char in enumerate(text):
        if text[i] in ['.', ':', '?']:
            print(text[i])
            print("")
        elif i > 0 and text[i] == " " and (text[i - 1] in ['.', ':', '?']):
            print("", end="")
        else:
            print(text[i], end="")
