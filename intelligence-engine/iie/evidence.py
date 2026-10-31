"""Evidence ladder, claim recording with quote verification, contradictions, and freshness.

Demand evidence ladder:
  L0 unsupported assumption
  L1 indirect market evidence (any public source: forums, reports, listings, papers)
  L2 verified buyer problem or expressed interest (direct, user-recorded)
  L3 qualified purchase interest or credible commercial commitment (direct, user-recorded)
  L4 actual paid order, deposit, or comparable transaction (direct, user-recorded)
  L5 repeat purchasing or sustained commercial performance (direct, user-recorded)

Public research can never lift a demand claim above L1. Only a human user can
record direct evidence (L2 and above). Agents, models, connectors, and operators
are refused in code.
"""
from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass

from .db import DB
from .text import quote_in_source
from .util import now_iso, parse_date, today

LEVEL_LABELS = {
    0: "L0 unsupported assumption",
    1: "L1 indirect market evidence",
    2: "L2 verified buyer problem or expressed interest",
    3: "L3 qualified purchase interest or commitment",
    4: "L4 paid order, deposit, or transaction",
    5: "L5 repeat purchasing or sustained performance",
}

SOURCE_TYPES = {
    "encyclopedia", "academic", "preprint", "industry_report", "news", "trade_publication",
    "company_site", "product_listing", "price_quote", "forum", "review", "patent", "design_registration",
    "standard", "government_data", "web_page", "search_snippet", "dataset", "manufacturer_spec",
}

# Claim support states (separate from the demand ladder).
SUPPORT = ("verified_quote", "source_unverified", "assumption", "contradicted", "calculated")

DIRECT_KINDS = {
    "interview": 2,
    "survey_response": 2,
    "expressed_interest": 2,
    "waitlist_signup": 2,
    "letter_of_intent": 3,
    "qualified_quote_request": 3,
    "preorder_commitment": 3,
    "deposit": 4,
    "paid_order": 4,
    "comparable_transaction": 4,
    "repeat_order": 5,
    "sales_record": 5,
}

HUMAN_ACTORS = {"user"}

# Days after which a claim of this type is flagged as possibly outdated.
FRESHNESS_DAYS = {
    "price_observation": 365,
    "cost_observation": 365,
    "market_size": 3 * 365,
    "competitor": 2 * 365,
    "regulation": 2 * 365,
    "problem_signal": 4 * 365,
    "technical_finding": 10 * 365,
    "demand_signal": 2 * 365,
}


class EvidencePermissionError(PermissionError):
    pass


@dataclass
class QuoteRef:
    source_id: str
    quote: str
    stance: str = "supports"  # supports | contradicts


def add_claim(
    db: DB,
    project_id: str,
    text: str,
    claim_type: str,
    created_by: str,
    refs: list[QuoteRef] | None = None,
    subject_type: str | None = None,
    subject_id: str | None = None,
    metric: str | None = None,
    value: float | None = None,
    unit: str | None = None,
    currency: str | None = None,
    origin: str = "research",
) -> tuple[str, list[str]]:
    """Record a claim. Each quote is checked against the stored source text.

    Returns (claim_id, problems). Quotes that are not found verbatim are stored
    with verified=0 and the claim's support drops to 'source_unverified'. A claim
    with no references is an assumption (L0).
    """
    problems: list[str] = []
    refs = refs or []
    verified_any = False
    checked: list[tuple[QuoteRef, bool]] = []
    for r in refs:
        src = db.get("sources", r.source_id)
        if src is None:
            problems.append(f"source {r.source_id} does not exist; reference dropped")
            continue
        ok = quote_in_source(r.quote, (src.get("title") or "") + "\n" + (src.get("content") or ""))
        if not ok:
            problems.append(f"quote not found verbatim in {r.source_id}: '{r.quote[:80]}'")
        verified_any = verified_any or (ok and r.stance == "supports")
        checked.append((r, ok))

    if not checked:
        support = "assumption"
        level = 0
    elif verified_any:
        support = "verified_quote"
        level = 1
    else:
        support = "source_unverified"
        level = 0

    with db.tx():
        cid = db.insert(
            "claims",
            {
                "project_id": project_id, "subject_type": subject_type, "subject_id": subject_id,
                "claim_type": claim_type, "text": text, "metric": metric, "value": value, "unit": unit,
                "currency": currency, "support": support, "evidence_level": level, "origin": origin,
                "created_by": created_by,
            },
        )
        for r, ok in checked:
            db.execute(
                "INSERT OR REPLACE INTO claim_sources(claim_id, source_id, quote, stance, verified) VALUES (?,?,?,?,?)",
                (cid, r.source_id, r.quote, r.stance, int(ok)),
            )
    return cid, problems


