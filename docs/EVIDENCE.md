# Evidence and version policy

A page can contain multiple claims with different evidence grades. **Mark each important claim**, not just the page as a whole.

| Label | What it means | Not sufficient for |
|---|---|---|
| **OFFICIAL** | Dated first-party *released* notes or in-game patch text | Assuming permanence across later updates |
| **OFFICIAL PREVIEW** | Developer preview / planned change | Claiming final deployment without a release check |
| **OBSERVED** | Screenshot, log, or described in-game test | Generalizing beyond the tested setup |
| **COMMUNITY** | Wiki, guide, Reddit or Steam discussion | Claiming developer confirmation |
| **INFERRED** | Math/logic based on stated premises | Ignoring capacity or hidden modifiers |
| **HYPOTHESIS** | Plausible untested interaction | Making a build recommendation as fact |
| **SUPERSEDED** | Known prior rule replaced by a later patch | Describing the current live game |
| **UNKNOWN** | No defensible answer yet | Filling with plausible numbers |

## Per-claim metadata (recommended)
- **Scenario:** e.g. Isles of Abyss / all scenarios / unknown
- **Last checked:** YYYY-MM-DD
- **Effective version:** confirmed patch version or unknown
- **Source:** direct URL(s), with publication date
- **Status:** one of the labels above
- **Supersedes / superseded by:** earlier or later behavior where applicable

## Resolve contradictions
1. Locate the claimed original source.
2. Check whether it is a **preview**, **released patch**, **hotfix**, or player observation.
3. Check newer updates in the patch history.
4. Separate different scenarios, difficulties and Tech levels.
5. If disagreement remains, mark **CONFLICT** explicitly and suggest a reproducible test.

## Example
```markdown
**Claim:** A pictured Memento has a 100% Fast Gunner trigger on weakspot hits.
**Status:** OFFICIAL (May 2026 preview), plus OBSERVED (October 2026 tooltip).
**Scope:** The pictured weapon and patch.
**Limit:** This does not prove the highest sustained damage per second.
```

## Citations
Link directly to the specific patch or source page. Do not cite an unsourced summary as if it were first-party documentation.
