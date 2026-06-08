#!/usr/bin/env python3
"""Harvest Ahrefs outgoing-link data per Hochschule domain. Resumable + cached."""
import urllib.request, urllib.parse, ssl, json, os, time, sys
KEY=os.environ["AHREFS_KEY"]
ctx=ssl.create_default_context()
RAW="_tools/ahrefs/raw"; os.makedirs(RAW, exist_ok=True)

def call(path, params, retries=4):
    url="https://api.ahrefs.com/v3/"+path+"?"+urllib.parse.urlencode(params)
    req=urllib.request.Request(url, headers={"Authorization":"Bearer "+KEY,"Accept":"application/json"})
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=120) as r:
                return r.status, json.loads(r.read())
        except urllib.error.HTTPError as e:
            body=e.read().decode()[:200]
            if e.code in (429,500,502,503):
                time.sleep(2**i); continue
            return e.code, {"error":body}
        except Exception as e:
            time.sleep(2**i); continue
    return "ERR", {"error":"retries exhausted"}

doms=json.load(open("_tools/ahrefs_domains.json"))
done=skip=0
for i,d in enumerate(doms):
    fp=f"{RAW}/{d}.json"
    if os.path.exists(fp): skip+=1; continue
    rec={"domain":d}
    s,dr=call("site-explorer/domain-rating",{"target":d,"date":"2026-06-01"})
    rec["dr"]= dr.get("domain_rating",{}).get("domain_rating") if s==200 else None
    s,st=call("site-explorer/outlinks-stats",{"target":d})
    rec["stats"]= st.get("metrics") if s==200 else {"error":st}
    s,ld=call("site-explorer/linkeddomains",{
        "target":d,"mode":"subdomains","limit":"75",
        "select":"domain,links_from_target,dofollow_links,domain_rating,is_root_domain",
        "order_by":"dofollow_links:desc",
        "where":json.dumps({"field":"dofollow_links","is":["gt",0]})})
    rec["linked"]= ld.get("linkeddomains",[]) if s==200 else []
    rec["linked_status"]= s
    json.dump(rec, open(fp,"w"))
    done+=1
    if done%20==0: print(f"  ...{done} fetched ({i+1}/{len(doms)})", flush=True)
    time.sleep(0.15)
print(f"DONE: fetched {done}, cached-skip {skip}, total {len(doms)}")
