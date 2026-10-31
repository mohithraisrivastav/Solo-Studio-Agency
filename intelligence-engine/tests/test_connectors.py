"""Connector parsing against documented response shapes, and honest failure handling."""
import httpx
import pytest

from iie.research.connectors import (Arxiv, StackExchange, Wikipedia, openalex_abstract, parse_crossref, parse_hn,
                                     parse_openalex, parse_patentsview, parse_semantic_scholar, parse_worldbank)
from iie.research.http import Fetcher, FetchError


def test_openalex_abstract_reconstruction():
    assert openalex_abstract({"chains": [1], "Steel": [0], "rust": [2]}) == "Steel chains rust"
    docs = parse_openalex({"results": [{"id": "W1", "display_name": "T", "publication_date": "2024-01-01",
                                        "abstract_inverted_index": {"a": [0]}, "primary_location": None}]})
    assert docs[0].url == "W1" and docs[0].published_at == "2024-01-01"


def test_crossref_semantic_hn_patents_worldbank_parsers():
    cr = parse_crossref({"message": {"items": [{"DOI": "10.1/x", "title": ["Title"], "container-title": ["J"],
                                                 "published": {"date-parts": [[2021, 3]]}, "abstract": "<jats:p>Abs</jats:p>"}]}})
    assert cr[0].published_at == "2021-03-01" and cr[0].content == "Abs"
    ss = parse_semantic_scholar({"data": [{"title": "P", "abstract": None, "year": 2020, "url": "https://s2/x"}]})
    assert ss[0].published_at == "2020"
    hn = parse_hn({"hits": [{"objectID": "5", "title": "Ask HN", "points": 3, "created_at": "2024-02-02T00:00:00Z"}]})
    assert hn[0].url.endswith("id=5") and hn[0].meta["points"] == 3
    pv = parse_patentsview({"patents": [{"patent_id": "123", "patent_title": "Chain guard", "patent_date": "2019-05-01"}]})
    assert pv[0].url.endswith("US123") and pv[0].source_type == "patent"
    wb = parse_worldbank([{}, [{"indicator": {"value": "GDP"}, "country": {"value": "India"}, "date": "2024", "value": 2600},
                                {"indicator": {"value": "GDP"}, "country": {"value": "India"}, "date": "2023", "value": None}]],
                         "NY.GDP.PCAP.CD", "IND")
    assert "2024: 2600" in wb[0].content


def test_arxiv_atom_parsing(settings):
    xml = ('<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/abs/1</id><title>A  title</title>'
           '<summary> Sum </summary><published>2024-04-01T00:00:00Z</published></entry></feed>')
    f = Fetcher(settings, transport=httpx.MockTransport(lambda r: httpx.Response(200, text=xml)), use_cache=False)
    docs = Arxiv(f, settings).search("x", 1)
    assert docs[0].title == "A title" and docs[0].published_at == "2024-04-01"


def test_wikipedia_and_stackexchange_through_fetcher(settings, transport):
    f = Fetcher(settings, transport=transport, use_cache=False)
    w = Wikipedia(f, settings).search("bicycle chain", 1)
    assert w and w[0].publisher == "Wikipedia" and "corrode" in w[0].content
    se = StackExchange(f, settings).search("rust", 2, site="bicycles")
    assert se[0].meta["score"] == 57 and se[0].source_type == "forum"


def test_proxy_refusal_becomes_network_blocked(settings):
    def refuse(req):
        raise httpx.ProxyError("403 Forbidden")
    f = Fetcher(settings, transport=httpx.MockTransport(refuse), use_cache=False)
    with pytest.raises(FetchError) as ei:
        Wikipedia(f, settings).search("x")
    assert ei.value.kind == "network_blocked"


def test_robots_txt_is_respected(settings):
    def h(req):
        if req.url.path == "/robots.txt":
            return httpx.Response(200, text="User-agent: *\nDisallow: /private")
        return httpx.Response(200, text="<html><title>t</title>ok</html>", headers={"content-type": "text/html"})
    f = Fetcher(settings, transport=httpx.MockTransport(h), use_cache=False)
    from iie.research.connectors import fetch_page
    assert fetch_page(f, "https://shop.example.com/public").title == "t"
    with pytest.raises(FetchError) as ei:
        fetch_page(f, "https://shop.example.com/private/item")
    assert ei.value.kind == "robots"


def test_keyed_connectors_report_missing_credentials(settings):
    from iie.research.connectors import Brave, PatentsView
    f = Fetcher(settings, use_cache=False)
    assert Brave(f, settings).configured()[0] is False
    assert PatentsView(f, settings).configured()[0] is False
