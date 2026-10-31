"""Test doubles. These are clearly test-only:

* MockTransport serves canned API responses shaped like each service's documented format.
* ScriptedProvider returns fixed, schema-valid outputs so every stage can be exercised
  without a local model. It is a test double, not a model.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from iie.config import Settings  # noqa: E402
from iie.llm import GenTask, Provider  # noqa: E402

# ------------------------------------------------------------------ HTTP fixtures

SE_ITEMS = [
    {"question_id": 101, "title": "Bike chain rusts every monsoon even after oiling", "link": "https://bicycles.stackexchange.com/q/101",
     "score": 57, "view_count": 21000, "answer_count": 6, "creation_date": 1690000000, "tags": ["chain", "rust"],
     "body": "<p>I commute daily. Each monsoon the chain rusts within weeks and I replace it for ₹1,200 each time.</p>"},
    {"question_id": 102, "title": "Is there a better way to store a bicycle in a small flat", "link": "https://bicycles.stackexchange.com/q/102",
     "score": 34, "view_count": 9800, "answer_count": 4, "creation_date": 1700000000, "tags": ["storage"],
     "body": "<p>Wall hooks damage rented walls. Floor stands take too much space.</p>"},
]
HN_HITS = [{"objectID": "9001", "title": "Ask HN: Why is bike maintenance so expensive in cities?", "points": 120,
            "num_comments": 88, "created_at": "2025-03-02T10:00:00Z", "story_text": "Repair shops charge a lot and wait times are long."}]
OPENALEX = {"results": [{"id": "https://openalex.org/W1", "doi": "https://doi.org/10.1/abc", "display_name": "Hydrophobic coatings for drivetrain corrosion",
                         "publication_date": "2023-05-01", "primary_location": {"source": {"display_name": "Wear"}, "landing_page_url": None},
                         "abstract_inverted_index": {"Sol-gel": [0], "coatings": [1], "reduce": [2], "chain": [3], "corrosion": [4]},
                         "cited_by_count": 12, "type": "article"}]}
WIKI_SEARCH = {"query": {"search": [{"pageid": 11, "title": "Bicycle chain"}]}}
WIKI_PAGES = {"query": {"pages": {"11": {"pageid": 11, "title": "Bicycle chain", "fullurl": "https://en.wikipedia.org/wiki/Bicycle_chain",
                                          "touched": "2026-09-01T00:00:00Z",
                                          "extract": "A bicycle chain is a roller chain that transfers power. Chains wear and corrode, "
                                                     "especially in wet climates. Replacement chains cost about ₹900 to ₹2,500."}}}}


def _handler(request: httpx.Request) -> httpx.Response:
    url = urlparse(str(request.url))
    qs = parse_qs(url.query)
    if url.path.endswith("/robots.txt"):
        return httpx.Response(404)
    if url.hostname == "en.wikipedia.org":
        return httpx.Response(200, json=WIKI_SEARCH if qs.get("list") == ["search"] else WIKI_PAGES)
    if url.hostname == "api.stackexchange.com":
        return httpx.Response(200, json={"items": SE_ITEMS})
    if url.hostname == "hn.algolia.com":
        return httpx.Response(200, json={"hits": HN_HITS})
    if url.hostname == "api.openalex.org":
        return httpx.Response(200, json=OPENALEX)
    return httpx.Response(404, text="not mocked")


@pytest.fixture
def transport() -> httpx.MockTransport:
    return httpx.MockTransport(_handler)


@pytest.fixture
def settings(tmp_path) -> Settings:
    s = Settings(home=tmp_path / "iiehome")
    s.connectors = ["wikipedia", "openalex", "stackexchange", "hackernews", "searxng", "brave", "patentsview"]
    s.ensure_dirs()
    return s


# ------------------------------------------------------------------ scripted provider

CONCEPTS = {
    "first_principles": ("Sealed oil-bath chain case", "fluidic", "risk_reduction", "polymer", "product_sale", "passive_object",
                         "Enclose the chain in a sealed case filled with oil so water never reaches the links."),
    "cross_domain": ("Lotus-leaf coated chain", "chemical", "performance", "metal", "licensing_royalty", "consumable",
                     "Transfer superhydrophobic surface chemistry from plant leaves to chain plates to shed water."),
    "inversion": ("Chain-as-a-service monsoon swap", "logistical", "convenience", "metal", "rental_access", "service_delivered",
                  "Riders never own chains; a courier swaps a fresh waxed chain every month during monsoon."),
    "constraint_transformation": ("Belt drive retrofit kit", "mechanical", "cost_saving", "composite", "product_sale", "installed_system",
                                  "Replace the steel chain with a carbon belt and split frame clamp that cannot rust."),
    "unmet_need": ("Rental-safe vertical bike stand", "material_structural", "access", "wood", "product_sale", "passive_object",
                   "A pressure-fit floor to ceiling pole with no wall drilling stores the bike vertically."),
    "combination": ("Hot-wax subscription for commuters", "chemical", "time_saving", "bio_based", "recurring_supply", "consumable",
                    "Combine immersion waxing with prepaid pickup so the chain is waxed every two weeks."),
    "radical": ("Self-cleaning chain guard with brush", "mechanical", "experience", "polymer", "product_sale", "tool",
                "Brushes inside a guard scrub grit off the chain on every pedal stroke."),
}


class ScriptedProvider(Provider):
    name = "scripted-test-double"
    kind = "test"
    model = "fixed-responses"

    def __init__(self):
        self.calls: list[str] = []

    def available(self):
        return True, "test double"

    def generate(self, task: GenTask) -> dict:
        self.calls.append(task.purpose)
        p, prompt = task.purpose, task.prompt
        claim_ids = re.findall(r"clm_[0-9a-f]{10}", prompt)
        src_ids = re.findall(r'<source id="(src_[0-9a-f]{10})"', prompt)
        if p == "plan_research":
            return {"framing": "Test framing", "queries": [{"text": "bicycle chain rust", "purpose": "problem"}]}
        if p.endswith(":claims"):
            out = []
            for sid, title in re.findall(r'<source id="(src_[0-9a-f]{10})"[^\n]*\nTITLE: ([^\n]+)', prompt):
                out.append({"source_id": sid, "claim_type": "problem_signal", "text": f"Signal: {title}", "quote": title})
            return {"claims": out}
        if p.startswith("discover:"):
            return {"opportunities": [{
                "title": "Monsoon drivetrain corrosion for city commuters", "problem": "Chains rust within weeks in monsoon",
                "who": "Daily bicycle commuters in wet Indian cities", "claim_ids": claim_ids[:3],
                "frequency_intensity": "every monsoon, repeated replacement", "current_alternatives": "oiling, replacement",
                "current_spend": "₹1,200 per chain", "why_gap_exists": "overlooked_segment",
                "gap_explanation": "commuter segment is small per city", "weakest_assumption": "riders will pay to avoid this",
                "test_for_weakest_assumption": "10 interviews with commuters"}]}
        if p.startswith("invent:"):
            method = p.split(":")[1]
            key = method if p.split(":")[2] != "diversity" else method
            t, pc, vt, mc, bm, im, princ = CONCEPTS[key]
            if p.endswith("diversity"):
                t = t + " alternative"
            return {"concepts": [{"title": t, "core_principle": princ, "how_it_works": princ, "assumption_challenged": "chains must be oiled",
                                  "user_value": vt, "target_buyer": "monsoon commuters", "materials": [mc], "process": "small batch",
                                  "business_model": bm, "why_different": "different mechanism", "key_risks": ["adoption"],
                                  "evidence_claim_ids": claim_ids[:2],
                                  "axes": {"principle_class": pc, "value_type": vt, "material_class": mc,
                                           "business_model_class": bm, "interaction_mode": im}}]}
        if p.startswith("originality:"):
            return {"closest_source_id": src_ids[0] if src_ids else "none", "overlap": "partial", "meaningful_difference": True,
                    "difference": "different mechanism"}
        if p.startswith("technical:"):
            return {"functional_principles": ["keep water out"], "technical_requirements": ["IP54 seal"],
                    "material_options": [{"material": "PP", "pros": "cheap", "cons": "UV"}],
                    "processes": [{"process": "3D print prototype", "in_house": True, "equipment": "FDM printer", "equipment_cost_inr": 25000, "notes": "ok"}],
                    "production_comparison": [{"method": "3D printing", "fit": "good", "notes": "prototype"}],
                    "parts": [{"name": "case", "shape": "box", "dims_mm": [400, 60, 120], "material": "PP"}],
                    "bom": [{"item": "PP sheet", "qty": 1, "unit": "sheet", "unit_cost_inr": 450, "source": "assumption"}],
                    "construction_sequence": ["cut", "weld"], "failure_modes": ["seal leaks"], "tests": ["spray test"],
                    "maturity": "concept_with_dimensions"}
        if p.startswith("economics:"):
            return {"price": 2499, "price_source": "assumption", "materials": [{"name": "PP case", "amount": 450, "source": "assumption"},
                    {"name": "seals", "amount": 120, "source": "observed", "ref": "clm_doesnotexist"}],
                    "founder_hours_per_unit": 1.5, "units_per_month": 40, "one_time": [{"name": "mould", "amount": 60000, "source": "assumption", "capex": True}],
                    "monthly_fixed": [{"name": "storage", "amount": 3000, "source": "assumption"}], "channel": "marketplace",
                    "channel_commission_rate": 0.15, "cac": 250, "shipping": 120, "packaging": 60, "rationale": "test"}
        if p.startswith("demand:"):
            keys = ["problem", "who", "frequency_intensity", "alternatives", "current_spend", "why_choose", "switch_trigger",
                    "reach", "acquisition_cost", "delivery_cost", "working_capital", "failure_risks"]
            return {"answers": [{"key": k, "answer": f"answer for {k}", "claim_ids": claim_ids[:1] + ["clm_fake000000"],
                                 "status": "evidenced" if k == "problem" else "assumption"} for k in keys]}
        if p.startswith("critique:"):
            return {"objections": [
                {"question": "Would anyone pay for this?", "objection": "No buyer has paid yet.", "severity": "major", "basis": "reasoning"},
                {"question": "Does something similar already exist?", "objection": "Chain cases exist.", "severity": "major",
                 "basis": "source", "source_ids": ["src_doesnotexist"], "disputes_role": "originality_investigator"}],
                "strongest_point": "Clear recurring problem", "simpler_alternative": "Sell wax and teach riders"}
        if p.startswith("experiments:"):
            return {"experiments": [{"assumption": "seal survives", "hypothesis": "no water after 1h spray", "method": "spray test",
                                     "cost_inr": 500, "duration_days": 2, "success_criteria": "dry", "failure_criteria": "wet",
                                     "evidence_level_target": 1}]}
        if p.startswith("decision:"):
            return {"summary": "Validate first.", "reasons_against": ["no buyer evidence"], "what_would_change_the_decision": ["deposits"]}
        raise AssertionError(f"unscripted purpose {p}")


class LyingProvider(ScriptedProvider):
    """A model that fabricates: fake sources, fake quotes, fake prices, fake customer interest."""
    name = "lying-test-double"

    def generate(self, task: GenTask) -> dict:
        p = task.purpose
        if p.endswith(":claims"):
            return {"claims": [{"source_id": "src_fabricated", "claim_type": "market_size", "text": "Market is ₹5,000 crore",
                                "quote": "the market is worth ₹5,000 crore", "metric": "market_size_inr", "value": 5e10, "currency": "INR"}]}
        if p.startswith("discover:"):
            return {"opportunities": [{"title": "Fabricated", "problem": "x", "who": "y", "claim_ids": ["clm_madeup0000"],
                                       "frequency_intensity": "high", "current_alternatives": "none", "why_gap_exists": "overlooked_segment",
                                       "gap_explanation": "z", "weakest_assumption": "w", "test_for_weakest_assumption": "t"}]}
        if p.startswith("economics:"):
            out = super().generate(task)
            out.update(price_source="observed", price_ref="clm_madeup0000")
            out["materials"] = [{"name": "PP", "amount": 100, "source": "quote", "ref": "clm_madeup0000"}]
            return out
        return super().generate(task)


@pytest.fixture
def scripted() -> ScriptedProvider:
    return ScriptedProvider()


def read_json(path: Path):
    return json.loads(path.read_text())
