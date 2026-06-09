# METHOD ADDENDUM — Breiterer Maßstab "wertvoll" (Tiefen-Re-Check)

Ergänzt _tools/METHOD.md. Ziel dieser Welle: ALLE Hochschulen mit **Partnerbereich,
externen Firmenlinks oder Firmen-Logos** als wertvoll erfassen — nicht nur klassische
Förderverein-/Sponsorenseiten.

## Was jetzt als "Firmenbezug" zählt (breiter als zuvor)
Prüfe auf der HAUPTDOMAIN gezielt diese Seitentypen und ihre Inhalte:
- Sponsoren / Förderer / Förderverein / Freunde (wie bisher)
- **Partner / Kooperationspartner / Unternehmenspartner / Netzwerkpartner**
- **Praxispartner / Partnerunternehmen / Ausbildungspartner / duale Partner**
- **Career-Service-Partner / Mentoring-Partner / Stellenpartner**
- **Mitgliedsunternehmen** (Fördervereine, Beiräte, Kuratorien)
- **Stifter / Stiftungsprofessuren-Geber** (sofern Firmen)

## Klassifikation (status-Werte für diese Welle)
- **FIRMEN-LINKS** = die Seite enthält >=6 externe dofollow-Links auf echte Firmen-Domains.
  (entspricht bisherigem "LINK VERIFIZIERT")
- **FIRMEN-LOGOS** = Firmen-Logowand/-Liste (>=4 Firmen) vorhanden, aber NICHT/​kaum verlinkt.
  (entspricht bisherigem "SPONSORING-SEITE")
- **PARTNERBEREICH** = NEU/leichter: Partner-/Kooperations-/Praxispartner-Seite existiert und
  nennt oder verlinkt 1–5 externe Firmen (auch ohne große Logowand). Outreach-würdig.
- **KEINE FIRMEN** = nur Hochschulen/Behörden/Verbände/Tools/Stipendien/eigene Domains; kein Firmenbezug.

## Ausschlusskriterien (zählen NICHT als Firma)
Andere Hochschulen/Unis, Studierenden-/Künstler-Portfolios, Behörden/Ministerien, Akkreditierer,
Fachverbände/e.V., Stiftungen, Verlage/Datenbanken, Bibliotheken, Social Media, Tools/CMS/Analytics,
Studierendenwerk, Job-/Bewertungsportale, eigene Schwester-Domains der Hochschule, Kliniken NUR wenn
sie reine Träger/Hochschulkliniken sind (privatwirtschaftliche Klinikkonzerne wie Asklepios/Helios zählen
als Firma).

## Hinweise pro Haus
Jede Batch-Zeile enthält: Name | Domain | bisheriger_Status | DR | Ahrefs-Firmen-Leads
(letztere sind automatische, teils verrauschte Hinweise aus Ahrefs-Ausgangslinks — als Suchhilfe nutzen,
NICHT blind übernehmen; immer auf der Seite verifizieren, ob es eine echte externe Firma ist und ob
dofollow verlinkt / nur Logo / nur Textnennung).

## Output je Hochschule (JSON, gleiche Schlüssel wie METHOD.md)
status (FIRMEN-LINKS | FIRMEN-LOGOS | PARTNERBEREICH | KEINE FIRMEN), hochschule, typ, verein,
firmenmitgliedschaft, jahresbeitrag, listungsseite (die konkrete Partner-/Firmen-Seite), bewertung
(mit Befund: welche Firmen, Logo/Link/Text, Anzahl dofollow), k1_*/k2_* Kontakte.
Bei FIRMEN-LINKS/FIRMEN-LOGOS in bewertung 3–8 konkrete Firmenbeispiele nennen.
