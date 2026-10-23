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


def first_path(data: object, paths: list[str]) -> str:
    for path in paths:
        if has_path(data, path):
            return path
    return ""


def path_count(data: object, paths: list[str]) -> int:
    return sum(1 for path in paths if has_path(data, path))


def missing_paths(data: object, paths: list[str]) -> list[str]:
    return [path for path in paths if not has_path(data, path)]


def present_paths(data: object, paths: list[str]) -> list[str]:
    return [path for path in paths if has_path(data, path)]


def any_path(data: object, paths: list[str]) -> bool:
    return path_count(data, paths) > 0


def all_paths(data: object, paths: list[str]) -> bool:
    if not paths:
        return False
    return path_count(data, paths) == len(paths)


def missing_count(data: object, paths: list[str]) -> int:
    return len(missing_paths(data, paths))


def present_count(data: object, paths: list[str]) -> int:
    return len(present_paths(data, paths))
