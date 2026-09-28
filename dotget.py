"""Read a nested value with a dotted path."""
from __future__ import annotations


def dig(data: object, path: str, default: object = None) -> object:
    current = data
    for part in (path or "").split("."):
        if part == "":
            raise ValueError("路径里有空段")
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current
