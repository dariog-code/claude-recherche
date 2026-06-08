#!/usr/bin/env python3
"""Update existing master-CSV rows from a JSON array (keyed by 'hochschule').
Updates: Status (new_status), Foerderer_Listungsseite (beste_seite), Listung_Domain_Bewertung (bewertung).
Optionally Kontakt1_Email/Verify/Quelle if provided non-empty.
If status changes to/from numbered classes, the Nr is REASSIGNED accordingly.
Git-commits per institution. Usage: update_rows.py <results.json>
"""
import sys, csv, json, subprocess, re
CSV="/home/user/claude-recherche/recherche_master_foerdervereine.csv"

def load(): return list(csv.reader(open(CSV)))
def save(rows):
    with open(CSV,"w",newline="") as f: csv.writer(f).writerows(rows)

def counters(rows):
    num=s=p=0
    for r in rows[1:]:
        nr=r[0].strip()
        if re.fullmatch(r"\d+",nr): num=max(num,int(nr))
        elif re.fullmatch(r"S\d+",nr): s=max(s,int(nr[1:]))
        elif re.fullmatch(r"P\d+",nr): p=max(p,int(nr[1:]))
    return {"num":num,"s":s,"p":p}

def git(*a): subprocess.run(["git","-C","/home/user/claude-recherche",*a],check=True,capture_output=True)

def main():
    data=json.load(open(sys.argv[1]))
    done=[]
    for it in data:
        rows=load(); c=counters(rows)
        name=it["hochschule"]
        idx=[i for i,r in enumerate(rows) if r[2]==name]
        if not idx:
            print("!! not found:",name); continue
        i=idx[0]; row=rows[i]
        old_status=row[1]; new_status=it.get("new_status",old_status) or old_status
        # reassign Nr only if class changed
        def cls(s):
            s=s.upper()
            if s.startswith("LINK VERIFIZIERT"): return "num"
            if s.startswith("SPONSORING"): return "s"
            if s.startswith("PRÜFEN") or s.startswith("PRUEFEN"): return "p"
            return "x"
        if cls(new_status)!=cls(old_status):
            cl=cls(new_status)
            if cl=="num": c["num"]+=1; row[0]=str(c["num"])
            elif cl=="s": c["s"]+=1; row[0]=f"S{c['s']}"
            elif cl=="p": c["p"]+=1; row[0]=f"P{c['p']}"
            else: row[0]="-"
        row[1]=new_status
        if it.get("beste_seite"): row[7]=it["beste_seite"]
        if it.get("bewertung"): row[8]=it["bewertung"]
        if it.get("k1_email"):
            row[11]=it["k1_email"]
            if it.get("k1_verify"): row[12]=it["k1_verify"]
            if it.get("k1_quelle"): row[13]=it["k1_quelle"]
        assert len(row)==19
        rows[i]=row; save(rows)
        chk=load(); bad=[j for j,r in enumerate(chk) if len(r)!=19]
        assert not bad, f"broke at {bad} ({name})"
        git("add",CSV)
        git("commit","-q","-m",f"Re-check {name}: {new_status} (Potenzial {it.get('potenzial','?')}) [{row[0]}]")
        done.append(f"{row[0]:4} {new_status:18} Pot={it.get('potenzial','?'):6} {name}")
    print(f"updated {len(done)} rows:")
    for d in done: print("  ",d)

if __name__=="__main__": main()
