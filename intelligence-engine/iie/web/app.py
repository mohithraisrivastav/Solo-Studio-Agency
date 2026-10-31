"""Web interface. Every page reads stored records; nothing is animated or simulated."""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .. import approvals
from ..commercial.economics import EconInputs, run_scenarios, sensitivity
from ..config import PACKAGE_DIR, Settings
from ..evidence import DIRECT_KINDS, age_label, freshness, level_label, record_direct_evidence
from ..guard import IndependenceViolation
from ..invention.methods import AXES
from ..llm import answer_operator_task
from ..llm.hardware import benchmark_ollama, choose_default, detect_hardware
from ..memory import progress_metrics
from ..orchestrator import Engine
from ..report import _latest, project_report
from ..research.connectors import fetch_page
from ..research.engine import import_bundle, store_doc
from ..roles import ROLES
from ..stages import STAGES, WORKFLOWS
from ..util import clip, money, now_iso

NAV = [
    ("/", "Portfolio"), ("/discovery", "Discovery Lab"), ("/invention", "Invention Lab"), ("/research", "Research Desk"),
    ("/design", "Design Workshop"), ("/commercial", "Commercial Studio"), ("/critique", "Critical Review"),
    ("/prototype", "Prototype Planner"), ("/activity", "Agent Activity"), ("/approvals", "Approvals"),
    ("/operator", "Operator Queue"), ("/settings", "Settings"),
]


