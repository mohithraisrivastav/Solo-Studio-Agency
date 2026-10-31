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


def test_resume_does_not_duplicate_rule_claims(settings, transport):
    """Claim extraction pauses for the operator; rule-based claims must not be created twice on resume."""
    e = Engine(settings, transport=transport)
    e.provider = OperatorProvider(e.db)
    pid = e.create_project("Find an opportunity", "discovery", settings={"industries": ["bicycles and urban mobility cycling"]})
    r = e.run(pid)
    assert r["status"] == "waiting_operator" and r["stage"] == "research"
    n1 = e.db.scalar("SELECT COUNT(*) FROM claims WHERE created_by='extractor'")
    e.run(pid)
    assert e.db.scalar("SELECT COUNT(*) FROM claims WHERE created_by='extractor'") == n1


def test_money_sentences_are_classified_conservatively(settings):
    from iie.context import Ctx
    from iie.research.engine import deterministic_claims
    e = Engine(settings, offline=True)
    pid = e.create_project("q", "discovery")
    p = e.db.get("projects", pid)
    ctx = Ctx(e.db, e.settings, e.provider, e.fetcher, e.connectors, e.fs, e.tools, p, None)
    with e.db.tx():
        sid = e.db.insert("sources", {"project_id": pid, "url": "https://example.org/x", "title": "Mixed money facts",
                                      "source_type": "news", "content":
                                      "The company started with INR 50,000 investment. "
                                      "The plywood is priced at ₹95 per sq ft in Pune. "
                                      "The furniture market is worth USD 25 billion this year."})
    deterministic_claims(ctx, e.db.get("sources", sid))
    types = {c["text"].split(" ")[1]: c["claim_type"] for c in e.db.query("claims", "project_id=?", (pid,))}
    assert types["company"] == "other"
    assert types["plywood"] == "price_observation"
    assert types["furniture"] == "market_size"
