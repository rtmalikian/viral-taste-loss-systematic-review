# Loop 2 verification (Phase 6) — Reviewer R6 (SCEPTIC, standing role)

- **Persona:** Reviewer R6, the Sceptic — verification of the Loop 1 open items only, against the revised files. No manuscript file was edited by this reviewer.
- **Date:** 2026-11-21
- **Scope:** the one Major left open in `loop1_R6.md` (Point 4, Data availability overclaim) and Minors N1–N4. Nothing outside that remit was re-reviewed.

**Summary verdict: the Major is DISCHARGED and Minors N1–N3 are DISCHARGED. N4 is discharged conditionally on this loop's own outcome (see Point 4). No Blocker and no Major remains open in my remit.**

---

## Point 1 — THE MAJOR (Data availability overclaim): DISCHARGED

The fix was taken on the harder branch: the package was completed rather than the sentence trimmed. The Data availability sentence (Declarations) is unchanged in wording, so it was re-checked item by item against the physical contents of `deposit/`:

| Sentence component | Physically present |
|---|---|
| protocol | `protocol-locked.md` ✓ |
| search log | `data/search-log.md` ✓ |
| screening and adjudication files | `data/screening/` (`screening_AB.csv`, `screening_final_TA.csv`, `screening_stats.json`, `prisma_counts_phase1.json`) plus `data/screening/adjudication/` (4 decision CSVs + 4 packets) ✓ |
| extraction sheets (both passes and the settled file) | `data/extraction/extraction_A_full.csv`, `extraction_B_full.csv`, pilots (`extraction_A_pilot.csv`, `extraction_B_pilot.csv`, `extraction_pilot_settled.csv`), `full_discrepancy_report.json`; settled file at `data/extraction_settled_full.csv` ✓ |
| risk of bias files | `data/rob_pass1_all.csv`, `data/rob_pass2_all.csv`, adjudicated `data/rob_adjudicated_full.csv` — the plural is now earned ✓ |
| analysis datasets | `data/analysis/` — pool CSVs (frequency, composite, recovery, Q3 treatment table), result JSONs for every pool, pool build logs, `statistician_handcheck.md`, `grade_assessment.md`, Q2 synthesis + Phase 6 annotation ✓ |
| code | `code/` (meta-analysis, Q2 build, figures, manuscript build) ✓ |
| LLM team log | `team-log.md` ✓ |

`data/fulltext/` (decision files, retrieval logs, chasing files, PRISMA counts) is also present, beyond what the sentence enumerates. The README was rewritten to describe the completed contents accurately, including the honest caveats (settled extraction and `final_included.csv` are the 389-record Phase 5 state, with the 26 Phase 6 exclusions identified via `prisma_counts_phase4.json` / Appendix E).

**Checksums:** `sha256sum -c checksums.sha256` run in `deposit/` — **93 of 93 entries OK, no failures**; the manifest covers every file in the package except the manifest itself (94 files total). The overclaim is closed: a reader following the Data availability statement will now find every enumerated category.

## Point 2 — Minor N2 (R02464 boundary) and N3 (below-threshold Q2 class): DISCHARGED, one residual observation

- **N2 — DISCHARGED.** Difference 6 now names the boundary case in the manuscript itself: "The boundary case is R02464, a correspondence that reports preliminary primary results of an ongoing multicentre study: primary data exists in it (a composite outcome only), so it is retained; a record enters the excluded class only where no primary data exists at all." Verified against `extraction/extraction_settled_full.csv`: R02464's settled fields print its own study's preliminary results (composite chemosensitive disorders in about 80% of cases; taste and/or smell disturbance as the only manifestation in 15.3%; spontaneous regression in 67.5%), all composite smell-and-taste with no taste-specific numerator — exactly as the disclosure's "(a composite outcome only)" states. The rule as printed is the rule as applied (Loop 1, Point 2). The hostile-quote risk from the design string's "no primary dataset presented" is now answered on the face of the manuscript.
- **N3 — DISCHARGED, with a residual observation (Minor, not blocking).** Difference 10 now declares: "12 retained case reports or series below the size threshold (among them R02393, a single case with primary data) carry Q2 theory codes and are counted in the pathogenesis tallies as the primary-data records they are; they are not part of the no-primary-data class excluded under the sixth difference." Recount from the settled file, retained set (389 − 26 = 363), design labelled case report or case series with n < 10 and a non-empty theory-code field: **exactly 12** — R00539 (n=6), R00801 (4 re-evaluated), R01378 (n=2), R01382 (n=4), R01519 (n=1), R01692 (n=6), R02125 (n=1), R02180 (n=3), R02393 (n=1, T1 — confirmed present with primary data), R02443 (n=1), R02693 (n=5), R02954 (n=1). The retained Q2-coded total independently reproduces as 214, matching the restated tally these records are counted in. **Observation:** one further retained record, R02135 (familial case cluster report, n=7, Q2 codes T3/T10), is below the size threshold and is likewise counted in the pathogenesis tallies as primary data, but falls outside the sentence's count of 12 because its settled design is labelled a cluster report rather than a case report/series. The disclosure's substance — these records are in the tallies, and none is in the excluded no-primary-data class — is true for R02135 as well; only the numeral depends on the design-label boundary. Recorded as a residual Minor observation for the author's awareness; it changes no count, tally or verdict, and I do not hold the loop open on it.

## Point 3 — Minor N1 (Figure 1 ordering / double-363): DISCHARGED

Verified on the rendered `manuscript/figures/fig1_prisma.png` (and the figure text as embedded in the PDF):

- The main-pool box now reads "Included from main pool: 363 (**stage count, before the eligibility-consistency step below**)" — the 363 is explicitly flagged as a stage count.
- The included-total box now shows the sequence in order: "Chasing full-text screening: 26 included… **Included total before the eligibility-consistency step: 389 records / INCLUDED TOTAL after the step: 363 records** (362 unique publications…)". The figure's arithmetic now resolves inside the box itself (363 + 26 = 389 → −26 → 363); the pre-step total whose absence caused the Loop 1 misread is present.
- The Results flow text flags the coincidence in words: the main-pool 363 is "(a stage count before citation chasing and before the eligibility-consistency step; **the final total after that step is also 363, by coincidence**)".

Residual cosmetics only: the Phase 6 step-description box still sits below the total box, but it is now a redundant confirmation ("Synthesis set: 363 records") rather than the sole carrier of the step, so the ordering no longer invites a misread. N1 is closed.

## Point 4 — Minor N4 (peer-review declaration): HOLDS, from my remit

The Declarations statement — the loops "closed with no Blocker or Major item open" — was false when printed during Loop 1 because my Major was open. That Major is now discharged (Point 1), Minors N1–N3 are discharged (Points 2–3), and no new Blocker or Major arose in my remit from the Loop 2 changes (the completed deposit, the two Difference disclosures and the redrawn Figure 1 were each verified against source files above). **From my remit, the statement now holds.** Its accuracy for the manuscript as a whole depends on the other reviewers' Loop 2 verdicts, which are outside my remit; if any other reviewer's Major remains open, the sentence must not stand as written.

## Gate statement

**No Blocker and no Major remains open in my remit. The Loop 1 Major (Data availability overclaim) is discharged by completion of the deposit package — 93/93 checksums verify and every enumerated category is physically present. Minors N1, N2 and N3 are discharged (N3 with one non-blocking residual observation on R02135). Minor N4's statement now holds from my remit. Loop 2 closes clean for Reviewer R6.**