def record_direct_evidence(
    db: DB,
    project_id: str,
    kind: str,
    actor: str,
    counterparty: str,
    occurred_on: str,
    concept_id: str | None = None,
    contact_ref: str | None = None,
    amount: float | None = None,
    currency: str | None = None,
    notes: str = "",
) -> str:
    """Record first-hand buyer evidence. Only a human user may do this."""
    if actor not in HUMAN_ACTORS:
        raise EvidencePermissionError(
            f"Actor '{actor}' cannot record direct buyer evidence. Only the user can log interviews, "
            "commitments, or payments. The engine never creates them."
        )
    if kind not in DIRECT_KINDS:
        raise ValueError(f"Unknown direct evidence kind '{kind}'. Use one of {sorted(DIRECT_KINDS)}")
    if not counterparty.strip():
        raise ValueError("Direct evidence needs an identifiable counterparty (name, company, or reference).")
    d = parse_date(occurred_on)
    if d is None or d > today():
        raise ValueError("occurred_on must be a real past or present date (YYYY-MM-DD).")
    level = DIRECT_KINDS[kind]
    if kind in ("deposit", "paid_order", "comparable_transaction") and not amount:
        raise ValueError("Payment evidence needs an amount and currency.")
    if amount and not currency:
        raise ValueError("Amounts must state their currency.")
    if level == 5 and kind == "repeat_order":
        prior = db.scalar(
            "SELECT COUNT(*) FROM direct_evidence WHERE project_id=? AND counterparty=? AND kind IN ('paid_order','deposit','repeat_order')",
            (project_id, counterparty),
        )
        if not prior:
            raise ValueError("A repeat order needs an earlier recorded order from the same counterparty.")
    with db.tx():
        return db.insert(
            "direct_evidence",
            {
                "project_id": project_id, "concept_id": concept_id, "kind": kind, "level": level,
                "counterparty": counterparty, "contact_ref": contact_ref, "occurred_on": d.isoformat(),
                "amount": amount, "currency": currency, "notes": notes, "recorded_by": actor,
                "recorded_at": now_iso(),
            },
        )


def demand_level(db: DB, project_id: str, concept_id: str | None = None) -> tuple[int, str]:
    """Highest demand evidence level, with an explanation."""
    where, params = "project_id=?", [project_id]
    if concept_id:
        where += " AND (concept_id=? OR concept_id IS NULL)"
        params.append(concept_id)
    rows = db.query("direct_evidence", where, tuple(params))
    if rows:
        best = max(rows, key=lambda r: r["level"])
        n = sum(1 for r in rows if r["level"] == best["level"])
        return best["level"], f"{n} user-recorded {best['kind']} record(s)"
    n_public = db.scalar(
        "SELECT COUNT(*) FROM claims WHERE project_id=? AND evidence_level>=1 AND claim_type IN "
        "('problem_signal','demand_signal','market_size','price_observation','competitor')",
        (project_id,),
    )
    if n_public:
        return 1, f"{n_public} verified public claim(s); no direct buyer evidence"
    return 0, "no verified evidence; demand is an assumption"


def freshness(claim_type: str, published_at: str | None, retrieved_at: str | None) -> tuple[str, int | None]:
    """Return ('current'|'possibly_outdated'|'date_unknown', age_days)."""
    pub = parse_date(published_at)
    if pub is None:
        return "date_unknown", None
    age = (today() - pub).days
    limit = FRESHNESS_DAYS.get(claim_type, 3 * 365)
    return ("possibly_outdated" if age > limit else "current"), age


