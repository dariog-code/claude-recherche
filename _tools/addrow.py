#!/usr/bin/env python3
"""Append one properly-quoted CSV row to the master file.
Reads 19 fields from a JSON list on argv[1]."""
import sys, csv, json
CSV = "/home/user/claude-recherche/recherche_master_foerdervereine.csv"
fields = json.loads(sys.argv[1])
assert len(fields) == 19, f"expected 19 fields, got {len(fields)}"
with open(CSV, "a", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(fields)
print("appended:", fields[0], fields[1], fields[2])
