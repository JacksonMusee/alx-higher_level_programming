#!/usr/bin/python3
def magic_string():
    magic_string.cnt = getattr(magic_string, 'cnt', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.cnt - 1)
