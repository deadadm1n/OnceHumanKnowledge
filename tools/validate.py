#!/usr/bin/env python3
import csv
from collections import Counter
from pathlib import Path

path = Path(__file__).parents[1] / "player-data" / "shroomazon-blueprints.csv"
with path.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 30, f"Expected 30 entries, got {len(rows)}"
counts = Counter(row["category"] for row in rows)
assert counts == {"weapon": 8, "armor": 15, "key_armor": 7}, counts
assert len({row["name"] for row in rows}) == len(rows), "Duplicate names"
print("Blueprint inventory validated:", dict(counts))