def create_app(settings: Settings | None = None, engine: Engine | None = None) -> FastAPI:
    eng = engine or Engine(settings)
    eng.recover()
    app = FastAPI(title="Independent Intelligence Engine")
    app.state.engine = eng
    app.state.pool = ThreadPoolExecutor(max_workers=2)
    tpl = Jinja2Templates(directory=str(PACKAGE_DIR / "web" / "templates"))
    tpl.env.filters.update(money=money, clip=clip, level=level_label, j=lambda x: json.dumps(x, indent=2, ensure_ascii=False, default=str))
    app.mount("/static", StaticFiles(directory=str(PACKAGE_DIR / "web" / "static")), name="static")
    db = eng.db

    def render(request: Request, name: str, **ctx):
        pid = request.query_params.get("project")
        base = {"nav": NAV, "path": request.url.path, "projects": db.query("projects", order="updated_at DESC"),
                "pid": pid, "provider": eng.provider.describe(),
                "pending_ops": db.scalar("SELECT COUNT(*) FROM operator_tasks WHERE status='pending'"),
                "pending_apr": db.scalar("SELECT COUNT(*) FROM approvals WHERE status='pending'")}
        return tpl.TemplateResponse(request, name, {**base, **ctx})

    def pfilter(request: Request) -> tuple[str, tuple]:
        pid = request.query_params.get("project")
        return ("project_id=?", (pid,)) if pid else ("1=1", ())

    def concept_title(cid: str | None) -> str:
        c = db.get("concepts", cid) if cid else None
        return c["title"] if c else ""

    def start(pid: str) -> None:
        app.state.pool.submit(eng.run, pid)

    # ---------------------------------------------------------- portfolio
    @app.get("/", response_class=HTMLResponse)
    def portfolio(request: Request):
        rows = []
        for c in db.query("concepts", "status IN ('shortlisted','active')", order="created_at DESC"):
            base = db.one("economics", "concept_id=? AND scenario='base' ORDER BY created_at DESC", (c["id"],))
            dec = db.one("decisions", "concept_id=? ORDER BY created_at DESC", (c["id"],))
            orc = db.one("originality_checks", "concept_id=? ORDER BY created_at DESC", (c["id"],))
            lvl = db.scalar("SELECT MAX(level) FROM direct_evidence WHERE concept_id=? OR (project_id=? AND concept_id IS NULL)",
                            (c["id"], c["project_id"])) or (1 if db.scalar("SELECT COUNT(*) FROM claims WHERE project_id=? AND evidence_level>=1", (c["project_id"],)) else 0)
            rows.append({"c": c, "econ": base, "dec": dec, "orc": orc, "level": lvl})
        return render(request, "portfolio.html", rows=rows, metrics=progress_metrics(db), workflows=list(WORKFLOWS))

    @app.post("/projects")
    def new_project(question: str = Form(...), workflow: str = Form("full"), mode: str = Form("fresh"),
                    budget: str = Form(""), industries: str = Form(""), seed: str = Form(""), run_now: str = Form("")):
        st = {}
        if industries.strip():
            st["industries"] = [x.strip() for x in industries.split(",") if x.strip()]
        if seed.strip():
            st["seed"] = int(seed)
        pid = eng.create_project(question, workflow, mode, None, float(budget) if budget.strip() else None, st)
        if run_now:
            start(pid)
        return RedirectResponse(f"/project/{pid}", 303)

    @app.get("/project/{pid}", response_class=HTMLResponse)
    def project(request: Request, pid: str):
        p = db.get("projects", pid)
        if not p:
            raise HTTPException(404)
        jobs = db.query("jobs", "project_id=?", (pid,), "created_at")
        stages = [STAGES[k] for k in WORKFLOWS[p["workflow"]]]
        return render(request, "project.html", p=p, jobs=jobs, stages=stages,
                      decisions=_latest(db.query("decisions", "project_id=?", (pid,), "created_at")),
                      ops=db.query("operator_tasks", "project_id=? AND status='pending'", (pid,)),
                      aprs=db.query("approvals", "project_id=? AND status='pending'", (pid,)), concept_title=concept_title)

    @app.post("/project/{pid}/run")
    def run_project(pid: str):
        start(pid)
        return RedirectResponse(f"/project/{pid}", 303)

    @app.get("/report/{pid}", response_class=PlainTextResponse)
    def report(pid: str):
        return project_report(db, pid)

    # ---------------------------------------------------------- discovery
    @app.get("/discovery", response_class=HTMLResponse)
    def discovery(request: Request):
        w, a = pfilter(request)
        return render(request, "discovery.html", opps=db.query("opportunities", w, a, "created_at DESC"))

    # ---------------------------------------------------------- invention
    @app.get("/invention", response_class=HTMLResponse)
    def invention(request: Request):
        w, a = pfilter(request)
        concepts = db.query("concepts", w, a, "family_id, created_at")
        fams: dict[str, list] = {}
        for c in concepts:
            fams.setdefault(c.get("family_id") or c["id"], []).append(c)
        return render(request, "invention.html", fams=fams, overlaps=db.query("concept_overlaps", w, a),
                      axes=AXES, concept_title=concept_title)

    @app.post("/concepts")
    def add_concept(project_id: str = Form(...), title: str = Form(...), principle: str = Form(...),
                    how_it_works: str = Form(""), user_value: str = Form(""), target_buyer: str = Form(""),
                    business_model: str = Form(""), principle_class: str = Form(...), value_type: str = Form(...),
                    material_class: str = Form(...), business_model_class: str = Form(...), interaction_mode: str = Form(...)):
        axes = {"principle_class": principle_class, "value_type": value_type, "material_class": material_class,
                "business_model_class": business_model_class, "interaction_mode": interaction_mode}
        with db.tx():
            db.insert("concepts", {"project_id": project_id, "title": title, "method": "user_supplied", "principle": principle,
                                   "user_value": user_value, "business_model": business_model, "axes": axes, "status": "active",
                                   "detail": {"how_it_works": how_it_works, "target_buyer": target_buyer, "core_principle": principle},
                                   "generation_mode": "user", "created_by": "user"})
            db.log(project_id, None, "user", "concept_added", title)
        return RedirectResponse(f"/invention?project={project_id}", 303)

    # ---------------------------------------------------------- research
    @app.get("/research", response_class=HTMLResponse)
    def research(request: Request):
        w, a = pfilter(request)
        srcs = db.query("sources", w, a, "created_at DESC")
        claims = db.query("claims", w, a, "evidence_level DESC, created_at DESC")
        cs = {}
        for r in db.conn.execute("SELECT claim_id, source_id, verified FROM claim_sources").fetchall():
            cs.setdefault(r[0], []).append((r[1], r[2]))
        src_by = {s["id"]: s for s in srcs}
        fresh = {}
        for c in claims:
            s = src_by.get((cs.get(c["id"]) or [(None,)])[0][0])
            st, age = freshness(c["claim_type"], (s or {}).get("published_at"), (s or {}).get("retrieved_at"))
            fresh[c["id"]] = f"{st} ({age_label(age)})"
        return render(request, "research.html", sources=srcs, claims=claims, cs=cs, fresh=fresh,
                      contradictions=db.query("contradictions", w, a), gaps=db.query("research_gaps", w, a, "created_at DESC"))

    @app.post("/research/bundle")
    def research_bundle(project_id: str = Form(...), bundle: str = Form(...), imported_by: str = Form(...)):
        from ..context import Ctx
        p = db.get("projects", project_id)
        ctx = Ctx(db, eng.settings, eng.provider, eng.fetcher, eng.connectors, eng.fs, eng.tools, p, None)
        import_bundle(ctx, json.loads(bundle), imported_by, "manual")
        return RedirectResponse(f"/research?project={project_id}", 303)

    @app.post("/research/fetch")
    def research_fetch(project_id: str = Form(...), url: str = Form(...), source_type: str = Form("web_page")):
        from ..context import Ctx
        p = db.get("projects", project_id)
        ctx = Ctx(db, eng.settings, eng.provider, eng.fetcher, eng.connectors, eng.fs, eng.tools, p, None)
        try:
            doc = fetch_page(eng.fetcher, url, source_type)
            store_doc(ctx, doc, "web_page", url, "page_fetch")
            ctx.log("research_investigator", "tool_call", f"fetched {url}", tool="fetch_page")
        except Exception as ex:  # noqa: BLE001
            with db.tx():
                db.insert("research_gaps", {"project_id": project_id, "connector": "web_page", "query": url, "reason": str(ex)})
        return RedirectResponse(f"/research?project={project_id}", 303)

    # ---------------------------------------------------------- design
    @app.get("/design", response_class=HTMLResponse)
    def design(request: Request):
        w, a = pfilter(request)
        return render(request, "design.html", plans=_latest(db.query("technical_plans", w, a, "created_at")),
                      artifacts=db.query("artifacts", w, a), concept_title=concept_title)

    @app.get("/artifact/{aid}")
    def artifact(aid: str):
        a = db.get("artifacts", aid)
        if not a:
            raise HTTPException(404)
        try:
            p = eng.fs.check(a["path"])
        except IndependenceViolation:
            raise HTTPException(403)
        return FileResponse(p, filename=Path(p).name)

    # ---------------------------------------------------------- commercial
    @app.get("/commercial", response_class=HTMLResponse)
    def commercial(request: Request):
        w, a = pfilter(request)
        econ = db.query("economics", w, a, "created_at")
        by: dict[str, dict] = {}
        for e in econ:
            by.setdefault(e["concept_id"], {})[e["scenario"]] = e
        answers = {}
        for r in db.query("demand_answers", w, a):
            answers.setdefault(r["concept_id"], []).append(r)
        return render(request, "commercial.html", by=by, answers=answers, concept_title=concept_title,
                      direct=db.query("direct_evidence", w, a, "recorded_at DESC"), kinds=DIRECT_KINDS,
                      concepts=db.query("concepts", w + " AND status IN ('shortlisted','active')", a))

    @app.post("/commercial/evidence")
    def add_direct(project_id: str = Form(...), kind: str = Form(...), counterparty: str = Form(...),
                   occurred_on: str = Form(...), concept_id: str = Form(""), amount: str = Form(""),
                   currency: str = Form(""), notes: str = Form(""), confirm_human: str = Form("")):
        if confirm_human != "yes":
            raise HTTPException(400, "Direct buyer evidence must be confirmed as recorded by you.")
        try:
            record_direct_evidence(db, project_id, kind, "user", counterparty, occurred_on, concept_id or None,
                                   amount=float(amount) if amount else None, currency=currency or None, notes=notes)
        except ValueError as ex:
            raise HTTPException(400, str(ex))
        return RedirectResponse(f"/commercial?project={project_id}", 303)

    @app.post("/commercial/recompute")
    def recompute(concept_id: str = Form(...), inputs: str = Form(...)):
        c = db.get("concepts", concept_id)
        inp = EconInputs.from_dict(json.loads(inputs))
        scen = run_scenarios(inp)
        with db.tx():
            for name, s in scen.items():
                outputs = dict(s["outputs"])
                if name == "base":
                    outputs["sensitivity"] = sensitivity(inp)
                db.insert("economics", {"project_id": c["project_id"], "concept_id": concept_id, "scenario": name,
                                        "inputs": s["inputs"], "outputs": outputs,
                                        "findings": {"items": s["findings"], "verdict": s["verdict"], "overrides": s["overrides"]},
                                        "created_by": "user"})
            db.log(c["project_id"], None, "user", "economics_recomputed", f"{c['title']}: {scen['base']['verdict']}")
        return RedirectResponse(f"/commercial?project={c['project_id']}", 303)

    # ---------------------------------------------------------- critique
    @app.get("/critique", response_class=HTMLResponse)
    def critique(request: Request):
        w, a = pfilter(request)
        crit = db.query("critiques", w + " AND status!='superseded'", a, "severity, created_at")
        by: dict[str, list] = {}
        for c in crit:
            by.setdefault(c["target_id"], []).append(c)
        return render(request, "critique.html", by=by, disagreements=db.query("disagreements", w + " AND status!='superseded'", a),
                      rejected=db.query("decisions", w + " AND verdict IN ('reject','revise','insufficient_evidence')", a),
                      concept_title=concept_title)

    # ---------------------------------------------------------- prototype
    @app.get("/prototype", response_class=HTMLResponse)
    def prototype(request: Request):
        w, a = pfilter(request)
        return render(request, "prototype.html", exps=db.query("experiments", w + " AND status!='superseded'", a, "status, cost_inr"),
                      concept_title=concept_title, outcomes=db.query("learnings", w + " AND kind='outcome'", a))

    @app.post("/experiments/{eid}/result")
    def exp_result(eid: str, status: str = Form(...), notes: str = Form(...), actual_cost_inr: str = Form("")):
        e = db.get("experiments", eid)
        if status not in ("passed", "failed", "inconclusive", "running"):
            raise HTTPException(400)
        result = {"notes": notes, "actual_cost_inr": float(actual_cost_inr) if actual_cost_inr else None, "recorded_at": now_iso()}
        db.update("experiments", eid, {"status": status, "result": result}, "user")
        with db.tx():
            db.insert("learnings", {"project_id": e["project_id"], "kind": "outcome", "ref_type": "experiment", "ref_id": eid,
                                    "text": f"{e['assumption']}: {status}. {notes}", "data": result, "created_by": "user"})
        return RedirectResponse(f"/prototype?project={e['project_id']}", 303)

    # ---------------------------------------------------------- activity
    @app.get("/activity", response_class=HTMLResponse)
    def activity(request: Request):
        w, a = pfilter(request)
        kind = request.query_params.get("kind")
        if kind:
            w, a = w + " AND kind=?", a + (kind,)
        events = db.query("events", w, a, "id DESC LIMIT 400")
        jobs = db.query("jobs", pfilter(request)[0], pfilter(request)[1], "created_at DESC LIMIT 100")
        return render(request, "activity.html", events=events, jobs=jobs, roles=ROLES)

    # ---------------------------------------------------------- approvals and operator
    @app.get("/approvals", response_class=HTMLResponse)
    def approvals_page(request: Request):
        return render(request, "approvals.html", pending=db.query("approvals", "status='pending'", order="created_at"),
                      decided=db.query("approvals", "status!='pending'", order="decided_at DESC LIMIT 50"),
                      kinds=approvals.GATED_KINDS)

    @app.post("/approvals/{aid}")
    def decide(aid: str, decision: str = Form(...)):
        approvals.decide(db, aid, decision == "approve", "user")
        a = db.get("approvals", aid)
        if a["project_id"]:
            start(a["project_id"])
        return RedirectResponse("/approvals", 303)

    @app.get("/operator", response_class=HTMLResponse)
    def operator(request: Request):
        return render(request, "operator.html", tasks=db.query("operator_tasks", "status='pending'", order="created_at"),
                      answered=db.query("operator_tasks", "status='answered'", order="answered_at DESC LIMIT 30"))

    @app.post("/operator/{tid}")
    def operator_answer(tid: str, answer: str = Form(...), answered_by: str = Form(...)):
        try:
            answer_operator_task(db, tid, json.loads(answer), answered_by)
        except Exception as ex:  # noqa: BLE001
            raise HTTPException(400, f"Answer rejected: {ex}")
        t = db.get("operator_tasks", tid)
        if not db.query("operator_tasks", "project_id=? AND status='pending'", (t["project_id"],)):
            start(t["project_id"])
        return RedirectResponse("/operator", 303)

    # ---------------------------------------------------------- settings
    @app.get("/settings", response_class=HTMLResponse)
    def settings_page(request: Request):
        from ..llm import OllamaProvider
        op = OllamaProvider(eng.settings.ollama_url)
        ok, why = op.available()
        return render(request, "settings.html", hw=detect_hardware(), ollama_ok=ok, ollama_why=why,
                      models=op.list_models() if ok else [], benches=db.query("benchmarks", order="ran_at DESC LIMIT 30"),
                      connectors={n: c.configured() for n, c in eng.connectors.items()}, s=eng.settings.to_json(),
                      describe=eng.describe())

    @app.post("/settings/benchmark")
    def run_benchmark():
        res = benchmark_ollama(db, eng.settings.ollama_url)
        best = choose_default(res)
        if best:
            eng.settings.ollama_model = best
            eng.settings.save()
        return RedirectResponse("/settings", 303)

    @app.post("/settings/probe")
    def probe():
        with db.tx():
            for n, c in eng.connectors.items():
                ok, why = c.probe()
                db.log(None, None, "research_investigator", "connector_probe", f"{n}: {'ok' if ok else why}", tool=n)
        return RedirectResponse("/activity?kind=connector_probe", 303)

    return app
