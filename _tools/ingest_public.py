#!/usr/bin/env python3
"""Ingest public-institution findings into a SEPARATE CSV (keeps Hochschul-CSV clean).
Usage: ingest_public.py <kategorie> <results.json>
Adds Ahrefs DR per listungsseite domain. Numbering: FIRMEN-LINKS->F#, FIRMEN-LOGOS->L#, PARTNERBEREICH->PB#, else '-'.
"""
import sys, csv, json, os, re, urllib.request, urllib.parse, ssl
CSV="/home/user/claude-recherche/recherche_oeffentliche_institutionen.csv"
KEY=os.environ.get("AHREFS_KEY",""); ctx=ssl.create_default_context()
COLS=["Nr","Kategorie","Status","Einrichtung","Typ","Verein","Firmenmitgliedschaft","Jahresbeitrag",
 "Listungsseite","Bewertung","Ahrefs_DR","K1_Name","K1_Funktion","K1_Email","K1_Verify","K1_Quelle",
 "K2_Name","K2_Funktion","K2_Email","K2_Verify","K2_Quelle"]
JK=["status","hochschule","typ","verein","firmenmitgliedschaft","jahresbeitrag","listungsseite","bewertung"]
JK2=["k1_name","k1_funktion","k1_email","k1_verify","k1_quelle","k2_name","k2_funktion","k2_email","k2_verify","k2_quelle"]
def regdom(s):
    m=re.search(r'([a-z0-9-]+(?:\.[a-z0-9-]+)+)',(s or '').lower())
    if not m: return ""
    p=m.group(1).split('/')[0].split('.'); return ".".join(p[-2:]) if len(p)>=2 else ""
def dr(t):
    if not (KEY and t): return ""
    url="https://api.ahrefs.com/v3/site-explorer/domain-rating?"+urllib.parse.urlencode({"target":t,"date":"2026-06-01"})
    req=urllib.request.Request(url, headers={"Authorization":"Bearer "+KEY})
    try:
        with urllib.request.urlopen(req,context=ctx,timeout=40) as r:
            v=json.loads(r.read())["domain_rating"]["domain_rating"]; return f"{v:.0f}" if v is not None else ""
    except Exception: return ""
def counters(rows):
    c={"F":0,"L":0,"PB":0}
    for r in rows[1:]:
        nr=r[0]
        for k in("PB","L","F"):
            if re.fullmatch(k+r"\d+",nr): c[k]=max(c[k],int(nr[len(k):]))
    return c
def assign(st,c):
    st=st.upper()
    if "FIRMEN-LINKS" in st: c["F"]+=1; return f"F{c['F']}"
    if "FIRMEN-LOGOS" in st: c["L"]+=1; return f"L{c['L']}"
    if "PARTNERBEREICH" in st: c["PB"]+=1; return f"PB{c['PB']}"
    return "-"
kat=sys.argv[1]; data=json.load(open(sys.argv[2]))
rows=list(csv.reader(open(CSV))) if os.path.exists(CSV) else [COLS]
c=counters(rows)
for it in data:
    nr=assign(it.get("status",""),c)
    d=regdom(it.get("listungsseite","")) or regdom(it.get("bewertung",""))
    row=[nr,kat]+[str(it.get(k,"") or "") for k in JK[:1-1] ] # placeholder
    # build explicitly
    row=[nr,kat,it.get("status",""),it.get("hochschule",""),it.get("typ",""),it.get("verein",""),
         it.get("firmenmitgliedschaft",""),it.get("jahresbeitrag",""),it.get("listungsseite",""),
         it.get("bewertung",""),dr(d)]+[str(it.get(k,"") or "") for k in JK2]
    assert len(row)==len(COLS), len(row)
    rows.append(row)
csv.writer(open(CSV,"w",newline="")).writerows(rows)
print(f"{kat}: +{len(data)} rows -> {CSV} (total {len(rows)-1})")
