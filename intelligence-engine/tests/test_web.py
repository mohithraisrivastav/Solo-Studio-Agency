"""Every page renders from stored records; forms enforce the same rules as the core."""
import json

from fastapi.testclient import TestClient

from iie.orchestrator import Engine
from iie.web.app import create_app

PAGES = ["/", "/discovery", "/invention", "/research", "/design", "/commercial", "/critique", "/prototype",
         "/activity", "/approvals", "/operator", "/settings"]


def test_all_pages_render_with_data(settings, transport, scripted):
    e = Engine(settings, provider=scripted, transport=transport)
    pid = e.create_project("web test", "full", budget_inr=200000, settings={"industries": ["bicycles and urban mobility cycling"]})
    e.run(pid)
    client = TestClient(create_app(engine=e))
    for p in PAGES:
        r = client.get(p)
        assert r.status_code == 200, (p, r.text[:500])
        r = client.get(p + f"?project={pid}")
        assert r.status_code == 200, p
    r = client.get(f"/project/{pid}")
    assert r.status_code == 200 and "Decisions" in r.text
    assert "Sealed oil-bath chain case" in client.get(f"/commercial?project={pid}").text
    assert client.get(f"/report/{pid}").text.startswith("# web test")
    art = e.db.one("artifacts", "project_id=? AND kind='cad_openscad'", (pid,))
    assert "CONCEPT GEOMETRY ONLY" in client.get(f"/artifact/{art['id']}").text


def test_forms_enforce_rules(settings, transport, scripted):
    e = Engine(settings, provider=scripted, transport=transport)
    pid = e.create_project("web forms", "full", budget_inr=200000, settings={"industries": ["bicycles and urban mobility cycling"]})
    e.run(pid)
    client = TestClient(create_app(engine=e))
    # direct evidence needs explicit human confirmation
    bad = client.post("/commercial/evidence", data={"project_id": pid, "kind": "interview", "counterparty": "A",
                                                     "occurred_on": "2026-10-01"})
    assert bad.status_code == 400
    ok = client.post("/commercial/evidence", data={"project_id": pid, "kind": "interview", "counterparty": "Asha, commuter",
                                                    "occurred_on": "2026-10-01", "confirm_human": "yes"}, follow_redirects=False)
    assert ok.status_code == 303
    assert e.db.one("direct_evidence", "project_id=?", (pid,))["recorded_by"] == "user"
    # recompute economics from edited inputs
    c = e.db.one("economics", "project_id=? AND scenario='base'", (pid,))
    inputs = dict(c["inputs"], price=4999)
    r = client.post("/commercial/recompute", data={"concept_id": c["concept_id"], "inputs": json.dumps(inputs)}, follow_redirects=False)
    assert r.status_code == 303
    assert e.db.one("economics", "concept_id=? AND created_by='user' AND scenario='base'", (c["concept_id"],))
    # experiment outcome becomes a learning record
    ex = e.db.one("experiments", "project_id=?", (pid,))
    client.post(f"/experiments/{ex['id']}/result", data={"status": "failed", "notes": "seal leaked"})
    assert e.db.one("learnings", "kind='outcome' AND ref_id=?", (ex["id"],))
    # manual concept entry
    client.post("/concepts", data={"project_id": pid, "title": "Hand idea", "principle": "magnets", "principle_class": "mechanical",
                                   "value_type": "convenience", "material_class": "metal", "business_model_class": "product_sale",
                                   "interaction_mode": "tool"})
    assert e.db.one("concepts", "title='Hand idea'")["created_by"] == "user"
