#!/usr/bin/env python3
"""Fetch a page (and optional extra pages on the same institution domain),
extract <a href> links, classify them as internal vs external, dofollow vs
nofollow, and report unique EXTERNAL company domains (dofollow) after filtering.

Usage: linkcheck.py <institution_registrable_domain> <url> [url2 ...]
"""
import sys, re, urllib.request, urllib.error, ssl, gzip, io
import tldextract
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"

# Domains that are never "company sponsors" — social, infra, gov, edu-generic, CDNs
JUNK_DOMAINS = {
    "facebook.com","twitter.com","x.com","instagram.com","linkedin.com","youtube.com",
    "youtu.be","xing.com","tiktok.com","vimeo.com","flickr.com","pinterest.com",
    "wikipedia.org","google.com","googleapis.com","gstatic.com","gmpg.org","w3.org",
    "schema.org","creativecommons.org","mastodon.social","threads.net","whatsapp.com",
    "bsky.app","researchgate.net","orcid.org","doi.org","dfg.de","bmbf.de","europa.eu",
    "datenschutz.de","adobe.com","apple.com","microsoft.com","mozilla.org",
    "deutschlandstipendium.de","stifterverband.org","stifterverband.de",
    "hochschulkompass.de","studienwahl.de","bund.de","jquery.com","cookiebot.com",
    "openstreetmap.org","maps.google.com","goo.gl","bit.ly","t.me","telegram.org",
    "addtoany.com","sharethis.com","paypal.com","sofortueberweisung.de",
}

def reg_domain(host):
    ext = tldextract.extract(host)
    if not ext.domain or not ext.suffix:
        return None
    return f"{ext.domain}.{ext.suffix}".lower()

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding":"gzip"})
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            data = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                data = gzip.decompress(data)
            enc = r.headers.get_content_charset() or "utf-8"
            return data.decode(enc, errors="replace"), r.geturl()
    except Exception as e:
        return None, f"ERROR: {e}"

def analyze(inst_domain, urls):
    inst_domain = inst_domain.lower()
    # company_domain -> {dofollow:bool, samples:set(text), hrefs:set}
    companies = {}
    fetched = []
    for url in urls:
        html, final = fetch(url)
        if html is None:
            fetched.append((url, final))
            continue
        fetched.append((url, f"OK ({len(html)} bytes) -> {final}"))
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if not href.lower().startswith("http"):
                continue
            m = re.match(r"https?://([^/]+)", href)
            if not m:
                continue
            host = m.group(1).split(":")[0]
            rd = reg_domain(host)
            if not rd:
                continue
            if rd == inst_domain:
                continue  # internal
            if rd in JUNK_DOMAINS:
                continue
            rel = a.get("rel") or []
            rel = [x.lower() for x in rel]
            dofollow = "nofollow" not in rel
            txt = a.get_text(" ", strip=True)[:60]
            e = companies.setdefault(rd, {"dofollow": False, "texts": set(), "n": 0})
            if dofollow:
                e["dofollow"] = True
            if txt:
                e["texts"].add(txt)
            e["n"] += 1
    return fetched, companies

def main():
    inst = sys.argv[1]
    urls = sys.argv[2:]
    fetched, companies = analyze(inst, urls)
    print(f"### Institution domain: {inst}")
    for u, status in fetched:
        print(f"  FETCH {u}\n        {status}")
    dofollow = {k:v for k,v in companies.items() if v["dofollow"]}
    nofollow_only = {k:v for k,v in companies.items() if not v["dofollow"]}
    print(f"\n### EXTERNAL company domains (dofollow): {len(dofollow)}")
    for d in sorted(dofollow):
        t = "; ".join(sorted(companies[d]["texts"]))[:80]
        print(f"  [dofollow x{companies[d]['n']}] {d}   {t}")
    print(f"\n### EXTERNAL company domains (NOFOLLOW only): {len(nofollow_only)}")
    for d in sorted(nofollow_only):
        t = "; ".join(sorted(companies[d]["texts"]))[:80]
        print(f"  [nofollow x{companies[d]['n']}] {d}   {t}")

if __name__ == "__main__":
    main()
