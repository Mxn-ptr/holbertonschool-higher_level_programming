#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        """ Test list of int """
        list = [1, 2, 34, 3, 4,]
        self.assertEqual(max_integer(list), 34)

    def test_list_floats(self):
        """ Test list of float """
        list = [1.2, 3.9, 18.7, 98.6]
        self.assertEqual(max_integer(list), 98.6)

    def test_empty_list(self):
        """ Test empty list """
        list = []
        self.assertEqual(max_integer(list), None)

    def test_max_at_the_beginning(self):
        """ Test max at the beginning """
        max_at_the_beginning = [98, 34, 17, 6, 18]
        self.assertEqual(max_integer(max_at_the_beginning), 98)

    def one_negative_number(self):
        """ Test with one negative number """
        list = [12, 76, 5, -34, 67]
        self.assertEqual(max_integer(list), 76)

    def only_negative_numbers(self):
        """ Test with only negative numbers """
        list = [-2, -95, -45, -18, -33]
        self.assertEqual(max_integer(list), -2)

    def test_list_of_one_element(self):
        """ Test with one element """
        list_of_one_element = [9]
        self.assertEqual(max_integer(list_of_one_element), 9)

if __name__ == '__main___':
    unittest.main()
