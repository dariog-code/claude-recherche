#!/usr/bin/env python3
"""Holt Ahrefs Domain Rating fuer alle Linkdomains der 150er-Liste und filtert DR>=50."""
import urllib.request, urllib.parse, ssl, json, os, time, csv
KEY=os.environ["AHREFS_KEY"]
ctx=ssl.create_default_context()
CACHE="_tools/dr_cache.json"
cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}

def dr(domain):
    if domain in cache: return cache[domain]
    url="https://api.ahrefs.com/v3/site-explorer/domain-rating?"+urllib.parse.urlencode(
        {"target":domain,"date":"2026-06-01"})
    req=urllib.request.Request(url,headers={"Authorization":"Bearer "+KEY,"Accept":"application/json"})
    val=None
    for i in range(4):
        try:
            with urllib.request.urlopen(req,context=ctx,timeout=90) as r:
                d=json.loads(r.read())
                val=d.get("domain_rating",{}).get("domain_rating")
                break
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(2**i); continue
            val=f"ERR{e.code}"; break
        except Exception:
            time.sleep(2**i); continue
    cache[domain]=val
    json.dump(cache,open(CACHE,"w"))
    return val

rows=list(csv.DictReader(open("outreach_150_final.csv")))
# registrable domain fuer DR (Subdomain -> Hauptdomain)
def reg(d):
    d=d.strip().lower()
    parts=d.split(".")
    # einfache Heuristik: letzte 2 Labels (de) bzw. 3 bei co.uk-aehnlich (hier nicht noetig)
    return ".".join(parts[-2:]) if len(parts)>=2 else d

for r in rows:
    d=reg(r["Linkdomain"])
    r["DR"]=dr(d)

# Schreibe DR zurueck + Filter
out_all="outreach_150_final.csv"
fields=rows[0].keys()
with open(out_all,"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

def num(x):
    try: return float(x)
    except: return -1

keep=[r for r in rows if num(r["DR"])>=50]
drop=[r for r in rows if num(r["DR"])<50]
with open("outreach_dr50.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(keep)

from collections import Counter
print(f"GEPRUEFT: {len(rows)}  |  DR>=50: {len(keep)}  |  raus (<50/Fehler): {len(drop)}")
print("Behalten Herkunft:",Counter(r['Herkunft'] for r in keep))
print("\n--- AUSSORTIERT (DR<50) ---")
for r in sorted(drop,key=lambda r:num(r['DR'])):
    print(f"  DR={str(r['DR'])[:5]:5} {r['Herkunft'][:8]:8} {r['Stadt'][:22]:22} {r['Linkdomain']}")
