"""
Parsers module for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import configparser
import json
from typing import Any, Dict

import toml
import xmltodict
import yaml

from .exceptions import ParserError

__all__ = [
    "BaseParser",
    "JSONParser",
    "YAMLParser",
    "TOMLParser",
    "INIParser",
    "XMLParser",
    "PARSER_CLASSES",
]


class BaseParser:
    """
    Base class for all parsers.
    """

    def parse(self, input_data: str) -> Dict[str, Any]:
        """
        Parse input data into a Python dictionary.

        Args:
            input_data (str): Input data as a string.

        Returns:
            Dict[str, Any]: Parsed data.

        Raises:
            ParserError: If parsing fails.
        """
        raise NotImplementedError("Parser must implement the parse method.")


class JSONParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Any]:
        try:
            return json.loads(input_data)
        except json.JSONDecodeError as e:
            raise ParserError(f"JSON parsing error: {e}") from e


class YAMLParser(BaseParser):
    def parse(self, content: str) -> Dict[str, Any]:
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as e:
            raise ParserError(f"YAML parsing error: {e}") from e


class TOMLParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Any]:
        try:
            return toml.loads(input_data)
        except toml.TomlDecodeError as e:
            raise ParserError(f"TOML parsing error: {e}") from e


class INIParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Any]:
        try:
            config = configparser.ConfigParser()
            config.read_string(input_data)
            return {
                section: dict(config.items(section)) for section in config.sections()
            }
        except configparser.Error as e:
            raise ParserError(f"INI parsing error: {e}") from e


class XMLParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Any]:
        try:
            data = xmltodict.parse(input_data)
            return data
        except Exception as e:
            raise ParserError(f"XML parsing error: {e}") from e


PARSER_CLASSES = {
    "json": JSONParser,
    "yaml": YAMLParser,
    "toml": TOMLParser,
    "ini": INIParser,
    "xml": XMLParser,
}
