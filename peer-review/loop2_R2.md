# Peer-review feedback loop, Loop 2 verification — Reviewer R2 (biostatistician)

- **Persona:** R2, biostatistician. Scope of this verification: ONLY the two points left in my remit after Loop 1 — (1) the Minor residual on R2-M7 (the over-absolute overlapping-cohorts clause in Difference 9) and (2) the non-blocking observation on `q2_synthesis_stats.json`. Verification only; no other manuscript text was re-reviewed and nothing was edited.
- **Date:** 2026-11-21
- **Files verified:** `manuscript/manuscript.md` (Difference 9, Difference 7, Results Q2 and Table 3), `analysis/synthesis/q1_frequency_pool_log.md`, `analysis/synthesis/build_q2_synthesis.py`, `analysis/synthesis/q2_synthesis_stats.json`, `analysis/synthesis/q2_synthesis_stats_phase6_note.md`, `deposit/data/analysis/q2_synthesis_stats_phase6_note.md`, `deposit/data/analysis/q2_synthesis_stats.json`, `deposit/data/analysis/q2_theory_counts.csv`, `deposit/checksums.sha256`, and `fulltext/prisma_counts_phase4.json`.

**Headline verdict: BOTH points FIXED. Nothing remains open in my remit — no Blocker, no Major, no Minor, and the archive observation is discharged.**

---

## Point 1 — R2-M7 residual: Difference 9 overlapping-cohorts clause — **FIXED (Minor closed)**

Difference 9 now reads: "the overlapping cohorts are handled one record per cohort per pool, so no linked report of the same cohort contributes twice to any pool (same-centre cohorts with overlapping periods that are not linked reports are retained as separate studies, and any partial participant overlap between them is unquantified in the source files)".

This matches what the pool logs support, on both halves:

- **Linked reports — the narrowed claim holds exactly.** The frequency pool log's "Linked / duplicate cohorts" section documents one-retained / one-excluded handling for every identical-cohort pair (e.g. R02711 retained / R02729 excluded; R01701 / R02319; R02365 retained with R01695 and R02856 excluded; R01669 / C11061; R00572 / R02714; R01017 retained / R02244 excluded; R02358 / R02872; R01739 / R02897; R02349 / R02932), and the Boscolo-Rizzo cross-stratum overlap sits in different strata (taste-specific vs composite), so no pooled estimate double-counts it. The claim is now scoped to linked reports of the same cohort, which is precisely what the log establishes — the Loop 1 suggested softening, adopted in substance and extended with the parenthetical.
- **Same-centre, non-linked cohorts — the parenthetical is accurate.** The log's "Same-centre flags (retained, different frames/periods)" entry lists R00934 / R01085 / R02057 (ESIC Faridabad: inpatients Jul–Sep 2020; OPD Sep 2020; May–Jun 2020 cohort) and R01255 / R02070 (Oswaldo Cruz Recife, overlapping 2020 periods), each retained and flagged "possible overlap" / "possible partial overlap" in its per-study row with no quantification anywhere in the log; R02438 is likewise retained with an overlap flag ("different sampling frame", Nord Franche-Comté, alongside the retained R01017). The manuscript's wording — retained as separate studies, partial overlap unquantified in the source files — states exactly this and no more.

The over-absolute "no participant is counted twice in any pool" gloss is gone. R2-M7 is fully closed at all grades.

## Point 2 — Observation on `q2_synthesis_stats.json` — **FIXED (observation discharged)**

`analysis/synthesis/q2_synthesis_stats_phase6_note.md` (2026-11-21) adequately handles the observation, and it is also inside the deposit package:

- **Builder scope stated, and corroborated.** The note states the Phase 4 builder "excluded only C8424, so they show the pre-restatement counts (223 coded studies, 409 assignments, speculative 164)". Verified: `build_q2_synthesis.py` sets `EXCLUDE = {"C8424"}` and names no other exclusion, and `q2_synthesis_stats.json` itself records `excluded` = C8424 only, `unique_q2_studies` 223 and 409 assignments — the pre-restatement values the note attributes to it.
- **Restated counts given, and correct.** The note gives 214 coded studies, 383 assignments, speculative 157 (73.4%), indirect-human 22, direct-human 15, mixed-as-stated 13, animal 5, in-vitro 2 — the grade counts sum to 214, and every value matches the manuscript (Results Q2 grade distribution and Difference 7) and the `q2_restated` block of `fulltext/prisma_counts_phase4.json` (214 / 383 / 157 / 73.4% / direct-human 15). The per-theory counts (T1 117, T2 17, T3 35, T4 61, T5 56, T6 24, T7 7, T8 10, T9 28, T10 2, T11 26) match Table 3's tagged-count column on all eleven rows and sum to 383.
- **Method stated, and checkable.** The note states the method — study-level directness propagated to each of a study's codes over `extraction/extraction_settled_full.csv` minus the 26 records listed in `fulltext/prisma_counts_phase4.json`, reproducing the Phase 4 files exactly when only C8424 is excluded. That is the same derivation I used in Loop 1 to reproduce both the original (223 / 409 / 164) and restated (214 / 383 / 157) sets exactly, and the cited prisma file does list exactly 26 `excluded_records` for the Phase 6 step.
- **Audit record preserved.** The note records that "the Phase 4 files are retained unchanged as the audit record", and they are: the deposited `q2_synthesis_stats.json` and `q2_theory_counts.csv` are byte-identical to the analysis versions and still carry the pre-restatement counts — annotated, not silently regenerated. The note also covers `q2_theory_counts.csv`, the other pre-restatement file in the same directory.
- **Present in the deposit.** `deposit/data/analysis/q2_synthesis_stats_phase6_note.md` is byte-identical to the analysis copy and is listed in `deposit/checksums.sha256`, so a reader who meets the 223 / 409 figures in the deposited stats file finds the explanation in the same directory, pointing to the manuscript's restated counts as the operative ones.

The Loop 1 observation asked for the deposited stats file to be "regenerated or annotated at deposit so the archive does not appear to contradict the manuscript". The annotation branch has been executed in both locations. Discharged.

---

## Overall verdict

- **Blocker remaining open in my remit: NONE.**
- **Major remaining open in my remit: NONE.**
- **Minor remaining open in my remit: NONE** — the sole Loop 1 Minor (R2-M7, Difference 9) is FIXED.
- **Non-blocking observations outstanding: NONE** — the `q2_synthesis_stats.json` observation is FIXED by the Phase 6 annotation note, present in both the analysis directory and the deposit package.

**Explicit statement: nothing remains open in my remit.** Both Loop 2 verification points pass as written; no further change is required from R2 on either point.
