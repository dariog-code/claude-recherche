# Progress-Log — Recherche Förderer/Sponsoring deutscher Hochschulen

## ⚠️ UMGEBUNGS-STATUS / BLOCKER (wichtig zuerst lesen)

**Stand 2026-06-06, Beginn der Cloud-Session.**

Diese Cloud-Session läuft hinter einer **restriktiven Netzwerk-Allowlist**. Konkret getestet:

| Ziel | Ergebnis |
|------|----------|
| WebSearch (über Anthropic) | ✅ funktioniert |
| GitHub MCP | ✅ funktioniert |
| `curl`/`WebFetch` auf Hochschul-Domains (fh-wedel.de, tu-dresden.de, kit.edu, uni-goettingen.de …) | ❌ **HTTP 403 `x-deny-reason: host_not_allowed`** |
| `api.hunter.io` (Email-Verifier / Domain-Search) | ❌ **HTTP 403 `Host not in allowlist`** |

**Folge:** Die beiden Kern-Verifikationsschritte der Methodik sind in dieser Session **nicht ausführbar**:
1. **HTML-/`<a href>`-Analyse** (Voraussetzung für Status „LINK VERIFIZIERT" und für Dofollow-/Subdomain-/≥6-Firmen-Prüfung) — Seiten lassen sich nicht abrufen.
2. **Hunter Email-Verifier** — der Hunter-Key liegt jetzt vor (vom Nutzer übermittelt, in `~/.hunter_key` gespeichert), aber `api.hunter.io` ist nicht in der Allowlist, der Key ist also wirkungslos.

**Was der Nutzer tun muss, damit die volle Recherche läuft** (eine der Optionen):
- Netzwerk-Policy der Environment auf **„No network restrictions"** umstellen, **oder**
- der Allowlist die Hosts **`api.hunter.io`** sowie die Hochschul-Domains (bzw. `*`) hinzufügen.
- Doku: https://code.claude.com/docs/en/claude-code-on-the-web

Sobald das erledigt ist, kann eine Folge-Session die hier vorbereitete `arbeitsliste.md` (Discovery + provisorische Einstufung) zügig mit echter Link- und Email-Verifikation abarbeiten.

**Was in dieser Session trotzdem geleistet wird (Degraded-Mode, nur WebSearch):**
- Aufbau der vollständigen `arbeitsliste.md` (alle Unis/HAW/private HS mit Domains, Fortschritt).
- WebSearch-Discovery je Institution: Kandidaten-URL finden, **Hauptdomain vs. Subdomain** aus der URL bewerten (machbar ohne Abruf), Modell (Sponsoring-mit-Gegenleistung vs. dual/Deutschlandstipendium) aus Snippets einschätzen.
- Die **Master-CSV bleibt sauber**: keine unverifizierten „LINK VERIFIZIERT"/„SPONSORING-SEITE"-Zeilen werden eingetragen. Discovery-Befunde landen als provisorische Einstufung in `arbeitsliste.md`; nur klar bestimmbare Modell-/Domain-Ausschlüsse werden ggf. als `AUSGESCHLOSSEN` ergänzt.
- Periodischer Re-Test des Netzwerks; falls die Allowlist während der Session geöffnet wird, wird automatisch auf volle Verifikation (curl-HTML + Hunter) umgeschaltet.

---

## Ausgangslage

Master-CSV vom Nutzer übernommen (Single Source of Truth): **55 Datenzeilen**
- LINK VERIFIZIERT: 4 (HdM Stuttgart, OTH Amberg-Weiden, TH Georg Agricola Bochum, THWS Würzburg-Schweinfurt)
- SPONSORING-SEITE: 15 (S1–S15)
- PRÜFEN / GRENZFALL / AUSGESCHLOSSEN: Rest

---

## Discovery-Log (chronologisch)

| Zeitstempel | Institution | Disposition (Discovery) | Notiz |
|-------------|-------------|--------------------------|-------|
| 2026-06-06 | TU Berlin | KANDIDAT (verify) | tu.berlin sponsoring-and-donating Hauptdomain, Gegenleistung Logo; Verlink./Email offen (Netz-Blocker) |
| 2026-06-06 | TU Dresden | KANDIDAT schwach | Hauptdomain /spenden, aber Spende o. Gegenleistung; Deutschlandstip.-Logo nur Event-Slides; GFF Förderverein |
| 2026-06-06 | TU Darmstadt | KANDIDAT (verify) | Hauptdomain werbung_promotion/universitaetsfoerderung; Detail auf Subdomain intern.tu-darmstadt.de |
| 2026-06-06 | TU Braunschweig | RAUS (Modell) | kein aktives Sponsoring lt. eigener Aussage; Partner ohne Links → AUSSCHLUSS-Kandidat |
| 2026-06-06 | TU Dortmund | KEIN FUND | keine allg. Hauptdomain-Sponsoring-Seite; nur Event-Sponsoren + Subdomains |
| 2026-06-06 | RPTU Kaiserslautern-Landau | KANDIDAT (verify) | rptu.de stiften-und-foerdern Hauptdomain; Sponsoring via proCampus GmbH; Freundeskreis eigene Domain |
| 2026-06-06 | Uni Göttingen | KANDIDAT (verify) gut | uni-goettingen.de/en/sponsors + Förder-Seite Hauptdomain; Gegenleistung Logo im Internet |
| 2026-06-06 | Uni Würzburg | RAUS-lean | nur Deutschlandstipendium-Logo-Nutzung; keine Sponsoring-mit-Link-Seite gefunden |
| 2026-06-06 | FAU Erlangen-Nürnberg | KANDIDAT (verify) | fau.de/outreach Hauptdomain Sponsoring m. Firmenlogo; Listung evtl. unibund.fau.de Subdomain |
| 2026-06-06 | Uni Augsburg | KANDIDAT (verify) | uni-augsburg.de/de/foerderer/foerdermoeglichkeiten Imagepartnerschaft/Sponsoring m. Gegenleistung |
| 2026-06-06 | Uni Bayreuth | KANDIDAT (verify) | uni-bayreuth.de supporting-the-university; Unternehmen tlw. marketing.uni-bayreuth.de (Subdomain); KUK Kontakt |
| 2026-06-06 | Uni Regensburg | KANDIDAT (verify) | uni-regensburg.de forschungsfoerderung/foerderer/wirtschaft; lt. Snippet Sponsoren-Logos auf Website |
| 2026-06-06 | Uni Konstanz | KANDIDAT schwach | Hauptdomain v.a. interne Richtlinien + Universitätsgesellschaft; öff. Angebot unklar |
| 2026-06-06 | Uni Freiburg | KANDIDAT (verify) | uni-freiburg.de/universitaet/foerdern-und-stiften; Freunde-Verein auf Subdomain |
| 2026-06-06 | Uni Mannheim | KANDIDAT (verify) | Sponsoring-Pakete inkl. Website-Präsenz, aber via career./service.uni-mannheim.de Subdomains; Hauptdomain stiftung/foerdern |
| 2026-06-06 | Uni Duisburg-Essen | KANDIDAT (verify) | uni-due.de due-stiftung/stiftenspenden + marketing/foerdervereine; Sponsoringpartnerschaften |
| 2026-06-06 | Uni Bielefeld | KANDIDAT schwach | uni-bielefeld.de 50jahre/sponsoren (Event) + UGBi Hauptdomain-Pfad |
| 2026-06-06 | Uni Kiel (CAU) | KANDIDAT (verify) | uni-kiel.de/foerderer Übersicht; Alumni&Freunde auf Subdomain |
| 2026-06-06 | Uni Jena | KANDIDAT schwach | uni-jena.de/spenden + friends-and-patrons; überwiegend Spende/Freundesverein |
| 2026-06-06 | Uni Leipzig | KANDIDAT (verify) | uni-leipzig.de/universitaet/foerdern-und-unterstuetzen; Universitätsgesellschaft auf Subdomain |
| 2026-06-06 | TH Wildau | KANDIDAT schwach | Freunde/Förderer + Fördergesellschaft auf Hauptdomain-Pfad; Förderstiftung eigene Domain |
| 2026-06-06 | TH Brandenburg | KEIN FUND | nur gruendung.th-brandenburg.de Subdomain; keine Hauptdomain-Sponsoring-Seite |
| 2026-06-06 | HS Magdeburg-Stendal (h2.de) | RAUS-lean | überwiegend Deutschlandstipendium; Förderer evtl. nur Textnennung |
| 2026-06-06 | HS Merseburg | KANDIDAT (verify) | Förderungen + Förderkreis Hauptdomain; Sponsoring n. Absprache; Kontakt karriere@hs-merseburg.de |
| 2026-06-06 | HS Anhalt | KEIN FUND | keine konkrete Hauptdomain-Seite gefunden |
| 2026-06-06 | HS Mittweida | KEIN FUND/SUBDOMAIN | nur 150jahre.hs-mittweida.de Jubiläums-Sponsoren (Subdomain) |
| 2026-06-06 | HTW Dresden | KANDIDAT schwach | Förderverein + Deutschlandstip. + Spende; Sponsoring-mit-Link unklar |
| 2026-06-06 | HTWK Leipzig | KANDIDAT (verify) GUT | partner-und-foerderer Hauptdomain; Logos auf Website lt. Snippet; Siemens/Festo/BMW → evtl. LINK VERIFIZIERT |
| 2026-06-06 | HS Schmalkalden | KEIN FUND | keine Hauptdomain-Sponsoring-Seite gefunden |
| 2026-06-06 | EAH Jena | KANDIDAT (verify) | eah-jena.de/hochschule/foerderkreis + /bw/partner-und-sponsoren Hauptdomain |
| 2026-06-06 | HS Nordhausen | KEIN FUND | nur Corporate Identity/HIKE |
| 2026-06-06 | HS Stralsund | KANDIDAT (verify) | hochschule-stralsund.de Hochschulförderverein; 24 Firmen; Logo auf Website lt. Snippet |
| 2026-06-06 | HS Wismar | RAUS-lean | Deutschlandstip. + Kooperations-/Wirtschaftspartner (operativ) |
| 2026-06-06 | HS Neubrandenburg | KEIN FUND | keine Hauptdomain-Seite gefunden |
| 2026-06-06 | FH Kiel | KANDIDAT (verify) | fh-kiel.de/.../starting/sponsoren-und-foerderer (Projekt Raceyard); Sponsoren-Galerie |
| 2026-06-06 | TH Lübeck | KANDIDAT (verify) | th-luebeck.de/.../foerdergesellschaft; 200+ Mitglieder inkl. Firmen |
| 2026-06-06 | HS Flensburg | KANDIDAT schwach | Alumni-/Förderverein; kein klares Firmen-Link-Listing |
| 2026-06-06 | HfT Stuttgart | KANDIDAT (verify) | hft-stuttgart.de/hft/foerderer-unterstuetzer; Sponsoring-Optionen f. Unternehmen |
| 2026-06-06 | Hochschule Aalen | RAUS-lean (Domain) | Förderverein auf ostwuerttemberg.suedwestmetall.de (Ausschlussliste) |
| 2026-06-06 | Hochschule Heilbronn | KANDIDAT (verify) GUT | hs-heilbronn.de/de/sponsoring + /de/foerderkreis + projektpartner-und-sponsoren Hauptdomain |
| 2026-06-06 | Hochschule Pforzheim | KANDIDAT (verify) GUT | hs-pforzheim.de/unternehmen/.../infrastruktur_und_ausstattungssponsoring + veranstaltungssponsoring Hauptdomain |

---

## ABSCHLUSSBERICHT (Session 2026-06-06)

### Wichtigster Punkt: Netzwerk-Blocker (siehe oben)
Die Kern-Verifikation (HTML/`<a href>`-Linkprüfung + Hunter Email-Verifier) war **nicht möglich**, weil die Netzwerk-Allowlist dieser Cloud-Environment **alle Hochschul-Domains UND api.hunter.io blockt** (HTTP 403 `host_not_allowed`). WebSearch (über Anthropic) war das einzige verfügbare Recherchewerkzeug. Der vom Nutzer gelieferte Hunter-Key ist gespeichert, aber bis zur Allowlist-Freigabe wirkungslos.

**Damit eine Folge-Session die echte Verifikation leisten kann, bitte EINES tun:**
- Environment-Netzwerk-Policy auf „No network restrictions" stellen, ODER
- der Allowlist `api.hunter.io` + Hochschul-Domains (bzw. `*`) hinzufügen.

### Geleistet (Degraded-Mode, nur WebSearch-Discovery)
- Master-CSV als SSOT übernommen + committet (unverändert, 55 Datenzeilen; **bewusst nicht mit unverifizierten Zeilen verwässert**).
- `arbeitsliste.md` aufgebaut (Startreihenfolge + erste BW-HAW) und mit Discovery-Befunden gefüllt.
- **41 Institutionen** per WebSearch vor-recherchiert (Startreihenfolge 1+2 vollständig = 38, plus 3 BW-HAW).

### Discovery-Ergebnis (provisorisch, Link-/Email-Verifikation steht aus)
- **KANDIDAT (verify) — stark** (Hauptdomain-Sponsoring + Logos-auf-Website laut Snippet, potenziell LINK VERIFIZIERT): **HTWK Leipzig**, **HS Heilbronn**, **HS Pforzheim**, **Uni Göttingen**, Uni Mannheim, Uni Regensburg.
- **KANDIDAT (verify) — normal**: TU Berlin, TU Darmstadt, RPTU, FAU, Uni Augsburg, Uni Bayreuth, Uni Freiburg, Uni Duisburg-Essen, Uni Kiel (CAU), Uni Leipzig, HS Merseburg, EAH Jena, HS Stralsund, FH Kiel, TH Lübeck, HfT Stuttgart.
- **KANDIDAT schwach**: TU Dresden, Uni Konstanz, Uni Bielefeld, Uni Jena, TH Wildau, HTW Dresden, HS Flensburg.
- **RAUS-lean (Modell/Domain)**: TU Braunschweig (kein aktives Sponsoring), Uni Würzburg (Deutschlandstip.-only), HS Magdeburg-Stendal (Deutschlandstip.), HS Wismar (Kooperations-/Praxispartner), HS Aalen (Förderverein auf suedwestmetall.de).
- **KEIN FUND (per WebSearch)** — manuell tiefer prüfen: TU Dortmund, TH Brandenburg, HS Anhalt, HS Mittweida, HS Nordhausen, HS Neubrandenburg, HS Schmalkalden.

### Empfohlene nächste Schritte (Folge-Session mit offenem Netz)
1. Zuerst die 6 **starken** Kandidaten verifizieren (curl-HTML: ≥6 verlinkte Firmen-Domains, dofollow? + Hunter-Email) → wahrscheinlichste neue LINK-VERIFIZIERT/SPONSORING-SEITE-Einträge.
2. Dann die 16 normalen Kandidaten; SUBDOMAIN-Fälle (z.B. Uni Mannheim career./service., Uni Bayreuth marketing.) auf Hauptdomain-Pendant prüfen.
3. RAUS-lean bestätigen und als AUSGESCHLOSSEN in Master-CSV übernehmen.
4. Rest der ~400 Institutionen aus dem Hochschulkompass abarbeiten (Startreihenfolge 3 + alle übrigen HAW/private HS).

### Manuelle Nachprüfung nötig
- Alle „KEIN FUND"-Fälle (WebSearch lieferte keine eindeutige Hauptdomain-Seite).
- Alle Kandidaten generell, da Dofollow/Subdomain/≥6-Firmen + Email in dieser Session technisch nicht prüfbar waren.
| 2026-06-06 | RWU Ravensburg-Weingarten | KANDIDAT (verify) | rwu.de support-association Hauptdomain; Firmenmitglieder |
| 2026-06-06 | HS Offenburg | RAUS-lean (Modell) | Kooperations-/Industriepartner + StudiumPlus auf Fakultäts-Subdomains |
| 2026-06-06 | HS Mannheim | KANDIDAT schwach/RAUS-lean | Trainee-/Partnerunternehmen (operativ); kein Hauptdomain-Förderer-Listing |
| 2026-06-06 | HS Ulm (THU) | KANDIDAT (verify) | thu.de/de/org/kom/prothu Hauptdomain; proTHU Förderverein, Firmen Mitglied |
| 2026-06-06 | HS Augsburg (THA) | KANDIDAT (verify) GUT | tha.de/hs-augsburg.de Hoersaalgalerie + unternehmen/Foerderverein; Hörsaal-/Laborsponsoring |
| 2026-06-06 | HS Landshut | KANDIDAT (verify) | Freundeskreis (BMW/Flottweg/ebm-papst/ERLUS); Hauptdomain-Logoseite suchen |
| 2026-06-06 | TH Rosenheim | KANDIDAT (verify) | th-rosenheim.de foerdervereine + labor unterstuetzer-und-sponsoren Hauptdomain |
| 2026-06-06 | HS Kempten | (bereits AUSGESCHLOSSEN) | Hinweis: Förderkreis + Hörsaal-/Laborsponsoring (Bosch/Siemens) evtl. später reconsidern |
| 2026-06-06 | HS Niederrhein | KANDIDAT schwach/RAUS-lean | angebote-fuer-unternehmen + Deutschlandstip.-Partner (employer branding) |
| 2026-06-06 | FH Münster | KEIN FUND | keine Förderer-/Sponsoren-Seite (Treffer = uni-muenster.de separat) |
| 2026-06-06 | TH OWL | KANDIDAT (verify) | th-owl.de/.../foerdervereine; Hochschulgesellschaft OWL e.V. |
| 2026-06-06 | HS Ruhr West | KANDIDAT (verify) | hochschule-ruhr-west.de/kooperationen/foerderverein + angebote-fuer-unternehmen |
| 2026-06-06 | HS Bochum | KANDIDAT (verify) | hochschule-bochum.de GDF Gesellschaft der Förderer; 23 Firmen |
| 2026-06-06 | Westfälische HS Gelsenkirchen | KANDIDAT (verify) GUT | w-hs.de/hochschule/partner-und-foerderer + fk-ge/mitglieder Hauptdomain |
| 2026-06-06 | HS Rhein-Waal | KANDIDAT schwach | Hauptdomain beschreibt 3 Fördervereine, die auf eigenen Domains liegen |
| 2026-06-06 | HS Hamm-Lippstadt | KANDIDAT (verify) GUT | hshl.de/forschung-unternehmen/foerderer/sponsoren (Hörsaalsponsoring) Hauptdomain |
| 2026-06-06 | HS Bielefeld (HSBI) | KANDIDAT schwach | hsbi.de/foerdergesellschaft (in Entw.) + Partnerunternehmen (operativ) |
| 2026-06-06 | HS Hannover | KANDIDAT (verify) | hs-hannover.de/.../foerderung; Fakultäts-Fördervereine |
| 2026-06-06 | Leibniz Uni Hannover (Bonus) | KANDIDAT (verify) | uni-hannover.de/.../fundraising/sponsoring Hauptdomain |
| 2026-06-06 | Ostfalia HS | KANDIDAT schwach/RAUS-lean | Partnerunternehmen (Logistik/dual) + Event-Sponsoring |
| 2026-06-06 | HS Emden/Leer | KANDIDAT schwach/RAUS-lean | Partnerunternehmen (Praxisverbund/dual) + Förderkreis (oldweb) |
| 2026-06-06 | TH Mittelhessen (THM) | KANDIDAT schwach/RAUS-lean | StudiumPlus (1080 duale Partner) + Kooperationen |
| 2026-06-06 | HS Fulda | KANDIDAT (verify) | hs-fulda.de/.../foerderverein + Deutschlandstip.; Fakultäts-Vereine eigene Domain |
| 2026-06-06 | HS RheinMain | KANDIDAT (verify) | hs-rm.de Förderkultur; „alle Förderer auf Homepage"; tlw. Deutschlandstip. |
| 2026-06-06 | TH Ingolstadt (THI) | KANDIDAT (verify) | thi.de/.../partner-und-foerderer; 330 Firmen; aber Sichtbarkeit tlw. physisch (Spendersäule) |

### UPDATE Zwischenstand (nach ~64 vor-recherchierten Institutionen)
Zusätzliche Regionen abgearbeitet: BW/Bayern-HAW, NRW-HAW, Niedersachsen-HAW, Hessen-HAW.
**Starke Kandidaten gesamt (Hauptdomain + Logos/Sponsoren-Listing laut Snippet → Priorität für Verifikation):**
HTWK Leipzig · HS Heilbronn · HS Pforzheim · Uni Göttingen · Uni Mannheim · Uni Regensburg · HS Augsburg (THA, Hörsaalgalerie) · Westfälische HS Gelsenkirchen · HS Hamm-Lippstadt.
**Weitere normale Kandidaten** (Förderverein/Sponsoring auf Hauptdomain, Verlinkung offen): TU Berlin, TU Darmstadt, RPTU, FAU, Uni Augsburg, Uni Bayreuth, Uni Freiburg, Uni Duisburg-Essen, Uni Kiel, Uni Leipzig, Leibniz Uni Hannover, HS Merseburg, EAH Jena, HS Stralsund, FH Kiel, TH Lübeck, HfT Stuttgart, RWU, THU Ulm, TH Rosenheim, HS Landshut, TH OWL, HS Ruhr West, HS Bochum, HS Hannover, HS Fulda, HS RheinMain, THI Ingolstadt.
**RAUS-lean / KEIN FUND**: siehe Tabelle oben.
| 2026-06-06 | HS Hof | KANDIDAT (verify) | hof-university.de freunde-und-foerderer + fundraising; Firmen im Vorstand |
| 2026-06-06 | HSWT Weihenstephan-Triesdorf | KANDIDAT (verify) schwach | hswt.de/.../foerdern-unterstuetzen; Deutschlandstip. + Bus-/Event-Sponsoring |
| 2026-06-06 | HS Biberach (HBC) | KANDIDAT (verify) | hochschule-biberach.de spende-sponsoring-patenschaft + unser-netzwerk |
| 2026-06-06 | HS Albstadt-Sigmaringen | KANDIDAT (verify) GUT | hs-albsig.de/netzwerk/partnerschaften/kooperationspartner (Sponsoren) + Raumsponsoring |
| 2026-06-06 | HS Trier | KANDIDAT (verify) | hochschule-trier.de/.../foerderer-und-netzwerk; Förderkreis + Umwelt-Campus Birkenfeld |
| 2026-06-06 | HS Koblenz | KANDIDAT schwach/RAUS-lean | dual geprägt (Partnerlogo, 300 Koop.-Firmen) + Förderkreise |
| 2026-06-06 | WHZ Zwickau | KANDIDAT (verify) | whz.de holzgestaltung/partner-sponsoren (viele Firmen) + Förderverein Mentor |
| 2026-06-06 | HS Zittau/Görlitz | KANDIDAT (verify) schwach | hszg.de/.../foerderer-vereine; Förderverein eigene Domain + Deutschlandstip. |
| 2026-06-06 | HS Mainz | KANDIDAT (verify) | hs-mainz.de/.../foerdervereine (Welsch-Gesellschaft) + Deutschlandstip. 32 Firmen |
| 2026-06-06 | HS Kaiserslautern | KANDIDAT schwach/RAUS-lean | dual (KOSMO) + Event-/Fahrzeug-Sponsoring |
| 2026-06-06 | HTW Berlin | KANDIDAT (verify) schwach | htw-berlin.de/.../foerdern-gefoerdert-werden + Förderverein; Kontakt matthias.zietz@htw-berlin.de |
| 2026-06-06 | BHT Berlin (Beuth) | KANDIDAT schwach/RAUS-lean | Förderverein FBHT + Beuth-Gesellschaft (eigene Domain); Partner v.a. IHK |
| 2026-06-06 | FH Dortmund | KANDIDAT schwach | fh-dortmund.de Fördergesellschaft/Hochschulförderung; stark Deutschlandstip. |
| 2026-06-06 | FH Südwestfalen | KANDIDAT schwach/RAUS-lean | Fördervereine eigene Domains + Deutschlandstip. |
| 2026-06-06 | HS Geisenheim | KEIN FUND | keine Förderer-Logo-Seite; Forschungs-/Industriepartner |
| 2026-06-06 | HS Worms | KANDIDAT (verify) GUT | hs-worms.de hoersaalsponsoring + foerderer-und-partner; Logos auf Website lt. Snippet |
| 2026-06-06 | HS Bremen (HSB) | KANDIDAT schwach/RAUS-lean | ~180 Firmen, aber dual/Praxis + Deutschlandstip. |
| 2026-06-06 | HS Bremerhaven | KANDIDAT (verify) | hs-bremerhaven.de/.../partner-und-foerderer + Förderverein; foerderverein@hs-bremerhaven.de |
| 2026-06-06 | WHU Otto Beisheim (privat) | KANDIDAT (verify) GUT | whu.edu spender-und-sponsoren/unterstuetzer; Henkel/BVB/Bertelsmann; 160 Partner |
| 2026-06-06 | Zeppelin Universität (privat) | KANDIDAT (verify) GUT | zu.de/universitaet/foerderer; Bosch/SAP/Rolls-Royce/KPMG/Würth |
| 2026-06-06 | Frankfurt School (privat) | KANDIDAT (verify) | frankfurt-school.de/.../corporate-partners; Modell Corporate Partnership/Recruiting |
| 2026-06-06 | HHL Leipzig (privat) | KANDIDAT schwach | hhl.de about-hhl + foundation; Kuratorium mit Firmen |
| 2026-06-06 | Constructor University Bremen (privat) | KEIN FUND | stiftungsfinanziert; keine Sponsoren-/Partner-Logoseite |
| 2026-06-06 | EBS Universität (privat) | KANDIDAT (verify) schwach | ebs.edu our-network/corporate-partners; McKinsey/Mercedes/UBS + Deutschlandstip. |
| 2026-06-06 | HfWU Nürtingen-Geislingen | KANDIDAT (verify) | hfwu.de/wirtschaftskontakte + Hochschulbund; STIHL/Festool/LBBW |
| 2026-06-06 | hsg Bochum | KANDIDAT (verify) schwach | hs-gesundheit.de/netzwerk/strategische-partner; Kliniken + Deutschlandstip. |

### ABSCHLUSS-UPDATE 2 (Stand ~90 Institutionen vor-recherchiert)
Abgedeckt: alle großen Unis (Startreihenfolge 1) + HAW/TH in allen 16 Bundesländern (Schwerpunkt Sachsen, Sachsen-Anhalt, Thüringen, MV, SH, Berlin/Brandenburg, NDS, Bremen, NRW, Hessen, RLP, BW, Bayern) + erste private Hochschulen.
**Starke Kandidaten (Priorität Verifikation), 13:** HTWK Leipzig · HS Heilbronn · HS Pforzheim · Uni Göttingen · Uni Mannheim · Uni Regensburg · HS Augsburg · Westf. HS Gelsenkirchen · HS Hamm-Lippstadt · HS Albstadt-Sigmaringen · HS Worms · WHU · Zeppelin Uni.
**Noch offen für spätere Discovery-Runden:** restliche private HS (SRH, IU, Fresenius, Macromedia, CBS, ISM, Hertie, Kühne Logistics, CODE, GISMA …), einzelne kleinere/konfessionelle HAW, Musik-/Kunsthochschulen (meist irrelevant).
**Unverändert gilt:** Verifikation (Dofollow-Links ≥6 Firmen + Hunter-Email) steht für ALLE Kandidaten aus, bis die Netzwerk-Allowlist geöffnet ist.

---

## SESSION 2026-06-07 — VOLLE VERIFIKATION (Netz offen)

Netzwerk-Allowlist offen (Hunter + Hochschul-Domains erreichbar, HTTP 200). Die in den Vorsessions blockierte Kern-Verifikation wurde durchgefuehrt.

### Vorgehen
- Tooling: `_tools/linkcheck.py` (dofollow/nofollow je Seite), `_tools/crawl.py` (Discovery), `_tools/hunter.sh` (E-Mail-Verify), `_tools/ingest.py` (CSV-Eintrag pro Institution), Methode in `_tools/METHOD.md`.
- 12 parallele Recherche-Subagenten (2 Wellen) haben ~140 Hochschulen nach einheitlicher Methode geprueft: Sponsoren-/Foerderer-Listenseite der Hauptdomain per HTML-Analyse (externe dofollow-Firmenlinks >=6 nach Filterung) + 1 Hunter-verifizierte Kontakt-E-Mail.
- Ergebnisse zentral validiert, pro Institution committet und gepusht. Roh-JSON je Batch in `_tools/results/`.

### Ergebnis (Master-CSV jetzt 200 Datenzeilen)
- LINK VERIFIZIERT: 17 (HSHL Hamm-Lippstadt, Frankfurt School, HS Hannover, HSWT, HS Mittweida, EAH Jena, HS Albstadt, Uni Osnabrueck, Uni Hohenheim, BTU Cottbus, bbw, Provadis, HFH + 4 Bestand)
- SPONSORING-SEITE: 24 (u.a. HTWK Leipzig, HS Heilbronn, TH Luebeck, FH/HAW Kiel, HS Hof, HS Biberach, TU Ilmenau, HSBA, CODE + 15 Bestand)
- PRUEFEN (Verlinkung): 88 · AUSGESCHLOSSEN: 65 · Rest Grenzfaelle
- Priorisierte Liste: siehe `ERGEBNIS_UEBERSICHT.md`.

### Wichtigste Erkenntnis
Die WebSearch-Vorrecherche ueberschaetzte viele Kandidaten: bei den meisten grossen Unis und vielen HAW sind Foerderer/Sponsoren real nur als TEXT oder physische Wand/Foto bzw. als nicht verlinkte Logos hinterlegt -> echte dofollow-Backlinks (LINK VERIFIZIERT) sind selten. Klassische Foerderverein-Logowaende mit Links finden sich v.a. bei mittelgrossen HAW und einzelnen Unis.
