#!/usr/bin/env python3
"""Build a temporary MkDocs input tree from the canonical repository documents.

No duplicated documentation needs to be maintained: source Markdown stays in-place.
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"
if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir()

for name in ("knowledge", "research", "sources", "docs", "player-data", "tools"):
    src = ROOT / name
    if src.exists():
        shutil.copytree(src, DEST / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

for src in ROOT.glob("*.md"):
    shutil.copy2(src, DEST / src.name)
for src in ROOT.glob("*.json"):
    shutil.copy2(src, DEST / src.name)

# Preserve linked issue templates and pull-request template if referenced in README.
github = ROOT / ".github"
if github.exists():
    for src in github.rglob("*"):
        if src.is_file() and src.suffix in {".md", ".yml", ".yaml"}:
            target = DEST / src.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)

landing = """# OnceHumanKnowledge

**A community-maintained, evidence-first guide to Once Human mechanics.**

Explore **[game mechanics](knowledge/README.md)**, the **[Isles of Abyss field guide](knowledge/scenarios/isles-of-abyss-field-guide.md)**, **[Deviation research](knowledge/deviations/README.md)**, and **[patch-history audits](research/README.md)**.

!!! warning "Research is version-specific"
    Guides distinguish official released changes, player observations, older mechanics, and unsolved questions. Always check patch date and scenario.

### Contribute

Spot an outdated mechanic? [Open an issue](https://github.com/deadadm1n/OnceHumanKnowledge/issues/new/choose) or propose a pull request after reviewing the [evidence guidelines](docs/EVIDENCE.md).

### What we cover

- Combat, weapon effects, blueprints, mods, calibration and builds
- Deviations, fusion, Securement, Mood and Power
- Agriculture, ranching, water, electricity and industry
- Isles of Abyss ships, hazards and scenario-specific progression
- Source-backed corrections, research questions and historical patch notes

This site is unofficial and not affiliated with the game's publisher.
"""
(DEST / "index.md").write_text(landing, encoding="utf-8")
print(f"Prepared MkDocs content in {DEST}")
