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
