#!/usr/bin/env python3
""" Unittesting for Utils """
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock



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
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test the nested map exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
    

class TestGetJson(unittest.TestCase):
    """ Test for get_json """

    @parameterized.expand([
        ("http://example.com",{"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ testing utils.get_json function """
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)

