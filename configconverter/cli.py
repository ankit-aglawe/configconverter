"""
Command-line interface for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import argparse
import logging
import os
import sys

from .converter import convert
from .exceptions import ConfigConverterError
from .utils import infer_format

logger = logging.getLogger("configconverter")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert configuration files between formats."
    )
    parser.add_argument("input_file", help="Path to the input configuration file.")
    parser.add_argument(
        "output_file", nargs="?", help="Path to the output configuration file."
    )
    parser.add_argument("-i", "--input-format", help="Format of the input file.")
    parser.add_argument("-o", "--output-format", help="Format of the output file.")
    parser.add_argument(
        "--indent", type=int, default=4, help="Indentation level for output."
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the output file if it exists.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print output to stdout instead of a file.",
    )
    parser.add_argument(
        "--pretty", action="store_true", help="Pretty-print the output (indent=4)."
    )
    parser.add_argument(
        "-v", "--version", action="version", version="configconverter 0.1.0"
    )
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Infer formats if not provided
    if not args.input_format:
        args.input_format = infer_format(args.input_file)
        if not args.input_format:
            logger.error(
                "Unable to infer input format. Please specify using --input-format."
            )
            sys.exit(1)
    if not args.output_format:
        if args.output_file:
            args.output_format = infer_format(args.output_file)
            if not args.output_format:
                logger.error(
                    "Unable to infer output format. Please specify using --output-format."
                )
                sys.exit(1)
        elif args.stdout:
            logger.error("Output format must be specified when using --stdout.")
            sys.exit(1)
        else:
            logger.error("Output file or --stdout must be specified.")
            sys.exit(1)

    # Set indentation if pretty is specified
    if args.pretty:
        args.indent = 4

    # Check if output file exists
    if (
        args.output_file
        and not args.stdout
        and os.path.exists(args.output_file)
        and not args.overwrite
    ):
        response = input(f"File {args.output_file} exists. Overwrite? [y/N]: ")
        if response.lower() != "y":
            sys.exit("Operation cancelled.")

    try:
        output_data = convert(
            input_data=args.input_file,
            input_format=args.input_format,
            output_format=args.output_format,
            indent=args.indent,
            from_file=True,
        )
        if args.stdout:
            print(output_data)
        else:
            if args.output_file:
                with open(args.output_file, "w", encoding="utf-8") as f:
                    f.write(output_data)
                logger.info(
                    "Conversion successful: %s -> %s", args.input_file, args.output_file
                )
            else:
                logger.error("Output file not specified.")
                sys.exit(1)
    except ConfigConverterError as e:
        logger.error("Error: %s", e)
        sys.exit(1)
