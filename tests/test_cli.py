# tests/test_cli.py

import os
import subprocess
import unittest


class TestCLI(unittest.TestCase):
    def test_cli_conversion(self):
        input_file = "test.json"
        output_file = "test.yaml"
        with open(input_file, "w") as f:
            f.write('{"name": "John", "age": 30}')
        try:
            subprocess.check_call(["configconverter", input_file, output_file])
            with open(output_file, "r") as f:
                content = f.read()
            self.assertIn("name: John", content)
            self.assertIn("age: 30", content)
        finally:
            os.remove(input_file)
            os.remove(output_file)

    def test_cli_help(self):
        result = subprocess.run(["configconverter", "--help"], stdout=subprocess.PIPE)
        self.assertIn("Usage:", result.stdout.decode())

    def test_cli_version(self):
        result = subprocess.run(
            ["configconverter", "--version"], stdout=subprocess.PIPE
        )
        self.assertIn("configconverter", result.stdout.decode())


if __name__ == "__main__":
    unittest.main()
