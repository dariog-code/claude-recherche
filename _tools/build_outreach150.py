#!/usr/bin/env python3
"""Baut die finale 150er Hybrid-Outreach-Liste:
- 44 OFFIZIELLE Stadt-/Gemeinde-Domains (recherche_staedte_offiziell.csv) -> Herkunft=offiziell
- aufgefuellt mit den staerksten STADT-NAHEN Portalen (outreach_staedte.csv) -> Herkunft=stadtnah
Dedupe nach Stadtname (offiziell gewinnt). Ranking stadtnah: sendbar > Status > DR.
"""
import csv, re

def norm(s):
    s=s.lower()
    s=re.sub(r'\s*\(.*?\)','',s)
    s=s.split(',')[0].split(' am ')[0].split(' an ')[0].split('/')[0]
    s=s.replace('ae','a').replace('oe','o').replace('ue','u').replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss')
    return re.sub(r'[^a-z]','',s)

OUT_COLS=["Herkunft","Status","Stadt","Linkdomain","Sponsoren_Partnerseite_URL","Firmen_ca",
          "DR","Email","Anrede","Ansprechpartner","Funktion","Hunter_Result","Versandempfehlung"]

rows=[]
seen=set()

# Hunter-verifizierte Kontakt-Overrides fuer offizielle Domains (Stand: heute)
# Stadt -> (email, name, funktion, hunter_result, versand)
OV={
 "Bremerhaven":("meier@erlebnis-bremerhaven.de","Karolin Meier","Erlebnis Bremerhaven","deliverable (100)","OK senden"),
 "Hamm":("stadtmarketing@stadt.hamm.de","","Stadtmarketing Hamm","deliverable (100)","OK senden"),
 "Dortmund":("katrin.pinetzki@stadtdo.de","Katrin Pinetzki","Presse/Kulturbetriebe","deliverable (100)","OK senden"),
 "Göttingen":("presse@goettingen.de","","Pressestelle Stadt Göttingen","deliverable (100)","OK senden"),
 "Jena":("stefanie.braune@jena.de","Stefanie Braune","Stadt Jena","risky/catch-all (82)","OK (Catch-all) senden"),
 "Aalen":("kultur@aalen.de","","Kultur & Tourismus Aalen","risky/catch-all (72)","OK (Catch-all) senden"),
 "Saarbrücken":("anne.kaib@saarbruecken.de","Anne Kaib","Stadt Saarbrücken","risky/catch-all (81)","OK (Catch-all) senden"),
 "Siegen":("info@kultursiegen.de","Katja Fünfsinn","Leiterin KulturSiegen","deliverable (100)","OK senden"),
 "Hildesheim":("m.biskup@stadt-hildesheim.de","Meike Biskup","Stadt Hildesheim","deliverable (100)","OK senden"),
 "Paderborn":("s.hermanns@paderborn.de","S. Hermanns","Stadt Paderborn (Libori)","risky/catch-all (80)","OK (Catch-all) senden"),
 "Wuppertal":("info@wuppertal-marketing.de","","Wuppertal Marketing","deliverable (100)","OK senden"),
 "Offenbach am Main":("info@offenbach.de","","Stadt Offenbach Wirtschaftsförderung","risky/catch-all (81)","OK (Catch-all) senden"),
 "Ingolstadt":("info@theater.ingolstadt.de","","Theater Ingolstadt","risky/catch-all (81)","OK (Catch-all) senden"),
 "Erfurt":("presse@erfurt.de","","Pressestelle Stadt Erfurt","deliverable (100)","OK senden"),
 "Lübeck":("presse@luebeck.de","","Pressestelle Hansestadt Lübeck","risky (76)","vorsichtig senden"),
 "Hagen":("","","Kulturbüro Hagen (hagen.de blockt SMTP-Check)","SMTP blockiert","manuell - Kontaktformular/Telefon"),
 "Schwerin":("info@schwerin.de","","Stadt Schwerin (Konservatorium)","deliverable (100)","OK senden"),
 "Düren":("presse@dueren.de","","Pressestelle Stadt Düren","risky/catch-all (72)","OK (Catch-all) senden"),
 "Rhede":("info@rhede.de","Martin Bröker","Stadt Rhede Kämmerei","deliverable (100)","OK senden"),
 "Seevetal":("stadtradeln@seevetal.de","","Gemeinde Seevetal Umwelt","deliverable (89)","OK senden"),
 "Lauterecken":("stadthaus@lauterecken.de","Isabel Steinhauer-Theis","Stadtbürgermeisterin","deliverable (100)","OK senden"),
 "Heide":("stadtmarketing@heide.de","","Stadtmarketing Heide","deliverable (100)","OK senden"),
 "Mainz":("pressestelle@stadt.mainz.de","Ellen König","Pressestelle/Kommunikation","risky/catch-all (78)","OK (Catch-all) senden"),
 "Magdeburg":("presse@magdeburg.de","","Pressestelle Stadt Magdeburg","deliverable (100)","OK senden"),
 "Braunschweig":("tobias.grosch@braunschweig.de","Tobias Grosch","Projektleiter Veranstaltungen Stadtmarketing","deliverable (100)","OK senden"),
}

