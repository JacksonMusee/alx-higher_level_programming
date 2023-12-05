#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ev_list = []

    for element in my_list:
        if element % 2 == 0:
            ev_list.append(True)
        else:
            ev_list.append(False)

    return ev_list
