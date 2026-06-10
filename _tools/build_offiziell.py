#!/usr/bin/env python3
"""Konsolidiert ausschliesslich OFFIZIELLE Stadt-/Gemeinde-Domains (stadt.de + Subdomains)
mit veroeffentlichter Firmen-Sponsoren-/Partnerseite. Separate Portale (Stadtmarketing-/
Tourismus-GmbH, Event-/Festival-Domains) sind ausgeschlossen.
Spalten kompatibel zur Outreach-Logik."""
import csv

COLS = ["Nr","Status","Stadt","Domain","Listungsseite","Firmen_ca","Bewertung",
        "K1_Name","K1_Funktion","K1_Email","K1_Verify","K2_Name","K2_Email","K2_Verify"]

# Status-Praefix: F = FIRMEN-LINKS (>=6 dofollow), L = FIRMEN-LOGOS (>=4 unverlinkt),
#                 PB = PARTNERBEREICH (1-5 Firmen)
rows = [
 # --- FIRMEN-LINKS (stark, >=6 dofollow Firmenlinks auf offizieller Domain) ---
 ["FIRMEN-LINKS","Nordhorn","nordhorn.de","nordhorn.de/portal/seiten/sponsor-innen-900000253-26710.html","~19","32 dofollow, ~19 echte Firmen auf offiz. Stadtdomain",
  "Karsten Müller","Leitung Wirtschaftsförderung","karsten.mueller@nordhorn.de","risky (accept_all)","VVV-Citymarketing","info@vvv-nordhorn.de","deliverable (100)"],
 ["FIRMEN-LINKS","Bremerhaven","bremerhaven.de","bremerhaven.de/de/veranstaltungen/sail-2025/service/sponsoren-medienpartner.77635.html","~30","~30 dofollow Firmen (aida, blg-logistics, eurogate, gewoba, swb) auf offiz. Domain",
  "Karolin Meier","Erlebnis Bremerhaven","meier@erlebnis-bremerhaven.de","nicht geprüft","Laura Bohlmann","laura.bohlmann@magistrat.bremerhaven.de","nicht geprüft"],
 ["FIRMEN-LINKS","Braunschweig","braunschweig.de","braunschweig.de/tdn/sponsoren-tdn.php","~34","34 Firmen mit dofollow (rel=external) auf offiz. Domain, HTML verifiziert",
  "Tobias Grosch","Projektleiter Veranstaltungen Stadtmarketing","tobias.grosch@braunschweig.de","Muster bestätigt","Nina-Rebecca Fritzler","stadtmarketing@braunschweig.de","Muster"],
 ["FIRMEN-LINKS","Hamm","hamm.de","hamm.de/erfahren/sponsoren","~27","27 dofollow Firmen auf offiz. Stadtdomain",
  "Stadtmarketing Hamm","Stadtmarketing","stadtmarketing@stadt.hamm.de","nicht geprüft","","",""],
 ["FIRMEN-LINKS","Dortmund","dortmund.de","dortmund.de/dortmund-erleben/freizeit-und-kultur/museen/dortmunder-dew21-museumsnacht/sponsor-innen/","~8","8 dofollow Firmen (DEW21-Museumsnacht) auf offiz. Domain",
  "Silke Hempel","Presse/Kulturbetriebe","shempel@stadtdo.de","nicht geprüft","Katrin Pinetzki","katrin.pinetzki@stadtdo.de","nicht geprüft"],
 ["FIRMEN-LINKS","Ravensburg","ravensburg.de","ravensburg.de/rv/wirtschaft-planen-bauen/stadtmarketing/partner.php","~17","22 dofollow, ~17 echte Firmen auf offiz. Domain",
  "Patricia della Monica","Abteilungsleitung Stadtmarketing","patricia.della-monica@ravensburg.de","deliverable (100)","","",""],
 ["FIRMEN-LINKS","Ludwigsburg","ludwigsburg.de","visit.ludwigsburg.de/start/presse+_+b2b/partner+und+sponsoren.html","~12","17 dofollow, >=12 Firmen auf offiz. Subdomain visit.ludwigsburg.de",
  "Mario Kreh","Leiter Tourismus & Events","m.kreh@ludwigsburg.de","deliverable (100)","Tourismus & Events","tourismusevents@ludwigsburg.de","deliverable (100)"],
 ["FIRMEN-LINKS","Langenfeld","langenfeld.de","langenfeld.de/Seiten/Mitglieder-von-Kommit-e-V.html","~6","10 dofollow, ~6 Firmen (KOMMIT) auf offiz. Domain",
  "Jan Chr. Zimmermann","Citymanager Stadt Langenfeld","info@langenfeld.de","deliverable (100)","","",""],
 ["FIRMEN-LINKS","Göttingen","goettingen.de","kultursommer.goettingen.de/sponsoren/","~8","dofollow Firmen-Sponsoren auf offiz. Subdomain kultursommer.goettingen.de",
  "J. Korrek","Kultursommer","j.korrek@goettingen.de","nicht geprüft","Öffentlichkeitsarbeit","oeffentlichkeitsarbeit@goettingen.de","nicht geprüft"],
 ["FIRMEN-LINKS","Mainz","mainz.de","mainz.de/angebote-entdecken/mobiliaet-und-verkehr/fahrrad/aktionen/stadtradeln","~16","16 dofollow Firmenlinks (Stadtradeln) auf offiz. Domain",
  "Ellen König","Pressestelle/Kommunikation","pressestelle@stadt.mainz.de","Muster","","",""],
 ["FIRMEN-LINKS","Magdeburg","magdeburg.de","wissenschaftsnacht.magdeburg.de/unterstuetzer","~6","6 dofollow Firmen + 13 unverlinkt auf offiz. (Sub)domain",
  "Pressestelle","Presse-/Öffentlichkeitsarbeit","presse@magdeburg.de","Muster","","",""],
 ["FIRMEN-LINKS","Jena","jena.de","rathaus.jena.de (Fassadenpreis)","~17","17 Firmen (Fassadenpreis) auf offiz. Subdomain rathaus.jena.de",
  "Stefanie Braune","Stadt Jena","stefanie.braune@jena.de","nicht geprüft","","",""],

 # --- FIRMEN-LOGOS (>=4 Firmen genannt, unverlinkt/Logowand, offizielle Domain) ---
 ["FIRMEN-LOGOS","Aalen","aalen.de","aalen.de/sponsoren-partner.85796.25.htm","~7","Sponsoren&Partner (Reichsstädter Tage) Logowand auf offiz. Domain",
  "Kultur & Tourismus Aalen","Stadtfest-Organisation","kultur@aalen.de","nicht geprüft","","",""],
 ["FIRMEN-LOGOS","Saarbrücken","saarbruecken.de","altstadtfest.saarbruecken.de/partner","~8","~8 Firmenlogos (Altstadtfest) auf offiz. Subdomain",
  "Anne Kaib","Stadt Saarbrücken","anne.kaib@saarbruecken.de","nicht geprüft","Christoph Conrad","christoph.conrad@saarbruecken.de","nicht geprüft"],
 ["FIRMEN-LOGOS","Siegen","siegen.de","siegen.de/kultur-tourismus/kultur-und-kunst/partner-und-sponsoren/","~7","7 Firmen (KulturSiegen) auf offiz. Domain",
  "Katja Fünfsinn","Leiterin KulturSiegen","info@kultursiegen.de","Funktionsadresse","","",""],
 ["FIRMEN-LOGOS","Gütersloh","guetersloh.de","guetersloh.de/de/rathaus/presseportal/news/meldungen/reihe-vier-jahreszeiten.php","~7","KulturPLUS+ 7 Firmen (Bertelsmann, Miele, Beckhoff) auf offiz. Domain",
  "Tim Burrows","Fachbereich Kultur / Eventmanagement","tim.burrows@guetersloh.de","Muster","","",""],
 ["FIRMEN-LOGOS","Hildesheim","stadt-hildesheim.de","stadt-hildesheim.de/portal/meldungen/sommerferien-...-900005052-33610.html","~4","Ferienpass 4 Firmen (Sparkasse HGP, EVI, BWV, Kühn) auf offiz. Domain",
  "Bereich Jugend/Ferienpass","Stadt Hildesheim","","","","",""],

 # --- PARTNERBEREICH (1-5 Firmen auf offizieller Domain) ---
 ["PARTNERBEREICH","Neuwied","neuwied.de","neuwied.de/deichstadtfest","3","3 dofollow Firmen (Deichstadtfest) auf offiz. Domain",
  "Amt für Stadtmarketing","Citymarketing","citymarketing@neuwied.de","risky (accept_all)","","",""],
 ["PARTNERBEREICH","Lingen","lingen.de","lingen.de/.../stadtjubilaeum-2025/sponsoring.html","Sponsoring","Stadtjubiläum-Sponsoring (Pakete) auf offiz. Domain, Sponsoren unverlinkt",
  "Ludger Tieke","Wirtschaftsförderung","l.tieke@lingen.de","deliverable (100)","Projektteam 1050","1050@lingen.de","deliverable (91)"],
 ["PARTNERBEREICH","Paderborn","paderborn.de","paderborn.de/microsite/libori/index.php","1-5","Libori-Sponsoring auf offiz. Domain",
  "S. Hermanns","Stadt Paderborn","s.hermanns@paderborn.de","nicht geprüft","","",""],
 ["PARTNERBEREICH","Wuppertal","wuppertal.de","wuppertal.de/microsite/langer-tisch/Sponsoren_/index.php","1-5","Langer Tisch Sponsoren auf offiz. Domain",
  "Wuppertal Marketing","Stadtmarketing","info@wuppertal-marketing.de","nicht geprüft","","",""],
 ["PARTNERBEREICH","Offenbach am Main","offenbach.de","offenbach.de/unternehmen/gruenderstadt-offenbach/partner.php","1-5","Gründerstadt-Partner auf offiz. Domain",
  "Stadt Offenbach","Wirtschaftsförderung","info@offenbach.de","nicht geprüft","","",""],
 ["PARTNERBEREICH","Ingolstadt","ingolstadt.de","theater.ingolstadt.de/service/haus/sponsoren-partner.html","1-5","Theater-Sponsoren auf offiz. Subdomain",
  "Theater Ingolstadt","Theater","info@theater.ingolstadt.de","nicht geprüft","","",""],
 ["PARTNERBEREICH","Rostock","rostock.de","rathaus.rostock.de/.../sponsoren_partner_der_29_hanse_sail_rostock/275389","6-7","Hanse Sail Sponsoren (Prosa) auf offiz. Subdomain",
  "Ulrich Kunze","Pressesprecher","presse@rostock.de","Muster","","",""],
 ["PARTNERBEREICH","Erfurt","erfurt.de","erfurt.de/ef/de/service/aktuelles/pm/2025/151660.html","3","Krämerbrückenfest 3 Firmen (Prosa) auf offiz. Domain","","","","","","",""],
 ["PARTNERBEREICH","Lübeck","luebeck.de","luebeck.de/de/presse/pressemeldungen/view/135212","3-5","Stadtradeln 3-5 Firmen (Prosa) auf offiz. Domain","","","","","","",""],
 ["PARTNERBEREICH","Hagen","hagen.de","hagen.de/aus-dem-rathaus/.../kulturbuero-hagen/","3","Kulturbüro Hauptsponsoren (Prosa) auf offiz. Domain","","","","","","",""],
 ["PARTNERBEREICH","Schwerin","schwerin.de","schwerin.de/.../konservatorium/sponsoren-foerderer-partner/","1","Konservatorium Sponsorenseite (Sparkassen-Stiftung) auf offiz. Domain","","","","","","",""],
 ["PARTNERBEREICH","Düren","dueren.de","dueren.de/.../lions-kulturtage...","1","Lions Kulturtage (Sparkasse Düren) auf offiz. Domain","","","","","","",""],
]

with open("recherche_staedte_offiziell.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(COLS)
    n=0
    for r in rows:
        n+=1
        w.writerow([n]+r)
print(f"{n} offizielle Stadt-Domains geschrieben.")
fl=sum(1 for r in rows if r[0]=="FIRMEN-LINKS")
lo=sum(1 for r in rows if r[0]=="FIRMEN-LOGOS")
pb=sum(1 for r in rows if r[0]=="PARTNERBEREICH")
print(f"FIRMEN-LINKS={fl}  FIRMEN-LOGOS={lo}  PARTNERBEREICH={pb}")
