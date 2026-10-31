"""HTTP fetching for research: robots.txt checks, disk cache, size limits, polite retries.

All fetched content is treated as untrusted data.
"""
from __future__ import annotations

import json
import time
import urllib.robotparser
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urlparse

import httpx

from ..guard import check_url
from ..util import now_iso, sha256

MAX_BYTES = 3_000_000
CACHE_TTL_S = 24 * 3600


class FetchError(RuntimeError):
    def __init__(self, message: str, kind: str = "error", host: str | None = None):
        super().__init__(message)
        self.kind = kind  # network_blocked | http_error | robots | too_large | timeout | error
        self.host = host


class Fetcher:
    def __init__(self, settings, transport: httpx.BaseTransport | None = None, use_cache: bool = True,
                 offline: bool = False):
        self.settings = settings
        self.use_cache = use_cache
        self.offline = offline
        self.cache_dir: Path = settings.cache_dir / "http"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.client = httpx.Client(
            timeout=settings.http_timeout,
            headers={"User-Agent": settings.user_agent, "Accept-Language": "en"},
            follow_redirects=True,
            transport=transport,
        )
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self.calls = 0

    def close(self) -> None:
        self.client.close()

    def _cache_path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    def _cached(self, key: str) -> dict | None:
        if not self.use_cache:
            return None
        p = self._cache_path(key)
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                return None
            if time.time() - data.get("ts", 0) < CACHE_TTL_S:
                return data
        return None

    def _store(self, key: str, data: dict) -> None:
        if self.use_cache:
            data["ts"] = time.time()
            self._cache_path(key).write_text(json.dumps(data), encoding="utf-8")

    def allowed_by_robots(self, url: str) -> bool:
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        if base not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                r = self.client.get(base + "/robots.txt", timeout=10)
                if r.status_code >= 400:
                    self._robots[base] = None  # no robots file: allowed
                else:
                    rp.parse(r.text.splitlines())
                    self._robots[base] = rp
            except httpx.HTTPError:
                self._robots[base] = None
        rp = self._robots[base]
        return True if rp is None else rp.can_fetch(self.settings.user_agent, url)

    def get(self, url: str, params: dict | None = None, headers: dict | None = None,
            check_robots: bool = False) -> dict:
        """Return {'status','text','url','content_type','retrieved_at'}; raises FetchError."""
        check_url(url)
        full = url + ("?" + urlencode(params, doseq=True) if params else "")
        key = sha256(full + json.dumps(headers or {}, sort_keys=True))
        hit = self._cached(key)
        if hit:
            return hit
        host = urlparse(url).hostname
        if self.offline:
            raise FetchError("research is disabled (offline mode)", "network_blocked", host)
        if check_robots and not self.allowed_by_robots(url):
            raise FetchError(f"robots.txt disallows fetching {url}", "robots", host)
        last_err: Exception | None = None
        for attempt in range(3):
            try:
                self.calls += 1
                with self.client.stream("GET", url, params=params, headers=headers) as r:
                    chunks, size = [], 0
                    for chunk in r.iter_bytes():
                        size += len(chunk)
                        if size > MAX_BYTES:
                            raise FetchError(f"response larger than {MAX_BYTES} bytes", "too_large", host)
                        chunks.append(chunk)
                    body = b"".join(chunks)
                    if r.status_code in (429, 500, 502, 503, 504) and attempt < 2:
                        time.sleep(1.5 * (attempt + 1))
                        continue
                    if r.status_code >= 400:
                        raise FetchError(f"HTTP {r.status_code} from {host}", "http_error", host)
                    data = {
                        "status": r.status_code,
                        "text": body.decode(r.encoding or "utf-8", errors="replace"),
                        "url": str(r.url),
                        "content_type": r.headers.get("content-type", ""),
                        "retrieved_at": now_iso(),
                    }
                    self._store(key, data)
                    return data
            except FetchError:
                raise
            except httpx.ProxyError as e:
                raise FetchError(f"network policy or proxy refused the connection to {host}", "network_blocked",
                                 host) from e
            except httpx.ConnectError as e:
                raise FetchError(f"cannot connect to {host}: {e}", "network_blocked", host) from e
            except httpx.TimeoutException as e:
                last_err = e
                continue
            except httpx.HTTPError as e:
                last_err = e
                break
        raise FetchError(f"request to {host} failed: {type(last_err).__name__}", "timeout", host)

    def get_json(self, url: str, params: dict | None = None, headers: dict | None = None) -> Any:
        data = self.get(url, params, headers)
        try:
            return json.loads(data["text"])
        except ValueError as e:
            raise FetchError(f"invalid JSON from {urlparse(url).hostname}", "http_error") from e
