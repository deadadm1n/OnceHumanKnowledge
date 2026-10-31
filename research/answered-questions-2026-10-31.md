# Answered research questions — evidence audit (2026-10-31)

Scope: answers found by following existing open questions. Labels: **official**, **cross-checked community**, **community observation**, **unresolved**. Do not assume guides written before 2026 balance patches reflect present behavior.

## 1. Is Key Armor limited to one equipped piece?
**Answer: YES — cross-checked community + wiki.** Wiki's Armor section explicitly says one piece at a time; multiple Steam discussions report the exact equip error. Therefore builds recommending Beret and Earthly Boots together are invalid.
- https://once-human.fandom.com/wiki/Armor
- https://steamcommunity.com/app/2139460/discussions/0/4515505458301369410/
**Confidence:** strong corroboration, though not yet backed by a current developer statement.

## 2. Can new mods be enhanced with Weapon Mod Parts?
**Answer: NO, not under the new system — official.** January 2026 overhaul introduced Mod Field Guide where highest-level versions unlocked are equipable, with total subattribute level up to 17. Spare/lower mods convert to Mod Dust, which buys mod crates. Developer explicitly explained old mod parts can be converted to Mod Dust. Legacy enhancement must be treated separately.
- https://www.oncehuman.game/news/devBlog/20251212/40781_1276354.html
- https://www.oncehuman.game/news/devBlog/20260123/40781_1283429.html
- https://www.oncehuman.game/m/news/devBlog/20251219/40781_1277631.html

## 3. Can a 6-star blueprint transfer its star level?
**Answer: YES, to a blueprint of the same rarity, but *transfer* not duplicate — official.** March 25 update retained Blueprint Conversion, and converted fragment economy to Starchrom. This is not free simultaneous 6-star gear.
- https://www.oncehuman.game/news/update/20260325/40780_1292938.html

## 4. Has R500 Memento's weakspot proc probability changed?
**Answer: YES — official 2026 balance patch.** May 21 dev blog specifically contrasts 80% before with **100% on weakspot hits** after adjustment (45% other hits). The player screenshot matches the newer value. Earlier guides using 80% are outdated.
- https://www.oncehuman.game/news/devBlog/20260521/40781_1301130.html

## 5. Has Holographic Resonance's proc cadence changed?
**Answer: YES — official proposed change in May balance blog.** The May 21 dev blog lists a 12-hit AoE trigger in its comparison and revised parameters. Cross-reference current tooltip before asserting an exact latest hit count, because the player's screenshot showed 11.
- https://www.oncehuman.game/news/devBlog/20260521/40781_1301130.html

## 6. How much Acid does a goat with Acid Secretion make?
**Answer: partial, community observation only.** A 2026 Reddit discussion reports **1–5 Acid per animal collection**, with randomness, but no controlled interval, trait tier or feed setup. Do *not* treat this as a universal rate per hour.
- https://www.reddit.com/r/OnceHumanOfficial/comments/1w43qo9/quick_question_regarding_specific_animal_traits/
**Confidence:** low until replicated.

## 7. Does Wish Box have a deadline before hourly conversion?
**Answer: secondary-source claim, not officially validated.** Wiki reports inserted items need five minutes to lock in, so additions after minute 55 won't convert at the next hour. Official 2025 announcement confirms hourly conversion, not the five-minute qualifier.
- https://once-human.fandom.com/wiki/Wish_Box
- https://www.oncehuman.game/news/update/20250115/40780_1206961.html
**Confidence:** conversion hourly = official; five-minute lock = community.

## 8. Is there a definitive public damage formula?
**Answer: NO verified universal equation surfaced in this pass.** Community proposals disagree on whether Crit and Weakspot bonuses combine additively or multiplicatively; some attacks are Status DMG yet can crit or weakspot. Official February 2026 changes explicitly altered damage typing for particular weapon effects. Record formula *by damage type and weapon* and validate against dummy numbers.
- https://www.oncehuman.game/news/devBlog/20260212/40781_1287008.html
- https://www.reddit.com/r/OnceHumanOfficial/comments/1ll0y61
- https://www.reddit.com/r/OnceHumanOfficial/comments/1uv437x/help_damage_calculations/
**Confidence:** official weapon type adjustment; proposed formulas are unverified.

## 9. What limits the value of damage calculators?
**Answer: secondary tool explicitly excludes procs and most mod bonuses** in some outputs. They can be used for baselines, but should not rank complete weapon builds without testing the missing mechanics.
- https://ohbuilds.com/planner.html?build=sks-crit

## New practical conclusions
- R500 weakspot Fast Gunner trigger is a *documented* advantage for an accurate player; it does not prove highest DPS.
- Do not recommend replacing one 6-star key setup with another without respecting one-Key-Armor restriction.
- Mark unresolved quantities with units (Acid/collection, salt/hour, damage/shot), never turn them into implied DPS or profit.
- Prioritize questions where current official docs contain the answer before asking the user for screenshots.
