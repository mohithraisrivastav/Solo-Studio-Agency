"""Command line interface: iie <command>."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import approvals
from .config import load_settings
from .evidence import DIRECT_KINDS, record_direct_evidence
from .llm import answer_operator_task
from .llm.hardware import benchmark_ollama, choose_default, detect_hardware
from .orchestrator import Engine
from .report import project_report


def _engine(args) -> Engine:
    s = load_settings(Path(args.home) if args.home else None)
    if getattr(args, "provider", None):
        s.model_provider = args.provider
    if getattr(args, "operator_research", False):
        s.operator_research = True
    return Engine(s, offline=getattr(args, "offline", False))


def _print(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="iie", description="Independent Intelligence Engine")
    ap.add_argument("--home", help="data directory (default $IIE_HOME or ./var)")
    ap.add_argument("--provider", choices=["auto", "ollama", "openai_compat", "operator", "none"])
    ap.add_argument("--offline", action="store_true", help="disable all external research")
    ap.add_argument("--operator-research", action="store_true", help="let an operator supply source bundles")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")
    sub.add_parser("hardware")
    sub.add_parser("models")
    b = sub.add_parser("benchmark")
    b.add_argument("--models", nargs="*")
    sub.add_parser("connectors")

    n = sub.add_parser("new")
    n.add_argument("question")
    n.add_argument("--workflow", default="full")
    n.add_argument("--mode", default="fresh", choices=["fresh", "evidence"])
    n.add_argument("--budget", type=float)
    n.add_argument("--title")
    n.add_argument("--industries", help="comma separated; omit for automatic selection")
    n.add_argument("--seed", type=int)
    n.add_argument("--concept-json", help="file with a concept to evaluate (evaluate/commercial workflows)")
    n.add_argument("--economics-json", help="file with economics inputs (commercial workflow)")

    r = sub.add_parser("run")
    r.add_argument("project")
    r.add_argument("--stop-after")
    rr = sub.add_parser("rerun", help="supersede a stage and later stages, then run again")
    rr.add_argument("project")
    rr.add_argument("stage")
    rr.add_argument("--reason", required=True)
    sub.add_parser("resume")
    st = sub.add_parser("status")
    st.add_argument("project", nargs="?")

    op = sub.add_parser("operator")
    op.add_argument("action", choices=["list", "show", "answer"])
    op.add_argument("task", nargs="?")
    op.add_argument("file", nargs="?")
    op.add_argument("--by", help="name of the person or agent answering")

    ev = sub.add_parser("evidence")
    ev.add_argument("action", choices=["direct"])
    ev.add_argument("project")
    ev.add_argument("--kind", choices=sorted(DIRECT_KINDS), required=True)
    ev.add_argument("--counterparty", required=True)
    ev.add_argument("--date", required=True)
    ev.add_argument("--concept")
    ev.add_argument("--amount", type=float)
    ev.add_argument("--currency")
    ev.add_argument("--notes", default="")
    ev.add_argument("--i-am-the-user", action="store_true", help="confirm a human is recording this")

    ap_ = sub.add_parser("approvals")
    ap_.add_argument("action", choices=["list", "approve", "deny"])
    ap_.add_argument("id", nargs="?")

    rp = sub.add_parser("report")
    rp.add_argument("project")
    rp.add_argument("--out")

    sv = sub.add_parser("serve")
    sv.add_argument("--host", default="127.0.0.1")
    sv.add_argument("--port", type=int, default=8765)

    args = ap.parse_args(argv)

    if args.cmd == "hardware":
        _print(detect_hardware())
        return 0
    if args.cmd == "serve":
        import uvicorn

        from .web.app import create_app
        s = load_settings(Path(args.home) if args.home else None)
        if args.provider:
            s.model_provider = args.provider
        uvicorn.run(create_app(s), host=args.host, port=args.port)
        return 0

    e = _engine(args)
    if args.cmd == "init":
        e.recover()
        e.settings.save()
        _print(e.describe())
    elif args.cmd == "models":
        from .llm import OllamaProvider
        p = OllamaProvider(e.settings.ollama_url)
        ok, why = p.available()
        _print({"ollama": why, "models": p.list_models() if ok else []})
    elif args.cmd == "benchmark":
        res = benchmark_ollama(e.db, e.settings.ollama_url, args.models)
        best = choose_default(res)
        if best:
            e.settings.ollama_model = best
            e.settings.save()
        _print({"results": [{k: v for k, v in r.items() if k != "hardware"} for r in res], "default": best})
    elif args.cmd == "connectors":
        _print({n: c.probe() for n, c in e.connectors.items()})
    elif args.cmd == "new":
        st = {}
        if args.industries:
            st["industries"] = [x.strip() for x in args.industries.split(",") if x.strip()]
        if args.seed:
            st["seed"] = args.seed
        if args.concept_json:
            st["concept"] = json.loads(Path(args.concept_json).read_text())
        if args.economics_json:
            st["economics"] = json.loads(Path(args.economics_json).read_text())
        pid = e.create_project(args.question, args.workflow, args.mode, args.title, args.budget, st)
        print(pid)
    elif args.cmd == "run":
        e.recover()
        _print(e.run(args.project, args.stop_after))
    elif args.cmd == "rerun":
        _print({"superseded": e.rerun_from(args.project, args.stage, args.reason), "run": e.run(args.project)})
    elif args.cmd == "resume":
        ids = e.recover()
        rows = e.db.query("projects", "status IN ('interrupted','waiting_operator','waiting_approval','paused','running')")
        _print({"recovered_jobs": ids, "results": {p["id"]: e.run(p["id"]) for p in rows}})
    elif args.cmd == "status":
        if args.project:
            _print(e.status(args.project))
        else:
            _print([{k: p[k] for k in ("id", "title", "workflow", "status", "updated_at")} for p in
                    e.db.query("projects", order="updated_at DESC")])
    elif args.cmd == "operator":
        if args.action == "list":
            _print([{k: t[k] for k in ("id", "project_id", "role", "purpose", "status")} for t in
                    e.db.query("operator_tasks", "status='pending'", order="created_at")])
        elif args.action == "show":
            t = e.db.get("operator_tasks", args.task)
            _print({"id": t["id"], "role": t["role"], "purpose": t["purpose"], "system": t["prompt"]["system"],
                    "prompt": t["prompt"]["prompt"], "schema": t["schema"]})
        else:
            if not args.by:
                print("--by is required: name who is answering", file=sys.stderr)
                return 2
            answer_operator_task(e.db, args.task, json.loads(Path(args.file).read_text()), args.by)
            print("answered")
    elif args.cmd == "evidence":
        if not args.i_am_the_user:
            print("Direct buyer evidence can only be recorded by the user. Add --i-am-the-user to confirm.", file=sys.stderr)
            return 2
        print(record_direct_evidence(e.db, args.project, args.kind, "user", args.counterparty, args.date, args.concept,
                                     amount=args.amount, currency=args.currency, notes=args.notes))
    elif args.cmd == "approvals":
        if args.action == "list":
            _print(e.db.query("approvals", "status='pending'", order="created_at"))
        else:
            approvals.decide(e.db, args.id, args.action == "approve", "user")
            print(args.action + "d")
    elif args.cmd == "report":
        text = project_report(e.db, args.project)
        if args.out:
            Path(args.out).write_text(text, encoding="utf-8")
            print(args.out)
        else:
            print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
