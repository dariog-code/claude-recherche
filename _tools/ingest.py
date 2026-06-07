#!/usr/bin/env python3
"""Ingest a JSON array of findings into the master CSV.
Assigns Nr per status, appends rows, and git-commits per institution.
Usage: ingest.py <results.json>
Pushing is done by the caller after the batch.
"""
import sys, csv, json, subprocess, re

CSV = "/home/user/claude-recherche/recherche_master_foerdervereine.csv"
COLS = ["Nr","Status","Hochschule","Typ","Verein","Firmenmitgliedschaft",
 "Jahresbeitrag_Firma","Foerderer_Listungsseite","Listung_Domain_Bewertung",
 "Kontakt1_Name","Kontakt1_Funktion","Kontakt1_Email","Kontakt1_Verify","Kontakt1_Quelle",
 "Kontakt2_Name","Kontakt2_Funktion","Kontakt2_Email","Kontakt2_Verify","Kontakt2_Quelle"]
KEYS = ["status","hochschule","typ","verein","firmenmitgliedschaft","jahresbeitrag",
 "listungsseite","bewertung","k1_name","k1_funktion","k1_email","k1_verify","k1_quelle",
 "k2_name","k2_funktion","k2_email","k2_verify","k2_quelle"]

def next_counters():
    rows=list(csv.reader(open(CSV)))
    num=0; s=0; p=0
    for r in rows[1:]:
        nr=r[0].strip()
        if re.fullmatch(r"\d+",nr): num=max(num,int(nr))
        elif re.fullmatch(r"S\d+",nr): s=max(s,int(nr[1:]))
        elif re.fullmatch(r"P\d+",nr): p=max(p,int(nr[1:]))
    return {"num":num,"s":s,"p":p}

def assign(status,c):
    st=status.upper()
    if st.startswith("LINK VERIFIZIERT"): c["num"]+=1; return str(c["num"])
    if st.startswith("SPONSORING"): c["s"]+=1; return f"S{c['s']}"
    if st.startswith("PRÜFEN") or st.startswith("PRUEFEN"): c["p"]+=1; return f"P{c['p']}"
    return "-"  # AUSGESCHLOSSEN / KEIN FUND

def git(*args):
    subprocess.run(["git","-C","/home/user/claude-recherche",*args],check=True,
                   capture_output=True)

def main():
    data=json.load(open(sys.argv[1]))
    c=next_counters()
    added=[]
    for it in data:
        nr=assign(it.get("status",""),c)
        row=[nr]+[str(it.get(k,"") or "") for k in KEYS]
        assert len(row)==19
        with open(CSV,"a",newline="") as f:
            csv.writer(f).writerow(row)
        # validate
        chk=list(csv.reader(open(CSV)))
        bad=[i for i,r in enumerate(chk) if len(r)!=19]
        assert not bad, f"CSV broke at {bad} after {it.get('hochschule')}"
        git("add",CSV)
        msg=f"{it.get('hochschule')}: {it.get('status')} [{nr}]"
        git("commit","-q","-m",msg)
        added.append(msg)
    print(f"ingested {len(added)} rows:")
    for m in added: print("  ",m)

if __name__=="__main__": main()
