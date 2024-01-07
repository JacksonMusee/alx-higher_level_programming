#!/usr/bin/python3
"""
Unittest for this function
max_integer(list=[])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Test if argument is list
    """

    def test_max(self):
        self.assertEqual(max_integer([3,4,7,8,9]), 9)
        self.assertEqual(max_integer([9,8,7,4,3]), 9)
        self.assertEqual(max_integer([4,3,9,7,8]), 9)
        self.assertEqual(max_integer([3,7,4,-8,9]), 9)
        self.assertEqual(max_integer([-3,-7,-8,-4,-9]), -3)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([]), None)
