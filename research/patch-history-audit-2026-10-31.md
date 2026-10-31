# Official patch-history vs knowledge-base audit — 2026-10-31

**Scope and honesty:** This is a focused cross-reference of the official patch archive and high-impact gameplay patches against the existing repository. It is **not** a claim that all ~56 major releases and hundreds of bug-fix notices since July 2024 have been individually read and fully normalized. The complete archive is much larger than this first audit.

## Source index
- [Official ongoing update archive](https://www.oncehuman.game/news/update/)
- [Community-maintained cross-linked patch index](https://wikily.gg/once-human/patches)
- [Historical release index, including 2024–2026](https://senseos.gg/wiki/once-human/updates/)
- Source-of-truth preference: official released patch notes > dated dev previews > independent patch index > community gameplay tests.

## High-confidence cross-checks and GitHub implications

| Date / version | Official change | Existing GitHub file / action | Disposition |
|---|---|---|---|
| 2025-03 / 1.4.3 | Generator electricity automatically networked within territory | `knowledge/industry/electricity-and-liquids.md` | Existing note supported; do not infer pipe rules from electricity |
| 2025-09 / 2.1.4 | Deviation fusion launch, parents vs consumable materials | `knowledge/deviations/fusion-mechanics.md` | Record historical implementation separately from later tweaks |
| 2025-12 / 2.2.4 | Battle Skill / Ultimate combat Deviation system | `knowledge/deviations/combat-skills-and-scenario-rules.md` | Current build advice needs 2025+ skills |
| 2026-01 / 2.3.1 | Mod Field Guide; calibration overhaul | `knowledge/progression/mods-blueprints-calibration.md` | Old manual enhancement and bench advice superseded for new gear |
| 2026-03 / 2.3.5 | Blueprint/Starchrom overhaul | Same file | Transfer rather than copy stars |
| 2026-05 / 2.4.1 | Memento weakspot Fast Gunner chance 80% to 100% and weakspot damage boost; P90 proc every **11** hits instead of 12, AoE radius 10m instead of 8m (dev preview) | `research/answered-questions-2026-10-31.md` | **Correct:** the 11-hit screenshot agrees with the May after-value. Don't call the screenshot a contradiction. Actual released tooltip is preferred over preview. |
| 2026-07 / 3.0.1 | SN700 Finale **introduced**, with Reverb stacks cleared upon reload or weapon switch | `knowledge/combat/balance-and-methodology.md` | **Correct:** July entry should be primarily labeled introduction rather than merely a sniper balance change. |
| 2026-07 / 3.0.1 | Shiny armor mod collection / scenario reward paths added | `knowledge/progression/mods-blueprints-calibration.md` | New acquisition route absent from overview |
| 2026-09 / 3.0.6 | Beastmaster summon initially 1 on Sep 16, stated plan to return to 3 on Sep 28 | `knowledge/ranching/beastmaster-2026.md` | Must distinguish announced future plan from implemented change; confirm Sep 28 release |
| 2026-10 / 3.1.1 | Isles of Abyss launched / scenario-specific Tech | `knowledge/scenarios/isles-of-abyss-2026.md` | Applies to 2026 Isles, not all scenarios |
| 2026-10-29 / 3.1.1 hotfix | Sunken Voyager loot crates publicly pickable for **2 minutes** after ship sinking; automatic specialty-resource production restricted to relevant calamity-zone **island range** | `knowledge/scenarios/isles-of-abyss-2026.md`, industry | **New high-impact rule** for Voyager and coastal factories |
| 2026-10-30 / 3.1.1 hotfix | Boat auto-repair facility interaction fixed; wilderness Precision Gear Set supply increased | Isles of Abyss / loot records | Relevant current patch, no combat formula change proven |

## Explicit corrections
1. The repo's earlier `research/answered-questions-2026-10-31.md` says May's Holographic Resonance notes were an unresolved '12-hit comparison'; **official before/after values say 12 -> 11**, and the player's screenshot showed 11. Correct that file, retaining official preview caveat.
2. The repo's `knowledge/combat/balance-and-methodology.md` loosely calls July 'sniper balance changes'. The important direct evidence is **new SN700 Finale** plus its Reverb mechanics. Avoid conflating introduction with nerf/buff.
3. For October 29 Isles of Abyss, automated specialty extraction is restricted to the relevant **island range**. A territory merely existing anywhere in a calamity-zone sea region is insufficient per the hotfix.
4. Under October 29 Voyager changes, anyone may pick up the sunken ship loot crate but it disappears after **two minutes**; prioritize fast retrieval.
5. This audit does not establish a universal damage formula, detailed growshroom/ranch production values, drop odds or all live item tooltips.

## Patch ingestion method for comprehensive coverage
Record one normalized entry per official notice with: `publication_date`, `game_version`, `change_type`, `system`, `scenario`, `item`, `old_behavior`, `new_behavior`, `source_url`, `effective_date`, `confidence`, `supersedes`, and `repo_pages_affected`.
Index announcements separately from developer previews and bug fixes. Resolve later hotfixes before claiming current behavior. Include cosmetic-only notices in source index, but prioritize gameplay-mechanical impacts.

## Primary citations
- https://www.oncehuman.game/news/devBlog/20260521/40781_1301130.html
- https://www.oncehuman.game/news/update/20260709/40780_1307147.html
- https://www.oncehuman.game/news/update/20261009/40780_1314019.html
- https://www.oncehuman.game/news/update/20261029/40780_1318118.html
- https://www.oncehuman.game/news/update/20261030/40780_1318256.html
