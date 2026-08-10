import urllib.request, urllib.parse, json, ssl, os, time, re, csv
ctx=ssl.create_default_context(); HK=os.environ["HUNTER_KEY"]
cache=json.load(open("_tools/hunter_cache.json"))
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(url,context=ctx,timeout=40) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(2**i); continue
            return {"_err":e.code}
        except Exception: time.sleep(2); continue
    return {"_err":1}
def verify(email):
    k="vf:"+email.lower()
    if k in cache: return cache[k].get('status')
    d=get(f"https://api.hunter.io/v2/email-verifier?email={urllib.parse.quote(email)}&api_key={HK}")
    st=d.get('data',{}).get('status') if not d.get('_err') else 'err'
    cache[k]={'status':st}; json.dump(cache,open("_tools/hunter_cache.json","w")); return st
def dsearch(dom):
    k="ds:"+dom
    if k in cache and (cache[k].get('data',{}) or {}).get('emails'): return cache[k]
    d=get(f"https://api.hunter.io/v2/domain-search?domain={dom}&limit=40&api_key={HK}")
    cache[k]=d; json.dump(cache,open("_tools/hunter_cache.json","w")); return d
GOOD=('valid','accept_all')
NAME=re.compile(r"^[A-Za-zÄÖÜäöüßé-]{2,}$"); BADW={'info','presse','team','stadt','rathaus','familie','tourismus','va','kita'}
def person(e):
    fn=(e.get('first_name') or '').strip(); ln=(e.get('last_name') or '').strip()
    return fn and ln and NAME.match(fn) and NAME.match(ln) and fn.lower() not in BADW and ln.lower() not in BADW
HIGH=['wirtschaft','presse','marketing','stadtmarketing','kommunik','öffentlich','medien','kultur','event','sponsor','tourism','sport','citymanag']
def rel(e):
    t=((e.get('position') or '')+(e.get('department') or '')).lower(); return (e.get('confidence') or 0)/10.0+(100 if any(w in t for w in HIGH) else 0)
bad=set()
for fn in ("bounces.json","bounces_all.json","bounces3.json","bounces4.json","bounces5.json"):
    try: bad|=set(k.lower() for k in json.load(open("_tools/"+fn)))
    except: pass
def pick(dom, exclude):
    pers=sorted([e for e in (dsearch(dom).get('data',{}) or {}).get('emails',[]) if person(e) and e['value'].lower() not in bad and e['value'].lower() not in exclude], key=rel, reverse=True)[:12]
    for want in (GOOD,('unknown',)):
        for e in pers:
            if verify(e['value']) in want: return (e['value'],f"{e['first_name']} {e['last_name']}",e.get('position') or e.get('department') or '',verify(e['value']))
    return None
cities={'Achern':'achern.de','Bad Salzuflen':'bad-salzuflen.de','Castrop-Rauxel':'castrop-rauxel.de','Buxtehude':'buxtehude.de','Dinslaken':'dinslaken.de','Kaltenkirchen':'kaltenkirchen.de'}
res={}
for s,dom in cities.items():
    to=pick(dom,set()); cc=pick(dom,{to[0].lower()}) if to else None
    res[s]={'to':to,'cc':cc}; json.dump(res,open("_tools/bounce5_fix.json","w"),ensure_ascii=False)
json.dump(cache,open("_tools/hunter_cache.json","w"))
print("FERTIG")
for s in cities:
    to=res[s]['to']; cc=res[s]['cc']
    print(f"{s:16} To " + (f"{to[0]:34} {to[1]} [{to[3]}]" if to else "—") + " | CC " + (f"{cc[0]}" if cc else "—"))
