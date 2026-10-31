"""Operator queue: pauses, schema validation, named answers, research bundles."""
import pytest

from iie.llm import OperatorProvider, answer_operator_task
from iie.orchestrator import Engine
from iie.schema import SchemaError


def test_operator_answers_must_be_named_and_valid(settings):
    e = Engine(settings, offline=True)
    e.provider = OperatorProvider(e.db)
    pid = e.create_project("q", "invention")
    r = e.run(pid)
    tid = r["tasks"][0]
    with pytest.raises(ValueError):
        answer_operator_task(e.db, tid, {"framing": "f", "queries": [{"text": "x", "purpose": "problem"}]}, "")
    with pytest.raises(SchemaError):
        answer_operator_task(e.db, tid, {"framing": "f"}, "tester")
    answer_operator_task(e.db, tid, {"framing": "f", "queries": [{"text": "x", "purpose": "problem"}]}, "tester")
    assert e.db.get("operator_tasks", tid)["answered_by"] == "tester"


def test_research_bundle_import_validates_sources(settings):
    settings.operator_research = True
    e = Engine(settings, offline=True)
    e.provider = OperatorProvider(e.db)
    pid = e.create_project("q", "invention")
    r = e.run(pid)
    answer_operator_task(e.db, r["tasks"][0], {"framing": "f", "queries": [{"text": "chain rust", "purpose": "problem"}]}, "tester")
    r = e.run(pid)
    assert r["status"] == "waiting_operator"
    t = e.db.get("operator_tasks", r["tasks"][0])
    assert "research_bundle" in t["purpose"]
    bundle = {"sources": [
        {"url": "https://example.org/real", "title": "Chains rust fast", "source_type": "forum", "retrieved_at": "2026-10-31",
         "retrieval_method": "web_search_snippet", "content": "My chain rusts every monsoon and costs ₹1,200 to replace."},
        {"url": "https://github.com/mohithraisrivastav/Solo-Studio-Agency", "title": "x", "source_type": "web_page",
         "retrieved_at": "2026-10-31", "retrieval_method": "x", "content": "excluded system content here"},
        {"url": "https://example.org/future", "title": "f", "source_type": "news", "retrieved_at": "2099-01-01",
         "retrieval_method": "x", "content": "future dated content is refused"},
    ]}
    answer_operator_task(e.db, t["id"], bundle, "tester")
    e.run(pid)
    srcs = e.db.query("sources", "project_id=?", (pid,))
    assert [s["url"] for s in srcs] == ["https://example.org/real"]
    assert srcs[0]["connector"] == "operator_bundle:tester"
