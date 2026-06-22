# Mail-Vorlage Hochschul-Sponsoring / Förderpartnerschaft (Thunderbird Mail Merge)

> Abgeleitet aus `mailvorlage_staedte_sponsoring.md` (Struktur) + der im Repo
> dokumentierten Hochschul-Strategie (`ERGEBNIS_UEBERSICHT.md`, `arbeitsliste.md`):
> Sponsoring/Förderer **mit Gegenleistung** = Nennung mit **Logo + Verlinkung**
> auf der Förderer-/Sponsoren-/Partnerseite der Hochschule.
>
> Platzhalter in `{{ }}` = Spalten der Versand-CSV (`mailmerge_hochschulen.csv`).
> Im Thunderbird-Mail-Merge-Add-on:
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · **Betreff/Text** unten.
> **Signatur NICHT einfügen** – ist in Thunderbird hinterlegt.

---

## Zwei Varianten je nach Ziel-Typ

- **Variante A — SPONSORING-SEITE** (Logos/Förderer sind gelistet, aber **NICHT verlinkt**):
  Hebel = um **Verlinkung** des Eintrags bitten. → Satz [A] im Text verwenden.
- **Variante B — LINK VERIFIZIERT / PARTNERBEREICH** (Partner werden bereits verlinkt):
  Hebel = als Förderer/Partner **aufgenommen + verlinkt** werden. → Satz [B] im Text.

(Für einen einzigen Serienlauf ohne Trennung kann der allgemeine Text ohne [A]/[B] genutzt werden.)

---

## Betreff

```
Förderengagement an {{Hochschule}} – Aufnahme in Ihren Förderer-/Partnerkreis
```

*(Alternative Betreffzeile:)*
```
{{Hochschule}}: Anfrage zu einer Sponsoring-/Förderpartnerschaft
```

---

## Mailtext

```
{{Anrede}}

wir sind auf {{Hochschule}} aufmerksam geworden – insbesondere auf die Seite, auf
der Sie Ihre Förderer und Partner vorstellen ({{Listungsseite}}).

Wir unterstützen gezielt Hochschulen – etwa über Projektförderungen, allgemeine
Unterstützung auf Fachbereichsebene oder als Förderer in Ihrem Partnerbereich –
und würden uns gern bei {{Hochschule}} engagieren.

Im Gegenzug freuen wir uns – wie Ihre übrigen Förderer und Partner – über eine
kurze Nennung mit Logo und Verlinkung auf Ihrer Förderer-/Partnerseite.

Können Sie mir sagen, welche Möglichkeiten einer Förder- oder Sponsoring-
Partnerschaft es bei Ihnen aktuell gibt und wer dafür der richtige Ansprechpartner
ist? Über eine kurze Rückmeldung freue ich mich sehr.

Herzliche Grüße
```

### Optionaler Zusatzsatz je Variante (vor „Können Sie mir sagen …" einfügen)

- **[A] SPONSORING-SEITE** (Logos unverlinkt):
```
Mir ist aufgefallen, dass die dort genannten Förderer derzeit ohne Verlinkung
erscheinen – über eine Verlinkung unseres Eintrags würden wir uns daher besonders
freuen.
```

- **[B] LINK VERIFIZIERT / PARTNERBEREICH** (Partner werden bereits verlinkt):
```
Da Sie Ihre Partner bereits mit Logo und Link präsentieren, würden wir uns über
eine Aufnahme in genau dieser Form sehr freuen.
```

---

## Platzhalter (= CSV-Spalten)

| Platzhalter | Inhalt |
|-------------|--------|
| `{{Anrede}}` | fertige Anrede („Guten Tag Frau …" bzw. „Sehr geehrte Damen und Herren,") |
| `{{Hochschule}}` | Name der Hochschule |
| `{{Listungsseite}}` | direkte URL der Förderer-/Sponsoren-/Partnerseite |
| `{{Email}}` / `{{Email_CC}}` | Adressen (An / CC) |
| `{{Ansprechpartner}}` / `{{Funktion}}` | Hauptkontakt (Referenz) |
| `{{Ansprechpartner_CC}}` / `{{Funktion_CC}}` | zweite Person (CC) |

## Hinweise zur Personalisierung
- `{{Anrede}}` ist je Zeile vorbefüllt – persönlich, wo ein Ansprechpartner bekannt ist.
- `{{Hochschule}}` + `{{Listungsseite}}` machen die Mail konkret und nachweisbar relevant.
- Konkretes Förderangebot (Projektförderung, Unterstützung auf Fachbereichsebene,
  Förderer im Partnerbereich) erhöht die Antwortquote – Deutschlandstipendium bewusst
  nicht als Aufhänger verwenden.
