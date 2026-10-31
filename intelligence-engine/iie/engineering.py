"""Technical analysis helpers: hazard flags, development plan schema, editable CAD and BOM output.

Everything produced here is a concept-stage document. Generated CAD is concept
geometry for discussion and prototyping, not a validated engineering drawing.
"""
from __future__ import annotations

import csv
import io
import re

from .schema import NUM, STR, STRS, arr, obj

HAZARDS: dict[str, dict] = {
    "electrical": {
        "words": r"\b(mains|230 ?v|240 ?v|110 ?v|wiring|wired|led driver|transformer|plug|socket|battery|lithium|"
                 r"li-ion|charger|heating element|heater|electric|electrical|electronics?|circuit|pcb|solar panel|inverter|"
                 r"bluetooth|usb|amplifier|motor|led|leds|speaker module|power supply)\b",
        "review": "Electrical safety review by a qualified engineer; insulation, earthing, and thermal tests. "
                  "Check which Indian (BIS) or export standards apply before any sale.",
    },
    "structural": {
        "words": r"\b(load[- ]bearing|structural|cantilever(ed)?|shel(f|ves)|shelving|chairs?|seats?|stools?|benches|bench|"
                 r"ladders?|hanging|suspended|ceilings?|wall[- ]mounted|brackets?|standoffs?|beams?|columns?|tables?|beds?|"
                 r"cribs?|railings?|scaffold|wardrobes?|tall units?|overhead)\b",
        "review": "Load calculation and physical load testing with a safety factor; structural engineer sign-off "
                  "for anything carrying people or mounted overhead.",
    },
    "pressure": {
        "words": r"\b(pressure|pressurised|pressurized|compressed|boiler|steam|vacuum|gas cylinder|pneumatic|hydraulic)\b",
        "review": "Pressure vessel rules and burst testing; specialist review mandatory.",
    },
    "chemical": {
        "words": r"\b(resins?|epoxy|solvents?|acids?|alkali|lye|glazes?|lead paint|lead-based|cadmium|formaldehyde|isocyanates?|"
                 r"preservatives?|termiticides?|pesticides?|insecticides?|borates?|varnish|lacquer|etchant|bleach|"
                 r"reagents?|mordant|bait)\b",
        "review": "Safety data sheets for every chemical, ventilation and PPE, waste disposal, and residue testing "
                  "of the finished product.",
    },
    "food_contact": {
        "words": r"\b(food[- ]contact|food[- ]grade|drinks?|beverages?|cups?|mugs?|bowls?|edible|water bottles?|"
                 r"tableware|cutlery|cooking surface|batter|curd)\b",
        "review": "Food-contact material compliance and migration testing (glazes, coatings, plastics).",
    },
    "medical": {
        "words": r"\b(medical|patient|clinic|therapy|therapeutic|diagnos\w*|wound|implant|hospital|health claim)\b",
        "review": "Medical device rules may apply; regulatory specialist review before any claim or sale.",
    },
    "children": {
        "words": r"\b(child|children|kid|kids|toy|toys|infant|baby|toddler|nursery)\b",
        "review": "Toy and child-product safety rules (small parts, toxicity, sharp edges); third-party testing.",
    },
    "fire_heat": {
        "words": r"\b(fire|flames?|candles?|burns?|burners?|kilns?|furnaces?|hot surfaces?|incandescent|blow ?torch|welding|"
                 r"flammable)\b",
        "review": "Fire and heat risk assessment; surface temperature and flammability tests.",
    },
    "uv_optical": {
        "words": r"\b(uv|ultraviolet|laser (pointer|diode|module)|infrared emitter|high[- ]intensity light)\b",
        "review": "Optical radiation safety (eye and skin exposure limits); specialist review.",
    },
}


def hazard_text(concept: dict) -> str:
    """Descriptive fields only; risk notes and comparisons mention hazards without having them."""
    d = concept.get("detail") or {}
    parts = [concept.get("title"), concept.get("principle"), d.get("how_it_works"), d.get("process"),
             " ".join(d.get("materials") or []), concept.get("business_model")]
    return " ".join(str(p) for p in parts if p)


def detect_hazards(text: str) -> list[dict]:
    low = (text or "").lower()
    out = []
    for cat, h in HAZARDS.items():
        hits = sorted(set(m.group(0) for m in re.finditer(h["words"], low)))
        if hits:
            out.append({"category": cat, "triggers": hits[:6], "mandatory_review": h["review"]})
    return out


