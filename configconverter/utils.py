"""
Utility functions for ConfigConverter.

Author: Ankit Aglawe <aglawe.ankit@gmail.com>
License: MIT
"""


def infer_format(filename: str) -> str:
    """
    Infer the format of a file based on its extension.

    Args:
        filename (str): The filename to infer the format from.

    Returns:
        str or None: The inferred format or None if unknown.
    """
    ext = filename.rsplit(".", 1)[-1].lower()
    return {
        "json": "json",
        "yaml": "yaml",
        "yml": "yaml",
        "toml": "toml",
        "ini": "ini",
        "conf": "ini",
        "cfg": "ini",
        "xml": "xml",
    }.get(ext)
