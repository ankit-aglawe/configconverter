# tests/test_converter.py

import unittest

from configconverter.converter import Converter
from configconverter.exceptions import ConversionError, UnsupportedFormatError


class TestConverter(unittest.TestCase):
    def test_conversion_json_to_yaml(self):
        converter = Converter("json", "yaml")
        input_data = '{"name": "John", "age": 30}'
        result = converter.convert(input_data, from_file=False)
        expected = "age: 30\nname: John\n"
        self.assertEqual(result, expected)

    def test_conversion_yaml_to_json(self):
        converter = Converter("yaml", "json", indent=2)
        input_data = "name: John\nage: 30"
        result = converter.convert(input_data, from_file=False)
        expected = '{\n  "age": 30,\n  "name": "John"\n}'
        self.assertEqual(result, expected)

    def test_unsupported_input_format(self):
        with self.assertRaises(UnsupportedFormatError):
            Converter("csv", "json")

    def test_unsupported_output_format(self):
        with self.assertRaises(UnsupportedFormatError):
            Converter("json", "csv")

    def test_conversion_error(self):
        converter = Converter("json", "yaml")
        input_data = '{"name": "John", "age": 30'  # Invalid JSON
        with self.assertRaises(ConversionError):
            converter.convert(input_data, from_file=False)


if __name__ == "__main__":
    unittest.main()
