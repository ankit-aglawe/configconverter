"""
Custom exceptions for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""


class ConversionError(Exception):
    """Base exception for conversion errors."""

    pass


class UnsupportedFormatError(ConversionError):
    """Exception raised when an unsupported format is specified."""

    pass


class EmitterError(ConversionError):
    """Exception raised during emitting processes."""

    pass


class ParserError(ConversionError):
    """Exception raised during parsing processes."""

    pass
