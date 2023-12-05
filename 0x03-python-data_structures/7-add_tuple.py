#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a_0 = 0
        tuple_a_1 = 0
    elif len(tuple_a) == 1:
        tuple_a_0 = tuple_a[0]
        tuple_a_1 = 0
    else:
        tuple_a_0 = tuple_a[0]
        tuple_a_1 = tuple_a[1]

    if len(tuple_b) == 0:
        tuple_b_0 = 0
        tuple_b_1 = 0
    elif len(tuple_b) == 1:
        tuple_b_0 = tuple_b[0]
        tuple_b_1 = 0
    else:
        tuple_b_0 = tuple_b[0]
        tuple_b_1 = tuple_b[1]

    return ((tuple_a_0 + tuple_b_0, tuple_a_1 + tuple_b_1))
