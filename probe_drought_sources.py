#!/usr/bin/env python3
"""Find out what the US Drought Monitor will actually serve us.

Nothing here changes any data. It asks a list of candidate URLs what they
return and prints a report, so the next decision is made on what the service
really offers rather than on a guessed URL pattern.

Why this exists: the county percentages we store answer "how much of
Montgomery County is in drought", which is not the question. The question is
whether THIS FARM is. Two things would answer it, and both need a URL we have
confirmed rather than assumed:

  1. The weekly map image for Maryland, so the farm's corner of the county is
     visible instead of averaged away.
  2. The weekly drought polygons, so the farm's own coordinates can be tested
     against them and reduced to a single honest category.

Run it from the repository root:

    python3 probe_drought_sources.py

It needs outbound network. The development container's egress policy blocks
droughtmonitor.unl.edu, so run it on the GitHub Actions runner via the
"Probe drought sources" workflow.
"""
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta

FARM_LAT, FARM_LON = 39.151, -77.462
FIPS = "24031"                      # Montgomery County, MD
UA = {"User-Agent": "RDBF-weather probe (github.com/RDBFarm/rdbf-weather)"}
TIMEOUT = 25


def recent_tuesdays(n=3):
    """USDM maps are valid for Tuesdays and published the Thursday after."""
    d = date.today()
    d -= timedelta(days=(d.weekday() - 1) % 7)      # back to Tuesday
    return [(d - timedelta(weeks=i)).strftime("%Y%m%d") for i in range(n)]


def probe(url, want=None, keep=0):
    """Return (ok, note, body). `want` is a substring the content type must have."""
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read()
            ctype = r.headers.get("Content-Type", "")
            note = f"{r.status} {ctype} {len(body):,}B"
            if want and want not in ctype:
                return False, note + f" (wanted {want})", body[:keep]
            if len(body) < 500:
                return False, note + " (suspiciously small)", body[:keep]
            return True, note, body[:keep] if keep else b""
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}", b""
    except Exception as e:
        return False, f"{type(e).__name__}: {e}", b""


def section(title):
    print(f"\n{'─' * 72}\n{title}\n{'─' * 72}")


def report(label, url, ok, note):
    print(f"  {'OK  ' if ok else 'no  '} {label}")
    print(f"       {url}")
    print(f"       {note}")


