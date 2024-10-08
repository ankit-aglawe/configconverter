"""
Emitters module for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import configparser
import json
from io import StringIO
from typing import Any, Dict
from xml.etree.ElementTree import Element, tostring

import toml
import yaml

from .exceptions import EmitterError

__all__ = [
    "BaseEmitter",
    "JSONEmitter",
    "YAMLEmitter",
    "TOMLEmitter",
    "INIEmitter",
    "XMLEmitter",
    "EMITTER_CLASSES",
]


class BaseEmitter:
    """
    Base class for all emitters.
    """

    def emit(self, data: Dict[str, Any], indent: int = 4, **options: Any) -> str:
        """
        Emit data from a Python dictionary into a string.

        Args:
            data (Dict[str, Any]): Data to emit.
            indent (int, optional): Indentation level. Defaults to 4.
            **options: Additional options for emitters.

        Returns:
            str: Emitted data as a string.

        Raises:
            EmitterError: If emitting fails.
        """
        raise NotImplementedError("Emitter must implement the emit method.")


class JSONEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], indent: int = 4, **options: Any) -> str:
        try:
            return json.dumps(data, indent=indent, **options)
        except (TypeError, ValueError) as e:
            raise EmitterError(f"JSON emitting error: {e}") from e


class YAMLEmitter(BaseEmitter):
    def emit(self, data: Any, indent: int = 4, **options: Any) -> str:
        try:
            return yaml.dump(data, indent=indent, **options)
        except yaml.YAMLError as e:
            raise EmitterError(f"YAML emitting error: {e}") from e


class TOMLEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], indent: int = 4, **options: Any) -> str:
        try:
            return toml.dumps(data)
        except (TypeError, ValueError) as e:
            raise EmitterError(f"TOML emitting error: {e}") from e


class INIEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], indent: int = 4, **options: Any) -> str:
        try:
            config = configparser.ConfigParser()
            for section, params in data.items():
                config[str(section)] = {}
                if isinstance(params, dict):
                    for k, v in params.items():
                        config[str(section)][str(k)] = str(v)
                else:
                    # Handle non-dict params by converting them to strings
                    config[str(section)]["value"] = str(params)
            output = StringIO()
            config.write(output)
            return output.getvalue()
        except (configparser.Error, TypeError, ValueError) as e:
            raise EmitterError(f"INI emitting error: {e}") from e


class XMLEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], indent: int = 4, **options: Any) -> str:
        try:
            if len(data) == 1:
                root_element = self._dict_to_xml(data)
            else:
                # Wrap multiple root elements under a single root
                wrapped_data = {"ConfigConverter": data}
                root_element = self._dict_to_xml(wrapped_data)
            xml_str = tostring(root_element, encoding="unicode")
            return xml_str
        except Exception as e:
            raise EmitterError(f"XML emitting error: {e}") from e

    def _dict_to_xml(self, data: Dict[str, Any]) -> Element:
        def build_element(key: str, value: Any) -> Element:
            elem = Element(key)
            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, list):
                        for item in v:
                            child = build_element(k, item)
                            elem.append(child)
                    else:
                        child = build_element(k, v)
                        elem.append(child)
            elif isinstance(value, list):
                for item in value:
                    child = build_element("item", item)
                    elem.append(child)
            else:
                elem.text = str(value)
            return elem

        if len(data) != 1:
            raise ValueError("XML root must have a single root element.")
        root_key = next(iter(data))
        root_value = data[root_key]
        return build_element(root_key, root_value)


EMITTER_CLASSES = {
    "json": JSONEmitter,
    "yaml": YAMLEmitter,
    "toml": TOMLEmitter,
    "ini": INIEmitter,
    "xml": XMLEmitter,
}
