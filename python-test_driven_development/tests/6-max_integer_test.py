#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function
    """

    def test_regular(self):
        """Test regular numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_not_list(self):
        """Test when the argument is not a list
        """
        with self.assertRaises(TypeError):
            max_integer(1)

    def negative_test(self):
        """Test negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)


if __name__ == '__main__':
    unittest.main()