# 1) offizielle Domains
for r in csv.DictReader(open("recherche_staedte_offiziell.csv")):
    stadt=r["Stadt"]
    email=r["K1_Email"].strip() or r["K2_Email"].strip()
    name=r["K1_Name"].strip() or r["K2_Name"].strip()
    funk=r["K1_Funktion"].strip()
    ver=r["K1_Verify"].strip() or r["K2_Verify"].strip()
    vl=ver.lower()
    if "deliverable" in vl or "(100)" in vl or "(91)" in vl or "(90)" in vl:
        hr,vs="deliverable","OK senden"
    elif "risky" in vl or "accept_all" in vl or "muster" in vl or "(8" in vl or "(7" in vl:
        hr,vs="risky/catch-all","OK (Catch-all) senden"
    else:
        hr,vs="ungeprüft","vor Versand verifizieren"
    if not email:
        hr,vs="kein Kontakt","Kontakt recherchieren"
    if stadt in OV:                       # verifizierter Override
        email,n2,f2,hr,vs=OV[stadt]
        if n2: name=n2
        if f2: funk=f2
    rows.append({"Herkunft":"offiziell","Status":r["Status"],"Stadt":stadt,
                 "Linkdomain":r["Domain"],"Sponsoren_Partnerseite_URL":r["Listungsseite"],
                 "Firmen_ca":r["Firmen_ca"],"DR":"","Email":email,"Anrede":"",
                 "Ansprechpartner":name,"Funktion":funk,"Hunter_Result":hr,"Versandempfehlung":vs})
    seen.add(norm(stadt))

# 2) stadtnahe Portale aus outreach_staedte.csv
cand=[]
for r in csv.DictReader(open("outreach_staedte.csv")):
    if norm(r["Stadt"]) in seen:        # offiziell hat Vorrang
        continue
    if r["Status"]=="KEINE FIRMEN":
        continue
    cand.append(r)

