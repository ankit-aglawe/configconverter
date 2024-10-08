"""
Converter module for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import logging
from typing import Any, Optional

from .emitters import EMITTER_CLASSES
from .exceptions import ConversionError, UnsupportedFormatError
from .parsers import PARSER_CLASSES

logger = logging.getLogger(__name__)


class Converter:
    """
    A class to convert configuration data between different formats.
    """

    def __init__(
        self, input_format: str, output_format: str, indent: int = 4, **options: Any
    ) -> None:
        self.input_format = input_format.lower()
        self.output_format = output_format.lower()
        self.indent = indent
        self.options = options

        logger.debug(
            "Initializing Converter: %s to %s", self.input_format, self.output_format
        )

        self.parser = self.get_parser()
        self.emitter = self.get_emitter()

    def get_parser(self):
        parser_class = PARSER_CLASSES.get(self.input_format)
        if not parser_class:
            logger.error("Unsupported input format: %s", self.input_format)
            raise UnsupportedFormatError(
                f"Unsupported input format: {self.input_format}"
            )
        return parser_class()

    def get_emitter(self):
        emitter_class = EMITTER_CLASSES.get(self.output_format)
        if not emitter_class:
            logger.error("Unsupported output format: %s", self.output_format)
            raise UnsupportedFormatError(
                f"Unsupported output format: {self.output_format}"
            )
        return emitter_class()

    def convert(self, input_data: str, from_file: bool = True) -> str:
        """
        Convert input data to the desired output format.

        Args:
            input_data (str): Input data as a string or file path.
            from_file (bool): Indicates if input_data is a file path.

        Returns:
            str: Converted data as a string.

        Raises:
            ConversionError: If an error occurs during conversion.
        """
        try:
            if from_file:
                logger.debug("Reading input data from file: %s", input_data)
                with open(input_data, "r", encoding="utf-8") as f:
                    input_data = f.read()
            logger.debug("Parsing input data.")
            data = self.parser.parse(input_data)
            logger.debug("Emitting output data.")
            output_data = self.emitter.emit(data, indent=self.indent, **self.options)
            return output_data
        except Exception as e:
            logger.exception("Conversion failed: %s", e)
            raise ConversionError(f"Conversion failed: {e}") from e


def convert(
    input_data: str,
    input_format: str,
    output_format: str,
    output_file: Optional[str] = None,
    indent: int = 4,
    from_file: bool = True,
    **options: Any,
) -> Optional[str]:
    """
    Convenience function to convert configuration data between formats.

    Args:
        input_data (str): Input data as a string or file path.
        input_format (str): Format of the input data.
        output_format (str): Desired output format.
        output_file (str, optional): Path to save the output data.
        indent (int, optional): Indentation level for the output data. Defaults to 4.
        from_file (bool, optional): Indicates if input_data is a file path.
        **options: Additional options for parsers or emitters.

    Returns:
        str or None: Output data as a string if output_file is None; otherwise, None.
    """
    logger.debug("Starting conversion from %s to %s.", input_format, output_format)
    converter = Converter(input_format, output_format, indent=indent, **options)
    output_data = converter.convert(input_data, from_file=from_file)

    if output_file:
        logger.debug("Writing output data to file: %s", output_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_data)
        return None
    else:
        return output_data
