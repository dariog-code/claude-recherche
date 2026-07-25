# Projekt: Städte-Sponsoring-Akquise

Recherche + Outreach an Städte/Kommunen für Sponsoring-Kooperationen
(Logo/Eintrag auf deren Sponsoren-/Partnerseiten).

## Wichtig: Outreach läuft in Wellen/Blöcken mit Nachfassmails

- **Master-Dokumentation:** `outreach/master_tracking.csv` — zentrale Liste aller
  kontaktierten Städte mit Welle, Erstkontakt-/Nachfass-Daten, Antwort, Ergebnis.
  **Bei jeder Versand-/Antwort-Aktion aktualisieren.**
- **Workflow & Wellen-Log:** `outreach/WORKFLOW.md`.
- Vorgehen: Welle versenden → Antworten pflegen → nach ~7–10 Werktagen die
  Städte ohne Antwort per **Nachfassmail** kontaktieren → nächste Welle ergänzen.

### Bisherige Wellen
- **Welle 1 — 2026-06-17 — 108 Städte** (Erstkontakt versendet).
  Datenquelle: `mailmerge_108.csv`. Für diese 108 folgen Nachfassmails.
- **Welle 2 — 66 Städte (DR ≥ 40)** — vorbereitet, noch nicht versendet.
  Datenquelle: `mailmerge_wave2.csv`. Inkl. Sportamt/Sportgala-Typ (Vorbild nuernberg.de Sportdialoge).

## Versand
- Vorlage: `mailvorlage_staedte_sponsoring.md`
- Thunderbird Mail Merge (Add-on), Platzhalter = CSV-Spalten (`{{Email}}`,
  `{{Email_CC}}`, `{{Stadt}}`, `{{Anrede}}`, `{{Sponsorenseite}}` …).
  Anleitung: `ANLEITUNG_Thunderbird_Mailmerge.md`. Versand erfolgt manuell durch
  den Nutzer (kein Mailversand aus dieser Umgebung).
- **Versandlimit (WICHTIG): Bei Versand über Mailchimp max. 60 Mails/Stunde.**
  Größere Listen in Blöcke à ≤ 60 pro Stunde aufteilen; bei Datei-/Batch-Erstellung
  entsprechend chunken (z. B. 60er-Pakete). Bei Thunderbird-Direktversand gilt die
  ~30-Sek.-Pause; das Mailchimp-Limit ist die härtere Grenze und hat Vorrang.

## Kontakt-Recherche
- E-Mail-Verifikation via Hunter.io (Cache: `_tools/hunter_cache.json`, ohne Key).
- Pro Stadt: relevanteste Person (Wirtschaftsförderung > Stadtmarketing > Presse >
  OB-Büro), möglichst mit zustellbarer persönlicher Adresse; CC = zweite Person.
