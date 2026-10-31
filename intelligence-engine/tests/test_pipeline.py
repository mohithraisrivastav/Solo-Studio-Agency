"""Full cycle with mocked research APIs and the scripted test double."""
from iie.orchestrator import Engine
from iie.report import project_report


def test_full_cycle_runs_every_stage(settings, transport, scripted):
    e = Engine(settings, provider=scripted, transport=transport)
    pid = e.create_project("Find an overlooked opportunity", "full", budget_inr=300000,
                           settings={"industries": ["bicycles and urban mobility cycling"]})
    res = e.run(pid)
    assert res["status"] == "complete", res
    jobs = {j["stage"]: j for j in e.status(pid)["jobs"]}
    assert jobs["research"]["status"] == "done"
    assert jobs["discovery"]["status"] == "done"
    assert jobs["comparison"]["status"] == "done"
    db = e.db
    assert db.scalar("SELECT COUNT(*) FROM sources WHERE project_id=?", (pid,)) >= 3
    assert db.scalar("SELECT COUNT(*) FROM claims WHERE project_id=? AND support='verified_quote'", (pid,)) >= 3
    # seven methods produced seven concepts; at least three families
    fams = {c["family_id"] for c in db.query("concepts", "project_id=?", (pid,))}
    assert len(fams) >= 3
    assert db.query("originality_checks", "project_id=?", (pid,))
    econ = db.query("economics", "project_id=? AND scenario='base'", (pid,))
    assert econ
    # the fake 'observed' seal cost reference was downgraded to an assumption
    mats = econ[0]["inputs"]["materials"]
    assert all(m["source"] == "assumption" for m in mats)
    # the critic's citation of a nonexistent source was downgraded to reasoning
    crit = db.query("critiques", "project_id=? AND objection LIKE '%Chain cases exist%'", (pid,))
    assert crit and crit[0]["basis"] == "reasoning"
    assert db.query("disagreements", "project_id=?", (pid,))
    assert db.query("experiments", "project_id=?", (pid,))
    decs = db.query("decisions", "project_id=?", (pid,))
    assert decs and all(d["verdict"] != "advance_to_prototype" for d in decs)  # no buyer evidence yet
    # demand answers dropped the fake claim id
    for a in db.query("demand_answers", "project_id=?", (pid,)):
        assert "clm_fake000000" not in a["claim_ids"]
    # artifacts written inside the engine workspace
    arts = db.query("artifacts", "project_id=? AND kind='cad_openscad'", (pid,))
    assert arts and "CONCEPT GEOMETRY ONLY" in open(arts[0]["path"]).read()
    text = project_report(db, pid)
    assert "## Decision" in text and "## Commercial analysis" in text
