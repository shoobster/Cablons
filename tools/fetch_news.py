#!/usr/bin/env python3
"""Fetches security headlines and writes assets/news.json.
Run by .github/workflows/news.yml on a schedule. Standard library only.
Handles RSS 2.0 and Atom feeds."""
import json, os, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

FEED = "https://feeds.feedburner.com/TheHackersNews?format=xml"
SOURCE = "The Hacker News"
SOURCE_URL = "https://thehackernews.com/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "news.json")
ATOM = "{http://www.w3.org/2005/Atom}"
LIMIT = 12

def iso_date(text):
    text = (text or "").strip()
    if not text:
        return ""
    try:
        return parsedate_to_datetime(text).date().isoformat()   # RFC 822 (RSS)
    except Exception:
        return text[:10]                                         # ISO (Atom)

def parse(root):
    items = []
    if root.tag == "rss" or root.find("channel") is not None:
        for it in root.iter("item"):
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            date = iso_date(it.findtext("pubDate"))
            if title and link:
                items.append({"title": title, "url": link, "date": date})
    else:
        for e in root.iter(ATOM + "entry"):
            title = (e.findtext(ATOM + "title") or "").strip()
            link = ""
            for l in e.findall(ATOM + "link"):
                if l.get("rel") in (None, "alternate"):
                    link = l.get("href", ""); break
            date = iso_date(e.findtext(ATOM + "updated") or e.findtext(ATOM + "published"))
            if title and link:
                items.append({"title": title, "url": link, "date": date})
    return items[:LIMIT]

def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "cablons-site-news/1.0 (+https://www.cablons.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        root = ET.fromstring(r.read())
    items = parse(root)
    if not items:
        sys.exit("feed returned no entries; leaving existing news.json untouched")
    data = {"source": SOURCE, "source_url": SOURCE_URL,
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "items": items}
    with open(OUT, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {len(items)} items from {SOURCE}")

if __name__ == "__main__":
    main()
