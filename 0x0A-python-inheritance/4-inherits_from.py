#!/usr/bin/python3
"""
Write a function that returns True if the objec.
Is t hat important
No
"""


def inherits_from(obj, a_class):
    """
    Turns True if the object is an instance of
    a cllass that inherited (directly or indirectly) from the specified cclass
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
