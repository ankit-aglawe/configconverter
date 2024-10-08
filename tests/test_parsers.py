# tests/test_parsers.py

import unittest

from configconverter.exceptions import ParserError
from configconverter.parsers import (
    INIParser,
    JSONParser,
    TOMLParser,
    XMLParser,
    YAMLParser,
)


class TestParsers(unittest.TestCase):
    def test_json_parser(self):
        parser = JSONParser()
        input_data = '{"name": "John", "age": 30}'
        expected = {"name": "John", "age": 30}
        result = parser.parse(input_data)
        self.assertEqual(result, expected)

    def test_yaml_parser(self):
        parser = YAMLParser()
        input_data = "name: John\nage: 30"
        expected = {"name": "John", "age": 30}
        result = parser.parse(input_data)
        self.assertEqual(result, expected)

    def test_toml_parser(self):
        parser = TOMLParser()
        input_data = 'name = "John"\nage = 30'
        expected = {"name": "John", "age": 30}
        result = parser.parse(input_data)
        self.assertEqual(result, expected)

    def test_ini_parser(self):
        parser = INIParser()
        input_data = "[DEFAULT]\nname = John\nage = 30"
        expected = {"DEFAULT": {"name": "John", "age": "30"}}
        result = parser.parse(input_data)
        self.assertEqual(result, expected)

    def test_xml_parser(self):
        parser = XMLParser()
        input_data = "<person><name>John</name><age>30</age></person>"
        expected = {
            "person": {
                "name": [{"__text__": "John"}],
                "age": [{"__text__": "30"}],
            }
        }
        result = parser.parse(input_data)
        self.assertEqual(result, expected)

    def test_invalid_json(self):
        parser = JSONParser()
        input_data = '{"name": "John", "age": 30'  # Missing closing brace
        with self.assertRaises(ParserError):
            parser.parse(input_data)


if __name__ == "__main__":
    unittest.main()
