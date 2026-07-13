# Mail-Vorlage Kultur-Sponsoring / Förderpartnerschaft (Thunderbird Mail Merge)

> Für Museen, Orchester/Konzerthäuser, Theater/Opern mit Sponsoren-/Partnerseite.
> Pitch = Engagement als **Förderer/Sponsor** → Gegenleistung: Nennung mit
> **Logo + Verlinkung** auf der Sponsoren-/Partnerseite.
> Platzhalter = Spalten der Versand-CSV (`mailmerge_kultur.csv`).
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · Signatur bleibt aus Thunderbird.

---

## Betreff

```
Förderengagement bei {{Institution}} – Aufnahme in Ihren Partner-/Sponsorenkreis
```

---

## Mailtext

```
{{Anrede}}

wir sind auf {{Institution}} aufmerksam geworden – insbesondere auf die Seite, auf
der Sie Ihre Sponsoren und Partner vorstellen ({{Listungsseite}}).

Wir unterstützen gezielt Kulturinstitutionen und ihre Programme – von einzelnen
Projekten und Ausstellungen/Produktionen bis hin zu einer dauerhaften
Partnerschaft – und würden uns gern bei {{Institution}} als Förderer engagieren.

Im Gegenzug freuen wir uns – wie Ihre übrigen Partner – über eine kurze Nennung
mit Logo und Verlinkung auf Ihrer Sponsoren-/Partnerseite.

Können Sie mir sagen, welche Möglichkeiten einer Förder- oder Sponsoring-
Partnerschaft es bei Ihnen gibt und wer dafür der richtige Ansprechpartner ist?
Über eine kurze Rückmeldung freue ich mich sehr.

Herzliche Grüße
```

---

## Platzhalter (= CSV-Spalten)
`{{Anrede}}`, `{{Institution}}`, `{{Listungsseite}}`, `{{Email}}`, `{{Email_CC}}`,
`{{Ansprechpartner}}`, `{{Funktion}}`, `{{Kategorie}}` (Museum / Orchester / Theater).

## Hinweise
- `{{Anrede}}` ist vorbefüllt (persönlich, wo Kontakt bekannt).
- Bei „PRÜFEN"-Zeilen ist nur ein Funktionspostfach hinterlegt (keine persönliche
  Sponsoring-Adresse veröffentlicht) – vor Versand kurz ansehen.
