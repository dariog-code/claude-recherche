import urllib.request, urllib.parse, json, ssl, os, time
ctx=ssl.create_default_context(); key=os.environ["HUNTER_KEY"]
cache=json.load(open("_tools/hunter_cache.json"))
def api(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(url,context=ctx,timeout=70) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(2**i); continue
            return {"_err":e.code}
        except Exception: time.sleep(2**i); continue
    return {"_err":"net"}
rows=json.load(open("_tools/wave2_pool.json"))
doms=sorted({c['Domain'] for c in rows})
new=0
for i,d in enumerate(doms,1):
    k="ds:"+d
    if k in cache: continue
    res=api(f"https://api.hunter.io/v2/domain-search?domain={urllib.parse.quote(d)}&limit=100&api_key={key}")
    if res.get("_err"):
        cache[k]={"data":{"emails":[]},"_err":res["_err"]}
    else:
        cache[k]=res
    new+=1
    json.dump(cache,open("_tools/hunter_cache.json","w"))
    time.sleep(0.5)
hit=sum(1 for d in doms if cache.get("ds:"+d,{}).get("data",{}).get("emails"))
print(f"Domains: {len(doms)} | neu abgefragt: {new} | mit Emails: {hit}")
