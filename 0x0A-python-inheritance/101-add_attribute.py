#!/usr/bin/python3
"""
Lorem ipsum
"""


def add_attribute(obj, key, value):
    """
    Add to new attribute
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
