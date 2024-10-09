import pytest

from configconverter.converter import convert
from configconverter.exceptions import ConversionError, UnsupportedFormatError

# Sample data for testing
sample_data = {
    "key1": "value1",
    "key2": 123,
    "key3": True,
    "section": {"subkey1": "subvalue1", "subkey2": [1, 2, 3]},
}

sample_json = '{"key1": "value1", "key2": 123, "key3": true, "section": {"subkey1": "subvalue1", "subkey2": [1, 2, 3]}}'
sample_yaml = """
key1: value1
key2: 123
key3: true
section:
  subkey1: subvalue1
  subkey2:
    - 1
    - 2
    - 3
"""

sample_toml = """
key1 = "value1"
key2 = 123
key3 = true

[section]
subkey1 = "subvalue1"
subkey2 = [1, 2, 3]
"""

sample_ini = """
[DEFAULT]
key1 = value1
key2 = 123
key3 = True

[section]
subkey1 = subvalue1
subkey2 = 1,2,3
"""

sample_xml = """
<root>
    <key1>value1</key1>
    <key2>123</key2>
    <key3>true</key3>
    <section>
        <subkey1>subvalue1</subkey1>
        <subkey2>1</subkey2>
        <subkey2>2</subkey2>
        <subkey2>3</subkey2>
    </section>
</root>
"""


def test_convert_json_to_yaml():
    output = convert(
        sample_json, input_format="json", output_format="yaml", from_file=False
    )
    assert "key1: value1" in output


def test_convert_yaml_to_json():
    output = convert(
        sample_yaml, input_format="yaml", output_format="json", from_file=False
    )
    assert '"key1": "value1"' in output


def test_convert_toml_to_json():
    output = convert(
        sample_toml, input_format="toml", output_format="json", from_file=False
    )
    assert '"key1": "value1"' in output


def test_convert_ini_to_json():
    output = convert(
        sample_ini, input_format="ini", output_format="json", from_file=False
    )
    assert '"section": {' in output


def test_convert_xml_to_json():
    output = convert(
        sample_xml, input_format="xml", output_format="json", from_file=False
    )
    assert '"root": {' in output


def test_convert_with_pretty_option():
    output = convert(
        sample_json,
        input_format="json",
        output_format="yaml",
        from_file=False,
        pretty=True,
    )
    assert "\n" in output  # Pretty output should contain newlines


def test_unsupported_input_format():
    with pytest.raises(UnsupportedFormatError):
        convert(
            sample_json,
            input_format="unsupported",
            output_format="json",
            from_file=False,
        )


def test_unsupported_output_format():
    with pytest.raises(UnsupportedFormatError):
        convert(
            sample_json,
            input_format="json",
            output_format="unsupported",
            from_file=False,
        )


def test_conversion_error():
    with pytest.raises(ConversionError):
        convert(
            "invalid json", input_format="json", output_format="yaml", from_file=False
        )


def test_infer_format():
    from configconverter.utils import infer_format

    assert infer_format("config.json") == "json"
    assert infer_format("config.yaml") == "yaml"
    assert infer_format("config.toml") == "toml"
    assert infer_format("config.ini") == "ini"
    assert infer_format("config.xml") == "xml"
    assert infer_format("config.unknown") is None
    assert infer_format("config.unknown") is None
