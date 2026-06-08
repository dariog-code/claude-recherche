# Methode 2 — Verlinkungspotenzial-Prüfung (Re-Check der PRÜFEN-Fälle)

Diese Häuser haben einen Förderverein/Sponsoring auf der Hauptdomain, aber in Runde 1 wurde
KEINE Logowand und KEINE ≥6 dofollow-Firmenlinks gefunden. Ziel jetzt: das **Verlinkungspotenzial**
(Outreach-Chance auf einen Backlink) konkret bewerten und übersehene Listen finden.

## Werkzeuge (in /home/user/claude-recherche/_tools/), immer zuerst `cd /home/user/claude-recherche`
- `python3 _tools/linkcheck.py <inst_domain> <url> [url2 ...]` → dofollow/nofollow je Seite (maßgeblich).
- `python3 _tools/crawl.py --auto <inst_domain>` / `crawl.py <inst_domain> <seed> ...` → Discovery (verrauscht, nur zum Finden).
- `bash _tools/hunter.sh verify <email>` / `search <domain>`.
- HTML direkt: `curl -sL -A "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0" "<url>"`

## Ablauf pro Hochschule
1. Ausgehend von der gegebenen Listungsseite GEZIELT nach einer **Mitglieder-/Sponsoren-/Partner-/„Wir danken"-Unterseite** suchen
   (Linktexte/Pfade: mitglieder, unsere-foerderer, unsere-sponsoren, partner, danke, wir-danken, foerderer, vorstand, jahresbericht).
   Auch Förderverein-Unterseiten der Hauptdomain prüfen. Mind. 3–6 plausible Unterseiten testen.
2. Auf den gefundenen Seiten feststellen:
   a) Werden **konkrete Firmen genannt**? Wie viele? Als **Logos (Bilder)**, als **Text**, oder als **dofollow-Links**?
   b) `linkcheck` zur exakten Zählung externer dofollow-Firmen-Domains (Filter wie Methode 1: eigene Domains/Subdomains,
      AStA/Studierendenwerk, Stiftungen/Vereine auf Eigendomain, Partner-Unis, Tools/Social, Behörden NICHT zählen).
3. Reklassifizieren / bewerten:
   - Wenn jetzt ≥6 dofollow-Firmenlinks → `new_status = "LINK VERIFIZIERT"`.
   - Wenn Logowand/Firmenliste mit ≥4 Firmen als Bilder/Text aber ohne Links → `new_status = "SPONSORING-SEITE"`.
   - Sonst bleibt `new_status = "PRÜFEN (Verlinkung)"`.
   - Zusätzlich IMMER ein **Verlinkungspotenzial** vergeben:
     - `hoch`  = konkrete Firmen werden öffentlich genannt/als Logo gezeigt, aber NICHT verlinkt → klarer Outreach-Hebel („Logo/Name ist da, bitte verlinken").
     - `mittel`= Förderverein mit Firmenmitgliedern existiert, Liste aber nicht öffentlich / nur auf Anfrage / nur Vorstand genannt.
     - `gering`= keine Firmen genannt; nur Stiftungen/Deutschlandstipendium/Privatpersonen / Verein auf Eigendomain.
4. EINE belastbare Outreach-Seite (beste_seite) angeben (die Seite, auf der ein Link am ehesten gesetzt würde / Firmen genannt sind).
5. Kontakt: nur wenn der bisherige Kontakt unbrauchbar ist, einen besseren per Hunter suchen/verifizieren; sonst leer lassen (Bestand bleibt).

## Ausgabe
EIN ```json-Codeblock = Array. Pro Hochschule die Schlüssel:
`hochschule` (EXAKT wie vorgegeben, dient als Schlüssel), `new_status`, `potenzial` (hoch|mittel|gering),
`beste_seite` (URL ohne https://), `bewertung` (NEU, beginnend mit "VERLINKUNGSPOTENZIAL <hoch|mittel|gering> (recheck 2026-06-08): " + konkrete Belege:
welche Unterseite, wie viele Firmen, Logos/Text/Links, welche Beispiel-Firmen),
optional `k1_email`/`k1_verify`/`k1_quelle` nur wenn besserer Kontakt gefunden (sonst "").
Nicht committen, keine Dateien ändern. Nur lesen/Skripte. Finale Antwort = 1–2 Zeilen + JSON-Block.
