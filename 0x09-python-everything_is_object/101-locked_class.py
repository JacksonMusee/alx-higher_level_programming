#!/usr/bin/python3
"""
Here we want to see who is the boss.
A class will control what happens inside.
Let's see.
"""


class LockedClass:
    """
    This class limits attibute name.
    You cannot name them whatever you want
    """
    __slots__ = ("first_name",)
