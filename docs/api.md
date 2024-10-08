# Python API Reference

Detailed documentation of the Python API.

## `convert` Function

```python
convert(
    input_data: str,
    input_format: str,
    output_format: str,
    output_file: Optional[str] = None,
    indent: int = 4,
    from_file: bool = True,
    **options: Any
) -> Optional[str]
```

### Parameters

- **input_data** (str): Input data as a string or file path.
- **input_format** (str): Format of the input data.
- **output_format** (str): Desired output format.
- **output_file** (str, optional): Path to save the output data. If `None`, the function returns the output data as a string.
- **indent** (int, optional): Indentation level for the output data. Defaults to `4`.
- **from_file** (bool, optional): Indicates if `input_data` is a file path (`True`) or a data string (`False`). Defaults to `True`.
- **\*\*options**: Additional options for parsers or emitters.

### Returns

- **str** or **None**: Output data as a string if `output_file` is `None`; otherwise, `None`.

### Raises

- **ConversionError**: If an error occurs during conversion.
- **UnsupportedFormatError**: If the specified format is not supported.

### Example

```python
from configconverter import convert

# Convert JSON string to YAML string
json_data = '{"name": "Alice", "age": 25}'
yaml_data = convert(json_data, 'json', 'yaml', from_file=False)
print(yaml_data)
```