# Anleitung: Serien-Mailing mit Thunderbird (Add-on „Mail Merge")

Damit verschickst du die Sponsoring-Anfrage an alle 108 Städte – personalisiert
mit Stadtname, Ansprechpartner und Sponsorenseite. Datei dazu: **`mailmerge_108.csv`**

---

## 0) Einmalig vorbereiten

1. **Add-on installieren:** Thunderbird → Menü (≡) → *Add-ons und Themes* →
   nach **„Mail Merge"** (von Alexander Bergmann) suchen → *Hinzufügen* →
   Thunderbird neu starten.
2. **CSV bereitlegen:** `mailmerge_108.csv` auf den Rechner speichern.
   Sie ist **UTF-8** kodiert und **kommagetrennt** (`,`) – das beim Import genau so wählen.
3. **Signatur:** Deine normale Thunderbird-Signatur bleibt aktiv – **nicht** in den
   Text mit einfügen (sie wird automatisch angehängt).

---

## 1) Neue Nachricht öffnen und Felder ausfüllen

Klicke **„Verfassen"** (neue Nachricht) und trage in die Felder **exakt** Folgendes
ein. Die `{{...}}` sind Platzhalter = Spaltennamen aus der CSV.

| Feld | Was eintragen (genau so kopieren) |
|------|-----------------------------------|
| **Von** | deine Absenderadresse (a.smyrnaios@eology.de) |
| **An** | `{{Email}}` |
| **Kopie (CC)** | `{{Email_CC}}` |
| **Betreff** | `Sponsoring-Kooperation mit {{Stadt}} – wir möchten Sie unterstützen` |

> CC-Feld einblenden: im Verfassen-Fenster neben „An" auf den Pfeil/„Kopie (CC)" klicken.
> Ist `{{Email_CC}}` in einer Zeile leer, lässt Mail Merge das CC einfach weg.

---

## 2) Mailtext einfügen

Schreib die Mail als **reinen Text** (Format → „Nur Text" ist am robustesten).
Füge genau diesen Text ein (mit den Platzhaltern):

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

**Verfügbare Platzhalter** (= CSV-Spalten), die du im Text/Betreff nutzen kannst:

| Platzhalter | Inhalt |
|-------------|--------|
| `{{Anrede}}` | fertige Anrede, z. B. „Guten Tag Frau Brink," bzw. „Sehr geehrte Damen und Herren," |
| `{{Stadt}}` | Stadtname |
| `{{Sponsorenseite}}` | direkte URL der Sponsoren-/Partnerseite |
| `{{Ansprechpartner}}` | Name der Hauptperson (To) |
| `{{Funktion}}` | Funktion/Rolle der Hauptperson |
| `{{Ansprechpartner_CC}}` / `{{Funktion_CC}}` | zweite Person (CC) |
| `{{Email}}` / `{{Email_CC}}` | Adressen (gehören in An/CC) |

> Die Anrede ist bereits fertig in der Spalte `{{Anrede}}` – du musst **kein**
> „Sehr geehrte/r" davor schreiben.

---

## 3) Seriendruck starten

1. Im Verfassen-Fenster: **Datei → Mail Merge** (oder Strg+Shift+M).
2. Im Dialog einstellen:
   - **Source / Quelle:** `CSV`
   - **File / Datei:** `mailmerge_108.csv` auswählen
   - **Character Set / Zeichensatz:** `UTF-8`
   - **Delimiter / Trennzeichen:** `,` (Komma)
   - **Send Mode / Sendemodus:** **„Send Later"** (empfohlen!) – legt alle Mails
     in **Postausgang**, du kannst vor dem Senden alles kontrollieren.
   - **Attachments:** leer lassen (kein Anhang)
3. Auf **OK** klicken. Mail Merge erzeugt jetzt 108 personalisierte Mails.

---

## 4) Kontrollieren und senden

1. Öffne **Postausgang** und prüfe **2–3 Mails stichprobenartig**:
   - Ist `{{Stadt}}`, `{{Anrede}}`, `{{Sponsorenseite}}` korrekt ersetzt?
   - Stimmt An/CC?
2. Wenn alles passt: **Senden → „Ungesendete Nachrichten senden"**.

> **Tipp – Probelauf:** Trag testweise in eine Kopie der CSV in eine Zeile bei
> `Email` **deine eigene Adresse** ein und schicke nur diese eine Zeile vorab an
> dich selbst, um Layout/Platzhalter zu sehen.

---

## 5) Wichtig vor dem Versand – die 7 „Status unklar"-Fälle

Diese Adressen sind offiziell veröffentlicht, konnten aber technisch nicht hart
bestätigt werden (Spalte `Versandempfehlung` = „senden – Status unklar").
Meist trotzdem zustellbar – **auf Bounces (Unzustellbar-Meldungen) achten**:

| Stadt | To-Adresse |
|-------|-----------|
| Göttingen | presse@goettingen.de |
| Langenfeld | info@langenfeld.de |
| Radebeul | presse@radebeul.de |
| Husum | presse@husum.de |
| Saalfeld | info@stadt-saalfeld.de |
| Cham | astrid.hermann@cham.de |
| Sömmerda | l.kob@stadtsoemmerda.de |

Optional: In der CSV nach Spalte **`Versandempfehlung`** sortieren und diese 7
zuletzt / getrennt versenden, um Bounces leicht zuzuordnen.

---

## Spaltenübersicht der CSV

`Email, Email_CC, Anrede, Ansprechpartner, Funktion, Ansprechpartner_CC,
Funktion_CC, Stadt, Domain, Sponsorenseite, DR, Status, Verify_To, Verify_CC,
Versandempfehlung`

(Die Spalten `Domain, DR, Status, Verify_*, Versandempfehlung` sind nur zur
Kontrolle/Sortierung – sie müssen nicht in die Mail.)
