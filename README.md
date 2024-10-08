
# ConfigConverter

Convert configuration files between different formats.

## Features

- Supports JSON, YAML, TOML, INI, and XML formats.
- Command-line interface and Python API.
- Easy to use and extend.

## Installation

```bash
pip install configconverter
```

## Command-Line Usage

```bash
configconverter [OPTIONS] INPUT_FILE [OUTPUT_FILE]
```

### Examples

- Convert `config.json` to `config.yaml`:

  ```bash
  configconverter config.json config.yaml
  ```

- Specify formats explicitly:

  ```bash
  configconverter -i ini -o toml settings.conf settings.toml
  ```

- Output to standard output:

  ```bash
  configconverter config.toml -o json --stdout
  ```

## Python API Usage

```python
from configconverter import convert

# Convert using file paths
convert('config.json', 'json', 'yaml', output_file='config.yaml')

# Convert using data strings
json_data = '{"name": "John", "age": 30}'
yaml_data = convert(json_data, 'json', 'yaml', from_file=False)
print(yaml_data)
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License.

