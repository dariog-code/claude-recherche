#!/usr/bin/env python3
"""Analyze harvested Ahrefs outgoing links: separate real company domains from
excluded ones (social/tools/edu/gov/library/own), per Hochschule."""
import json, os, re, csv

RAW="_tools/ahrefs/raw"

# domains/substrings that are NOT company-backlink targets
EXCLUDE_SUBSTR = [
    # social / platforms / tools
    "facebook.","instagram.","youtube.","youtu.be","linkedin.","twitter.","x.com",
    "xing.","tiktok.","vimeo.","soundcloud.","spotify.","flickr.","pinterest.",
    "google.","gstatic.","googleapis.","microsoft.","office.com","office365","live.com",
    "sharepoint.","outlook.","apple.com","adobe.com","mozilla.","browsehappy.",
    "github.","gitlab.","zoom.us","wikipedia.","wikimedia.","creativecommons.",
    "padlet.","sciebo.","asimut.","primuss.","reservix.","eventim.","eventbrite.",
    "mailchimp.","twingle.","betterplace.","bildungsspender.","whatsapp.","wa.me",
    "t.me","telegram.","threema.","mastodon.","bsky.","researchgate.","orcid.",
    "doi.org","dnb.de","datacite.","zenodo.","slideshare.","issuu.","calameo.",
    "academyfive.","heavenhr.","personio.","jobteaser.","joborama.","dj-extensions.",
    "cookiebot.","usercentrics.","matomo.","cellms.","trainex","incom.org","4me.com",
    "studycheck.","studydrive.","studieren.de","hochschulkompass.","studis-online.",
    # library / catalog
    "gbv.de","kobv.de","bsz-bw.","ibs-bw.","eopac.","ebscohost.","ebsco.","opac",
    "swisscovery","k10plus","worldcat.","jstor.","de.gruyter",
    # gov / science orgs / accreditation / funding
    ".gov",".europa.eu","bund.de","bmbf.","bmwk.","daad.","hrk.de","dfg.de",
    "wissenschaftsrat.","akkreditierung","fibaa.","aqas.","acquin.","zeva.",
    "stiftung-akkreditierung","aacsb.","amba","equis","efmd.","che.de","chevalier",
    "stipendium","stipendien","arbeiterkind.","arbeitsagentur.","esf.","foerderdatenbank",
    "bayern.de","nrw.de","sachsen.de","rlp.de","berlin.de","hamburg.de","thueringen.de",
    "baden-wuerttemberg.","niedersachsen.","brandenburg.","hessen.de","saarland.",
    "schleswig-holstein","mecklenburg","bremen.de",
    # studierendenwerk
    "studierendenwerk","studentenwerk","stw-","stwhh.","my-stuwe.",
]
# regex for educational / academic partner domains (not companies)
EDU_RE = re.compile(r"(^|\.)(uni-|fh-|hs-|haw-|th-|hfm-|hfmt|hfbk|hfg-|hmt-|hmtm|adbk|"
                    r"kunstakademie|musikhochschule|hochschule|universit|akademie\.|"
                    r"\.edu$|\.edu\.|\.ac\.|hs21\.|dhbw|fernuni|leuphana|charite|mh-)")

def is_company(dom, target):
    d=dom.lower()
    if d==target or d.endswith("."+target): return False
    # shared stem with target (own sister domains e.g. doepfer-*, apollon-*)
    stem=target.split(".")[0].split("-")[0]
    if len(stem)>=5 and d.split(".")[0].startswith(stem): return False
    for s in EXCLUDE_SUBSTR:
        if s in d: return False
    if EDU_RE.search(d): return False
    # foundations / vereins as own funding vehicles
    if d.startswith("foerder") or d.startswith("freunde") or "-stiftung." in d or d.startswith("stiftung"):
        return False
    return True

rows=[]
for fn in sorted(os.listdir(RAW)):
    if not fn.endswith(".json"): continue
    rec=json.load(open(f"{RAW}/{fn}"))
    t=rec["domain"]
    comp=[x for x in rec.get("linked",[]) if is_company(x["domain"], t)]
    comp.sort(key=lambda x:-x["dofollow_links"])
    rows.append({
        "domain":t, "dr":rec.get("dr"),
        "linked_domains_total": (rec.get("stats") or {}).get("linked_domains_dofollow"),
        "company_dofollow_domains": len(comp),
        "top": comp[:12],
    })

rows.sort(key=lambda r:-(r["company_dofollow_domains"] or 0))
json.dump(rows, open("_tools/ahrefs/analysis.json","w"), ensure_ascii=False, indent=1)
print(f"analyzed {len(rows)} domains")
print("\nTop 30 Hochschulen nach Anzahl ausgehender DOFOLLOW-Firmendomains (Ahrefs):")
print(f"{'#firms':>6} {'DR':>5}  domain")
for r in rows[:30]:
    print(f"{r['company_dofollow_domains']:>6} {str(r['dr'] or '-'):>5}  {r['domain']}")
