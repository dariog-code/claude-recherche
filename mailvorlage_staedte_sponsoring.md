# Erstkontakt-Mailvorlage Städte-Sponsoring (Thunderbird Mail Merge)

> NEUE Anfrage (Erstkontakt) für Städte, die wir noch NICHT angeschrieben haben.
> Gleicher Stil wie die Nachfass: 1.000-€-Angebot, Freital-Referenz mit Link,
> LinkedIn-Verifizierung — aber OHNE „vor einigen Tagen hatte ich geschrieben".
>
> Formatierung: jeder Absatz als EINE durchgehende Zeile (kein Zeilenumbruch im
> Satz), Absätze durch EINE Leerzeile getrennt. Im Verfassen-Fenster HTML-Modus
> (Optionen → Format → „Nur HTML"), dann bricht Thunderbird sauber um und der
> Link ist klickbar.
>
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · Signatur aus Thunderbird.

---

## Betreff

```
Sponsoring-Kooperation mit {{Stadt}}
```

---

## Mailtext

```
{{Anrede}}

wir sind auf {{Stadt}} aufmerksam geworden – insbesondere auf Ihre Sponsoren-/Partnerseite ({{Sponsorenseite}}).

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
- Für die letzte offene Welle: Datenquelle `mailmerge_welle_final.csv` (41 Städte).
- Mailchimp: max. 60 Mails/Stunde. Pause im Mail-Merge-Add-on kann kurz stehen (3–5 Sek.).
- Nachfass-Version (für später) steht in `mailvorlage_staedte_nachfass.md`.
