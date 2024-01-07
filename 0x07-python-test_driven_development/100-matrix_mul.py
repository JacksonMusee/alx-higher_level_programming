#!/usr/bin/python3
"""
This module is very interesting
We will attempt to real mathematians
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices
    But first it confirms multiplicability
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for item in m_a:
        if not isinstance(item, list):
            raise TypeError('m_a must be a list of lists')

    for item in m_b:
        if not isinstance(item, list):
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("m_b should contain only integers or floats")

    len_ma_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_ma_a:
            raise TypeError("each row of m_a must be of the same size")

    len_mb_a = len(m_b[0])
    for row in m_b:
        if len(row) != len_mb_a:
            raise TypeError("each row of m_b must be of the same size")

    if len_ma_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    pd_mat = []
    pd_elemt = 0
    for i in range(0, len(m_a)):
        pd_mat.append([])
        for k in range(0, len_mb_a):
            for j in range(0, len_ma_a):
                pd_elemt += m_a[i][j] * m_b[j][k]
            pd_mat[i].append(pd_elemt)
            pd_elemt = 0

    return pd_mat
