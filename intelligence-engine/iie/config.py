"""Fresh configuration for this engine only.

The data home defaults to ``<project>/var`` or ``$IIE_HOME``. Nothing here reads
configuration from any other system. Credentials come only from environment
variables at runtime and are never written to the database or config file.
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parent

DEFAULT_CONNECTORS = [
    "wikipedia",
    "openalex",
    "crossref",
    "arxiv",
    "semantic_scholar",
    "stackexchange",
    "hackernews",
    "worldbank",
    "searxng",
    "brave",
    "patentsview",
    "operator_bundle",
]

# Credentials are read from these environment variables only.
SECRET_ENV = {
    "brave": "IIE_BRAVE_API_KEY",
    "patentsview": "IIE_PATENTSVIEW_API_KEY",
    "searxng": "IIE_SEARXNG_URL",
    "smtp_host": "IIE_SMTP_HOST",
    "smtp_user": "IIE_SMTP_USER",
    "smtp_password": "IIE_SMTP_PASSWORD",
    "openai_compat_key": "IIE_OPENAI_COMPAT_KEY",
}


def default_home() -> Path:
    env = os.environ.get("IIE_HOME")
    return Path(env).expanduser().resolve() if env else (PROJECT_ROOT / "var").resolve()


@dataclass
class Settings:
    home: Path = field(default_factory=default_home)
    # Model provider: auto | ollama | openai_compat | operator | none
    model_provider: str = "auto"
    ollama_url: str = "http://127.0.0.1:11434"
    ollama_model: str | None = None
    ollama_embed_model: str | None = None
    openai_compat_url: str | None = None
    openai_compat_model: str | None = None
    # Research
    research_enabled: bool = True
    connectors: list[str] = field(default_factory=lambda: list(DEFAULT_CONNECTORS))
    operator_research: bool = False  # allow an operator to supply source bundles
    max_queries_per_stage: int = 14
    max_sources_per_query: int = 5
    saturation_window: int = 3
    http_timeout: float = 20.0
    user_agent: str = "IndependentIntelligenceEngine/0.1 (local research tool; respects robots.txt)"
    contact_email: str | None = None  # sent to OpenAlex/Crossref polite pools if set
    # Commercial defaults (all flagged as assumptions when used)
    currency: str = "INR"
    founder_hourly_value_inr: float = 600.0
    equipment_threshold_inr: float = 50000.0
    premium_price_threshold_inr: float = 200000.0
    max_revisits: int = 2

    @property
    def db_path(self) -> Path:
        return self.home / "iie.db"

    @property
    def workspace(self) -> Path:
        return self.home / "workspace"

    @property
    def cache_dir(self) -> Path:
        return self.home / "cache"

    @property
    def config_path(self) -> Path:
        return self.home / "config.json"

    def ensure_dirs(self) -> None:
        for p in (self.home, self.workspace, self.cache_dir, self.home / "logs", self.home / "exports"):
            p.mkdir(parents=True, exist_ok=True)

    def secret(self, name: str) -> str | None:
        env = SECRET_ENV.get(name)
        return os.environ.get(env) if env else None

    def to_json(self) -> dict:
        d = asdict(self)
        d["home"] = str(self.home)
        return d

    def save(self) -> None:
        self.ensure_dirs()
        data = self.to_json()
        data.pop("home", None)
        self.config_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_settings(home: Path | None = None) -> Settings:
    s = Settings(home=(home or default_home()))
    if s.config_path.exists():
        data = json.loads(s.config_path.read_text(encoding="utf-8"))
        for k, v in data.items():
            if hasattr(s, k) and k != "home":
                setattr(s, k, v)
    s.ensure_dirs()
    return s
