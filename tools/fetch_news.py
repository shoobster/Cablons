#!/usr/bin/env python3
"""Fetches The Register security headlines and writes assets/news.json.
Run by .github/workflows/news.yml on a schedule. Standard library only."""
import json, os, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

FEED = "https://www.theregister.com/security/headlines.atom"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "news.json")
NS = {"a": "http://www.w3.org/2005/Atom"}
LIMIT = 12

def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "cablons-site-news/1.0 (+https://www.cablons.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    items = []
    for e in root.findall("a:entry", NS):
        title = (e.findtext("a:title", default="", namespaces=NS) or "").strip()
        link = ""
        for l in e.findall("a:link", NS):
            if l.get("rel") in (None, "alternate"):
                link = l.get("href", ""); break
        updated = (e.findtext("a:updated", default="", namespaces=NS) or "")[:10]
        if title and link:
            items.append({"title": title, "url": link, "date": updated})
        if len(items) >= LIMIT:
            break
    if not items:
        sys.exit("feed returned no entries; leaving existing news.json untouched")
    data = {"source": "The Register", "source_url": "https://www.theregister.com/security/",
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "items": items}
    with open(OUT, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {len(items)} items")

if __name__ == "__main__":
    main()
