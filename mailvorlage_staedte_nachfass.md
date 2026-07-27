# Nachfass-Mailvorlage Städte-Sponsoring (Thunderbird Mail Merge)

> WICHTIG zur Formatierung: Jeder Absatz steht als EINE durchgehende Zeile
> (kein Zeilenumbruch mitten im Satz), Absätze durch EINE Leerzeile getrennt.
> So bricht Thunderbird den Text automatisch sauber um. Harte Umbrüche im Satz
> vermeiden – die übernimmt Thunderbird 1:1 und die Mail wirkt „zerhackt".
> Tipp: Im Verfassen-Fenster HTML-Format nutzen (Optionen → Format → HTML) oder
> Nur-Text mit „format=flowed" – dann wird sauber umbrochen.
>
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · Signatur aus Thunderbird.

---

## Betreff

```
Nachfrage: Sponsoring-Kooperation mit {{Stadt}}
```

---

## Mailtext

```
{{Anrede}}

vor einigen Tagen hatte ich Ihnen geschrieben, weil wir {{Stadt}} gern als Sponsor unterstützen würden – mit Blick auf Ihre Sponsoren-/Partnerseite ({{Sponsorenseite}}).

Vielleicht ist meine Nachricht im Tagesgeschäft untergegangen – das verstehe ich gut. Deshalb melde ich mich kurz noch einmal:

Wir würden {{Stadt}} gern als Sponsor unterstützen und im Gegenzug – wie Ihre übrigen Partner – mit einem kurzen Eintrag (Name und Logo, idealerweise mit Verlinkung) auf Ihrer Sponsoren-/Partnerseite genannt werden.

Können Sie mir kurz sagen, welche Möglichkeiten es bei Ihnen gibt und wer der richtige Ansprechpartner ist? Diese Anfrage ist ernst gemeint! Es geht um 1.000,00 Euro pro Kunde für Events oder Anschaffungen eurer Wahl. Für Ideen von eurer Seite bin ich sehr offen.

Die Stadt Freital hat unter „Kooperationspartner" jetzt zwei unserer Kunden aufgelistet (https://www.freital.de/Kultur-Tourismus/Feste-Veranstaltungen/Freital-sucht-den-Schlagerstar-2025/Die-Sponsoren/). Wir würden uns freuen, wenn das auch bei euch möglich ist.

Prüfen Sie die Echtheit gern über mein LinkedIn-Profil: linkedin.com/in/mario-strack-head-of-content-outreach

Herzliche Grüße
Mario Strack
```

---

## Platzhalter
`{{Anrede}}`, `{{Stadt}}`, `{{Sponsorenseite}}`, `{{Email}}`, `{{Email_CC}}`.

## Hinweise
- Nur an Städte ohne Antwort senden (Reagierende in der Nachfass-CSV bereits ausgeschlossen).
- Mailchimp: max. 60 Mails/Stunde → Listen > 60 in 60er-Blöcke aufteilen.
- Nach Versand in `master_tracking.csv`: `Nachfass1_Datum` + `Nachfass1_Status = versendet`.
