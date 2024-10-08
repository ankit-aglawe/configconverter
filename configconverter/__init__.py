"""
ConfigConverter: A tool to convert configuration files between different formats.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

from .converter import convert
from .exceptions import (
    ConfigConverterError,
    ConversionError,
    EmitterError,
    ParserError,
    UnsupportedFormatError,
)

__version__ = "0.1.0"

__all__ = [
    "convert",
    "ConfigConverterError",
    "UnsupportedFormatError",
    "ConversionError",
    "ParserError",
    "EmitterError",
]
