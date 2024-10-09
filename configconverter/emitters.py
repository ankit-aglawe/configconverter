"""
Emitters module for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""

import configparser
import json
from io import StringIO
from typing import Any, Dict
from xml.dom.minidom import parseString

import dicttoxml
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

    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        """
        Emit data from a Python dictionary into a string.

        Args:
            data (Dict[str, Any]): Data to emit.
            **options: Additional options for emitters.

        Returns:
            str: Emitted data as a string.

        Raises:
            EmitterError: If emitting fails.
        """
        raise NotImplementedError("Emitter must implement the emit method.")


class JSONEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        try:
            indent = options.get("indent", 4)
            pretty = options.get("pretty", False)
            if pretty:
                return json.dumps(data, indent=indent)
            else:
                return json.dumps(data)
        except (TypeError, ValueError) as e:
            raise EmitterError(f"JSON emitting error: {e}") from e


class YAMLEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        try:
            default_flow_style = not options.get("pretty", False)
            return yaml.dump(
                data, default_flow_style=default_flow_style, sort_keys=False
            )
        except yaml.YAMLError as e:
            raise EmitterError(f"YAML emitting error: {e}") from e


class TOMLEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        try:
            return toml.dumps(data)
        except (TypeError, ValueError) as e:
            raise EmitterError(f"TOML emitting error: {e}") from e


class INIEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        try:
            config = configparser.ConfigParser()
            for section, params in data.items():
                if isinstance(params, dict):
                    config[str(section)] = {}
                    for k, v in params.items():
                        if isinstance(v, dict):
                            # Handle nested dictionaries by flattening keys
                            for sub_k, sub_v in v.items():
                                config[str(section)][f"{k}.{sub_k}"] = str(sub_v)
                        else:
                            config[str(section)][str(k)] = str(v)
                else:
                    # Handle non-dict params by placing them in the DEFAULT section
                    if "DEFAULT" not in config:
                        config["DEFAULT"] = {}
                    config["DEFAULT"][str(section)] = str(params)
            output = StringIO()
            config.write(output)
            return output.getvalue()
        except (configparser.Error, TypeError, ValueError, AttributeError) as e:
            raise EmitterError(f"INI emitting error: {e}") from e


class XMLEmitter(BaseEmitter):
    def emit(self, data: Dict[str, Any], **options: Any) -> str:
        try:
            root_name = options.get("root_name", "root")
            pretty = options.get("pretty", False)
            xml_bytes = dicttoxml.dicttoxml(
                data, custom_root=root_name, attr_type=False
            )
            if pretty:
                dom = parseString(xml_bytes)
                return dom.toprettyxml()
            else:
                return xml_bytes.decode()
        except Exception as e:
            raise EmitterError(f"XML emitting error: {e}") from e


EMITTER_CLASSES = {
    "json": JSONEmitter,
    "yaml": YAMLEmitter,
    "toml": TOMLEmitter,
    "ini": INIEmitter,
    "xml": XMLEmitter,
}
