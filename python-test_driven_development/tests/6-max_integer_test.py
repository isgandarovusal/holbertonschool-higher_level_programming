#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_regular_list(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_mixed_numbers(self):
        """Test with positive and negative numbers."""
        self.assertEqual(max_integer([-1, 5, 10, -2]), 10)

    def test_max_at_beginning(self):
        """Test a list where the max is at the start."""
        self.assertEqual(max_integer([100, 50, 20, 10]), 100)

    def test_max_in_middle(self):
        """Test a list where the max is in the middle."""
        self.assertEqual(max_integer([10, 20, 100, 50, 20]), 100)

    def test_none_argument(self):
        """Test passing None to the function."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_of_strings(self):
        """Test a list containing strings."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])

if __name__ == '__main__':
    unittest.main()
