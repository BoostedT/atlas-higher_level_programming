#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function
    """

    def test_max_integer(self):
        """Test max_integer function
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1, 2, 3, 4]), 4)

        def test_type_error(self):
            """type error test
            """
            self.assertRaises(TypeError, max_integer, [1, 2, "hello"])
            self.assertRaises(TypeError, max_integer, [1, [1, 2]])
            
    def negative_test(self):
        """Test negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1, -2, -3, -4]), -1)