def main():
    tuesdays = recent_tuesdays()
    print(f"Probing for {FARM_LAT}, {FARM_LON} · FIPS {FIPS}")
    print(f"Map dates tried: {', '.join(tuesdays)}")

    found = {"images": [], "polygons": [], "county": []}

    # ── 1. The county API we already use, as a baseline ──────────────────────
    # If this fails too, the run has no network and the rest of the report
    # means nothing.
    section("1. County percentages — the source already in fetch_weather.py")
    end = date.today()
    start = end - timedelta(days=21)
    fmt = lambda d: f"{d.month}/{d.day}/{d.year}"    # no leading zeros
    url = ("https://usdmdataservices.unl.edu/api/CountyStatistics/"
           "GetDroughtSeverityStatisticsByAreaPercent"
           f"?aoi={FIPS}&startdate={fmt(start)}&enddate={fmt(end)}&statisticsType=1")
    ok, note, _ = probe(url)
    report("county area percentages", url, ok, note)
    if ok:
        found["county"].append(url)
    else:
        print("\n  !! The known-good endpoint failed. Treat every 'no' below as")
        print("     unproven rather than as a real absence.")

    # ── 2. Map images ────────────────────────────────────────────────────────
    section("2. Map images — candidate direct URLs")
    patterns = [
        ("Maryland, traditional colours", "https://droughtmonitor.unl.edu/data/png/{d}/{d}_MD_trd.png"),
        ("Maryland, no basemap",          "https://droughtmonitor.unl.edu/data/png/{d}/{d}_MD_none.png"),
        ("Maryland, county lines",        "https://droughtmonitor.unl.edu/data/png/{d}/{d}_MD_cnty.png"),
        ("Northeast region",              "https://droughtmonitor.unl.edu/data/png/{d}/{d}_northeast_trd.png"),
        ("CONUS",                         "https://droughtmonitor.unl.edu/data/png/{d}/{d}_usdm.png"),
    ]
    for label, pat in patterns:
        for d in tuesdays:
            url = pat.format(d=d)
            ok, note, _ = probe(url, want="image")
            report(f"{label} · {d}", url, ok, note)
            if ok:
                found["images"].append(url)
                break       # the pattern works; no need to try older dates

    # ── 3. Map images, discovered rather than guessed ────────────────────────
    # If the patterns above all miss, the state page still has to reference the
    # image somewhere. Scrape it rather than keep guessing.
    section("3. Map images — scraped from the state page")
    for page in ("https://droughtmonitor.unl.edu/CurrentMap/StateDroughtMonitor.aspx?MD",
                 "https://droughtmonitor.unl.edu/CurrentMap.aspx"):
        ok, note, body = probe(page, keep=400_000)
        report("page fetch", page, ok, note)
        if not ok:
            continue
        html = body.decode("utf-8", "replace")
        srcs = sorted(set(re.findall(r'(?:src|href)="([^"]+\.(?:png|gif|jpg))"', html, re.I)))
        for s in srcs[:25]:
            full = s if s.startswith("http") else "https://droughtmonitor.unl.edu/" + s.lstrip("/")
            print(f"       image referenced: {full}")
            found["images"].append(full)
        if not srcs:
            print("       no image references found in the markup")

    # ── 4. Polygons, so the farm's own point can be tested ───────────────────
    # This is the one worth having. A polygon set reduces to a single category
    # for these coordinates: "the farm is in D0", not "4.66% of the county is
    # in D1". Point-in-polygon is a dozen lines of pure Python, no dependency.
    section("4. Drought polygons — for a point query at the farm")
    candidates = [
        ("weekly GeoJSON", "https://droughtmonitor.unl.edu/data/json/usdm_{d}.json"),
        ("current GeoJSON", "https://droughtmonitor.unl.edu/data/json/usdm_current.json"),
        ("weekly shapefile zip", "https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_{d}_M.zip"),
    ]
    for label, pat in candidates:
        urls = [pat.format(d=d) for d in tuesdays] if "{d}" in pat else [pat]
        for url in urls:
            ok, note, _ = probe(url)
            report(f"{label}", url, ok, note)
            if ok:
                found["polygons"].append(url)
                break

    # ArcGIS hosts the USDM layers and supports a point query directly, which
    # would save downloading polygons at all. Ask the catalogue where they are
    # rather than hardcoding an organisation id that may change.
    section("5. Drought polygons — ArcGIS services, via the catalogue")
    search = ("https://www.arcgis.com/sharing/rest/search?"
              + urllib.parse.urlencode({
                  "q": 'title:"USDM" type:"Feature Service"',
                  "f": "json", "num": 10}))
    ok, note, body = probe(search, keep=200_000)
    report("catalogue search", search, ok, note)
    if ok:
        try:
            for item in json.loads(body).get("results", []):
                print(f"       {item.get('title')}  [{item.get('owner')}]")
                print(f"         {item.get('url')}")
                if item.get("url"):
                    found["polygons"].append(item["url"])
        except Exception as e:
            print(f"       could not parse: {type(e).__name__}: {e}")

    # ── Verdict ──────────────────────────────────────────────────────────────
    section("What this means")
    if found["images"]:
        print(f"  {len(found['images'])} image URL(s) reachable — a real map can replace the")
        print("  county percentage chart. First one:")
        print(f"    {found['images'][0]}")
    else:
        print("  No map image reachable. Either the patterns are wrong and the")
        print("  scrape found nothing, or the host is blocked from this runner.")
    print()
    if found["polygons"]:
        print(f"  {len(found['polygons'])} polygon source(s) reachable — the farm's own")
        print("  coordinates can be reduced to a single drought category. This is")
        print("  the better answer; the map is the picture of it.")
    else:
        print("  No polygon source reachable — a point query is not available yet,")
        print("  so the county percentage stays the only machine-readable figure.")
    print()
    print("  Nothing was changed. This run only asked questions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
