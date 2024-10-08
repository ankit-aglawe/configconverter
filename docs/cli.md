# Command-Line Interface

Detailed documentation of the command-line interface.

## Syntax

```bash
configconverter [OPTIONS] INPUT_FILE [OUTPUT_FILE]
```

## Options

### `-i, --input-format FORMAT`

Specify the format of the input file. Supported formats:

- `json`
- `yaml`
- `toml`
- `ini`
- `xml`

### `-o, --output-format FORMAT`

Specify the format of the output file. Supported formats are the same as input formats.

### `--indent N`

Set indentation level for the output file (default is 4).

### `--overwrite`

Overwrite the output file if it exists without prompting.

### `--stdout`

Print the output to standard output instead of writing to a file.

### `--pretty`

Pretty-print the output with default indentation (indent=4).

### `-v, --version`

Show the version of ConfigConverter and exit.

### `-h, --help`

Show the help message and exit.

## Examples

**Convert INI to TOML:**

```bash
configconverter -i ini -o toml settings.ini settings.toml
```

**Convert XML to JSON and print to stdout:**

```bash
configconverter config.xml -o json --stdout
```

**Overwrite existing file without prompting:**

```bash
configconverter config.yaml config.json --overwrite
```