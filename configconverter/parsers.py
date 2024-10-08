"""
Parsers module for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import configparser
import json
import xml.etree.ElementTree as ET
from typing import Any, Dict

import toml
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
    def parse(self, input_data: str) -> Any:
        try:
            return yaml.safe_load(input_data)
        except yaml.YAMLError as e:
            raise ParserError(f"YAML parsing error: {e}") from e


class TOMLParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Any]:
        try:
            return toml.loads(input_data)
        except toml.TomlDecodeError as e:
            raise ParserError(f"TOML parsing error: {e}") from e


class INIParser(BaseParser):
    def parse(self, input_data: str) -> Dict[str, Dict[str, str]]:
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
            root = ET.fromstring(input_data)
            return self._xml_to_dict(root)
        except ET.ParseError as e:
            raise ParserError(f"XML parsing error: {e}") from e

    def _xml_to_dict(self, element: ET.Element) -> Dict[str, Any]:
        def internal_iter(e: ET.Element) -> Dict[str, Any]:
            d: Dict[str, Any] = {}
            if e.text and e.text.strip():
                d["__text__"] = e.text.strip()
            for key, value in e.attrib.items():
                d[f"@{key}"] = value
            for child in e:
                child_tag = child.tag
                child_dict = internal_iter(child)
                d.setdefault(child_tag, []).append(child_dict)
            return d

        return {element.tag: internal_iter(element)}


PARSER_CLASSES = {
    "json": JSONParser,
    "yaml": YAMLParser,
    "toml": TOMLParser,
    "ini": INIParser,
    "xml": XMLParser,
}
