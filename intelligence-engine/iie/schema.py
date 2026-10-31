"""A small JSON-schema subset validator for model and operator outputs.

Supports: type (object, array, string, number, integer, boolean, null), properties,
required, items, enum, minItems, maxItems, minimum, maximum. Unknown keys are allowed.
"""
from __future__ import annotations

from typing import Any


class SchemaError(ValueError):
    pass


_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
    "null": type(None),
}


def _is_type(value: Any, t: str) -> bool:
    if t == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if t == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    return isinstance(value, _TYPES[t])


def validate(value: Any, schema: dict, path: str = "$") -> None:
    t = schema.get("type")
    if t is not None:
        types = t if isinstance(t, list) else [t]
        if not any(_is_type(value, x) for x in types):
            raise SchemaError(f"{path}: expected {t}, got {type(value).__name__}")
    if "enum" in schema and value not in schema["enum"]:
        raise SchemaError(f"{path}: {value!r} not in {schema['enum']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise SchemaError(f"{path}: {value} < minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            raise SchemaError(f"{path}: {value} > maximum {schema['maximum']}")
    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                raise SchemaError(f"{path}: missing required '{req}'")
        for k, sub in schema.get("properties", {}).items():
            if k in value and value[k] is not None:
                validate(value[k], sub, f"{path}.{k}")
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise SchemaError(f"{path}: needs at least {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise SchemaError(f"{path}: allows at most {schema['maxItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                validate(item, schema["items"], f"{path}[{i}]")


def obj(required: list[str] | None = None, **props: dict) -> dict:
    return {"type": "object", "properties": props, "required": required or list(props)}


def arr(items: dict, min_items: int = 0, max_items: int | None = None) -> dict:
    s: dict[str, Any] = {"type": "array", "items": items, "minItems": min_items}
    if max_items is not None:
        s["maxItems"] = max_items
    return s


STR = {"type": "string"}
NUM = {"type": "number"}
INT = {"type": "integer"}
BOOL = {"type": "boolean"}
STRS = {"type": "array", "items": {"type": "string"}}
