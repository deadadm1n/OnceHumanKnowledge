# Coastal industrial operation: salt, fluids, farming and Wish Box

**Scope:** a reproducible operations model, not a claim that all facilities have fixed universal rates.

## Production graph
```text
Seawater ─┬─> Salt craft ─> Wish Box deposits ─> hourly randomized outputs
          └─> Purification ─> Stored usable water ─> Sprinklers ─> Crops
                                                            ├─> Food buffs
                                                            ├─> Seeds/fertilizer
                                                            └─> Feed ─> Ranch Energy ─> Animal byproducts
Electricity ─────> pumps, purifier, grow lights and relevant facilities
```

## What to measure
| Node | Useful unit | Hidden confounder |
|---|---|---|
| Seawater pump | liters/min or item stacks/10m | location, nearby extraction materials, power |
| Filter | clean-water units/hour | inputs, storage and pipe routing |
| Salt stoves | salt/hour sustained | queue slots, ingredients, parallel work lines |
| Sprinkler | affected planters and water/hour | geometry, planter crop preference |
| Growshroom | harvests/hour, seeds/hour | Energy/Mood, planting downtime, available seed |
| Livestock | Acid/hour, feed/hour | Energy band, individual trait, offline behavior |
| Wish Box | output value/8k salt/hour | random distribution, drop tables and batch behavior |

## Existing observation vs capacity
Player observed two salt per five seconds during active cooking; **inferred maximum** 24/min or 1,440/hour *per stove* assumes constant ingredients, no queue gaps and both production lanes active. Eight stoves yield *theoretical* 11,520/hour, but actual sustained output can be far lower.
One test of Corrosive Agent changed four-hour decay to 20 minutes; equivalent **12x faster countdown in that specific case**. Don't promise same result for every food type or storage condition.
Wish Box accepted 8,000 salt and produced useful loot; no statistically estimated expected returns.

## Practical factory optimization
1. Determine **bottleneck** first (water input, queue fill, power or output storage).
2. Measure each production stage **with empty output storage**, over fixed intervals.
3. Record input amounts and maintenance clicks so 'passive' throughput isn't overstated.
4. For randomized outputs, report number of independent cycles, totals and variability.
5. Compare marginal gain from adding one facility against power and territory cap.
6. Keep experimental batch and commercial production separate to avoid corrupting measurements.

## Electricity and location
Official March 2025 notes introduced a territory electricity management UI and automatically networked generators within a territory. That's different from asserting liquids travel automatically. Isles of Abyss October 29 hotfix restricts **specialty-resource** automatic production to matching calamity-zone island ranges.
Do not assume placing a base in ocean water alone yields every resource.

## Sources
- https://www.oncehuman.game/news/update/20250313/40780_1218778.html
- https://www.oncehuman.game/news/update/20261029/40780_1318118.html
- https://www.oncehuman.game/news/update/20250115/40780_1207023.html
