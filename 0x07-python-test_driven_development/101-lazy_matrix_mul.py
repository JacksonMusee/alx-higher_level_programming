#!/usr/bin/python3
"""
This module contains only the one function
See the code for details
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices
    Using numpy
    """

    product = numpy.dot(m_a, m_b)

    return product
