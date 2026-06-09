#!/usr/bin/env python3
"""Update existing master-CSV rows from a re-check JSON (match by hochschule name).
Maps broadened status values, updates fields in place, then renumbers all rows.
Usage: update_ingest.py <results.json>
"""
import sys, csv, json, re

CSV="/home/user/claude-recherche/recherche_master_foerdervereine.csv"
KEYS=["status","hochschule","typ","verein","firmenmitgliedschaft","jahresbeitrag",
 "listungsseite","bewertung","k1_name","k1_funktion","k1_email","k1_verify","k1_quelle",
 "k2_name","k2_funktion","k2_email","k2_verify","k2_quelle"]
MAP={"FIRMEN-LINKS":"LINK VERIFIZIERT","FIRMEN-LOGOS":"SPONSORING-SEITE",
     "PARTNERBEREICH":"PARTNERBEREICH","KEINE FIRMEN":"AUSGESCHLOSSEN"}

def norm(s): return re.sub(r"\s+"," ",(s or "").strip().lower())

def renumber(rows):
    n=s=pb=p=0
    for r in rows[1:]:
        st=r[1].upper()
        if st.startswith("LINK VERIFIZIERT"): n+=1; r[0]=str(n)
        elif st.startswith("SPONSORING"): s+=1; r[0]=f"S{s}"
        elif st.startswith("PARTNERBEREICH"): pb+=1; r[0]=f"PB{pb}"
        elif st.startswith("PRÜFEN") or st.startswith("PRUEFEN"): p+=1; r[0]=f"P{p}"
        else: r[0]="-"

def main():
    data=json.load(open(sys.argv[1]))
    rows=list(csv.reader(open(CSV)))
    idx={norm(r[2]):r for r in rows[1:]}
    upd=miss=0; log=[]
    for it in data:
        st=(it.get("status","") or "").strip().upper()
        st=MAP.get(st,st)
        row=idx.get(norm(it.get("hochschule","")))
        if not row:
            miss+=1; log.append(f"  !! NO MATCH: {it.get('hochschule')}"); continue
        vals=[st]+[str(it.get(k,"") or "") for k in KEYS[1:]]
        # row layout: [Nr, status, hochschule, typ, verein, firmenmit, jahr, listung, bewert, k1.., k2..]
        # status (i=0) always set; other fields only overwrite when new value non-empty
        for i,v in enumerate(vals):
            if i==0 or v.strip(): row[i+1]=v
        upd+=1; log.append(f"  {it.get('hochschule')[:48]}: -> {st}")
    renumber(rows)
    bad=[i for i,r in enumerate(rows) if len(r)!=19]
    assert not bad, f"row width broke at {bad}"
    csv.writer(open(CSV,"w",newline="")).writerows(rows)
    print(f"updated {upd}, no-match {miss}")
    for m in log: print(m)

if __name__=="__main__": main()
