#!/usr/bin/env python3
"""Build a temporary MkDocs input tree from the canonical repository documents.

No duplicated documentation needs to be maintained: source Markdown stays in-place.
"""
from pathlib import Path
import shutil
import json
import re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".site-src"
if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir()

for name in ("knowledge", "research", "sources", "docs", "player-data", "tools", "data", "assets"):
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

# Build human-readable catalog pages from original, machine-readable JSON.
catalog_root = DEST / "encyclopedia"
catalog_root.mkdir(exist_ok=True)

def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")

def safe(value):
    return escape(str(value or "Not yet verified"))

dev = json.loads((ROOT / "data" / "deviations.json").read_text(encoding="utf-8"))
gear = json.loads((ROOT / "data" / "gear-observed.json").read_text(encoding="utf-8"))
dev_index = ["# Deviation encyclopedia", "", "68 **core Deviation entries** organized by role. This is **not** the full catalog of every seasonal variant or skin.", "", "!!! warning \"Incomplete mechanics\"\n    Skills, trait eligibility, variants and securement conditions require individual evidence. An empty field is **unknown**, not absence.", "", "**Sources:** [TH.GL core index](https://oncehuman.th.gl/db/deviations) · [Wikily](https://wikily.gg/once-human/deviations) · [Trait reference](https://once-human.fandom.com/wiki/Deviation/traits)", ""]
for role in ("Combat", "Crafting", "Territory"):
    dev_index += [f"## {role} Deviations", "", "| Deviation | Reported function | Research state |", "|---|---|---|"]
    for x in dev["entries"]:
        if x["role"] != role:
            continue
        filename = slug(x["name"]) + ".md"
        dev_index.append(f"| [{x['name']}](deviations/{filename}) | {x['known_function'] or 'Research pending'} | {x['status']} |")
        page = [f"# {x['name']}", "", f"**Category:** {role} · **Snapshot:** {x['snapshot']}", "",
                "## What it does", "", x["known_function"] or "**Not yet documented.**", "",
                "## Skills and abilities", "", "Detailed current ability text: **not yet verified**.", "",
                "## Possible passive traits", "", "Individual trait eligibility and passive levels: **not yet verified**.", "",
                "## Securement and recovery", "", "Preferred environment, Power/Mood behavior: **not yet verified**.", "",
                "## Acquisition and variants", "", "Locations and seasonal variants: **not yet verified**.", "",
                "## Sources", "", f"- [Core catalog]({x['source']})", "- [Traits and passive reference](https://once-human.fandom.com/wiki/Deviation/traits)", "",
                "[← All Deviations](../deviations.md)"]
        p = catalog_root / "deviations" / filename
        p.parent.mkdir(exist_ok=True)
        p.write_text("\n".join(page) + "\n", encoding="utf-8")
    dev_index.append("")
(catalog_root / "deviations.md").write_text("\n".join(dev_index) + "\n", encoding="utf-8")

weapons_index = ["# Weapon encyclopedia", "", "This is a **player-observed subset**, not all weapons in the game. Tier V screenshots may reflect blueprint stars and other modifiers.", "",
                 "!!! note \"Tier ≠ blueprint stars\"\n    Tiers I–V refer to crafted item tier. Blueprint stars are a separate progression system. Blank tier cells below mean no verified observation.", "",
                 "| Weapon | Class | Effect | Observed Tier V damage |", "|---|---|---|---:|"]
for x in gear["weapons"]:
    name,fn = x["name"],slug(x["name"]) + ".md"
    stats=x["stats_by_tier"]["5"]
    weapons_index.append(f"| [{name}](weapons/{fn}) | {x['class']} | {x['effect']} | {stats['damage']} |")
    page=[f"# {name}","",f"**Class:** {x['class']} · **Effect:** {x['effect']} · **Observed blueprint stars:** {x['owned_blueprint_stars']}","",
          "## Stats by crafted tier","",
          "| Tier | Damage | Fire rate (RPM) | Magazine | Crit rate | Crit damage | Weakspot damage |",
          "|---|---:|---:|---:|---:|---:|---:|"]
    for i in range(1,6):
        v=x["stats_by_tier"][str(i)]
        if v is None: page.append(f"| {i} | — | — | — | — | — | — |")
        else:page.append(f"| {i} | {v['damage']} | {v['fire_rate_rpm']} | {v['magazine']} | {v['crit_rate_pct']}% | {v['crit_damage_pct']}% | {v['weakspot_damage_pct']}% |")
    page+=["","**Evidence:** Player screenshot transcribed October 2026; values are **not** controlled unmodified base stats.",
           "","## Ability, mods and build interactions","","See current tooltip and [damage methodology](../../knowledge/combat/damage-and-build-testing.md) before claiming any optimal build.",
           "","## Cross-reference","","- [External gear database](https://oncehuman.th.gl/db/gear)","","[← All Weapons](../weapons.md)"]
    p=catalog_root/"weapons"/fn;p.parent.mkdir(exist_ok=True);p.write_text("\n".join(page)+"\n",encoding="utf-8")
weapons_index+=["","**For the wider weapon roster and other tiers:** [TH.GL gear database](https://oncehuman.th.gl/db/gear) (independent; values need patch checks)."]
(catalog_root/"weapons.md").write_text("\n".join(weapons_index)+"\n",encoding="utf-8")

armor_index=["# Armor encyclopedia","","**22 observed pieces** from one inventory, including seven Key Armor pieces. This is **not** a full global armor list.","",
             "| Piece | Slot | Set / special effect | Observed stars |", "|---|---|---|---:|"]
for x in gear["armor"]:
    fn=slug(x["name"])+".md"
    armor_index.append(f"| [{x['name']}](armor/{fn}) | {x['slot']} | {x.get('set') or x.get('effect') or '—'} | {x['owned_blueprint_stars']} |")
    body=[f"# {x['name']}","",f"**Slot:** {x['slot']} · **Set:** {x.get('set') or 'Key Armor'} · **Key Armor:** {'Yes' if x['is_key_armor'] else 'No'} · **Observed stars:** {x['owned_blueprint_stars']}","",
          "## Stats by crafted tier","",
          "| Tier | HP | PSI Intensity | Other properties |","|---|---:|---:|---|"]
    for i in range(1,6):body.append(f"| {i} | — | — | Unverified |")
    body+=["","## Set bonuses / unique effect","","Full current tooltip is **not yet transcribed and patch-verified**.","",
           "## Build restrictions","","Community sources strongly support equipping **one Key Armor at a time**. Verify with live UI if rules change.","",
           "[← All Armor](../armor.md)"]
    p=catalog_root/"armor"/fn;p.parent.mkdir(exist_ok=True);p.write_text("\n".join(body)+"\n",encoding="utf-8")
armor_index+=["","**For more armor and external tier tables:** [TH.GL gear database](https://oncehuman.th.gl/db/gear) and [Wikily armor blueprints](https://wikily.gg/once-human/)."]
(catalog_root/"armor.md").write_text("\n".join(armor_index)+"\n",encoding="utf-8")

print(f"Prepared MkDocs content in {DEST}")
