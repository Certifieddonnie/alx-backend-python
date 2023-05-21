#!/usr/bin/env python3
""" Unittesting for Utils """
import unittest
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """ A Test Class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test the access nested map """
        self.assertEqual(access_nested_map(nested_map, path), result)
