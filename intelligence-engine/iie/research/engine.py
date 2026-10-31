"""Research workflow: run queries across connectors, store citations, extract verified claims."""
from __future__ import annotations

from dataclasses import dataclass, field

from ..context import Ctx, source_block
from ..evidence import SOURCE_TYPES, QuoteRef, add_claim, find_money
from ..guard import IndependenceViolation, check_url
from ..llm import GenTask, OperatorProvider
from ..schema import STR, arr, obj
from ..text import injection_suspect, sentences
from ..util import clip, now_iso, parse_date, sha256, today
from .connectors import PURPOSE_DEFAULTS, Doc
from .http import FetchError

CLAIM_TYPES = [
    "problem_signal", "demand_signal", "market_size", "price_observation", "cost_observation", "competitor",
    "technical_finding", "regulation", "buyer_behaviour", "supply_signal", "other",
]


@dataclass
class RQuery:
    text: str
    purpose: str = "background"
    connectors: list[str] | None = None
    params: dict = field(default_factory=dict)
    industry: str | None = None

    def key(self) -> str:
        return sha256(f"{self.purpose}|{self.text}|{sorted(self.params.items())}|{self.connectors}")[:16]

    def to_dict(self) -> dict:
        return {"text": self.text, "purpose": self.purpose, "connectors": self.connectors, "params": self.params,
                "industry": self.industry}

    @classmethod
    def from_dict(cls, d: dict) -> "RQuery":
        return cls(d["text"], d.get("purpose", "background"), d.get("connectors"), d.get("params") or {},
                   d.get("industry"))


def store_doc(ctx: Ctx, doc: Doc, connector: str, query: str, retrieval_method: str = "api",
              retrieved_at: str | None = None) -> tuple[str, bool]:
    existing = ctx.db.one("sources", "project_id=? AND url=?", (ctx.project_id, doc.url))
    if existing:
        return existing["id"], False
    meta = dict(doc.meta or {})
    if injection_suspect(doc.title + " " + doc.content):
        meta["injection_suspect"] = True
    with ctx.db.tx():
        sid = ctx.db.insert("sources", {
            "project_id": ctx.project_id, "url": doc.url, "title": clip(doc.title, 400),
            "publisher": doc.publisher, "source_type": doc.source_type if doc.source_type in SOURCE_TYPES else "web_page",
            "connector": connector, "query": query, "retrieved_at": retrieved_at or now_iso(),
            "published_at": doc.published_at, "content": doc.content, "content_hash": sha256(doc.content or ""),
            "retrieval_method": retrieval_method, "meta": meta,
        })
    return sid, True


def _gap(ctx: Ctx, connector: str, query: str, reason: str) -> None:
    with ctx.db.tx():
        ctx.db.insert("research_gaps", {"project_id": ctx.project_id, "job_id": ctx.job_id, "connector": connector,
                                        "query": query, "reason": reason})


BUNDLE_SCHEMA = obj(
    ["sources"],
    sources=arr(obj(
        ["url", "title", "source_type", "retrieved_at", "retrieval_method", "content"],
        url=STR, title=STR, publisher=STR, source_type={"type": "string", "enum": sorted(SOURCE_TYPES)},
        published_at=STR, retrieved_at=STR, retrieval_method=STR, content=STR, query=STR,
    )),
    notes=STR,
    unfulfilled={"type": "array", "items": STR},
)


def import_bundle(ctx: Ctx, bundle: dict, imported_by: str, label: str = "manual") -> dict:
    """Validate and store an operator-supplied source bundle. Returns counts and rejections."""
    added, dup, rejected = 0, 0, []
    for s in bundle.get("sources", []):
        try:
            check_url(s["url"])
        except (ValueError, IndependenceViolation) as e:
            rejected.append({"url": s.get("url"), "reason": str(e)})
            continue
        r_date = parse_date(s.get("retrieved_at"))
        if r_date is None or r_date > today():
            rejected.append({"url": s["url"], "reason": "retrieved_at missing or in the future"})
            continue
        if len((s.get("content") or "").strip()) < 20:
            rejected.append({"url": s["url"], "reason": "no usable content"})
            continue
        doc = Doc(url=s["url"], title=s["title"], content=s["content"], source_type=s["source_type"],
                  publisher=s.get("publisher"), published_at=s.get("published_at"),
                  meta={"imported_by": imported_by, "label": label, "query": s.get("query")})
        _, new = store_doc(ctx, doc, f"operator_bundle:{imported_by}", s.get("query", ""),
                           retrieval_method=s.get("retrieval_method", "operator"), retrieved_at=s["retrieved_at"])
        added += int(new)
        dup += int(not new)
    ctx.log("research_investigator", "bundle_import", f"imported {added} sources ({dup} duplicates, "
            f"{len(rejected)} rejected) from {imported_by}", detail={"rejected": rejected,
                                                                      "notes": bundle.get("notes")})
    for q in bundle.get("unfulfilled", []) or []:
        _gap(ctx, "operator_bundle", q, "operator could not find evidence")
    return {"added": added, "duplicates": dup, "rejected": rejected}


