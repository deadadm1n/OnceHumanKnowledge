# Ranching, breeding, Energy and classes — practical reference

**Scope:** mechanics introduced/altered September 16 and September 28, 2026. **Source status:** OFFICIAL, except test suggestions.

## Animal Energy replaces old maintenance
Official 3.0.6 update removed separate animal **Tameness** and **Hydration** stats. Main ranching outcomes now depend on **Energy**.

| Energy | Byproducts | Youngling growth | Breeding readiness | Slaughter |
|---|---|---|---|---|
| 80–100% | Efficient | Normal | Can breed | Larger yields |
| 20–80% | Normal | Normal | Cannot breed | Moderate |
| 0–20% | Paused | Paused | Cannot breed | Smaller yields |

**Important:** the boundary row wording is from the official chart; avoid claiming exact behavior at precisely 20% or 80% without a live check.

- Animal trait slots unlock at **levels 20, 30, 40, and 50**. Previously unlocked traits retained.
- Previous *Docile* Tameness-related effect is replaced with youngling growth-speed benefit.
- **Mixed Meat, Mixed Grain, and Mixed Herb Feed** raise Energy.
- Offline feed draws from troughs. Dropped food on territory ground is **not** consumed offline.
- Body Boost Feed is **not** consumed while offline.
- The animal list indicates Energy, courtship and breeding cooldowns.
- Resource Tracking in World Map displays species distribution.

## Summoning and riding ≠ breeding capacity
- Adults need **more than 20% Energy** to be summoned.
- Summoned animals default to idle; Beast Whistle issues commands.
- Death reduces Energy.
- Only Beastmasters can create/change saddles and animal gear; traders can transfer saddled animals for others to ride, retaining some equipment benefit.
- Non-Beastmasters can summon eligible saddled animals in the wild but **not during combat or in dungeons**.
- Beastmasters start with Deer/Boar/Bear companion choice plus Whistle and Basic Saddle; class grants relevant crafting formulas.
- September 28 update increased Beastmaster simultaneous summons to **three**; other classes remain at one. This is *active summons*, not a claimed ranch-slot capacity.

## Gardener cross-system interactions (official September update)
- Portable Planter Boxes can hold different biomechanical crops with independently tracked cooldowns; multiple kinds can be deployed concurrently.
- Planter Box now consumes durability and disappears with its contents when durability exhausts.
- Grafted crop choice for the six listed biomechanical unit types affects **appearance**, not underlying skill power.
- **Rainfall Reaper biomechanical:** grants Status DMG bonus in an area.
- **Flare Bulbfly biomechanical:** grants Weapon DMG bonus in an area.
- **Watcher biomechanical:** petrifies a target.
- **Balloon biomechanical:** taunts then explodes for damage scaling with target maximum health.
- **The Portal biomechanical:** shoot placed portal to teleport back.

## High-value unsolved question: Acid Secretion goats
Existing reports provide Acid per *collection*, not Acid per *hour* or a proven trait-tier formula.
Collect: goat level, trait, Energy%, elapsed hours, offline vs online, actual Acid, feed consumed. A robust farming calculation needs `Acid/hour = Acid/collection × collections/hour`, then deduct feed and maintenance.

## Sources
- https://www.oncehuman.game/news/update/20261009/40780_1314019.html (document describes September 16 update despite URL directory)
- https://www.oncehuman.game/news/update/20260924/40780_1315053.html
- https://www.oncehuman.game/news/devBlog/20260923/40781_1314860.html
