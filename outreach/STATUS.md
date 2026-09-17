# STATUS / Übergabe — Städte-Sponsoring-Akquise

**Stand:** 2026-09-17 · **Repo:** dariog-code/claude-recherche · **Branch:** claude/sweet-carson-aZHuF

## Ergebnis-Bilanz

- Zusage: **4**
- Interesse: **24**
- Rückfrage: **2**
- In Bearbeitung: **4**
- Absage: **9**
- kein Programm: **1**
- Kontaktiert gesamt (Master-Zeilen): 211

## Versandstatus

- Welle 1: 108/108 Erstkontakt versendet
- Welle 2: 64/66 Erstkontakt versendet
- Welle 3: 37/37 Erstkontakt versendet
- Nachfass-1 Welle 1: komplett versendet. Nachfass-2 (78 Städte) vorbereitet: `mailmerge_nachfass2_welle1_teil1/2.csv`.
- Bounce-Korrekturen (Runden 1–4) versendet.

## Zusagen (abzuwickeln)

- **Freital** — Tilo Harder (tilo.harder@freital.de) — Logo/Verlinkung platzieren + Konditionen/Laufzeit (1 Jahr) finalisieren
- **Sondershausen** — Arne Wiegand (wiegand@sondershausen.de) — Bedingungen klären + Logo/Verlinkung bis Event 20.09.2026 platzieren
- **Plauen** — Lars Krämer (Julian.Schwenkglenks@plauen.de) — Kunden + Ziel-URLs liefern; Laufzeit ab 01.01.2027 (1 Jahr)
- **Straubing** — Martina Burmberger (Martina.Burmberger@Straubing.de) — Konditionen/Logo/Verlinkung finalisieren

## In Verhandlung / in Bearbeitung / Rückfragen

- **Saarbrücken** — Tobias Raab (TOBIAS.RAAB@saarbruecken.de) — Passiv – auf Rückmeldung warten (melden sich bei Interesse)
- **Bad Kissingen** — Leitung Abteilung IV (leitungabteilungIV@stadt.badkissingen.de) — Wiedervorlage ab KW35 (~2026-08-25), falls keine Rückmeldung
- **Leer (Ostfriesland)** — Cindy Grätz (Cindy.Graetz@Leer.de) — Nachfassen/konkret machen (Konditionen anbieten)
- **Gevelsberg** — Markus Marsurkewitz (markus.marsurkewitz@stadtgevelsberg.de) — Wiedervorlage: nachfassen Anfang September (~2026-09-08)
- **Sömmerda** — Lena Kob (l.kob@stadtsoemmerda.de) — Rücksprache/Klärung mit Lena Kob (offene Fragen beantworten)
- **Bocholt** — Nikolaus Kellermann (Nikolaus.Kellermann@bocholt.de) — Anliegen klar erklären (Sponsoring: Nennung+Logo+Verlinkung, ab 1.000€)
- **Ludwigsburg** — Kerstin Huber (k.huber@ludwigsburg.de) — In Verhandlung: Rückfrage beantworten / Konditionen abstimmen

## Interesse (24) — Kurzliste

- Erfurt — Laura Schmidt
- Bremerhaven — Laura Bohlmann
- Ludwigsburg — Kerstin Huber
- Aalen — André Mandel
- Deggendorf — Sandro Pfeiffer
- Radebeul — Ute Leder
- Limburg an der Lahn — Hilmar von Schenck
- Hildesheim — Meike Biskup
- Rudolstadt — Ulrike Haas
- Arnstadt — Jörg Neumann
- Wesseling — Michelle Engels
- Osterode am Harz — Frau Aulich
- Herzogenaurach — Judith Jochmann
- Nienburg/Weser — M. Fortmann
- Kamen — Birgit Klotzbach
- Altenburg — Christian Graf
- Seevetal — Isabell Michelchen
- Weißenfels — Michael Kraft
- Regensburg — Georg Barfuß
- Speyer — Mario Daum
- Frankenthal — Jan-Luca Dittrich
- Landau in der Pfalz — Berfin Tunc
- Germersheim — Katharina Keller
- Ulm — S. Clauss

## Wichtige Dateien

- `outreach/master_tracking.csv` — zentrale Wahrheit (jede Stadt 1 Zeile)
- `outreach/WORKFLOW.md` — Regeln, Wellen-Log, QA, Versandlimit
- `outreach/leitstand.html` — Panel-Quelle (rechts angezeigtes Dashboard)
- `mailvorlage_staedte_sponsoring.md` (Erstkontakt) / `mailvorlage_staedte_nachfass.md` / `mailvorlage_staedte_nachfass2.md`
- `mailmerge_*.csv` — Versandlisten je Welle/Block

## Regeln (verbindlich)

- Jede gelieferte Liste/Vorlage IMMER als Datei ausspielen.
- Jede Stadt MUSS echte Sponsorenseite haben (Spalte nie leer), sonst aus Versand.
- Mailchimp: max. 60 Mails/Stunde → 60er-Blöcke.
- Vorlagen: 1.000-€-Angebot, Freital-Referenz + Link, LinkedIn-Verifizierung; HTML-Modus, keine Hard-Wraps.
- Leitstand bei jeder Aktion aktualisieren (Quelle: outreach/leitstand.html).

## Umzug in anderen Account — 3 Schritte

1. Dem anderen Account Zugriff auf das GitHub-Repo `dariog-code/claude-recherche` (Branch `claude/sweet-carson-aZHuF`) geben.
2. Dort neue Claude-Code-Session auf dem Repo starten.
3. Sagen: "Lies `outreach/STATUS.md` und `outreach/WORKFLOW.md`, stell den Leitstand aus `outreach/leitstand.html` wieder her und mach weiter."

## Offene nächste Schritte

- Nachfass-2 Welle 1 (78) senden, dann im Master als versendet markieren.
- Zusagen abwickeln (Sondershausen Event ab 20.09.! · Plauen ab 01.01.2027 · Freital · Straubing).
- Rückmeldungen weiter pflegen.