# Electricity and liquid transport — versioned reference

## Electricity [official, 2025-03-13]
Update 1.4.3 added an **Electricity Management** generator screen and total/current consumption visualization in Construction mode. Generators **automatically form a territory electrical network by default**; running wires between generators isn't required for that purpose. Therefore earlier advice suggesting a mandatory central power pole for every generator is inaccurate or unnecessarily complicated.

Source: https://www.oncehuman.game/news/update/20250313/40780_1218778.html

## Liquids [official plan, not proof of delivery]
The same 2025-03-13 notice said water/production management improvements were **postponed to April 24**: selectable outputs for pumps, rainwater collectors, water filters and brewing barrels; pipe transport of Impure Acid and Barreled Crude Oil. Because a scheduled future feature is not confirmation of deployment, verify subsequent patch and in-game UI before asserting the options exist.

## Technical tests
- In Construction mode, inspect current and total power usage.
- Record generator watts and consumption with each facility enabled/disabled.
- Compare hydro output with solar in actual placement conditions.
- Empty tanks, run extraction pump 10 minutes, measure resource count.
- Test which facilities can receive liquid by pipe, gravity, or manual transfer.
- Measure sprinkler output and coverage at the planter level.

## Do not assume
- 'Hydraulic Generator' is the same item label as Hydropower.
- Pipe direction is universal; power and elevation can matter.
- A 1,000-capacity sprinkler consumes 1,000 water per operation.
