# Examples

Real-world examples of using ConfigConverter.

## Batch Conversion

Convert all JSON files in a directory to YAML.

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

## Custom Indentation

Convert a file with custom indentation.

```bash
configconverter config.json config.yaml --indent 2
```

## Using in a Python Script

Integrate ConfigConverter into your Python application.

```python
from configconverter import convert

def convert_config(input_path: str, output_path: str):
    convert(input_path, 'toml', 'ini', output_file=output_path)

if __name__ == '__main__':
    convert_config('settings.toml', 'settings.ini')
```