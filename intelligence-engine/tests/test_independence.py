"""Test 9: Independence. No component reads excluded systems, personal memory, or old repositories."""
import ast
import sys
from pathlib import Path

import pytest

from iie.config import PACKAGE_DIR
from iie.guard import IndependenceViolation, SafeFS, check_url
from iie.orchestrator import Engine
from iie.research.http import Fetcher

ALLOWED_THIRD_PARTY = {"fastapi", "starlette", "uvicorn", "jinja2", "httpx", "pydantic", "multipart"}
EXCLUDED_WORDS = ("solo-studio", "solo_studio", "studio brain", "studio_brain", "studio-brain", "mohith os",
                  "mohith_os", "mohith-os", "studiobrain")


def _py_files():
    return [p for p in PACKAGE_DIR.rglob("*.py")]


def test_imports_are_stdlib_or_declared_dependencies():
    stdlib = set(sys.stdlib_module_names)
    for f in _py_files():
        tree = ast.parse(f.read_text())
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module.split(".")[0]]
            for n in names:
                assert n in stdlib or n in ALLOWED_THIRD_PARTY or n == "iie", f"{f.name} imports {n}"


def test_no_source_file_references_excluded_systems_outside_the_guard():
    for f in list(_py_files()) + list((PACKAGE_DIR / "web" / "templates").glob("*.html")):
        if f.name == "guard.py":
            continue
        low = f.read_text().lower()
        for w in EXCLUDED_WORDS:
            assert w not in low, f"{f} mentions '{w}'"


def test_safe_fs_blocks_everything_outside_engine_storage(tmp_path):
    fs = SafeFS(tmp_path / "home")
    for p in ["/etc/passwd", str(Path.home() / ".claude" / "memory.json"), str(tmp_path / "other.db"),
              str(tmp_path / "home" / ".." / "escape.txt")]:
        with pytest.raises(IndependenceViolation):
            fs.check(p)
    with pytest.raises(IndependenceViolation):
        fs.check(tmp_path / "home" / "ssa" / "notes.md")
    # even an approved private read cannot reach excluded systems
    for p in ["/data/Studio_Brain/graph.db", "/home/x/SSA/memory.md", "/home/x/mohith-os/x.json"]:
        with pytest.raises(IndependenceViolation):
            fs.grant_private_read(p)


def test_urls_to_excluded_systems_are_refused():
    for u in ["https://github.com/mohithraisrivastav/Solo-Studio-Agency", "https://www.notion.so/workspace/page",
              "https://chatgpt.com/share/abc", "https://claude.ai/chat/123"]:
        with pytest.raises(IndependenceViolation):
            check_url(u)
    for u in ["http://127.0.0.1:8000/", "http://10.0.0.5/x", "http://localhost/x"]:
        with pytest.raises(ValueError):
            check_url(u)
    assert check_url("https://api.openalex.org/works")


def test_fresh_database_has_no_attached_or_imported_data(settings):
    e = Engine(settings, offline=True)
    dbs = [r[1] for r in e.db.conn.execute("PRAGMA database_list").fetchall()]
    assert dbs == ["main"]
    assert e.db.meta("origin").startswith("fresh database")
    for table in ("projects", "sources", "claims", "concepts", "learnings", "decisions"):
        assert e.db.scalar(f"SELECT COUNT(*) FROM {table}") == 0
    assert Path(e.db.path).resolve().is_relative_to(settings.home.resolve())


def test_full_run_opens_only_engine_files(settings, transport, scripted):
    """Audit every file the engine opens during a complete cycle."""
    opened: list[str] = []

    def hook(event, args):
        if event == "open" and args and isinstance(args[0], (str, bytes, Path)):
            opened.append(str(args[0]))

    e = Engine(settings, provider=scripted, transport=transport)
    pid = e.create_project("independence audit", "full", budget_inr=100000,
                           settings={"industries": ["bicycles and urban mobility cycling"]})
    sys.addaudithook(hook)  # hooks cannot be removed; it only records
    marker = len(opened)
    e.run(pid)
    files = opened[marker:]
    home = str(settings.home.resolve())
    allowed_prefixes = (home, str(PACKAGE_DIR), sys.prefix, sys.base_prefix, "/usr/lib", "/usr/local/lib", "/proc", "/sys",
                        "/dev", "/etc/ssl", "/etc/pki", "/root/.ccr", "/usr/share")
    bad = [f for f in files if not f.startswith(allowed_prefixes) and not f.isdigit()]
    assert not bad, f"engine opened files outside its storage: {bad[:10]}"
    for f in files:
        low = f.lower()
        assert ".claude" not in low and "studio_brain" not in low and "mohith-os" not in low
