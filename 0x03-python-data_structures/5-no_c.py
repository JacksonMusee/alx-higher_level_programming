#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    c_indexes = []
    new_str = ""

    while idx < len(my_string):
        if my_string[idx] in ('c', 'C'):
            c_indexes.append(idx)
        idx += 1

    for i in range(len(my_string)):
        if i not in c_indexes:
            new_str = new_str + my_string[i]

    return new_str
