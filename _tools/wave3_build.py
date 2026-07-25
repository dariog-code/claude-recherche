import urllib.request, urllib.parse, json, ssl, os, time, re, csv
ctx=ssl.create_default_context(); HK=os.environ["HUNTER_KEY"]; AK=os.environ["AHREFS_KEY"]
cache=json.load(open("_tools/hunter_cache.json")); drc=json.load(open("_tools/dr_cache.json"))
def get(url,hdr=None):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=hdr or {}),context=ctx,timeout=90) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(2**i); continue
            return {"_err":e.code}
        except Exception: time.sleep(2**i); continue
    return {"_err":"net"}
def dsearch(dom):
    k="ds:"+dom
    if k in cache: return cache[k]
    d=get(f"https://api.hunter.io/v2/domain-search?domain={dom}&limit=50&api_key={HK}")
    cache[k]=d; json.dump(cache,open("_tools/hunter_cache.json","w")); return d
def verify(email):
    if not email: return None
    k="vf:"+email.lower()
    if k in cache: return cache[k].get('status')
    d=get(f"https://api.hunter.io/v2/email-verifier?email={urllib.parse.quote(email)}&api_key={HK}")
    st=d.get('data',{}).get('status') if not d.get('_err') else 'err'
    cache[k]={'status':st}; json.dump(cache,open("_tools/hunter_cache.json","w")); return st
def dr(dom):
    if dom in drc and isinstance(drc[dom],(int,float)): return int(round(drc[dom]))
    resp=get(f"https://api.ahrefs.com/v3/site-explorer/domain-rating?target={urllib.parse.quote(dom)}&date=2026-06-01",{"Authorization":"Bearer "+AK,"Accept":"application/json"})
    v=None
    if isinstance(resp,dict):
        dd=resp.get("domain_rating"); v=dd.get("domain_rating") if isinstance(dd,dict) else dd
    drc[dom]=v; json.dump(drc,open("_tools/dr_cache.json","w"))
    try: return int(round(float(v)))
    except: return ''
NAME_RE=re.compile(r"^[A-Za-zÄÖÜäöüßéèáàóô-]{2,}$")
BAD={'familie','team','stadt','rathaus','info','presse','kontakt','herr','frau','service','tourismus','mus','touris','nn','na'}
def is_person(e):
    fn=(e.get('first_name') or '').strip(); ln=(e.get('last_name') or '').strip()
    if not fn or not ln or not NAME_RE.match(fn) or not NAME_RE.match(ln): return False
    return fn.lower() not in BAD and ln.lower() not in BAD
HIGH=['wirtschaftsförder','stadtmarketing','citymanagement','sponsor','presse','press','öffentlichkeitsarbeit','kommunikation','communication','marketing','economic','medien','tourism','event','kultur','sport']
MED=['bürgermeister','mayor','leitung','head','director','chief','manager','referent','amtsleit','dezernent']
def rel(e):
    t=((e.get('position') or '')+' '+(e.get('department') or '')).lower(); s=(e.get('confidence') or 0)/10.0
    if any(w in t for w in HIGH): s+=100
    elif any(w in t for w in MED): s+=40
    return s
GOOD=('valid','accept_all'); OKISH=('valid','accept_all','unknown')
def fallback(dom):
    for mb in ('presse','pressestelle','info','kontakt','stadtmarketing','wirtschaftsfoerderung','sport','rathaus','stadt'):
        if verify(f"{mb}@{dom}") in GOOD: return f"{mb}@{dom}",verify(f"{mb}@{dom}")
    return f"info@{dom}",verify(f"info@{dom}")
def nm(p): return (f"{p.get('vorname') or ''} {p.get('nachname') or ''}").strip()
pool=json.load(open("_tools/wave3_pool.json"))
rows=[]; gaps=[]
for c in pool:
    dom=c['_regdom']; d=dsearch(dom)
    emails=(d.get("data",{}) or {}).get("emails",[]) or []
    pers=sorted([e for e in emails if is_person(e)],key=rel,reverse=True)[:3]
    cand=[{'vorname':e.get('first_name'),'nachname':e.get('last_name'),'funktion':e.get('position') or e.get('department') or '','email':e['value'],'verify':verify(e['value'])} for e in pers]
    to=next((p for p in cand if p['verify'] in GOOD),None) or next((p for p in cand if p['verify'] in OKISH),None)
    if to is None:
        to={'vorname':'','nachname':'','funktion':'','email':'','verify':None}
        fb,fs=fallback(dom); to['email']=fb; to['verify']=fs; gaps.append(c['stadt'])
    cc=next((p for p in cand if p is not to and p.get('email') and nm(p) and nm(p)!=nm(to)),None)
    anr=f"Guten Tag {nm(to)}," if nm(to) else "Sehr geehrte Damen und Herren,"
    v=to['verify']; empf={'valid':'senden','accept_all':'OK (catch-all) senden','unknown':'senden – Status unklar'}.get(v,'PRÜFEN – Adresse')
    rows.append({'Email':to['email'],'Email_CC':cc['email'] if cc else '','Anrede':anr,'Ansprechpartner':nm(to),'Funktion':to['funktion'],
        'Ansprechpartner_CC':nm(cc) if cc else '','Funktion_CC':cc['funktion'] if cc else '','Stadt':c['stadt'],'Domain':dom,
        'Sponsorenseite':c['sponsorenseite'],'DR':dr(dom),'Status':'','Verify_To':v or '','Verify_CC':(cc['verify'] or '') if cc else '','Versandempfehlung':empf})
json.dump(cache,open("_tools/hunter_cache.json","w")); json.dump(drc,open("_tools/dr_cache.json","w"))
rows.sort(key=lambda r:-(int(r['DR']) if str(r['DR']).isdigit() else 0))
fields=['Email','Email_CC','Anrede','Ansprechpartner','Funktion','Ansprechpartner_CC','Funktion_CC','Stadt','Domain','Sponsorenseite','DR','Status','Verify_To','Verify_CC','Versandempfehlung']
with open("mailmerge_wave3.csv","w",newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
from collections import Counter
print("mailmerge_wave3.csv:",len(rows),"| Versand:",dict(Counter(r['Versandempfehlung'] for r in rows)))
print("mit CC:",sum(1 for r in rows if r['Email_CC']),"| namentl. To:",sum(1 for r in rows if r['Ansprechpartner']))
drs=[int(r['DR']) for r in rows if str(r['DR']).isdigit()]
print(f"DR: min {min(drs)} / median {sorted(drs)[len(drs)//2]} / max {max(drs)} | <40: {sum(1 for d in drs if d<40)}")
print("Gaps (kein zustellbarer Personentreffer):", gaps)
