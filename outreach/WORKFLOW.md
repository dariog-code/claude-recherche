# Outreach-Workflow: Städte-Sponsoring

Dieses Verzeichnis dokumentiert die Akquise-Kampagne (Sponsoring-Anfragen an
Städte) und dient als **dauerhafte Master-Dokumentation**. Wir arbeiten in
**Wellen/Blöcken** und mit **Nachfassmails**.

## Dateien

- **`master_tracking.csv`** — die Master-Liste. Jede kontaktierte Stadt = eine
  Zeile, mit Welle, Erstkontakt- und Nachfass-Daten, Antwort und Ergebnis.
  *Diese Datei ist die zentrale Wahrheit und wird bei jeder Aktion aktualisiert.*
- Versand-Vorlage: `../mailvorlage_staedte_sponsoring.md`
- Versand-Anleitung (Thunderbird Mail Merge): `../ANLEITUNG_Thunderbird_Mailmerge.md`
- Datenquelle der Welle 1: `../mailmerge_108.csv`

## Vorgehen (Wellen-Prinzip)

1. **Welle versenden:** Block von Städten per Thunderbird Mail Merge anschreiben
   (Erstkontakt). In `master_tracking.csv` Welle + `Erstkontakt_Datum` +
   `Erstkontakt_Status = versendet` eintragen.
