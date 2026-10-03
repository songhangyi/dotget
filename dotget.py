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


def dig_all(data: object, paths: list[str], default: object = None) -> dict[str, object]:
    return {path: dig(data, path, default) for path in paths}


def has_path(data: object, path: str) -> bool:
    missing = object()
    return dig(data, path, missing) is not missing
