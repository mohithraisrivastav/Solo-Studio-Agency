"""Research connectors using public, documented APIs.

Each connector returns Doc objects. None of them invent content: when a service
is unreachable they raise FetchError, and the engine records a research gap.
Parsing follows each service's documented response format.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from urllib.parse import quote, urlparse

from ..text import strip_html
from .http import Fetcher, FetchError


@dataclass
class Doc:
    url: str
    title: str
    content: str
    source_type: str
    publisher: str | None = None
    published_at: str | None = None
    meta: dict = field(default_factory=dict)


class Connector:
    name = "base"
    source_type = "web_page"
    description = ""
    secret: str | None = None  # name in Settings.secret()
    covers: tuple[str, ...] = ()  # research purposes this connector suits

    def __init__(self, fetcher: Fetcher, settings):
        self.fetcher = fetcher
        self.settings = settings

    def configured(self) -> tuple[bool, str]:
        if self.secret and not self.settings.secret(self.secret):
            return False, f"needs {self.secret} credential in environment"
        return True, "ready"

    def search(self, query: str, limit: int = 5, **params) -> list[Doc]:
        raise NotImplementedError

    def probe(self) -> tuple[bool, str]:
        ok, why = self.configured()
        if not ok:
            return ok, why
        try:
            self.search("material", 1)
            return True, "reachable"
        except FetchError as e:
            return False, f"{e.kind}: {e}"


class Wikipedia(Connector):
    name = "wikipedia"
    source_type = "encyclopedia"
    description = "Wikipedia search and page introductions (MediaWiki API)"
    covers = ("background", "technical", "market", "competitor")
    API = "https://en.wikipedia.org/w/api.php"

    def search(self, query, limit=5, **params):
        data = self.fetcher.get_json(self.API, {"action": "query", "list": "search", "srsearch": query,
                                                "srlimit": limit, "format": "json", "utf8": 1})
        hits = data.get("query", {}).get("search", [])
        if not hits:
            return []
        ids = "|".join(str(h["pageid"]) for h in hits)
        pages = self.fetcher.get_json(self.API, {"action": "query", "prop": "extracts|info", "exintro": 1,
                                                 "explaintext": 1, "inprop": "url", "pageids": ids,
                                                 "exlimit": 20, "format": "json"})
        return parse_wikipedia_pages(pages)


def parse_wikipedia_pages(pages: dict) -> list[Doc]:
    out = []
    for p in pages.get("query", {}).get("pages", {}).values():
        if not p.get("extract"):
            continue
        out.append(Doc(url=p.get("fullurl") or f"https://en.wikipedia.org/?curid={p.get('pageid')}",
                       title=p.get("title", ""), content=p["extract"][:6000], source_type="encyclopedia",
                       publisher="Wikipedia", published_at=(p.get("touched") or "")[:10] or None,
                       meta={"note": "published_at is the last edit date"}))
    return out


class OpenAlex(Connector):
    name = "openalex"
    source_type = "academic"
    description = "OpenAlex scholarly works (free, no key)"
    covers = ("technical", "emerging", "prior_art", "market")
    API = "https://api.openalex.org/works"

    def search(self, query, limit=5, **params):
        p = {"search": query, "per-page": limit}
        if self.settings.contact_email:
            p["mailto"] = self.settings.contact_email
        if params.get("from_year"):
            p["filter"] = f"from_publication_date:{params['from_year']}-01-01"
        return parse_openalex(self.fetcher.get_json(self.API, p))


def openalex_abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos: list[tuple[int, str]] = []
    for word, idxs in inv.items():
        for i in idxs:
            pos.append((i, word))
    return " ".join(w for _, w in sorted(pos))


def parse_openalex(data: dict) -> list[Doc]:
    out = []
    for w in data.get("results", []):
        loc = w.get("primary_location") or {}
        src = (loc.get("source") or {}).get("display_name")
        url = w.get("doi") or loc.get("landing_page_url") or w.get("id")
        abstract = openalex_abstract(w.get("abstract_inverted_index"))
        out.append(Doc(url=url, title=w.get("display_name") or w.get("title") or "", content=abstract,
                       source_type="academic", publisher=src or "OpenAlex", published_at=w.get("publication_date"),
                       meta={"cited_by": w.get("cited_by_count"), "type": w.get("type"), "openalex_id": w.get("id")}))
    return out


class Crossref(Connector):
    name = "crossref"
    source_type = "academic"
    description = "Crossref metadata for published works"
    covers = ("technical", "prior_art")
    API = "https://api.crossref.org/works"

    def search(self, query, limit=5, **params):
        p = {"query": query, "rows": limit}
        if self.settings.contact_email:
            p["mailto"] = self.settings.contact_email
        return parse_crossref(self.fetcher.get_json(self.API, p))


def _crossref_date(item: dict) -> str | None:
    for k in ("published", "published-print", "published-online", "issued", "created"):
        parts = (item.get(k) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            dp = parts[0] + [1, 1]
            try:
                return _dt.date(int(dp[0]), int(dp[1] or 1), int(dp[2] or 1)).isoformat()
            except (ValueError, TypeError):
                return str(dp[0])
    return None


def parse_crossref(data: dict) -> list[Doc]:
    out = []
    for it in data.get("message", {}).get("items", []):
        title = (it.get("title") or [""])[0]
        venue = (it.get("container-title") or [None])[0]
        out.append(Doc(url=it.get("URL") or f"https://doi.org/{it.get('DOI')}", title=title,
                       content=strip_html(it.get("abstract") or ""), source_type="academic",
                       publisher=venue or it.get("publisher"), published_at=_crossref_date(it),
                       meta={"doi": it.get("DOI"), "type": it.get("type")}))
    return out


class Arxiv(Connector):
    name = "arxiv"
    source_type = "preprint"
    description = "arXiv preprints (Atom API)"
    covers = ("technical", "emerging", "prior_art")
    API = "https://export.arxiv.org/api/query"

    def search(self, query, limit=5, **params):
        words = [w for w in re.findall(r"[A-Za-z0-9]+", query)][:6]
        sq = " AND ".join(f"all:{w}" for w in words) or "all:materials"
        data = self.fetcher.get(self.API, {"search_query": sq, "start": 0, "max_results": limit})
        return parse_arxiv(data["text"])


def parse_arxiv(xml_text: str) -> list[Doc]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    out = []
    for e in root.findall("a:entry", ns):
        title = " ".join((e.findtext("a:title", "", ns) or "").split())
        summary = " ".join((e.findtext("a:summary", "", ns) or "").split())
        out.append(Doc(url=(e.findtext("a:id", "", ns) or "").strip(), title=title, content=summary,
                       source_type="preprint", publisher="arXiv",
                       published_at=(e.findtext("a:published", "", ns) or "")[:10] or None,
                       meta={"note": "preprint, not peer reviewed"}))
    return out


class SemanticScholar(Connector):
    name = "semantic_scholar"
    source_type = "academic"
    description = "Semantic Scholar paper search"
    covers = ("technical", "prior_art", "emerging")
    API = "https://api.semanticscholar.org/graph/v1/paper/search"

    def search(self, query, limit=5, **params):
        data = self.fetcher.get_json(self.API, {"query": query, "limit": limit,
                                                "fields": "title,abstract,year,url,venue,publicationDate,citationCount"})
        return parse_semantic_scholar(data)


def parse_semantic_scholar(data: dict) -> list[Doc]:
    out = []
    for p in data.get("data", []) or []:
        out.append(Doc(url=p.get("url") or "", title=p.get("title") or "", content=p.get("abstract") or "",
                       source_type="academic", publisher=p.get("venue") or "Semantic Scholar",
                       published_at=p.get("publicationDate") or (str(p["year"]) if p.get("year") else None),
                       meta={"cited_by": p.get("citationCount")}))
    return out


STACK_SITES = {
    "home": ["diy"], "construction": ["diy", "engineering"], "woodworking": ["woodworking"],
    "food": ["cooking"], "hospitality": ["travel", "cooking"], "travel": ["travel"], "finance": ["money"],
    "agriculture": ["gardening"], "gardening": ["gardening"], "manufacturing": ["engineering", "3dprinting"],
    "electronics": ["electronics"], "photography": ["photo"], "cycling": ["bicycles"], "pets": ["pets"],
    "parenting": ["parenting"], "education": ["academia", "matheducators"], "outdoors": ["outdoors"],
    "work": ["workplace", "freelancing"], "law": ["law"], "software": ["softwareengineering"],
    "brewing": ["homebrew"], "music": ["music"], "sustainability": ["sustainability"],
    "health_fitness": ["fitness"], "vehicles": ["mechanics"], "textiles": ["crafts"], "crafts": ["crafts"],
}


class StackExchange(Connector):
    name = "stackexchange"
    source_type = "forum"
    description = "Stack Exchange questions (recurring practical problems, with votes and views)"
    covers = ("problem", "demand")
    API = "https://api.stackexchange.com/2.3/search/advanced"

    def search(self, query, limit=5, **params):
        site = params.get("site") or "diy"
        data = self.fetcher.get_json(self.API, {"order": "desc", "sort": params.get("sort", "relevance"),
                                                "q": query, "site": site, "pagesize": limit, "filter": "withbody"})
        return parse_stackexchange(data, site)


def parse_stackexchange(data: dict, site: str) -> list[Doc]:
    out = []
    for q in data.get("items", []):
        title = strip_html(q.get("title", ""))
        created = q.get("creation_date")
        out.append(Doc(url=q.get("link", ""), title=title,
                       content=title + "\n" + strip_html(q.get("body", ""))[:4000], source_type="forum",
                       publisher=f"{site}.stackexchange.com",
                       published_at=_dt.datetime.fromtimestamp(created, _dt.timezone.utc).date().isoformat() if created else None,
                       meta={"score": q.get("score"), "views": q.get("view_count"), "answers": q.get("answer_count"),
                             "tags": q.get("tags", []), "site": site}))
    return out


class HackerNews(Connector):
    name = "hackernews"
    source_type = "forum"
    description = "Hacker News stories and comments (Algolia API)"
    covers = ("problem", "emerging", "competitor")
    API = "https://hn.algolia.com/api/v1/search"

    def search(self, query, limit=5, **params):
        data = self.fetcher.get_json(self.API, {"query": query, "tags": params.get("tags", "story"),
                                                "hitsPerPage": limit})
        return parse_hn(data)


def parse_hn(data: dict) -> list[Doc]:
    out = []
    for h in data.get("hits", []):
        text = strip_html(h.get("story_text") or h.get("comment_text") or "")
        title = h.get("title") or h.get("story_title") or text[:80]
        out.append(Doc(url=f"https://news.ycombinator.com/item?id={h.get('objectID')}", title=title or "",
                       content=(title or "") + "\n" + text[:4000], source_type="forum", publisher="Hacker News",
                       published_at=(h.get("created_at") or "")[:10] or None,
                       meta={"points": h.get("points"), "comments": h.get("num_comments"), "linked_url": h.get("url")}))
    return out


class WorldBank(Connector):
    name = "worldbank"
    source_type = "government_data"
    description = "World Bank indicators. Query format: 'indicator:CODE country:ISO3'"
    covers = ("market",)
    API = "https://api.worldbank.org/v2/country/{country}/indicator/{code}"

    def search(self, query, limit=5, **params):
        m_ind = re.search(r"indicator:([A-Z0-9_.]+)", query)
        m_cty = re.search(r"country:([A-Za-z]{3})", query)
        if not m_ind:
            return []
        code, country = m_ind.group(1), (m_cty.group(1) if m_cty else "IND").upper()
        data = self.fetcher.get_json(self.API.format(country=country, code=code),
                                     {"format": "json", "per_page": 10, "mrv": 5})
        return parse_worldbank(data, code, country)

    def probe(self):
        try:
            self.search("indicator:NY.GDP.PCAP.CD country:IND")
            return True, "reachable"
        except FetchError as e:
            return False, f"{e.kind}: {e}"


def parse_worldbank(data, code: str, country: str) -> list[Doc]:
    if not isinstance(data, list) or len(data) < 2 or not data[1]:
        return []
    rows = [r for r in data[1] if r.get("value") is not None]
    if not rows:
        return []
    name = rows[0]["indicator"]["value"]
    cname = rows[0]["country"]["value"]
    lines = [f"{r['date']}: {r['value']}" for r in rows]
    return [Doc(url=f"https://data.worldbank.org/indicator/{code}?locations={country[:2]}",
                title=f"{name} - {cname}", content=f"{name} for {cname}. " + "; ".join(lines),
                source_type="government_data", publisher="World Bank", published_at=f"{rows[0]['date']}-12-31",
                meta={"indicator": code, "country": country, "values": {r["date"]: r["value"] for r in rows}})]


class SearXNG(Connector):
    name = "searxng"
    source_type = "search_snippet"
    description = "Self-hosted SearXNG web search (set IIE_SEARXNG_URL)"
    secret = "searxng"
    covers = ("problem", "market", "price", "competitor", "prior_art", "background")

    def search(self, query, limit=5, **params):
        base = self.settings.secret("searxng").rstrip("/")
        data = self.fetcher.get_json(base + "/search", {"q": query, "format": "json"})
        return parse_web_results([{"url": r.get("url"), "title": r.get("title"), "snippet": r.get("content"),
                                   "date": r.get("publishedDate")} for r in data.get("results", [])][:limit])


class Brave(Connector):
    name = "brave"
    source_type = "search_snippet"
    description = "Brave Search API (set IIE_BRAVE_API_KEY)"
    secret = "brave"
    covers = ("problem", "market", "price", "competitor", "prior_art", "background")
    API = "https://api.search.brave.com/res/v1/web/search"

    def search(self, query, limit=5, **params):
        data = self.fetcher.get_json(self.API, {"q": query, "count": limit},
                                     headers={"Accept": "application/json",
                                              "X-Subscription-Token": self.settings.secret("brave")})
        return parse_web_results([{"url": r.get("url"), "title": r.get("title"), "snippet": r.get("description"),
                                   "date": r.get("page_age")} for r in data.get("web", {}).get("results", [])])


def parse_web_results(items: list[dict]) -> list[Doc]:
    out = []
    for r in items:
        if not r.get("url"):
            continue
        out.append(Doc(url=r["url"], title=strip_html(r.get("title") or ""), content=strip_html(r.get("snippet") or ""),
                       source_type="search_snippet", publisher=urlparse(r["url"]).hostname,
                       published_at=(r.get("date") or "")[:10] or None,
                       meta={"note": "search snippet only; open the page to verify"}))
    return out


class PatentsView(Connector):
    name = "patentsview"
    source_type = "patent"
    description = "USPTO PatentsView PatentSearch API (set IIE_PATENTSVIEW_API_KEY). Endpoint may change; verify."
    secret = "patentsview"
    covers = ("prior_art",)
    API = "https://search.patentsview.org/api/v1/patent/"

    def search(self, query, limit=5, **params):
        q = {"_text_any": {"patent_abstract": query}}
        f = ["patent_id", "patent_title", "patent_abstract", "patent_date"]
        data = self.fetcher.get_json(self.API, {"q": json.dumps(q), "f": json.dumps(f),
                                                "o": json.dumps({"size": limit})},
                                     headers={"X-Api-Key": self.settings.secret("patentsview")})
        return parse_patentsview(data)


def parse_patentsview(data: dict) -> list[Doc]:
    out = []
    for p in data.get("patents", []) or []:
        pid = p.get("patent_id")
        out.append(Doc(url=f"https://patents.google.com/patent/US{pid}", title=p.get("patent_title") or "",
                       content=p.get("patent_abstract") or "", source_type="patent", publisher="USPTO (PatentsView)",
                       published_at=p.get("patent_date"), meta={"patent_id": pid}))
    return out


def fetch_page(fetcher: Fetcher, url: str, source_type: str = "web_page") -> Doc:
    """Fetch one public page (robots.txt respected) and keep its visible text."""
    data = fetcher.get(url, check_robots=True)
    raw = data["text"]
    title_m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.IGNORECASE | re.DOTALL)
    date_m = re.search(r'(?:article:published_time|datePublished)"?\s*(?:content=|:)\s*"(\d{4}-\d{2}-\d{2})', raw)
    text = strip_html(raw) if "html" in data["content_type"] or raw.lstrip().startswith("<") else raw
    return Doc(url=data["url"], title=strip_html(title_m.group(1)) if title_m else url, content=text[:20000],
               source_type=source_type, publisher=urlparse(data["url"]).hostname,
               published_at=date_m.group(1) if date_m else None)


REGISTRY: dict[str, type[Connector]] = {
    c.name: c for c in (Wikipedia, OpenAlex, Crossref, Arxiv, SemanticScholar, StackExchange, HackerNews,
                        WorldBank, SearXNG, Brave, PatentsView)
}

PURPOSE_DEFAULTS = {
    "problem": ["stackexchange", "hackernews", "searxng", "brave"],
    "demand": ["stackexchange", "hackernews", "searxng", "brave"],
    "market": ["wikipedia", "openalex", "worldbank", "searxng", "brave"],
    "technical": ["openalex", "semantic_scholar", "arxiv", "crossref", "wikipedia"],
    "emerging": ["openalex", "arxiv", "hackernews"],
    "prior_art": ["patentsview", "openalex", "semantic_scholar", "searxng", "brave", "wikipedia"],
    "competitor": ["searxng", "brave", "wikipedia", "hackernews"],
    "price": ["searxng", "brave"],
    "background": ["wikipedia", "openalex"],
}


def build_connectors(fetcher: Fetcher, settings) -> dict[str, Connector]:
    return {n: REGISTRY[n](fetcher, settings) for n in settings.connectors if n in REGISTRY}


def quote_url(s: str) -> str:
    return quote(s, safe="")