2. **Antworten pflegen:** eingehende Reaktionen in `Antwort` / `Ergebnis`
   festhalten (z. B. „Interesse", „Absage", „kein Sponsoring möglich", „Logo
   eingetragen").
3. **Nachfassen:** Städte **ohne Antwort** nach ca. **7–10 Werktagen** mit einer
   Nachfassmail kontaktieren → `Nachfass1_Datum` / `Nachfass1_Status`.
   Bei weiterhin keiner Antwort optional zweite Nachfassrunde (`Nachfass2_*`).
4. **Nächste Welle:** neue Städte recherchieren und als **Welle 2, 3, …**
   ergänzen — gleiches Schema.

## Offene Aufgaben — nächste Session (Stand 2026-07-14)

1. **Welle 3 – Personenlücken gezielt nachrecherchieren** (namentliche, zustellbare
   Person statt Funktionspostfach; Web-Recherche wie bei Welle-1-Lücken, WebSearch-
   Budget ist in frischer Session wieder voll). Betroffen:
   Marburg (pressestelle@), Kiel (presse@kieler-woche.de), Bergisch Gladbach (info@),
   Greven (pressestelle@), **St. Ingbert (PRÜFEN)**, **Stade (PRÜFEN)**.
   → gefundene persönliche Adresse per Hunter verifizieren, in `mailmerge_wave3.csv`
   und `mailmerge_staedte_block2.csv` + Master ersetzen.
2. **Welle 4 – neue Städte nachlegen** nach bewährtem Prinzip (Sponsoren-/Partner-/
   Kooperationsseiten auf offizieller Stadt-Domain: StadtRadeln, Stadtfeste,
   Stadtmarketing-Partner, Sportamt/Sportgala). DR ≥ 40 via Ahrefs, To+CC via Hunter,
   gegen `_tools/exclude_staedte.txt` (= Master) ausschließen. 60er-chunked ausspielen.
   Schon vorgemerkte Tier-2-Leads: Amberg, Ibbenbüren, Peine, Werne, Kempten,
   Gladbeck, Bottrop, Sindelfingen. Bei zu wenig Volumen: Kriterien um Event-/
   Tourismus-/City-Marketing-Domains erweitern (laut Pilot sehr ergiebig, hohe DR).
3. **Nachfass-2 Welle 1** fällig ab ~28.07. (für weiterhin nicht antwortende Städte).


## Leitstand-Artifact (IMMER aktuell halten)

- Rechte-Panel-Übersicht (Status + Mail-Merge-Ablauf): **https://claude.ai/code/artifact/b020bfad-75b7-4e0c-ad2c-6e68a8d26fdb**
- Quelle liegt IM REPO: `outreach/leitstand.html` (überlebt Umgebungs-Resets). Bei jeder Aktion diese Datei aktualisieren, nach `scratchpad/uebersicht.html` kopieren und unter derselben Artifact-URL republizieren. **Bei jeder Aktion** (Versand markiert, neue Rückmeldung, neue Welle, Nachfass) aktualisieren und unter **derselben URL** neu publizieren (`url`-Param, damit der Link stabil bleibt).
- Inhalt: „Heute"-Versandplan (Blöcke), KPIs, Wellen-Status, Rückmeldungen, Mail-Merge-Ablauf.

## Regel: Dateien immer ausspielen

- Jede gelieferte Liste/Vorlage **immer als Datei** an den Nutzer senden (nicht nur beschreiben).


## Aktive Mailvorlage

- **Immer diese aktuelle Version nehmen:** `../mailvorlage_staedte_nachfass.md`
  (enthält 1.000-€-Angebot, Freital-Referenz **mit freital.de-Link** zur Kooperationspartner-Seite, LinkedIn-Profil).
- Absätze als durchgehende Zeilen (kein Hard-Wrap); im HTML-Modus verfassen.

## QA-Regel (IMMER prüfen)

- **Jede Stadt MUSS eine echte offizielle Sponsoren-/Kooperationsseite haben** (Spalte `Sponsorenseite` nie leer). Vor jedem Versand kontrollieren; Städte ohne echte Seite auf offizieller Domain aus dem Versand nehmen (nicht mit leerer `()`-Klammer senden). Ziel: 100 % Abdeckung.

## Versandlimit (WICHTIG)

- **Mailchimp: max. 60 Mails pro Stunde.** An diese Grenze halten.
- Listen > 60 in **60er-Blöcke pro Stunde** aufteilen; Restlisten entsprechend chunken.
- Bei Thunderbird-Direktversand ~30 Sek. Pause; das Mailchimp-Limit hat Vorrang.

## Status-Werte (Konvention)

- `Erstkontakt_Status` / `Nachfass*_Status`: `versendet`, `vorbereitet (nicht versendet)`, `bounce`, `—`
- `Antwort_Datum`: Datum der Rückmeldung (YYYY-MM-DD)
- `Antwort`: kurze Notiz zur Rückmeldung (Originalton/Kern)
- `Ergebnis`: `offen`, `Interesse`, `Zusage`, `Absage`, `kein Programm`, `eingetragen`
- `Naechste_Aktion`: konkreter nächster Schritt (z. B. „Telefontermin vereinbaren", „Logo/Material senden")

## Rückmeldungen (Log)

| Datum | Welle | Stadt | Person | Ergebnis | Nächste Aktion |
|-------|-------|-------|--------|----------|----------------|
| 2026-06-17 | 1 | Herzogenaurach | Judith Jochmann | Interesse (positiv) | **Telefontermin vereinbaren** |
| 2026-06-17 | 1 | Weißenfels | Katja Henze (CC) | Interesse | Konditionen/Material senden |
| 2026-06-17 | 1 | Glauchau | Michael Hecht | Absage (nur regionale Unternehmen) | — nicht nachfassen |
| 2026-07-14 | 1 | Aalen | Karin Haisch / Angela Neufischer | Interesse (Telefonat gehalten) | Ergebnis festhalten |
| 2026-06-17 | 1 | Wesseling | S. Burum | Interesse (Telefonat) | Telefontermin vereinbaren |
| 2026-06-17 | 1 | Sömmerda | Lena Kob | Rückfrage (Klärung nötig) | Rücksprache führen |
| 2026-06-17 | 1 | Rudolstadt | T. Melior | Interesse (Sponsoren-Infos, Subdomain) | Konditionen + Verlinkung prüfen |
| 2026-06-17 | 1 | Arnstadt | Carsten Römhildt | Interesse | Konditionen abstimmen |
| 2026-07-14 | 1 | Freital | kultur@freital.de | **ZUSAGE (1 Jahr)** | Logo/Verlinkung platzieren |
| 2026-07-14 | 1 | Kamen | Birgit Klotzbach | Interesse (Telefonat gehalten) | Ergebnis festhalten |

## Wellen-Log

| Welle | Datum Erstkontakt | Anzahl | Inhalt | Status |
|-------|-------------------|--------|--------|--------|
| **1** | 2026-06-17 | **108** | Städte DR ≥ 50 mit Sponsoren-/Partnerseite; je 1–2 Ansprechpartner (To+CC) | Erstkontakt versendet |
| **2** | (geplant) | **66** | Neue Städte DR ≥ 40 mit Sponsoren-/Partnerseite (inkl. Sportamt/Sportgala-Typ); je 1–2 Ansprechpartner (To+CC). Datei: `../mailmerge_wave2.csv` | vorbereitet, noch nicht versendet |
| **3** | (geplant) | **37** | Weitere Städte DR ≥ 42 (Freiburg, Kiel, Krefeld, Heidelberg, Ulm, Wolfsburg …). Datei: `../mailmerge_wave3.csv` | vorbereitet, noch nicht versendet |

### Notizen Welle 2
- 66 neue Städte (dedupliziert gegen Welle 1), Quelle: 5 Recherche-Agenten (StadtRadeln, Stadtfeste, Stadtmarketing-Partner, Sport-/Kultur-Events, **Sportamt/Sportdialoge** — Vorbild nuernberg.de) + 6 aus DR-Cache.
- Kontakte: 66/66 mit namentlicher Person, 63 persönliche To-Adressen, 61 mit CC.
- 56 verifiziert zustellbar (28 valid + 28 accept_all), 10 „Status unklar" (offiziell veröffentlicht, Server ohne Verifikationsantwort).
- **DR per Ahrefs exakt verifiziert: alle 66 ≥ 40** (Spitze: Hamburg 89, Nürnberg 83, Dresden 82, Frankfurt 81).

### Notizen Welle 1
- Quelle/Auswahl: `staedte_GESAMT_dr50.csv` (Domains mit veröffentlichter Sponsorenseite).
- Kontakte: 108/108 mit namentlicher Person, 103 persönliche To-Adressen, 97 mit CC.
- 7 Adressen „Status unklar" (offiziell veröffentlicht, technisch nicht hart
  verifizierbar): Göttingen, Langenfeld, Radebeul, Husum, Saalfeld, Cham, Sömmerda
  → auf Bounces achten.
- **Nachfass-1 KOMPLETT versendet: 2026-07-14** an alle 98 offenen Städte (Teilversand 61 + 37; Reagierende ausgeschlossen). Nachfass-2 ggf. ab ~28.07.
