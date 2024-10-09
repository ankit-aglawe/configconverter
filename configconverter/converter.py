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
from .utils import infer_format

logger = logging.getLogger(__name__)


def convert(
    input_data: str,
    input_format: Optional[str] = None,
    output_format: Optional[str] = None,
    output_file: Optional[str] = None,
    from_file: bool = True,
    **options: Any,
) -> Optional[str]:
    """
    Convert input data to the desired output format.

    Args:
        input_data (str): Input data as a string or file path.
        input_format (str, optional): Format of the input data.
        output_format (str, optional): Desired output format.
        output_file (str, optional): Path to write the output. If None, returns the output as a string.
        from_file (bool, optional): Indicates if input_data is a file path.
        **options: Additional options such as 'indent' and 'pretty'.

    Returns:
        Optional[str]: Converted data as a string if output_file is None.

    Raises:
        ConversionError: If an error occurs during conversion.
    """
    if from_file:
        input_format = input_format or infer_format(input_data)
        if not input_format:
            raise UnsupportedFormatError(
                "Could not infer input format from file extension."
            )
    else:
        if not input_format:
            raise ValueError("input_format must be specified when from_file is False.")

    if output_file:
        output_format = output_format or infer_format(output_file)
        if not output_format:
            raise UnsupportedFormatError(
                "Could not infer output format from output_file extension."
            )
    else:
        if not output_format:
            raise ValueError(
                "output_format must be specified when output_file is None."
            )

    if input_format not in PARSER_CLASSES:
        raise UnsupportedFormatError(f"Unsupported input format: {input_format}")
    if output_format not in EMITTER_CLASSES:
        raise UnsupportedFormatError(f"Unsupported output format: {output_format}")

    parser = PARSER_CLASSES[input_format]()
    emitter = EMITTER_CLASSES[output_format]()

    try:
        if from_file:
            logger.debug(f"Reading input data from file: {input_data}")
            with open(input_data, "r", encoding="utf-8") as f:
                input_content = f.read()
        else:
            input_content = input_data
            logger.debug("Using input data as string.")

        logger.debug("Parsing input data.")
        data = parser.parse(input_content)

        logger.debug("Emitting output data.")
        output_data = emitter.emit(data, **options)

        if output_file:
            logger.debug(f"Writing output to file: {output_file}")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(output_data)
            logger.info(f"Conversion successful: {input_format} -> {output_format}")
            return None
        else:
            logger.info(f"Conversion successful: {input_format} -> {output_format}")
            return output_data

    except Exception as e:
        logger.exception(f"Conversion failed: {e}")
        raise ConversionError(f"Conversion failed: {e}") from e
