#!/usr/bin/python3
"""
Lorem ipsum
Clear enough
"""


class MyInt(int):
    """
    Mynt s a rebel
    """
    def __init__(self, val):
        self.val = val

    def __eq__(self, val2):
        if self.val == val2:
            case = False
        else:
            case = True
        return case

    def __ne__(self, val2):
        if self.val != val2:
            case = False
        else:
            case = True
        return case
