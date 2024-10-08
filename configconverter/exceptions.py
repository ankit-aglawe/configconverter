"""
Custom exceptions for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""


class ConfigConverterError(Exception):
    """Base exception for configconverter errors."""


class UnsupportedFormatError(ConfigConverterError):
    """Exception for unsupported file formats."""


class ConversionError(ConfigConverterError):
    """Exception for errors during conversion."""


class ParserError(ConfigConverterError):
    """Exception for errors during parsing."""


class EmitterError(ConfigConverterError):
    """Exception for errors during emitting."""
