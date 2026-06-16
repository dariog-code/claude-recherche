# Mail-Vorlage Städte-Sponsoring (Thunderbird Mail Merge)

> Platzhalter in doppelten geschweiften Klammern entsprechen den Spalten in `mailmerge_108.csv`.
> Im Thunderbird-Mail-Merge-Add-on: **An:** `{{Email}}` · **Betreff** und **Text** unten einfügen.
> **Signatur NICHT einfügen** – sie ist bereits in Thunderbird hinterlegt.

---

## Betreff

```
Sponsoring-Kooperation mit {{Stadt}} – wir möchten Sie unterstützen
```

*(Alternative Betreffzeile:)*
```
{{Stadt}}: Anfrage zur Partnerschaft auf Ihrer Sponsorenseite
```

---

## Mailtext

```
{{Anrede}}

wir sind auf {{Stadt}} aufmerksam geworden – insbesondere auf die Seite, auf der
Sie Ihre Sponsoren und Partner vorstellen ({{Sponsorenseite}}).

Genau hier möchten wir anknüpfen: Wir unterstützen regelmäßig Städte, Gemeinden
und ihre Veranstaltungen, Vereine und Projekte als Sponsor. Dabei geht es uns um
eine partnerschaftliche, regionale Zusammenarbeit – sei es bei Stadtfesten,
Sport- und Kulturveranstaltungen, ehrenamtlichen Initiativen oder Aktionen wie
dem Stadtradeln.

Wir würden {{Stadt}} gern als Sponsor unterstützen und freuen uns, wenn wir im
Gegenzug – wie Ihre übrigen Partner – mit einem kurzen Eintrag (Name und Logo,
idealerweise mit Verlinkung) auf Ihrer Sponsoren-/Partnerseite genannt werden.

Können Sie mir sagen, welche Sponsoring-Möglichkeiten es bei Ihnen aktuell gibt
und wer dafür der richtige Ansprechpartner ist? Über eine kurze Rückmeldung
freue ich mich sehr.

Herzliche Grüße
```

---

## Hinweise zur Personalisierung

- **`{{Anrede}}`**: ist je Zeile vorbefüllt – persönlich („Sehr geehrte Frau …")
  wo ein Ansprechpartner bekannt ist, sonst „Sehr geehrte Damen und Herren,".
- **`{{Stadt}}`** und **`{{Sponsorenseite}}`**: aus der CSV, machen die Mail
  konkret und nachweisbar relevant (kein Massen-Eindruck).
- Optional kannst du einen Satz zur konkreten Sponsoring-Leistung ergänzen
  (Betrag, Sachpreis, Aktion) – das erhöht die Antwortquote deutlich.
