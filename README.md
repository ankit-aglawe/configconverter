# ConfigConverter

[![PyPI Version](https://img.shields.io/pypi/v/configconverter.svg)](https://pypi.org/project/configconverter/)
[![Python Versions](https://img.shields.io/pypi/pyversions/configconverter.svg)](https://pypi.org/project/configconverter/)
[![License](https://img.shields.io/pypi/l/configconverter.svg)](https://github.com/ankitaglawe/configconverter/blob/main/LICENSE)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](https://ankit-aglawe.github.io/configconverter/)

**ConfigConverter** is a powerful and easy-to-use tool designed to convert configuration files between various formats, including JSON, YAML, TOML, INI, and XML. Whether you're a developer, system administrator, or DevOps engineer, ConfigConverter streamlines your workflow by simplifying the process of managing and converting configuration files.

## Features

- **Multi-Format Support:** Seamlessly convert between JSON, YAML, TOML, INI, and XML formats.
- **Command-Line Interface (CLI):** Perform conversions directly from your terminal with simple commands.
- **Python API:** Integrate conversion functionality into your Python projects effortlessly.
- **Extensible and Customizable:** Easily extend the tool to support additional formats or custom conversion logic.
- **User-Friendly:** Intuitive design ensures a smooth experience for both beginners and advanced users.

## Installation

### Via PyPI

Install ConfigConverter using `pip`:

```bash
pip install configconverter
```

### From Source

Clone the repository and install using Poetry:

```bash
git clone https://github.com/ankitaglawe/configconverter.git
cd configconverter
poetry install
```

## Quick Start

### Command-Line Usage

Convert `config.json` to `config.yaml`:

```bash
configconverter config.json config.yaml
```

Specify input and output formats explicitly:

```bash
configconverter -i ini -o toml settings.conf settings.toml
```

Output the converted configuration to standard output:

```bash
configconverter config.toml -o json --stdout
```

### Python API Usage

#### Convert Using File Paths

```python
from configconverter import convert

# Convert JSON to YAML and save to a file
convert('config.json', 'json', 'yaml', output_file='config.yaml')
```

#### Convert Using Data Strings

```python
from configconverter import convert

# Convert JSON string to YAML string
json_data = '{"name": "John", "age": 30}'
yaml_data = convert(json_data, 'json', 'yaml', from_file=False)
print(yaml_data)
```

## Detailed Documentation

For comprehensive guides, advanced usage, and API references, visit the [ConfigConverter Documentation](https://ankit-aglawe.github.io/configconverter/).

## Examples

### Batch Conversion

Convert all JSON files in a directory to YAML:

```python
import os
from configconverter import convert

input_dir = 'json_configs'
output_dir = 'yaml_configs'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.json', '.yaml'))
        convert(input_file, 'json', 'yaml', output_file=output_file)
```

### Custom Indentation

Convert a file with custom indentation:

```bash
configconverter config.json config.yaml --indent 2
```

## Contributing

Contributions are welcome! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your help is greatly appreciated.

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add awesome feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

For more detailed guidelines, refer to the [Contributing Guide](https://github.com/ankitaglawe/configconverter/blob/main/docs/contributing.md).

## License

This project is licensed under the [MIT License](https://github.com/ankitaglawe/configconverter/blob/main/LICENSE).

## Contact

- **Author:** Ankit Aglawe
- **Email:** [aglawe.ankit@gmail.com](mailto:aglawe.ankit@gmail.com)
- **GitHub:** [ankitaglawe](https://github.com/ankitaglawe)
- **Documentation:** [ConfigConverter Docs](https://ankit-aglawe.github.io/configconverter/)
- **PyPI:** [configconverter](https://pypi.org/project/configconverter/)

## Useful Links

- [Project Repository](https://github.com/ankitaglawe/configconverter)
- [PyPI Package](https://pypi.org/project/configconverter/)
- [Documentation](https://ankit-aglawe.github.io/configconverter/)
- [Issue Tracker](https://github.com/ankitaglawe/configconverter/issues)
