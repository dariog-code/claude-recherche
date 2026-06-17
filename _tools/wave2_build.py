import urllib.request, urllib.parse, json, ssl, os, time, re, csv
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
def norm(s):
    s=(s or '').lower().strip().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss').replace('é','e').replace('è','e').replace('á','a')
    return re.sub(r'[^a-z-]','',s)
GOOD=('valid','accept_all'); OKISH=('valid','accept_all','unknown')
def patterns(f,l,dom):
    f=norm(f); l=norm(l); lnoh=l.replace('-','')
    cands=[f"{f}.{l}",f"{l}",(f"{f[0]}.{l}" if f else None),f"{l}.{f}",f"{f}{l}",(f"{f[0]}{l}" if f else None),
           (f"{l}{f[0]}" if f else None),f"{f}.{lnoh}",lnoh]
    seen=set(); out=[]
    for c in cands:
        if c and c not in seen: seen.add(c); out.append(f"{c}@{dom}")
    return out
# Gaps integrieren
gaps={}
for fn in ("wave2_gaps_1","wave2_gaps_2"):
    for c in json.load(open(f"_tools/results/{fn}.json")):
        gaps[c['stadt']]=c['personen']
def resolve_gap(stadt,plist):
    maildom=None
    for p in plist:
        if p.get('email') and '@' in p['email']:
            maildom=p['email'].split('@')[1].lower()
            if p.get('email_typ')=='persoenlich': break
    out=[]
    for p in plist:
        em=p.get('email'); typ=p.get('email_typ'); st=None
        if em and typ=='persoenlich':
            st=verify(em)
            if st not in OKISH:
                for cand in patterns(p.get('vorname'),p.get('nachname'),em.split('@')[1]):
                    if verify(cand) in GOOD: em,st=cand,verify(cand); break
        elif em and typ=='funktion':
            best=None
            if p.get('vorname') and p.get('nachname') and maildom:
                for cand in patterns(p['vorname'],p['nachname'],maildom):
                    if verify(cand) in GOOD: best=(cand,verify(cand)); break
            if best: em,st=best
            else: st=verify(em)
        out.append({'vorname':(p.get('vorname') or '').strip(),'nachname':(p.get('nachname') or '').strip(),
                    'funktion':p.get('funktion',''),'email':em,'verify':st})
    def rank(p):
        pers=p['email'] and p['email'].split('@')[0].lower() not in ('info','presse','pressestelle','kontakt','wirtschaftsfoerderung','wirtschaft','stadtmarketing','rathaus','stadt','poststelle','sport')
        if p['verify'] in GOOD and pers: return 0
        if p['verify'] in ('unknown',) and pers: return 1
        if p['verify'] in GOOD: return 2
        if p['verify'] in OKISH: return 3
        return 4
    out.sort(key=rank); return out

persons=json.load(open("_tools/persons_wave2.json"))
pool={c['Stadt']:c for c in json.load(open("_tools/wave2_pool.json"))}
def regdom(d): 
    p=d.split('.'); return '.'.join(p[-2:])
def func_fallback(rd):
    for mb in ('presse','pressestelle','info','kontakt','stadtmarketing','wirtschaftsfoerderung','sport','rathaus','stadt'):
        if verify(f"{mb}@{rd}") in GOOD: return f"{mb}@{rd}",verify(f"{mb}@{rd}")
    return f"info@{rd}",verify(f"info@{rd}")
def nm(p): return (f"{p.get('vorname') or ''} {p.get('nachname') or ''}").strip()

rows=[]
for stadt,meta in pool.items():
    rd=meta['Domain']
    if stadt in gaps:
        cands=resolve_gap(stadt,gaps[stadt])
    else:
        cands=persons.get(stadt,{}).get('kandidaten',[])
    to=next((p for p in cands if p.get('email') and p['verify'] in GOOD),None) \
       or next((p for p in cands if p.get('email') and p['verify'] in OKISH),None)
    if to is None:
        to=dict(cands[0]) if cands else {'vorname':'','nachname':'','funktion':'','email':'','verify':None}
        fb,fs=func_fallback(rd); to=dict(to); to['email']=fb; to['verify']=fs
    cc=next((p for p in cands if p is not to and p.get('email') and nm(p) and nm(p)!=nm(to)),None)
    anr=f"Guten Tag {nm(to)}," if nm(to) else "Sehr geehrte Damen und Herren,"
    v=to.get('verify')
    empf={'valid':'senden','accept_all':'OK (catch-all) senden','unknown':'senden – Status unklar'}.get(v,'PRÜFEN – Adresse')
    rows.append({'Email':to.get('email',''),'Email_CC':cc.get('email','') if cc else '','Anrede':anr,
        'Ansprechpartner':nm(to),'Funktion':to.get('funktion',''),
        'Ansprechpartner_CC':nm(cc) if cc else '','Funktion_CC':cc.get('funktion','') if cc else '',
        'Stadt':stadt,'Domain':rd,'Sponsorenseite':meta['Sponsorenseite'],'DR':meta.get('DR_est',''),
        'Status':meta.get('Typ',''),'Verify_To':v or '','Verify_CC':(cc.get('verify') or '') if cc else '',
        'Versandempfehlung':empf})
json.dump(cache,open("_tools/hunter_cache.json","w"))
rows.sort(key=lambda r:-(float(r['DR']) if str(r['DR']).replace('.','').isdigit() else 0))
fields=['Email','Email_CC','Anrede','Ansprechpartner','Funktion','Ansprechpartner_CC','Funktion_CC',
        'Stadt','Domain','Sponsorenseite','DR','Status','Verify_To','Verify_CC','Versandempfehlung']
with open("mailmerge_wave2.csv","w",newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
from collections import Counter
GENp=('info','presse','pressestelle','kontakt','wirtschaftsfoerderung','wirtschaft','stadtmarketing','rathaus','stadt','poststelle','sport','tourismus')
print("mailmerge_wave2.csv:",len(rows),"Zeilen |",dict(Counter(r['Versandempfehlung'] for r in rows)))
print("mit CC:",sum(1 for r in rows if r['Email_CC']),"| persönliche To:",sum(1 for r in rows if r['Email'].split('@')[0].lower() not in GENp))
print("\nPRÜFEN/unklar:")
for r in rows:
    if not r['Versandempfehlung'].startswith(('senden','OK')) or 'unklar' in r['Versandempfehlung']:
        print(f"  {r['Stadt']:20} {r['Email']:38} [{r['Verify_To']}] {r['Versandempfehlung']}")
