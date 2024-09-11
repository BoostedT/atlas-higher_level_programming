#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function
    """
    def test_max_integers(self):
        """Test max_integer with integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 2]), 2)
        self.assertEqual(max_integer([1, 1, 2, 1]), 2)
        self.assertEqual(max_integer([1, 2, 1, 1]), 2)
        self.assertEqual(max_integer([2, 1, 1, 1]), 2)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -2]), -1)
        self.assertEqual(max_integer([-1, -1, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -1, -1]), -1)
        self.assertEqual(max_integer([-2, -1, -1, -1]), -1)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()