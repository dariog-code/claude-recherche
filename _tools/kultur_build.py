import urllib.request, urllib.parse, json, ssl, os, time, re, csv
ctx=ssl.create_default_context(); HK=os.environ["HUNTER_KEY"]; AK=os.environ["AHREFS_KEY"]
cache=json.load(open("_tools/hunter_cache.json"))
drc=json.load(open("_tools/dr_cache.json"))
def get(url,hdr=None):
    for i in range(4):
        try:
            req=urllib.request.Request(url,headers=hdr or {})
            with urllib.request.urlopen(req,context=ctx,timeout=90) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503): time.sleep(2**i); continue
            return {"_err":e.code}
        except Exception: time.sleep(2**i); continue
    return {"_err":"net"}
def verify(email):
    if not email: return None
    k="vf:"+email.lower()
    if k in cache: return cache[k].get('status')
    d=get(f"https://api.hunter.io/v2/email-verifier?email={urllib.parse.quote(email)}&api_key={HK}")
    st=d.get('data',{}).get('status') if not d.get('_err') else 'err'
    cache[k]={'status':st}; json.dump(cache,open("_tools/hunter_cache.json","w")); return st
def dr(domain):
    d=domain.lower()
    if d in drc and isinstance(drc[d],(int,float)): return int(round(drc[d]))
    resp=get(f"https://api.ahrefs.com/v3/site-explorer/domain-rating?target={urllib.parse.quote(d)}&date=2026-06-01",
             {"Authorization":"Bearer "+AK,"Accept":"application/json"})
    v=None
    if isinstance(resp,dict):
        dd=resp.get("domain_rating")
        v=dd.get("domain_rating") if isinstance(dd,dict) else dd
    drc[d]=v; json.dump(drc,open("_tools/dr_cache.json","w"))
    try: return int(round(float(v)))
    except: return ''
def norm(s):
    s=(s or '').lower().strip().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    return re.sub(r'[^a-z-]','',s)
def patterns(name,dom):
    parts=name.split()
    if len(parts)<2: return []
    f=norm(parts[0]); l=norm(parts[-1])
    return [f"{f}.{l}@{dom}",f"{l}@{dom}",f"{f[0]}.{l}@{dom}",f"{f}{l}@{dom}"]
GOOD=('valid','accept_all'); OKISH=('valid','accept_all','unknown')
def is_person(nm):
    nm=(nm or '').strip()
    return bool(nm) and ' ' in nm and not any(x in nm.lower() for x in ('development','sponsoring','freundeskreis','festivalbüro','abteilung','team','pool'))

items=[]
for fn,kat in (("kultur_museen","Museum"),("kultur_orchester","Orchester/Festival"),("kultur_theater","Theater/Oper")):
    for e in json.load(open(f"_tools/results/{fn}.json")):
        e['kategorie']=kat; items.append(e)
# dedupe: key = email(lower) if present else institution
seen={}; uniq=[]
for e in items:
    key=(e.get('email') or '').strip().lower() or norm(e['institution'])
    if key in seen: continue
    seen[key]=1; uniq.append(e)

rows=[]
for e in uniq:
    dom=e['domain'].strip().lower()
    email=(e.get('email') or '').strip(); typ=e.get('email_typ','')
    name=(e.get('ansprechpartner') or '').strip()
    maildom=email.split('@')[1] if '@' in email else dom
    st=verify(email) if email else None
    # persönliche Mail nicht zustellbar / keine Mail aber Name -> Muster
    if (not email or (typ=='persoenlich' and st not in OKISH)) and is_person(name):
        for cand in patterns(name,maildom):
            if verify(cand) in GOOD: email,st=cand,verify(cand); break
    if not email:  # weiter nichts -> info@
        email=f"info@{dom}"; st=verify(email)
    anr=f"Guten Tag {name}," if is_person(name) else "Sehr geehrte Damen und Herren,"
    empf={'valid':'senden','accept_all':'OK (catch-all) senden','unknown':'senden – Status unklar'}.get(st,'PRÜFEN – Adresse')
    rows.append({'Email':email,'Email_CC':'','Anrede':anr,'Institution':e['institution'],
        'Kategorie':e['kategorie'],'Listungsseite':e.get('sponsorenseite',''),
        'Ansprechpartner':name if is_person(name) else '','Funktion':e.get('funktion',''),
        'DR':dr(dom),'Domain':dom,'Verify_To':st or '','Versandempfehlung':empf,'Evidenz':e.get('evidenz','')[:120]})
def drk(x):
    try: return -int(x['DR'])
    except: return 0
rows.sort(key=drk)
json.dump(cache,open("_tools/hunter_cache.json","w")); json.dump(drc,open("_tools/dr_cache.json","w"))
fields=['Email','Email_CC','Anrede','Institution','Kategorie','Listungsseite','Ansprechpartner','Funktion','DR','Domain','Verify_To','Versandempfehlung','Evidenz']
with open("mailmerge_kultur.csv","w",newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
from collections import Counter
print("mailmerge_kultur.csv:",len(rows),"Institutionen (dedupliziert)")
print("Versand:",dict(Counter(r['Versandempfehlung'] for r in rows)))
print("mit Ansprechpartner:",sum(1 for r in rows if r['Ansprechpartner']))
drs=[int(r['DR']) for r in rows if str(r['DR']).isdigit()]
print(f"DR: min {min(drs)} / median {sorted(drs)[len(drs)//2]} / max {max(drs)} | >=60: {sum(1 for d in drs if d>=60)}")
print("\nTop 12:")
for r in rows[:12]: print(f"  DR{str(r['DR']):>3} {r['Institution'][:34]:34} {r['Email']:36} [{r['Verify_To']}]")
print("\nPRÜFEN:")
for r in rows:
    if r['Versandempfehlung'].startswith('PRÜFEN'): print(f"  {r['Institution'][:30]:30} {r['Email']}")
