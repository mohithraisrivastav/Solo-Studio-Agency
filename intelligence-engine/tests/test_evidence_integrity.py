"""Test 7: Evidence integrity with research disabled, even when the model fabricates."""
import pytest

from conftest import LyingProvider
from iie.evidence import EvidencePermissionError, QuoteRef, add_claim, demand_level, record_direct_evidence
from iie.orchestrator import Engine


def test_offline_run_with_fabricating_model_creates_no_evidence(settings):
    e = Engine(settings, provider=LyingProvider(), offline=True)
    pid = e.create_project("Find an overlooked opportunity", "full", budget_inr=200000,
                           settings={"industries": ["bicycles and urban mobility cycling"]})
    res = e.run(pid)
    assert res["status"] == "complete"
    db = e.db
    assert db.scalar("SELECT COUNT(*) FROM sources") == 0, "no sources may appear without research"
    assert db.scalar("SELECT COUNT(*) FROM claims WHERE support='verified_quote'") == 0
    assert db.scalar("SELECT COUNT(*) FROM claims WHERE evidence_level>0") == 0
    assert db.scalar("SELECT COUNT(*) FROM direct_evidence") == 0
    assert db.scalar("SELECT COUNT(*) FROM research_gaps") > 0, "gaps must be recorded"
    # fabricated opportunity citing a made-up claim is not treated as supported
    for o in db.query("opportunities", "project_id=?", (pid,)):
        assert o["status"] == "unsupported" and o["claim_ids"] == []
    jobs = {j["stage"]: j["status"] for j in e.status(pid)["jobs"]}
    assert jobs["research"] == "incomplete" and jobs["discovery"] == "incomplete"
    assert demand_level(db, pid) == (0, "no verified evidence; demand is an assumption")
    for d in db.query("decisions", "project_id=?", (pid,)):
        assert d["verdict"] not in ("advance_to_prototype",)


def test_fabricated_price_reference_is_downgraded(settings, transport):
    e = Engine(settings, provider=LyingProvider(), transport=transport)
    pid = e.create_project("Evaluate a concept", "commercial", budget_inr=100000,
                           settings={"concept": {"title": "Test case", "core_principle": "seal water out"}})
    e.run(pid)
    base = e.db.one("economics", "project_id=? AND scenario='base'", (pid,))
    assert base["inputs"]["price_source"] == "assumption"
    assert all(m["source"] == "assumption" for m in base["inputs"]["materials"])
    codes = [f["code"] for f in base["findings"]["items"]]
    assert "PRICE_UNSUPPORTED" in codes


def test_quotes_must_exist_in_source(settings):
    e = Engine(settings, offline=True)
    pid = e.create_project("q", "discovery")
    with e.db.tx():
        sid = e.db.insert("sources", {"project_id": pid, "url": "https://example.org/a", "title": "A page",
                                      "content": "Chains cost about ₹900 in Pune.", "source_type": "web_page"})
    ok, _ = add_claim(e.db, pid, "price", "price_observation", "research_investigator", [QuoteRef(sid, "cost about ₹900 in Pune")])
    bad, probs = add_claim(e.db, pid, "price", "price_observation", "research_investigator", [QuoteRef(sid, "cost about ₹400 in Pune")])
    assert e.db.get("claims", ok)["support"] == "verified_quote"
    assert e.db.get("claims", bad)["support"] == "source_unverified" and e.db.get("claims", bad)["evidence_level"] == 0
    assert probs


@pytest.mark.parametrize("actor", ["commercial_analyst", "buyer_researcher", "operator", "model", "decision_director"])
def test_only_the_user_can_record_buyer_evidence(settings, actor):
    e = Engine(settings, offline=True)
    pid = e.create_project("q", "discovery")
    with pytest.raises(EvidencePermissionError):
        record_direct_evidence(e.db, pid, "paid_order", actor, "Asha Rao", "2026-10-01", amount=2500, currency="INR")


def test_user_evidence_climbs_the_ladder_with_rules(settings):
    e = Engine(settings, offline=True)
    pid = e.create_project("q", "discovery")
    record_direct_evidence(e.db, pid, "interview", "user", "Ravi K, commuter", "2026-10-02")
    assert demand_level(e.db, pid)[0] == 2
    with pytest.raises(ValueError):  # payment needs an amount
        record_direct_evidence(e.db, pid, "deposit", "user", "Ravi K, commuter", "2026-10-03")
    with pytest.raises(ValueError):  # repeat order needs an earlier order
        record_direct_evidence(e.db, pid, "repeat_order", "user", "New Person", "2026-10-03", amount=10, currency="INR")
    with pytest.raises(ValueError):  # future dates refused
        record_direct_evidence(e.db, pid, "interview", "user", "X", "2099-01-01")
    record_direct_evidence(e.db, pid, "deposit", "user", "Ravi K, commuter", "2026-10-04", amount=500, currency="INR")
    assert demand_level(e.db, pid)[0] == 4
