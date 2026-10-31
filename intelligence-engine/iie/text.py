"""Text utilities: tokenising, TF-IDF similarity, quote checks, cosmetic-difference detection."""
from __future__ import annotations

import html
import math
import re
from collections import Counter
from html.parser import HTMLParser

STOPWORDS = frozenset(
    """a an and are as at be been but by can could do does for from had has have how i if in into is it its
    of on or our so such than that the their them then there these they this those to too very was we were
    what when where which while who why will with would you your not no yes also more most other some any
    each about over under between using use used via per one two three new make made like just only
    than it's i'm i've don't can't there's""".split()
)

COSMETIC_TERMS = frozenset(
    """red blue green yellow black white grey gray gold golden silver bronze copper brass pink purple orange
    brown beige cream ivory teal navy matte gloss glossy satin polished brushed textured smooth color colour
    colors colours colourway finish finishes shade tone hue palette small medium large larger smaller tall
    taller short shorter wide wider narrow mini compact xl size sizes sized dimension dimensions inch inches
    cm mm metre meter version edition style styled styling modern classic minimal minimalist vintage retro
    rustic elegant premium luxury deluxe pro plus lite name named branded brand logo pattern patterned motif
    decorative decoration ornamental look looks aesthetic aesthetics variant variants option options""".split()
)


def strip_html(text: str) -> str:
    class _P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.parts: list[str] = []
            self.skip = 0

        def handle_starttag(self, tag, attrs):
            if tag in ("script", "style", "noscript", "svg", "head"):
                self.skip += 1
            elif tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "tr", "section", "article"):
                self.parts.append("\n")

        def handle_endtag(self, tag):
            if tag in ("script", "style", "noscript", "svg", "head") and self.skip:
                self.skip -= 1

        def handle_data(self, data):
            if not self.skip:
                self.parts.append(data)

    p = _P()
    try:
        p.feed(text or "")
        p.close()
    except Exception:
        return re.sub(r"<[^>]+>", " ", html.unescape(text or ""))
    out = "".join(p.parts)
    out = re.sub(r"[ \t\r\f\v]+", " ", out)
    out = re.sub(r"\n\s*\n+", "\n", out)
    return out.strip()


def _stem(w: str) -> str:
    for suf in ("ations", "ation", "ings", "ing", "edly", "ed", "ies", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)] + ("y" if suf == "ies" else "")
    return w


def tokens(text: str, keep_stop: bool = False) -> list[str]:
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return [_stem(w) for w in words if (keep_stop or w not in STOPWORDS) and len(w) > 1]


class TfIdf:
    def __init__(self, docs: list[str]):
        self.docs_tokens = [tokens(d) for d in docs]
        n = len(docs)
        df: Counter[str] = Counter()
        for t in self.docs_tokens:
            df.update(set(t))
        self.idf = {w: math.log((1 + n) / (1 + c)) + 1.0 for w, c in df.items()}
        self.vectors = [self._vec(t) for t in self.docs_tokens]

    def _vec(self, toks: list[str]) -> dict[str, float]:
        tf = Counter(toks)
        v = {w: (1 + math.log(c)) * self.idf.get(w, 1.0) for w, c in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {w: x / norm for w, x in v.items()}

    def vector(self, text: str) -> dict[str, float]:
        return self._vec(tokens(text))

    @staticmethod
    def cosine(a: dict[str, float], b: dict[str, float]) -> float:
        if len(a) > len(b):
            a, b = b, a
        return sum(x * b.get(w, 0.0) for w, x in a.items())

    def sim(self, i: int, j: int) -> float:
        return self.cosine(self.vectors[i], self.vectors[j])


def similarity(a: str, b: str, corpus: list[str] | None = None) -> float:
    docs = [a, b] + list(corpus or [])
    t = TfIdf(docs)
    return t.sim(0, 1)


def jaccard(a: str, b: str) -> float:
    sa, sb = set(tokens(a)), set(tokens(b))
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def normalize_for_quote(text: str) -> str:
    t = (text or "").lower()
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-").replace(" ", " ")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def quote_in_source(quote: str, content: str) -> bool:
    """True if the quote appears verbatim (after normalising whitespace, case, and typographic marks).

    Ellipses split a quote into parts that must appear in order.
    """
    q = normalize_for_quote(quote)
    c = normalize_for_quote(content)
    if len(q) < 8:
        return False
    parts = [p.strip(" .") for p in re.split(r"\.\.\.|…", q) if p.strip(" .")]
    pos = 0
    for p in parts:
        i = c.find(p, pos)
        if i < 0:
            return False
        pos = i + len(p)
    return True


def cosmetic_only_difference(a: str, b: str) -> tuple[bool, list[str]]:
    """Decide whether two concept descriptions differ only in cosmetic terms.

    Returns (is_cosmetic, differing_terms). A pair is cosmetic when the texts share
    most content words and nearly all differing words are colour, size, finish,
    style, or naming words.
    """
    ta, tb = set(tokens(a)), set(tokens(b))
    if not ta or not tb:
        return False, []
    shared = ta & tb
    diff = (ta ^ tb)
    if not diff:
        return True, []
    cosmetic = {w for w in diff if w in COSMETIC_TERMS or w.isdigit() or _stem(w) in COSMETIC_TERMS}
    overlap = len(shared) / max(1, min(len(ta), len(tb)))
    substantive = sorted(diff - cosmetic)
    return (overlap >= 0.6 and len(substantive) <= max(2, int(0.15 * len(diff)))), substantive


INJECTION_PATTERNS = [
    r"ignore (all |any )?(previous|prior|above) (instructions|prompts)",
    r"disregard (the )?(system|previous) (prompt|instructions)",
    r"you are now ",
    r"system prompt",
    r"act as (an? )?(admin|developer|system)",
    r"<\s*/?\s*(system|assistant|instructions?)\s*>",
    r"send (this|the) (data|file|credentials)",
]


def injection_suspect(text: str) -> bool:
    low = (text or "").lower()
    return any(re.search(p, low) for p in INJECTION_PATTERNS)


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|\n+", text or "")
    return [p.strip() for p in parts if len(p.strip()) > 15]
