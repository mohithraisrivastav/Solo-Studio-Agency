"""Independence and safety guard.

Hard rules enforced in code:

1. File access is limited to this engine's data home and its own package
   directory. Anything else raises IndependenceViolation. Users can grant a
   single private file read through an approved ``access_private_data`` action,
   but excluded systems stay blocked even with approval.
2. URLs that point at excluded personal systems are refused, whatever the
   approval state. Integration with them is out of scope.
3. Local network targets are refused for research fetches (SSRF protection).
   Only configured model endpoints may use localhost.

The marker lists below exist only to block access. Nothing in this package
reads from these systems.
"""
from __future__ import annotations

import ipaddress
import re
from pathlib import Path
from urllib.parse import urlparse

from .config import PACKAGE_DIR, PROJECT_ROOT


class IndependenceViolation(PermissionError):
    """Raised when code tries to touch an excluded system or a path outside the engine."""


# Substring markers (lower-case) for excluded personal systems.
EXCLUDED_MARKERS: tuple[str, ...] = (
    "solo-studio-agency",
    "solo_studio_agency",
    "solostudioagency",
    "studio-brain",
    "studio_brain",
    "studiobrain",
    "mohith-os",
    "mohith_os",
    "mohithos",
    "mohithraisrivastav",
)

# Exact path components (lower-case) that are refused for private file access.
EXCLUDED_COMPONENTS: frozenset[str] = frozenset(
    {"ssa", "brain", "studio brain", "mohith os", ".claude", "claude_memory", "memories", ".chatgpt"}
)

# URL markers for personal memory, chat history, and old repository hosts.
EXCLUDED_URL_MARKERS: tuple[str, ...] = EXCLUDED_MARKERS + (
    "notion.so",
    "notion.site",
    "chatgpt.com",
    "chat.openai.com",
    "claude.ai",
)

_EXCLUDED_COMPONENT_RE = re.compile(r"^(ssa)([-_ .].*)?$", re.IGNORECASE)


def _has_excluded_marker(text: str) -> str | None:
    low = text.lower()
    for m in EXCLUDED_MARKERS:
        if m in low:
            return m
    return None


def _excluded_component(parts: tuple[str, ...]) -> str | None:
    for part in parts:
        low = part.lower()
        if low in EXCLUDED_COMPONENTS or _EXCLUDED_COMPONENT_RE.match(low):
            return part
    return None


class SafeFS:
    """All engine file access goes through this object."""

    def __init__(self, home: Path):
        self.home = Path(home).resolve()
        self.allowed_roots = (self.home, PACKAGE_DIR.resolve())
        self._granted: set[Path] = set()

    def check(self, path: str | Path, write: bool = False) -> Path:
        p = Path(path).expanduser()
        if not p.is_absolute():
            p = self.home / p
        p = p.resolve()
        roots = (self.home,) if write else self.allowed_roots
        for root in roots:
            try:
                rel = p.relative_to(root)
            except ValueError:
                continue
            marker = _has_excluded_marker(str(rel)) or _excluded_component(rel.parts)
            if marker:
                raise IndependenceViolation(f"Path {p} touches an excluded system marker '{marker}'.")
            return p
        if not write and p in self._granted:
            return p
        raise IndependenceViolation(
            f"Path {p} is outside the engine's own storage. Access needs an approved access_private_data action."
        )

    def grant_private_read(self, path: str | Path) -> Path:
        """Called only by the approval gate after a user approves a private file read."""
        p = Path(path).expanduser().resolve()
        marker = _has_excluded_marker(str(p)) or _excluded_component(p.parts)
        if marker:
            raise IndependenceViolation(
                f"{p} belongs to an excluded system ('{marker}'). Integration is out of scope, even with approval."
            )
        self._granted.add(p)
        return p

    def read_text(self, path: str | Path) -> str:
        return self.check(path).read_text(encoding="utf-8")

    def write_text(self, path: str | Path, text: str) -> Path:
        p = self.check(path, write=True)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p


def check_url(url: str, allow_local: bool = False) -> str:
    """Validate an outbound URL. Raises IndependenceViolation or ValueError."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Only http(s) URLs are allowed, got '{parsed.scheme}'.")
    low = url.lower()
    for m in EXCLUDED_URL_MARKERS:
        if m in low:
            raise IndependenceViolation(f"URL refers to an excluded system ('{m}'): {url}")
    host = (parsed.hostname or "").lower()
    if not host:
        raise ValueError("URL has no host.")
    if not allow_local:
        if host in ("localhost",) or host.endswith(".local") or host.endswith(".internal"):
            raise ValueError(f"Local host '{host}' is not allowed for research fetches.")
        try:
            ip = ipaddress.ip_address(host)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                raise ValueError(f"Private address '{host}' is not allowed for research fetches.")
        except ValueError as e:
            if "not allowed" in str(e):
                raise
    return url


def project_root() -> Path:
    return PROJECT_ROOT
