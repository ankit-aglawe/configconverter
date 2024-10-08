# Usage

ConfigConverter can be used both as a command-line tool and as a Python library.

## Command-Line Interface

### Basic Syntax

```bash
configconverter [OPTIONS] INPUT_FILE [OUTPUT_FILE]
```

### Options

- `-i, --input-format FORMAT` : Specify the format of the input file.
- `-o, --output-format FORMAT`: Specify the format of the output file.
- `--indent N`               : Set indentation level for output file.
- `--overwrite`              : Overwrite the output file if it exists.
- `--stdout`                 : Print output to stdout instead of a file.
- `--pretty`                 : Pretty-print the output (indent=4).
- `-v, --version`            : Show the version and exit.
- `-h, --help`               : Show help message and exit.

### Examples

**Convert `config.json` to `config.yaml`:**

```bash
configconverter config.json config.yaml
```

**Specify formats explicitly:**

```bash
configconverter -i ini -o toml settings.conf settings.toml
```

**Output to standard output:**

```bash
configconverter config.toml -o json --stdout
```

## Python Library

Import the `convert` function from the `configconverter` module.

### Basic Usage

```python
from configconverter import convert

# Convert using file paths
convert('config.json', 'json', 'yaml', output_file='config.yaml')

# Convert using data strings
json_data = '{"name": "John", "age": 30}'
yaml_data = convert(json_data, 'json', 'yaml', from_file=False)
print(yaml_data)
```

### Parameters

- `input_data` (str): Input data as a string or file path.
- `input_format` (str): Format of the input data.
- `output_format` (str): Desired output format.
- `output_file` (str, optional): Path to save the output data.
- `indent` (int, optional): Indentation level for the output data. Defaults to 4.
- `from_file` (bool, optional): Indicates if `input_data` is a file path. Defaults to True.
- `**options`: Additional options for parsers or emitters.