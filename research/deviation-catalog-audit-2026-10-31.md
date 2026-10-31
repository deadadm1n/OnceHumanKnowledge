# Deviation catalog research audit — 31 October 2026

## Coverage / limits
- **68** core entries in TH.GL; **98** entries in OnceHumanDB; **263** entries including skins and variants in Wikily. These are **not contradictory counts of the same unit**; they have different inclusion criteria.
- **23 of our 68 core entries** now include researched ability summaries from individual TH.GL pages. Exact skill coefficients and passive compatibility remain gaps.
- Wikily is useful as a **variant discovery index** but a listed skin is not proof of a gameplay mechanical difference.
- Research records use paraphrases, link each individual reference and distinguish **SECONDARY_DATABASE** from developer patch documentation.

## Confirmed developer changes worth treating as higher priority
1. December 23, 2025: Combat Deviations gain Battle Skills and Ultimates. Old pages listing only throw/auto attack may be incomplete. https://www.oncehuman.game/news/devBlog/20251218/40781_1277420.html
2. January/February 2026: some abilities and vulnerabilities were rebalanced; do not assume 2024 modifiers are current.
3. April 8, 2026: Fusion completion time explicitly changed to **5 minutes**. https://www.oncehuman.game/news/update/20260408/40780_1295195.html
4. April 8, 2026: Wish Box, Paper Doll and H37 item rewards adjusted to revised item categories, and Digby Boy no longer gathers Tin. https://www.oncehuman.game/news/update/20260408/40780_1295195.html
5. July 14, 2026: Voodoo Doll Ultimate vulnerability had a bug where scaling ignored Skill Rating; fixed in 3.0.1. https://www.oncehuman.game/news/update/20260714/40780_1307619.html
6. October 21, 2026: Duet introduced and multiple Morphed Deviation variants published, supporting fusion. https://www.oncehuman.game/banner/20261021/41906_1317280.html

## Research conflicts discovered
- TH.GL lists **Artisan's Touch, Pyro Dino, Gazocchio and Zeno-Purifier** as fusion-only in a location summary, **while simultaneously listing boss or Securement Box chances** in their own source rows. Until the same patch/scenario conditions are reconciled, neither should be presented as an exclusive acquisition rule.
- TH.GL marks Buzzy Bee and Atomic Snail as Manibus-only. A player owning one in Isles of Abyss does not prove it was **acquired in Isles**; transfer and scenario provenance need checking.
- TH.GL's combat ability rows for Butterfly, Festering Gel, Pyro Dino and others contain **? placeholders** for coefficients; do not transcribe them as zero or guess.
- Fusion abilities and passive skills from *Deviation: Survive, Capture, Preserve* are not necessarily valid in Isles of Abyss. Scenario must be part of every trait record.

## Research method for expansion
For each entry record `name, role, variant_id, ability name, ability effect, numeric coefficients + units, skill rating scaling, Activity recovery, Mood / Power, securement preferences, possible passive traits, capture sources with scenario & patch, fusion eligibility, source links, evidence grade, date checked`.
**Do not** infer trait eligibility by Deviation role alone.

## Practical next priorities
1. Resolve conflicting acquisition routes for the four named Deviations against 2026 patch notes.
2. Separate current Battle Skill/Ultimate from pre-overhaul combat ability text for each Combat Deviation.
3. Expand variant discovery separately; Wikily lists 263 including many skins and variations, not 263 confirmed distinct mechanics.
4. Audit passive trait eligibility with current in-game UI; avoid copying cross-scenario Symbiosis passive tables.
5. Quantify Skill/Activity scaling through tests, not assumed linear ratings.
