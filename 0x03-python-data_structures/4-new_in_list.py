#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return

    if idx < 0 or idx >= len(my_list):
        return my_list

    my_copy = my_list.copy()
    my_copy[idx] = element

    return my_copy
