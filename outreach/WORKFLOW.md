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

- `Erstkontakt_Status` / `Nachfass*_Status`: `versendet`, `bounce`, `—`
- `Ergebnis`: `offen`, `Interesse`, `Zusage`, `Absage`, `kein Programm`, `eingetragen`
- `Antwort`: kurze Notiz / Datum der Rückmeldung

## Wellen-Log

| Welle | Datum Erstkontakt | Anzahl | Inhalt | Status |
|-------|-------------------|--------|--------|--------|
| **1** | 2026-06-17 | **108** | Städte DR ≥ 50 mit Sponsoren-/Partnerseite; je 1–2 Ansprechpartner (To+CC) | Erstkontakt versendet |

### Notizen Welle 1
- Quelle/Auswahl: `staedte_GESAMT_dr50.csv` (Domains mit veröffentlichter Sponsorenseite).
- Kontakte: 108/108 mit namentlicher Person, 103 persönliche To-Adressen, 97 mit CC.
- 7 Adressen „Status unklar" (offiziell veröffentlicht, technisch nicht hart
  verifizierbar): Göttingen, Langenfeld, Radebeul, Husum, Saalfeld, Cham, Sömmerda
  → auf Bounces achten.
- **Nachfass-1 fällig ab ca.:** 2026-06-30 (für Städte ohne Antwort).
