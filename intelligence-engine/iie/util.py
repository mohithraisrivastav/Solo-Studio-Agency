"""Small shared helpers: ids, time, hashing, JSON."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import uuid
from typing import Any


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today() -> _dt.date:
    return _dt.datetime.now(_dt.timezone.utc).date()


def parse_date(value: str | None) -> _dt.date | None:
    """Parse ISO-like dates ('2024', '2024-05', '2024-05-02', full timestamps)."""
    if not value:
        return None
    v = str(value).strip()
    try:
        if len(v) == 4 and v.isdigit():
            return _dt.date(int(v), 1, 1)
        if len(v) == 7 and v[4] == "-":
            return _dt.date(int(v[:4]), int(v[5:7]), 1)
        return _dt.date.fromisoformat(v[:10])
    except ValueError:
        return None


def sha256(text: str | bytes) -> str:
    if isinstance(text, str):
        text = text.encode("utf-8", "replace")
    return hashlib.sha256(text).hexdigest()


def dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, default=str)


def loads(text: str | None, default: Any = None) -> Any:
    if text is None or text == "":
        return default
    try:
        return json.loads(text)
    except (TypeError, ValueError):
        return default


def clip(text: str | None, n: int) -> str:
    text = text or ""
    return text if len(text) <= n else text[: n - 1] + "…"


def money(amount: float | None, currency: str = "INR") -> str:
    """Format money with its currency. INR uses lakh/crore grouping."""
    if amount is None:
        return "n/a"
    if amount != amount or amount in (float("inf"), float("-inf")):  # NaN or inf
        return "not reachable"
    sign = "-" if amount < 0 else ""
    a = abs(amount)
    if currency == "INR":
        whole = f"{a:.0f}"
        if len(whole) > 3:
            head, tail = whole[:-3], whole[-3:]
            groups = []
            while len(head) > 2:
                groups.insert(0, head[-2:])
                head = head[:-2]
            if head:
                groups.insert(0, head)
            whole = ",".join(groups) + "," + tail
        return f"{sign}₹{whole}"
    return f"{sign}{currency} {a:,.0f}"
