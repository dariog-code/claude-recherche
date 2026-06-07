#!/usr/bin/env python3
"""Crawl an institution's sponsoring/Foerderer area and produce a verdict.

Usage:
  crawl.py <inst_registrable_domain> <seed_url> [seed_url2 ...]
  crawl.py --auto <inst_registrable_domain>        # try common paths from homepage

Strategy: fetch seeds, then follow same-domain links whose URL/anchor text match
sponsor/foerder/partner/mitglied/unterstuetz/freunde/danke/stiften keywords
(depth 1 from seeds, capped). Aggregate EXTERNAL dofollow company domains (after
junk filtering) and company-like logos (img alt containing 'logo').
"""
import sys, re, urllib.request, ssl, gzip, json
import tldextract
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE

JUNK = {
 "facebook.com","twitter.com","x.com","instagram.com","linkedin.com","youtube.com",
 "youtu.be","xing.com","tiktok.com","vimeo.com","flickr.com","pinterest.com","spotify.com",
 "wikipedia.org","google.com","googleapis.com","gstatic.com","gmpg.org","w3.org","wa.me",
 "schema.org","creativecommons.org","mastodon.social","threads.net","whatsapp.com","t.me",
 "bsky.app","researchgate.net","orcid.org","doi.org","dfg.de","bmbf.de","europa.eu","eua.eu",
 "adobe.com","apple.com","microsoft.com","mozilla.org","jquery.com","cookiebot.com",
 "deutschlandstipendium.de","stifterverband.org","stifterverband.de","telegram.org",
 "hochschulkompass.de","studienwahl.de","bund.de","openstreetmap.org","maps.google.com",
 "goo.gl","bit.ly","addtoany.com","sharethis.com","paypal.com","threema.id","threema.ch",
 "hrk.de","akkreditierungsrat.de","charta-der-vielfalt.de","arbeiterkind.de",
 "datenschutz.de","e-fellows.net","studis-online.de","hochschulpakt.de","daad.de",
 "che.de","wissenschaftsrat.de","gov","bafin.de","studierendenwerk.de",
}
# institutional logo alt-texts to ignore when counting company logos
INST_LOGO_RE = re.compile(r"akkreditier|weltoffen|familiengerecht|charta|vielfalt|"
    r"deutschlandstip|european university|hrk|audit|gegen fremdenfeind|"
    r"metropolregion|innovative hochschule|systemakkredit|fairtrade|"
    r"facebook|instagram|youtube|linkedin|twitter|xing|tiktok|zur startseite|"
    r"logo der hochschul|logo hochschul|zurück zur|nachhaltig|klimaneutral", re.I)
KW = re.compile(r"sponsor|foerder|förder|partner|mitglied|unterstuetz|unterstütz|"
    r"freunde|danke|stiften|spenden|netzwerk|alumni|kuratorium", re.I)
COMMON = ["/sponsoring","/de/sponsoring","/foerderer","/foerderverein","/partner",
    "/partner-und-foerderer","/unsere-sponsoren","/sponsoren","/freunde-und-foerderer",
    "/stiften-und-foerdern","/foerdern-und-stiften","/foerdervereine"]

def reg(host):
    e=tldextract.extract(host)
    return f"{e.domain}.{e.suffix}".lower() if e.domain and e.suffix else None

def fetch(url):
    try:
        req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"gzip"})
        with urllib.request.urlopen(req,timeout=25,context=ctx) as r:
            data=r.read()
            if r.headers.get("Content-Encoding")=="gzip": data=gzip.decompress(data)
            enc=r.headers.get_content_charset() or "utf-8"
            return data.decode(enc,errors="replace"), r.geturl(), None
    except Exception as e:
        return None,url,str(e)

def crawl(inst, seeds, max_pages=18):
    inst=inst.lower()
    seen=set(); queue=list(seeds); pages=[]; companies={}; logos=set()
    depth={u:0 for u in seeds}
    while queue and len(pages)<max_pages:
        url=queue.pop(0)
        if url in seen: continue
        seen.add(url)
        html,final,err=fetch(url)
        if html is None:
            pages.append((url,f"ERR {err}")); continue
        pages.append((url,f"OK {len(html)}b"))
        soup=BeautifulSoup(html,"html.parser")
        # company logos
        for img in soup.find_all("img"):
            alt=(img.get("alt") or "").strip()
            if alt and re.search(r"logo|sponsor|partner",alt,re.I) and not INST_LOGO_RE.search(alt):
                logos.add(alt[:60])
        for a in soup.find_all("a",href=True):
            href=a["href"].strip()
            au=urljoin(final,href)
            p=urlparse(au)
            if p.scheme not in ("http","https"): continue
            host=p.netloc.split(":")[0]; rd=reg(host)
            if not rd: continue
            txt=a.get_text(" ",strip=True)[:50]
            if rd==inst:
                # follow same-domain keyword links at depth<2
                d=depth.get(url,0)
                if d<1 and au not in seen and (KW.search(p.path) or KW.search(txt or "")):
                    if au not in depth: depth[au]=d+1; queue.append(au)
                continue
            if rd in JUNK or rd.endswith(".gov"): continue
            rel=[x.lower() for x in (a.get("rel") or [])]
            df="nofollow" not in rel
            e=companies.setdefault(rd,{"df":False,"texts":set(),"n":0,"src":set()})
            if df: e["df"]=True
            if txt: e["texts"].add(txt)
            e["n"]+=1; e["src"].add(url.replace("https://","").replace("http://","")[:50])
    return pages,companies,logos

def main():
    args=sys.argv[1:]
    if args[0]=="--auto":
        inst=args[1]; seeds=[f"https://www.{inst}{p}" for p in COMMON]
    else:
        inst=args[0]; seeds=args[1:]
    pages,companies,logos=crawl(inst,seeds)
    df={k:v for k,v in companies.items() if v["df"]}
    nf={k:v for k,v in companies.items() if not v["df"]}
    print(f"=== {inst} ===")
    ok=[p for p in pages if p[1].startswith('OK')]
    print(f"pages fetched OK: {len(ok)}/{len(pages)}")
    for u,s in pages:
        if s.startswith('OK'): print(f"  + {u}")
    print(f"\nEXTERNAL dofollow company domains: {len(df)}")
    for d in sorted(df):
        print(f"  [df x{companies[d]['n']}] {d}  | {'; '.join(sorted(companies[d]['texts']))[:60]}")
    print(f"\nEXTERNAL nofollow-only domains: {len(nf)}")
    for d in sorted(nf):
        print(f"  [nf x{companies[d]['n']}] {d}  | {'; '.join(sorted(companies[d]['texts']))[:50]}")
    print(f"\nCompany-like logos (img alt): {len(logos)}")
    for l in sorted(logos): print(f"  * {l}")
    verdict="KEIN FUND"
    if len(df)>=6: verdict="LINK VERIFIZIERT (>=6 dofollow)"
    elif len(df)>=1 or len(logos)>=4: verdict="SPONSORING-SEITE (Logos/Teil-Links)"
    print(f"\nAUTO-VERDICT: {verdict}  (dofollow={len(df)}, logos={len(logos)})")

if __name__=="__main__": main()
