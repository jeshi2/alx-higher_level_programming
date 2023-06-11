#!/usr/bin/python3
"""Unittest for max_integer([..]) module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing only one element
        self.assertEqual(max_integer([42]), 42)

        # Test with a large list of integers
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

        # Test with a list containing duplicate elements
        self.assertEqual(max_integer([1, 2, 3, 4, 4, 3, 2, 1]), 4)

        # Test with a list containing a float
        self.assertEqual(max_integer([1, 2, 3, 4.5]), 4.5)

        # Test with a list containing a string
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, '4'])
