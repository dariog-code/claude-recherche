# Verifikations-Methode (Förderer/Sponsoring deutscher Hochschulen)

Ziel: pro Hochschule prüfen, ob die **Hauptdomain** Sponsoren/Förderer mit
**externen dofollow-Links auf Firmen-Domains** zeigt (SEO-Backlink-Projekt, eology).

## Werkzeuge (in /home/user/claude-recherche/_tools/)
Immer zuerst `cd /home/user/claude-recherche`.
- `python3 _tools/linkcheck.py <inst_domain> <url> [url2 ...]`
  → listet pro angegebener Seite EXTERNE dofollow- und nofollow-Domains (genau, EINE Seite). Das ist das maßgebliche Zählwerkzeug.
- `python3 _tools/crawl.py --auto <inst_domain>`  oder  `crawl.py <inst_domain> <seed> ...`
  → Discovery-Crawl. ACHTUNG: SEHR VERRAUSCHT (folgt Alumni/Netzwerk-Links, mischt Partner-Unis, Cafés, Tools rein). NUR zum FINDEN von Kandidatenseiten benutzen, NIEMALS die Zählung daraus übernehmen.
- `bash _tools/hunter.sh verify <email>`  /  `bash _tools/hunter.sh search <domain>`
  → Hunter E-Mail-Verifikation / Domain-Suche.
- Seiten-HTML direkt ansehen: `curl -sL -A "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0" "<url>"`

## Ablauf pro Hochschule
1. Finde die **Sponsoren-/Förderer-/Partner-LISTENSEITE** auf der Hauptdomain (nicht Subdomain, nicht die eigene Vereins-Domain). Starte mit der gegebenen Kandidaten-URL; bei 404 Homepage/Bereich abrufen und echte Seite suchen, oder `crawl.py --auto` zur Discovery, dann mit `linkcheck.py` die genaue Seite bestätigen.
2. Auf der GENAUEN Seite: zähle EXTERNE **dofollow**-Links auf DISTINKTE echte **Firmen**-Domains. NICHT mitzählen:
   - eigene Domain & weitere eigene Subdomains/verwandte Domains (z.B. `*-<name>.de`, `<name>.net`)
   - studentische Körperschaften (AStA, Studierendenwerk, AKAFÖ, Starkstrom u.ä. studentische e.V.)
   - Deutschlandstipendium / Stipendien- / Talent-Programme
   - Stiftungen/Fördervereine auf EIGENER Domain
   - Tools/CDN/Social (jimdo, expo-ip, webuntis, fundraisingbox, cookiebot, google, facebook, linkedin, youtube, spotify …)
   - Partner-UNIVERSITÄTEN (deutsch/ausländisch, .edu/.ac.*/uni-* / Erasmus-Partner)
   - Behörden/Ministerien
   Prüfe außerdem, ob Firmen-**Logos als BILDER** vorhanden sind (img alt mit Firmenname/„Logo …"), auch wenn NICHT verlinkt.
3. EINSTUFUNG:
   - `LINK VERIFIZIERT`: ≥6 distinkte dofollow-Firmenlinks auf der Hauptdomain. Beispiel-Firmen nennen.
   - `SPONSORING-SEITE`: „Wir danken unseren Sponsoren/Förderern"-artige Seite auf der Hauptdomain mit Firmen-LOGOS (≥4) und/oder 1–5 dofollow-Firmenlinks (Gegenleistung belegt), aber keine ≥6 Links. Firmen nennen.
   - `PRÜFEN (Verlinkung)`: Sponsoring/Förderung auf Hauptdomain angeboten/beschrieben, aber KEINE Logowand und KEINE Firmenlinks gefunden.
   - `AUSGESCHLOSSEN`: nur Deutschlandstipendium, ODER rein dual/Praxispartner ohne Sponsoring, ODER Förderverein nur auf eigener externer Domain, ODER kein Gegenleistungs-Modell. (Ausnahme: hat eine duale Partnerseite ≥6 dofollow-Firmenlinks, dann `LINK VERIFIZIERT` mit Vermerk „Modell dual".)
   - `KEIN FUND`: gar keine Sponsoring-/Förderer-Seite auf der Hauptdomain.
4. EINE Kontakt-E-Mail finden (bevorzugt sponsoring@/foerderverein@/fundraising@/genannte Person; sonst `hunter.sh search` für passende Person; sonst info@/kontakt@). Mit `hunter.sh verify` prüfen. Ergebnis notieren: „deliverable" / „risky (accept_all)" / „invalid". Bei Catch-all-Server (accept_all=True) vermerken.
5. EHRLICH und belegbasiert. NIE LINK VERIFIZIERT ohne tatsächlich gesehene ≥6 Firmen-dofollow-Links. Logos-als-Bilder ohne Link = SPONSORING-SEITE.

## Ausgabe
Nach ALLEN Institutionen: EIN ```json-Codeblock mit einem JSON-Array. Jedes Element hat die String-Schlüssel:
`status, hochschule, typ, verein, firmenmitgliedschaft, jahresbeitrag, listungsseite, bewertung, k1_name, k1_funktion, k1_email, k1_verify, k1_quelle, k2_name, k2_funktion, k2_email, k2_verify, k2_quelle`
- `bewertung` = ausführlicher Beleg, beginnend mit „(curl 2026-06-07)": welche Seite, wie viele dofollow-Firmenlinks, welche Firmen, Logos, Modell-Hinweise.
- `listungsseite` = exakte URL ohne https:// .
- Leere Felder = "" (besonders k2_* wenn nur ein Kontakt).
Nicht committen, keine Dateien ändern, kein git. Nur lesen/Skripte ausführen. Finale Antwort = kurze 1–2-Zeilen-Zusammenfassung + der JSON-Block.
