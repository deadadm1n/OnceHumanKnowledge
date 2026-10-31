#!/usr/bin/env python3
"""Dependency-free check for catalog entries and local Markdown links."""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
targets = list(catalog.get("read_first", []))
for collection in catalog.get("collections", []):
    targets.append(collection["entry"])
    targets.extend(collection["files"])
for target in targets:
    if not (root / target).is_file():
        errors.append(f"Missing catalog path: {target}")

pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
for file in root.rglob("*.md"):
    for raw in pattern.findall(file.read_text(encoding="utf-8")):
        address = raw.split(' ', 1)[0].strip('<>')
        if not address or address.startswith(('#', 'http:', 'https:', 'mailto:')):
            continue
        relative = unquote(address.split('#', 1)[0].split('?', 1)[0])
        destination = (file.parent / relative).resolve()
        if not destination.is_relative_to(root.resolve()) or not destination.exists():
            errors.append(f"{file.relative_to(root)} -> {raw} (not found)")
for error in errors:
    print("ERROR:", error, file=sys.stderr)
if errors:
    sys.exit(1)
print(f"PASS: {len(targets)} catalog paths and local Markdown links")
