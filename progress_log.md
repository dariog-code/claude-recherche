# Progress-Log — Recherche Förderer/Sponsoring deutscher Hochschulen

## ⚠️ UMGEBUNGS-STATUS / BLOCKER (wichtig zuerst lesen)

**Stand 2026-06-06, Beginn der Cloud-Session.**

Diese Cloud-Session läuft hinter einer **restriktiven Netzwerk-Allowlist**. Konkret getestet:

| Ziel | Ergebnis |
|------|----------|
| WebSearch (über Anthropic) | ✅ funktioniert |
| GitHub MCP | ✅ funktioniert |
| `curl`/`WebFetch` auf Hochschul-Domains (fh-wedel.de, tu-dresden.de, kit.edu, uni-goettingen.de …) | ❌ **HTTP 403 `x-deny-reason: host_not_allowed`** |
| `api.hunter.io` (Email-Verifier / Domain-Search) | ❌ **HTTP 403 `Host not in allowlist`** |

**Folge:** Die beiden Kern-Verifikationsschritte der Methodik sind in dieser Session **nicht ausführbar**:
1. **HTML-/`<a href>`-Analyse** (Voraussetzung für Status „LINK VERIFIZIERT" und für Dofollow-/Subdomain-/≥6-Firmen-Prüfung) — Seiten lassen sich nicht abrufen.
2. **Hunter Email-Verifier** — der Hunter-Key liegt jetzt vor (vom Nutzer übermittelt, in `~/.hunter_key` gespeichert), aber `api.hunter.io` ist nicht in der Allowlist, der Key ist also wirkungslos.

**Was der Nutzer tun muss, damit die volle Recherche läuft** (eine der Optionen):
- Netzwerk-Policy der Environment auf **„No network restrictions"** umstellen, **oder**
- der Allowlist die Hosts **`api.hunter.io`** sowie die Hochschul-Domains (bzw. `*`) hinzufügen.
- Doku: https://code.claude.com/docs/en/claude-code-on-the-web

Sobald das erledigt ist, kann eine Folge-Session die hier vorbereitete `arbeitsliste.md` (Discovery + provisorische Einstufung) zügig mit echter Link- und Email-Verifikation abarbeiten.

**Was in dieser Session trotzdem geleistet wird (Degraded-Mode, nur WebSearch):**
- Aufbau der vollständigen `arbeitsliste.md` (alle Unis/HAW/private HS mit Domains, Fortschritt).
- WebSearch-Discovery je Institution: Kandidaten-URL finden, **Hauptdomain vs. Subdomain** aus der URL bewerten (machbar ohne Abruf), Modell (Sponsoring-mit-Gegenleistung vs. dual/Deutschlandstipendium) aus Snippets einschätzen.
- Die **Master-CSV bleibt sauber**: keine unverifizierten „LINK VERIFIZIERT"/„SPONSORING-SEITE"-Zeilen werden eingetragen. Discovery-Befunde landen als provisorische Einstufung in `arbeitsliste.md`; nur klar bestimmbare Modell-/Domain-Ausschlüsse werden ggf. als `AUSGESCHLOSSEN` ergänzt.
- Periodischer Re-Test des Netzwerks; falls die Allowlist während der Session geöffnet wird, wird automatisch auf volle Verifikation (curl-HTML + Hunter) umgeschaltet.

---

## Ausgangslage

Master-CSV vom Nutzer übernommen (Single Source of Truth): **55 Datenzeilen**
- LINK VERIFIZIERT: 4 (HdM Stuttgart, OTH Amberg-Weiden, TH Georg Agricola Bochum, THWS Würzburg-Schweinfurt)
- SPONSORING-SEITE: 15 (S1–S15)
- PRÜFEN / GRENZFALL / AUSGESCHLOSSEN: Rest

---

## Discovery-Log (chronologisch)

| Zeitstempel | Institution | Disposition (Discovery) | Notiz |
|-------------|-------------|--------------------------|-------|