def detect_contradictions(db: DB, project_id: str, tolerance: float = 1.5) -> list[str]:
    """Flag numeric claims on the same metric (same unit/currency) that disagree by more than `tolerance`x."""
    rows = db.query(
        "claims",
        "project_id=? AND metric IS NOT NULL AND value IS NOT NULL AND support!='assumption'",
        (project_id,),
    )
    groups: dict[tuple, list[dict]] = {}
    for r in rows:
        key = (r["metric"].strip().lower(), (r["unit"] or "").lower(), (r["currency"] or "").upper())
        groups.setdefault(key, []).append(r)
    created = []
    existing = {(c["claim_a"], c["claim_b"]) for c in db.query("contradictions", "project_id=?", (project_id,))}
    for key, items in groups.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                a, b = items[i], items[j]
                va, vb = abs(a["value"]), abs(b["value"])
                if min(va, vb) <= 0:
                    continue
                ratio = max(va, vb) / min(va, vb)
                if ratio > tolerance and (a["id"], b["id"]) not in existing:
                    with db.tx():
                        cid = db.insert(
                            "contradictions",
                            {
                                "project_id": project_id, "metric": key[0], "claim_a": a["id"], "claim_b": b["id"],
                                "ratio": round(ratio, 2), "status": "open",
                                "note": f"{a['value']} vs {b['value']} {key[2] or key[1]}".strip(),
                            },
                        )
                    created.append(cid)
    # Stance-based contradictions: the same claim cited as supported and contradicted.
    for r in db.conn.execute(
        "SELECT cs.claim_id FROM claim_sources cs JOIN claims c ON c.id=cs.claim_id "
        "WHERE c.project_id=? GROUP BY cs.claim_id HAVING SUM(cs.stance='supports')>0 AND SUM(cs.stance='contradicts')>0",
        (project_id,),
    ).fetchall():
        cid = r[0]
        if (cid, cid) not in existing:
            with db.tx():
                created.append(db.insert("contradictions", {
                    "project_id": project_id, "metric": "stance", "claim_a": cid, "claim_b": cid,
                    "ratio": None, "status": "open", "note": "sources disagree on this claim"}))
    return created


_MONEY_RE = re.compile(
    r"(?P<cur>₹|rs\.?|inr|\$|usd|us\$|€|eur|£|gbp)\s?(?P<num>\d+(?:,\d{2,3})*(?:\.\d+)?)\s?(?P<mult>lakhs?|crores?|million|billion|mn|bn|k|m)?\b",
    re.IGNORECASE,
)
_CUR = {"₹": "INR", "rs": "INR", "rs.": "INR", "inr": "INR", "$": "USD", "usd": "USD", "us$": "USD",
        "€": "EUR", "eur": "EUR", "£": "GBP", "gbp": "GBP"}
_MULT = {"lakh": 1e5, "lakhs": 1e5, "crore": 1e7, "crores": 1e7, "k": 1e3, "m": 1e6, "mn": 1e6,
         "million": 1e6, "billion": 1e9, "bn": 1e9}


def find_money(text: str) -> list[tuple[float, str, str]]:
    """Return (amount, currency, matched_text) for money mentions in text."""
    out = []
    for m in _MONEY_RE.finditer(text or ""):
        try:
            num = float(m.group("num").replace(",", ""))
        except ValueError:
            continue
        mult = _MULT.get((m.group("mult") or "").lower(), 1.0)
        cur = _CUR.get(m.group("cur").lower().rstrip(), _CUR.get(m.group("cur").lower(), "UNKNOWN"))
        out.append((num * mult, cur, m.group(0)))
    return out


def level_label(level: int | None) -> str:
    return LEVEL_LABELS.get(level or 0, "L0 unsupported assumption")


def age_label(days: int | None) -> str:
    if days is None:
        return "date unknown"
    if days < 60:
        return f"{days} days old"
    return f"{days / 365:.1f} years old"


def iso_today() -> str:
    return _dt.date.today().isoformat()
