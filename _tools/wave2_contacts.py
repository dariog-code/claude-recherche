import urllib.request, urllib.parse, json, ssl, os, time, re
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
def verify(email):
    if not email: return None
    k="vf:"+email.lower()
    if k in cache: return cache[k].get('status')
    d=api(f"https://api.hunter.io/v2/email-verifier?email={urllib.parse.quote(email)}&api_key={key}")
    st=d.get('data',{}).get('status') if not d.get('_err') else 'err'
    cache[k]={'status':st}; json.dump(cache,open("_tools/hunter_cache.json","w")); return st
NAME_RE=re.compile(r"^[A-Za-zÄÖÜäöüßéèáàóô-]{2,}$")
BAD={'familie','team','stadt','rathaus','info','presse','kontakt','herr','frau','hallo','service',
     'buergerbuero','redaktion','webmaster','allgemein','zentrale','post','poststelle','no','na','nn','tourismus','mus','touris'}
def is_person(e):
    fn=(e.get('first_name') or '').strip(); ln=(e.get('last_name') or '').strip()
    if not fn or not ln: return False
    if not NAME_RE.match(fn) or not NAME_RE.match(ln): return False
    if fn.lower() in BAD or ln.lower() in BAD: return False
    return True
HIGH=['wirtschaftsförder','wirtschaftsforder','stadtmarketing','citymanagement','sponsor','presse','press',
      'öffentlichkeitsarbeit','offentlichkeitsarbeit','kommunikation','communication','marketing','economic',
      'public relations','medien','spokes','tourism','tourismus','event','veranstaltung','kultur','sport']
MED=['oberbürgermeister','bürgermeister','mayor','büroleitung','geschäftsführ','leitung','head',
     'director','chief','executive','management','manager','staff','referent','amtsleit','dezernent']
def relscore(e):
    txt=((e.get('position') or '')+' '+(e.get('department') or '')).lower()
    s=(e.get('confidence') or 0)/10.0
    if any(w in txt for w in HIGH): s+=100
    elif any(w in txt for w in MED): s+=40
    return s
GOOD=('valid','accept_all'); OKISH=('valid','accept_all','unknown')
def func_fallback(rd):
    for mb in ('presse','pressestelle','info','kontakt','stadtmarketing','wirtschaftsfoerderung','sport','rathaus','stadt'):
        st=verify(f"{mb}@{rd}")
        if st in GOOD: return f"{mb}@{rd}",st
    return f"info@{rd}",verify(f"info@{rd}")
rows=json.load(open("_tools/wave2_pool.json"))
persons={}; gaps=[]
for c in rows:
    rd=c['Domain']
    emails=(cache.get("ds:"+rd,{}).get("data",{}) or {}).get("emails",[]) or []
    pers=sorted([e for e in emails if is_person(e)],key=relscore,reverse=True)[:3]
    chosen=[]
    for e in pers:
        st=verify(e['value'])
        chosen.append({'vorname':e.get('first_name'),'nachname':e.get('last_name'),
            'funktion':e.get('position') or e.get('department') or '','email':e['value'],'verify':st})
    # To deliverable?
    to=next((p for p in chosen if p['verify'] in GOOD),None) or next((p for p in chosen if p['verify'] in OKISH),None)
    persons[c['Stadt']]={'domain':rd,'kandidaten':chosen}
    if to is None:
        gaps.append(c['Stadt'])
json.dump(cache,open("_tools/hunter_cache.json","w"))
json.dump(persons,open("_tools/persons_wave2.json","w"),ensure_ascii=False)
deliverable=len(rows)-len(gaps)
print(f"Städte: {len(rows)} | mit zustellbarer Person (Hunter): {deliverable} | Lücken: {len(gaps)}")
print("Lücken (brauchen Web-Recherche):")
for g in gaps: print("  ",g)
