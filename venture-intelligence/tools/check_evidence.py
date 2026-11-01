#!/usr/bin/env python3
"""Check a specialist's markdown file against standards/EVIDENCE.md.

Finds:
  - lines with money, percentages, or large numbers that carry no evidence tag
  - [S#] tags that point to no row in the Sources table
  - Sources rows without a URL or a retrieved date

Prints a tag summary so the Director can see how much rests on sources versus assumptions.

Usage: python3 tools/check_evidence.py <file.md> [more files...]
Exit code 1 if any problem is found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"\[(S\s*\d+(?:\s*[,;]\s*S?\s*\d+)*|I|A|K|H)\]")
S_NUM_RE = re.compile(r"\d+")
NUMERIC_RE = re.compile(
    r"(₹|Rs\.?\s?\d|INR\s?\d|\$\s?\d|USD\s?\d|€\s?\d|£\s?\d|\d\s?%|\d+(\.\d+)?\s?(lakh|crore|million|billion|bn|mn)\b)",
    re.IGNORECASE,
)
SOURCE_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")
URL_RE = re.compile(r"https?://\S+")
DATE_RE = re.compile(r"\b(20\d\d|19\d\d)(-\d\d)?(-\d\d)?\b")


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    problems: list[str] = []

    # locate the Sources section
    src_start = None
    for i, line in enumerate(lines):
        if re.match(r"^#+\s*(\d+\.\s*)?Sources\b", line.strip(), re.IGNORECASE):
            src_start = i
    sources: dict[int, str] = {}
    if src_start is None:
        problems.append("no Sources section found")
    else:
        for line in lines[src_start:]:
            m = SOURCE_ROW_RE.match(line.strip())
            if m:
                n = int(m.group(1))
                sources[n] = line
                if not URL_RE.search(line):
                    problems.append(f"source {n} has no URL")
                if not DATE_RE.search(line):
                    problems.append(f"source {n} has no date")

    counts = {"S": 0, "I": 0, "A": 0, "K": 0}
    in_code = False
    body = lines if src_start is None else lines[:src_start]
    for no, line in enumerate(body, 1):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or s.startswith("#") or re.match(r"^\|?\s*-{3,}", s):
            continue
        tags = TAG_RE.findall(s)
        for t in tags:
            if t.startswith("S"):
                counts["S"] += 1
                for n in S_NUM_RE.findall(t):
                    if sources and int(n) not in sources:
                        problems.append(f"line {no}: [S{n}] has no matching source row")
            else:
                counts[t] += 1
        if NUMERIC_RE.search(s) and not tags:
            problems.append(f"line {no}: number without an evidence tag: {s[:110]}")

    total = sum(counts.values()) or 1
    print(f"{path}: tags S={counts['S']} I={counts['I']} A={counts['A']} K={counts['K']} "
          f"(sourced share {counts['S'] / total:.0%}); sources listed={len(sources)}; problems={len(problems)}")
    return problems


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    bad = 0
    for arg in argv:
        probs = check(Path(arg))
        for p in probs[:60]:
            print("  -", p)
        if len(probs) > 60:
            print(f"  ... and {len(probs) - 60} more")
        bad += bool(probs)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
