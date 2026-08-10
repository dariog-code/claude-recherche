# Nachfass-2-Mailvorlage Städte-Sponsoring (Thunderbird Mail Merge)

> Zweite (letzte) Erinnerung für Welle-1-Städte, die auf Erstkontakt UND
> Nachfass-1 nicht geantwortet haben. Social Proof: es machen bereits mehrere
> Städte mit (Freital, Plauen, Straubing …).
>
> Format: Absätze als durchgehende Zeilen (kein Hard-Wrap), HTML-Modus.
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · Signatur aus Thunderbird.

---

## Betreff

```
Nochmals kurz: Sponsoring-Kooperation mit {{Stadt}}
```

---

## Mailtext

```
{{Anrede}}

ich hatte mich vor einiger Zeit bei Ihnen gemeldet, weil wir {{Stadt}} gern als Sponsor unterstützen würden – mit einem kurzen Eintrag (Name und Logo, idealerweise mit Verlinkung) auf Ihrer Sponsoren-/Partnerseite ({{Sponsorenseite}}). Da ich noch keine Rückmeldung habe, versuche ich es kurz ein letztes Mal.

Inzwischen arbeiten bereits mehrere Städte mit uns zusammen – zum Beispiel Freital, Plauen und Straubing. Die Zusammenarbeit ist unkompliziert: ein fester Beitrag ab 1.000,00 Euro pro Kunde für Events oder Anschaffungen eurer Wahl, im Gegenzug die Nennung mit Logo und Verlinkung – wie bei Ihren übrigen Partnern.

Als Referenz: Die Stadt Freital hat unter „Kooperationspartner" bereits zwei unserer Kunden aufgelistet (https://www.freital.de/Kultur-Tourismus/Feste-Veranstaltungen/Freital-sucht-den-Schlagerstar-2025/Die-Sponsoren/).

Können Sie mir kurz sagen, ob und wie das bei Ihnen möglich ist – oder wer der richtige Ansprechpartner wäre? Auch ein kurzes „passt aktuell nicht" hilft mir weiter.

Prüfen Sie die Echtheit gern über mein LinkedIn-Profil: linkedin.com/in/mario-strack-head-of-content-outreach

Herzliche Grüße
Mario Strack
```

---

## Platzhalter
`{{Anrede}}`, `{{Stadt}}`, `{{Sponsorenseite}}`, `{{Email}}`, `{{Email_CC}}`.

## Hinweise
- Datenquelle: `mailmerge_nachfass2_welle1.csv` (78 Städte, in 60er-Blöcke gechunkt).
- Nur Welle-1-Städte ohne jede Antwort (Reagierende sind ausgeschlossen).
- Nach Versand im Master: `Nachfass2_Datum` + `Nachfass2_Status = versendet`.