def run_research(ctx: Ctx, queries: list[RQuery], actor: str = "research_investigator",
                 label: str = "research", max_queries: int | None = None) -> dict:
    """Run queries with checkpointing, saturation stop, and honest gap recording."""
    cp = ctx.checkpoint()
    state = cp.get(label) or {"done": [], "unavailable": {}, "new_by_query": {}, "stopped": None, "used": []}
    unavailable: dict[str, str] = state["unavailable"]
    limit = ctx.settings.max_sources_per_query
    queries = queries[: (max_queries or ctx.settings.max_queries_per_stage)]
    zero_streak = 0
    if not ctx.settings.research_enabled:
        state["stopped"] = "research disabled in settings"
    for q in queries:
        if state["stopped"]:
            break
        k = q.key()
        if k in state["done"]:
            continue
        names = q.connectors or PURPOSE_DEFAULTS.get(q.purpose, ["wikipedia"])
        new_count = 0
        for name in names:
            c = ctx.connectors.get(name)
            if c is None or name in unavailable:
                continue
            ok, why = c.configured()
            if not ok:
                unavailable[name] = why
                _gap(ctx, name, q.text, why)
                continue
            try:
                docs = c.search(q.text, limit, **q.params)
                ctx.log(actor, "tool_call", f"{name}: '{clip(q.text, 80)}' -> {len(docs)} results", tool=name)
            except FetchError as e:
                ctx.log(actor, "tool_error", f"{name}: {e}", tool=name)
                if e.kind in ("network_blocked", "timeout"):
                    unavailable[name] = f"{e.kind}: {e}"
                _gap(ctx, name, q.text, f"{e.kind}: {e}")
                continue
            if name not in state["used"]:
                state["used"].append(name)
            for d in docs:
                if not d.url:
                    continue
                d.meta = {**(d.meta or {}), "label": label, "purpose": q.purpose, "industry": q.industry}
                _, new = store_doc(ctx, d, name, q.text)
                new_count += int(new)
        state["done"].append(k)
        state["new_by_query"][k] = new_count
        zero_streak = zero_streak + 1 if new_count == 0 else 0
        if zero_streak >= ctx.settings.saturation_window and any(state["new_by_query"].values()):
            state["stopped"] = f"saturation: {zero_streak} queries in a row added no new sources"
        ctx.save_checkpoint({**ctx.checkpoint(), label: state})
        ctx.heartbeat()

    fulfilled = sum(1 for v in state["new_by_query"].values() if v)
    summary = {"queries_run": len(state["done"]), "queries_with_new_sources": fulfilled,
               "unavailable_connectors": unavailable, "stopped": state["stopped"], "used": state["used"]}

    # Operator-supplied research when connectors could not reach sources.
    if ctx.settings.operator_research and fulfilled < max(1, len(queries) // 2):
        task = GenTask(
            role=actor, purpose=f"{label}:research_bundle", system="You are the research operator.",
            prompt=_bundle_prompt(queries, unavailable), schema=BUNDLE_SCHEMA, max_tokens=8000,
        )
        task.project_id, task.job_id = ctx.project_id, ctx.job_id
        op = OperatorProvider(ctx.db)
        answer = op.generate(task)  # raises OperatorPending until answered
        row = ctx.db.one("operator_tasks", "request_key=?", (task.request_key(),))
        if not state.get("bundle_imported"):
            res = import_bundle(ctx, answer, (row or {}).get("answered_by") or "operator", label)
            state["bundle_imported"] = True
            ctx.save_checkpoint({**ctx.checkpoint(), label: state})
            summary["operator_bundle"] = res
        if "operator_bundle" not in state["used"]:
            state["used"].append("operator_bundle")
            summary["used"] = state["used"]
            ctx.save_checkpoint({**ctx.checkpoint(), label: state})
    ctx.log(actor, "research_summary", f"{label}: {summary}")
    return summary


def _bundle_prompt(queries: list[RQuery], unavailable: dict) -> str:
    lines = [
        "The engine's own connectors could not reach enough sources. Unavailable connectors:",
        *[f"- {k}: {v}" for k, v in unavailable.items()],
        "",
        "Run these research queries with a real retrieval tool and return what you actually found:",
        *[f"- [{q.purpose}{'/' + q.industry if q.industry else ''}] {q.text}"
          + (f"  (params: {q.params})" if q.params else "") for q in queries],
        "",
        "For each source give the real URL, title, publisher, source_type, published_at if shown, retrieved_at "
        "(today's date), retrieval_method (e.g. 'web_search_snippet' or 'web_fetch_extract'), and content: text "
        "copied from the page or search snippet. Do not paraphrase inside content. If nothing was found for a "
        "query, list it under 'unfulfilled'. Never fabricate a source.",
    ]
    return "\n".join(lines)


EXTRACT_SCHEMA = obj(
    ["claims"],
    claims=arr(obj(
        ["source_id", "claim_type", "text", "quote"],
        source_id=STR, claim_type={"type": "string", "enum": CLAIM_TYPES}, text=STR, quote=STR,
        metric=STR, value={"type": ["number", "null"]}, unit=STR, currency=STR,
        stance={"type": "string", "enum": ["supports", "contradicts"]},
    )),
)


def deterministic_claims(ctx: Ctx, src: dict) -> int:
    """Claims that need no model: forum problem titles, explicit money mentions."""
    n = 0
    st = src.get("source_type")
    content = src.get("content") or ""
    if st == "forum" and src.get("title"):
        meta = src.get("meta") or {}
        signal = ", ".join(f"{k}={meta[k]}" for k in ("score", "views", "points", "comments") if meta.get(k) is not None)
        add_claim(ctx.db, ctx.project_id, f"Recurring problem raised publicly: {src['title']}" +
                  (f" ({signal})" if signal else ""), "problem_signal", "extractor",
                  [QuoteRef(src["id"], src["title"])])
        n += 1
    if st in ("product_listing", "price_quote", "company_site", "search_snippet", "web_page", "news",
              "trade_publication", "industry_report"):
        for sent in sentences(content)[:200]:
            for amount, cur, raw in find_money(sent)[:2]:
                low = sent.lower()
                ctype = "market_size" if ("market" in low and amount >= 1e7) else "price_observation"
                add_claim(ctx.db, ctx.project_id, clip(sent, 300), ctype, "extractor",
                          [QuoteRef(src["id"], sent)], value=amount, currency=cur)
                n += 1
                break
            if n >= 6:
                break
    return n


def extract_claims(ctx: Ctx, source_ids: list[str], focus: str, actor: str = "research_investigator",
                   label: str = "extract") -> dict:
    cp = ctx.checkpoint()
    done = set(cp.get(label, []))
    todo = [s for s in source_ids if s not in done]
    srcs = [ctx.db.get("sources", s) for s in todo]
    srcs = [s for s in srcs if s]
    det = sum(deterministic_claims(ctx, s) for s in srcs if s["id"] not in done)
    created, problems = 0, []
    batches = [srcs[i:i + 6] for i in range(0, len(srcs), 6)]
    tasks = []
    for b in batches:
        usable = [s for s in b if not (s.get("meta") or {}).get("injection_suspect")]
        if not usable:
            continue
        prompt = (f"Research focus: {focus}\n\nExtract factual claims relevant to the focus from these sources. "
                  "Each claim needs an exact quote from its source. Use metric names like 'retail_price_inr:<item>' "
                  "or 'market_size_usd:<segment>' so numbers on the same thing can be compared. Skip sources "
                  "with nothing relevant.\n\n" + "\n\n".join(source_block(s) for s in usable))
        tasks.append(GenTask(role=actor, purpose=f"{label}:claims", system="You are the Research Investigator. "
                             "You extract verifiable claims with exact quotes.", prompt=prompt,
                             schema=EXTRACT_SCHEMA, temperature=0.1, max_tokens=2500))
    results = ctx.generate(tasks) if tasks else []
    if results:
        valid_ids = {s["id"] for s in srcs}
        for res in results:
            for c in res.get("claims", []):
                if c["source_id"] not in valid_ids:
                    problems.append(f"claim cites unknown source {c['source_id']}")
                    continue
                _, probs = add_claim(ctx.db, ctx.project_id, c["text"], c["claim_type"], actor,
                                     [QuoteRef(c["source_id"], c["quote"], c.get("stance") or "supports")],
                                     metric=c.get("metric"), value=c.get("value"), unit=c.get("unit"),
                                     currency=c.get("currency"), origin="model_extraction")
                problems.extend(probs)
                created += 1
    ctx.save_checkpoint({**ctx.checkpoint(), label: sorted(done | {s["id"] for s in srcs})})
    if problems:
        ctx.log(actor, "verification_failures", f"{len(problems)} quote/source problems", detail=problems[:50])
    return {"deterministic_claims": det, "model_claims": created, "problems": problems,
            "model_used": results is not None}
