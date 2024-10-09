"""
Command-line interface for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import argparse
import logging
import sys

from .converter import convert
from .exceptions import ConversionError, UnsupportedFormatError


def main():
    parser = argparse.ArgumentParser(
        description="ConfigConverter: Convert configuration files between formats."
    )
    parser.add_argument("input", help="Input file path or data string.")
    parser.add_argument("output", nargs="?", help="Output file path.")
    parser.add_argument(
        "--from-file",
        action="store_true",
        help="Interpret input as a file path.",
    )
    parser.add_argument(
        "--input-format",
        help="Specify the input format if it cannot be inferred.",
    )
    parser.add_argument(
        "--output-format",
        help="Specify the output format if it cannot be inferred.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the output file if it exists.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the output.",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=4,
        help="Indentation level for the output.",
    )
    parser.add_argument(
        "--root-name",
        type=str,
        default="root",
        help="Root element name for XML output.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="ConfigConverter 0.2.0",
        help="Show the version and exit.",
    )

    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    options = {
        "indent": args.indent,
        "pretty": args.pretty,
    }
    if args.root_name:
        options["root_name"] = args.root_name

    try:
        convert(
            input_data=args.input,
            input_format=args.input_format,
            output_format=args.output_format,
            output_file=args.output,
            from_file=args.from_file,
            **options,
        )
    except (ConversionError, UnsupportedFormatError, ValueError) as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
    except FileExistsError as e:
        logger.error(f"Error: {e}")
        sys.exit(1)
        sys.exit(1)
