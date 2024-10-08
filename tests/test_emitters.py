# tests/test_emitters.py

import unittest

from configconverter.emitters import (
    INIEmitter,
    JSONEmitter,
    TOMLEmitter,
    XMLEmitter,
    YAMLEmitter,
)
from configconverter.exceptions import EmitterError


class TestEmitters(unittest.TestCase):
    def test_json_emitter(self):
        emitter = JSONEmitter()
        data = {"name": "John", "age": 30}
        expected = '{\n    "name": "John",\n    "age": 30\n}'
        result = emitter.emit(data, indent=4)
        self.assertEqual(result, expected)

    def test_yaml_emitter(self):
        emitter = YAMLEmitter()
        data = {"name": "John", "age": 30}
        expected = "age: 30\nname: John\n"
        result = emitter.emit(data)
        self.assertEqual(result, expected)

    def test_toml_emitter(self):
        emitter = TOMLEmitter()
        data = {"name": "John", "age": 30}
        expected = 'age = 30\nname = "John"\n'
        result = emitter.emit(data)
        self.assertEqual(result, expected)

    def test_ini_emitter(self):
        emitter = INIEmitter()
        data = {"DEFAULT": {"name": "John", "age": "30"}}
        expected = "[DEFAULT]\nage = 30\nname = John\n\n"
        result = emitter.emit(data)
        self.assertEqual(result, expected)

    def test_xml_emitter(self):
        emitter = XMLEmitter()
        data = {"person": {"name": "John", "age": "30"}}
        expected = "<person><name>John</name><age>30</age></person>"
        result = emitter.emit(data)
        self.assertEqual(result, expected)

    def test_invalid_data(self):
        emitter = JSONEmitter()
        data = {"name": "John", "age": set([30])}  # Sets are not JSON serializable
        with self.assertRaises(EmitterError):
            emitter.emit(data)


if __name__ == "__main__":
    unittest.main()
