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

if __name__ == '__main___':
    unittest.main()

