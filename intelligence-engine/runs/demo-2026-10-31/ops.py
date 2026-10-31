"""Demo helper: dump pending operator tasks, and submit answers keyed by task purpose.

Usage:
  python ops.py dump            -> writes operator/pending.md with every prompt and schema
  python ops.py answer FILE     -> FILE maps purpose -> answer JSON; submits matching pending tasks
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from iie.config import load_settings  # noqa: E402
from iie.db import open_db  # noqa: E402
from iie.llm import answer_operator_task  # noqa: E402

BY = "Claude Code session operator (cloud session, 2026-10-31)"
db = open_db(load_settings(HERE / "home").db_path)
if sys.argv[1] == "dump":
    out = []
    for t in db.query("operator_tasks", "status='pending'", order="created_at"):
        out += [f"## {t['purpose']}  ({t['id']}, role {t['role']})", "", t["prompt"]["prompt"], "",
                "SCHEMA: " + json.dumps(t["schema"]), ""]
    (HERE / "operator" / "pending.md").write_text("\n".join(out))
    print(len(out) and "\n".join(l for l in out if l.startswith("## ")))
else:
    answers = json.loads(Path(sys.argv[2]).read_text())
    rows = db.query("operator_tasks", "status='pending'")
    pend = {t["purpose"]: t for t in rows}
    pend.update({t["id"]: t for t in rows})
    for purpose, ans in answers.items():
        t = pend.get(purpose)
        if not t:
            print("no pending task for", purpose)
            continue
        answer_operator_task(db, t["id"], ans, BY)
        print("answered", purpose)
