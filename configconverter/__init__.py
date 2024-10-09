"""
ConfigConverter: A tool to convert configuration files between different formats.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

from configconverter.converter import convert
from configconverter.exceptions import (
    ConversionError,
    EmitterError,
    ParserError,
    UnsupportedFormatError,
)

__version__ = "0.2.0"

__all__ = [
    "convert",
    "ConversionError",
    "UnsupportedFormatError",
    "ParserError",
    "EmitterError",
]
