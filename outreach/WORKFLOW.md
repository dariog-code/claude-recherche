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

## Wellen-Log

| Welle | Datum Erstkontakt | Anzahl | Inhalt | Status |
|-------|-------------------|--------|--------|--------|
| **1** | 2026-06-17 | **108** | Städte DR ≥ 50 mit Sponsoren-/Partnerseite; je 1–2 Ansprechpartner (To+CC) | Erstkontakt versendet |
| **2** | (geplant) | **66** | Neue Städte DR ≥ 40 mit Sponsoren-/Partnerseite (inkl. Sportamt/Sportgala-Typ); je 1–2 Ansprechpartner (To+CC). Datei: `../mailmerge_wave2.csv` | vorbereitet, noch nicht versendet |

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
- **Nachfass-1 fällig ab ca.:** 2026-06-30 (für Städte ohne Antwort).
