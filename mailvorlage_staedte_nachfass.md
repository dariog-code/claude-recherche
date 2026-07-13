# Nachfass-Mailvorlage Städte-Sponsoring (Thunderbird Mail Merge)

> Für Städte aus Welle 1, die nach ~7–10 Werktagen **nicht geantwortet** haben.
> Freundliche, kurze Erinnerung – kein Vorwurf. Platzhalter = Spalten der
> Nachfass-CSV (`mailmerge_nachfass_welle1.csv`).
> **An:** `{{Email}}` · **CC:** `{{Email_CC}}` · Signatur bleibt aus Thunderbird.

---

## Betreff

```
Nachfrage: Sponsoring-Kooperation mit {{Stadt}}
```

*(Alternative:)*
```
Kurze Erinnerung – Partnerschaft mit {{Stadt}}
```

---

## Mailtext

```
{{Anrede}}

vor einigen Tagen hatte ich Ihnen geschrieben, weil wir {{Stadt}} gern als
Sponsor unterstützen würden – mit Blick auf Ihre Sponsoren-/Partnerseite
({{Sponsorenseite}}).

Vielleicht ist meine Nachricht im Tagesgeschäft untergegangen – das verstehe ich
gut. Deshalb melde ich mich kurz noch einmal: Wir würden {{Stadt}} gern als
Sponsor unterstützen und im Gegenzug – wie Ihre übrigen Partner – mit einem
kurzen Eintrag (Name und Logo, idealerweise mit Verlinkung) auf Ihrer Sponsoren-/
Partnerseite genannt werden.

Können Sie mir kurz sagen, welche Möglichkeiten es bei Ihnen gibt und wer der
richtige Ansprechpartner ist? Über eine kurze Rückmeldung freue ich mich sehr –
auch wenn es aktuell nicht passt.

Herzliche Grüße
```

---

## Platzhalter
`{{Anrede}}`, `{{Stadt}}`, `{{Sponsorenseite}}`, `{{Email}}`, `{{Email_CC}}`,
`{{Ansprechpartner}}`, `{{Funktion}}` — identisch zur Erstkontakt-Vorlage.

## Hinweise
- Nur an Städte senden, die **noch nicht geantwortet** haben (Ergebnis = offen).
  Interessenten/Absagen sind in der Nachfass-CSV bereits ausgeschlossen.
- Nach dem Versand in `master_tracking.csv`: `Nachfass1_Datum` + `Nachfass1_Status = versendet`.