PART = obj(["name", "shape", "dims_mm"], name=STR, shape={"type": "string", "enum": ["box", "cylinder", "tube", "sphere", "cone"]},
           dims_mm={"type": "array", "items": NUM}, position_mm={"type": "array", "items": NUM},
           rotate_deg={"type": "array", "items": NUM}, material=STR)
BOM_ITEM = obj(["item", "qty", "unit", "unit_cost_inr", "source"], item=STR, qty=NUM, unit=STR, unit_cost_inr=NUM,
               source={"type": "string", "enum": ["assumption", "observed", "quote"]}, ref=STR, note=STR)

PLAN_SCHEMA = obj(
    ["functional_principles", "technical_requirements", "material_options", "processes", "bom",
     "construction_sequence", "failure_modes", "tests", "maturity"],
    functional_principles=STRS,
    technical_requirements=STRS,
    material_options=arr(obj(["material", "pros", "cons"], material=STR, pros=STR, cons=STR)),
    processes=arr(obj(["process", "in_house", "equipment", "notes"], process=STR, in_house={"type": "boolean"},
                      equipment=STR, equipment_cost_inr={"type": ["number", "null"]}, notes=STR)),
    production_comparison=arr(obj(["method", "fit", "notes"], method=STR, fit={"type": "string",
                                  "enum": ["good", "possible", "poor"]}, notes=STR)),
    prototype_dimensions=STR,
    tolerances=STR,
    parts=arr(PART),
    bom=arr(BOM_ITEM),
    tools_equipment=STRS,
    construction_sequence=STRS,
    assembly=STR,
    safety_requirements=STRS,
    failure_modes=STRS,
    maintenance=STR,
    tests=STRS,
    low_cost_validation=STR,
    maturity={"type": "string", "enum": ["rough_concept", "concept_with_dimensions", "prototype_tested", "validated_design"]},
)


def openscad(concept_title: str, parts: list[dict]) -> str:
    lines = [
        f"// {concept_title}",
        "// CONCEPT GEOMETRY ONLY. Not a validated engineering drawing. Dimensions in mm.",
        "// Generated by the Independent Intelligence Engine from the technical plan's parts list.",
        "$fn = 64;",
        "",
    ]
    for i, p in enumerate(parts):
        name = re.sub(r"[^a-zA-Z0-9_]", "_", p.get("name", f"part{i}")).lower() or f"part{i}"
        d = list(p.get("dims_mm") or [10, 10, 10]) + [10, 10, 10]
        shape = p.get("shape", "box")
        if shape == "box":
            body = f"cube([{d[0]}, {d[1]}, {d[2]}]);"
        elif shape == "cylinder":
            body = f"cylinder(h = {d[1]}, d = {d[0]});"
        elif shape == "tube":
            body = f"difference() {{ cylinder(h = {d[2]}, d = {d[0]}); translate([0, 0, -1]) cylinder(h = {d[2] + 2}, d = {d[1]}); }}"
        elif shape == "sphere":
            body = f"sphere(d = {d[0]});"
        else:
            body = f"cylinder(h = {d[2]}, d1 = {d[0]}, d2 = {d[1]});"
        pos = list(p.get("position_mm") or [0, 0, 0]) + [0, 0, 0]
        rot = list(p.get("rotate_deg") or [0, 0, 0]) + [0, 0, 0]
        lines += [f"// {p.get('name')} ({p.get('material', 'material tbd')})",
                  f"module {name}() {{ {body} }}",
                  f"translate([{pos[0]}, {pos[1]}, {pos[2]}]) rotate([{rot[0]}, {rot[1]}, {rot[2]}]) {name}();", ""]
    return "\n".join(lines)


def bom_csv(bom: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["item", "qty", "unit", "unit_cost_inr", "line_cost_inr", "source", "ref", "note"])
    total = 0.0
    for b in bom:
        line = float(b.get("qty", 0)) * float(b.get("unit_cost_inr", 0))
        total += line
        w.writerow([b.get("item"), b.get("qty"), b.get("unit"), b.get("unit_cost_inr"), round(line, 2),
                    b.get("source"), b.get("ref", ""), b.get("note", "")])
    w.writerow(["TOTAL", "", "", "", round(total, 2), "", "", "currency INR"])
    return buf.getvalue()