# Hunter-verifizierte Kontakt-Korrekturen fuer stadtnahe Zeilen (Original-Kontakt unzustellbar)
STADTNAH_OV={
 "coburg":("diana.schmitt@coburg.de","Diana Schmitt","Wirtschaftsförderung Stadt Coburg","deliverable","OK senden"),
 "frankfurt":("info@frankfurt.de","","Stadt Frankfurt am Main","deliverable","OK senden"),
 "hannover":("presse@hannover.de","","Pressestelle Stadt Hannover","risky/catch-all","OK (Catch-all) senden"),
 "badhomburg":("nina.gerlach@bad-homburg.de","Nina Gerlach","Leitung City-Marketing Bad Homburg","risky/catch-all (82)","OK (Catch-all) senden"),
 "furth":("miguel.ortega@fuerth.de","Miguel Ortega","GF Stadtmarketing Fürth (SMTP ungeprüft, Hunter conf 98)","unbestätigt","vorsichtig senden"),
 "fellbach":("presse@fellbach.de","","Pressestelle Stadt Fellbach","risky/catch-all (73)","OK (Catch-all) senden"),
 "landshut":("thomas.kolbinger@landshut.de","Thomas Kolbinger","Pressestelle/OB-Büro Landshut (SMTP ungeprüft, Hunter conf 99)","unbestätigt","vorsichtig senden"),
 "bietigheimbissingen":("presse@bietigheim-bissingen.de","","Pressestelle Bietigheim-Bissingen","risky/catch-all (73)","OK (Catch-all) senden"),
 "reutlingen":("peter.wilke@reutlingen.de","Peter Wilke","Wirtschaftsförderung Reutlingen","risky/catch-all (78)","OK (Catch-all) senden"),
}

statrank={"FIRMEN-LINKS":0,"FIRMEN-LOGOS":1,"PARTNERBEREICH":2}
def sendbar(r): return r.get("Versandempfehlung","").startswith("OK")
def dr(r):
    try: return int(r.get("DR_Linkdomain") or 0)
    except: return 0
cand.sort(key=lambda r:(0 if sendbar(r) else 1, statrank.get(r["Status"],3), -dr(r)))

# Memmingen ergaenzen (staerkstes noch nicht gelistetes stadtnahes Portal: 105 dofollow Firmen)
if norm("Memmingen") not in seen:
    cand.insert(0,{"Status":"FIRMEN-LINKS","Stadt":"Memmingen","Linkdomain":"stadtmarketing-memmingen.de",
        "Sponsoren_Partnerseite_URL":"stadtmarketing-memmingen.de/einkaufen","DR_Linkdomain":"",
        "Email":"info@stadtmarketing-memmingen.de","Anrede":"","Ansprechpartner":"Emma Brader",
        "Funktion":"Geschäftsstelle Stadtmarketing Memmingen","Hunter_Result":"deliverable",
        "Versandempfehlung":"OK senden"})

need=150-len(rows)
for r in cand[:need]:
    em,nm,fu=r["Email"],r["Ansprechpartner"],r["Funktion"]
    hr,vs=r["Hunter_Result"],r["Versandempfehlung"]
    ov=STADTNAH_OV.get(norm(r["Stadt"]))
    if ov:
        em,n2,f2,hr,vs=ov
        if n2: nm=n2
        if f2: fu=f2
    rows.append({"Herkunft":"stadtnah","Status":r["Status"],"Stadt":r["Stadt"],
                 "Linkdomain":r["Linkdomain"],"Sponsoren_Partnerseite_URL":r["Sponsoren_Partnerseite_URL"],
                 "Firmen_ca":"","DR":r.get("DR_Linkdomain",""),"Email":em,"Anrede":r["Anrede"],
                 "Ansprechpartner":nm,"Funktion":fu,
                 "Hunter_Result":hr,"Versandempfehlung":vs})
    seen.add(norm(r["Stadt"]))

with open("outreach_150_final.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=OUT_COLS); w.writeheader()
    for i,r in enumerate(rows,1):
        w.writerow(r)

from collections import Counter
print(f"GESAMT: {len(rows)}")
print("Herkunft:",Counter(r['Herkunft'] for r in rows))
print("Status:",Counter(r['Status'] for r in rows))
print("Versand:",Counter(r['Versandempfehlung'] for r in rows))
print("--- offizielle Zeilen ohne sendbaren Kontakt: ---")
for r in rows:
    if r["Herkunft"]=="offiziell" and not r["Versandempfehlung"].startswith("OK"):
        print(" ",r["Stadt"],"|",r["Email"] or "(keine)","|",r["Versandempfehlung"])
