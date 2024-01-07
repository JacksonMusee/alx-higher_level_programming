#!/usr/bin/python3
"""
This module has only one function. See Documentaon for more infor.
But 'cause they want more explanation.
Still repeatng
"""


def add_integer(a, b=98):
    """
    This function adds two integers and return the sum
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
