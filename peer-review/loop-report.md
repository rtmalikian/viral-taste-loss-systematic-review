# Loop Report — Viral Taste-Loss Review, Phase 6 (peer-review feedback loop)

**Date:** 2026-11-21
**Process:** Run under the author's direction of 2026-11-21 02:16 PT ("make the reviewers feedback less of a gate and more of a loop") and the process amendment filed at `manuscript/peer-review/process-amendment-2026-11-21.md` and in `team-log.md`: implement feedback in fix → re-review loops with the original reviewers until no Blocker and no Major remains open; escalate to the author only after 3 loops with a point still open.
**Outcome: the loop closed in 3 loops (Loop 1 full-panel verification, Loop 2 targeted verification, Loop 3 two spot-verifications). No Blocker, no Major and no Minor remains open with any reviewer. Nothing is escalated to the author.**

## Final counts (Phase 6)

- Included: **363 records, 362 unique publications** (Ohla 2022 pair R01101/R02974 both retained; different DOIs; neither contributes data).
- Question membership (provisional mapping): **Q1 339, Q2 280, Q3 82**.
- Excluded at the eligibility-consistency step: 26 records (Appendix E now 87 rows).
- Q2 restated: 214 coded studies, 383 assignments, speculative 157 (73.4%), direct-human 15.
- RoB bands (retained): low 62, moderate 214, high/serious/critical 61, not assessable 26.
- Abstract: 997 words (limit 1,000). Manuscript: 113 pages.
- **Manuscript QA gate: PASS** on the final build (`manuscript_qa_gate.py`, run after the Loop 3 edits). Figure 1 regenerated twice in Phase 6 and visually re-inspected both times (log: `manuscript/figure-inspection-log.md`).

## Proof that no pooled number changed

The 26 excluded records were verified — by the coordinator and independently by R2, R5 and R6 — to appear in **none** of the pool files: `q1_frequency_pool.csv` (137 rows), `q1_frequency_composite.csv` (27), `q1_recovery_pool.csv`, `q1_recovery_composite.csv`, `q3_treatment_table.csv` (23). All pooled estimates, confidence/prediction intervals, GRADE ratings and verdicts are byte-identical in substance to Phase 5; only descriptive counts were restated, each identified where it appears. The pre-restatement Q2 archive files (`q2_synthesis_stats.json`, `q2_theory_counts.csv`) are retained unchanged and annotated by `analysis/synthesis/q2_synthesis_stats_phase6_note.md`.

## Item-by-item closure table

| Item | Reviewer | What was done | Closed |
|---|---|---|---|
| 26-record no-primary-data class (incl. C8424); sceptic A1–A4 | Panel / R6 | Decision taken on eligibility-consistency grounds: all 26 formally excluded (Difference 6), listed in Appendix E with the standard reason; class = 20 narrative/bibliographic reviews, 4 letters, 1 hypothesis paper, 1 correspondence, all with no primary data; boundary cases R02464 (primary data, retained, named in Difference 6) and R02393 (primary data, separate case class) documented; all counts harmonised (Abstract, PLS, Results, Discussion, Appendices C/D/E, Figure 1, `prisma_counts_phase4.json`) | Loop 1 (R1, R2, R5, R6 verified by independent recount) |
| R1-M3 (Major) | R1 | Tiered differentiation log for all 179 competing reviews (`competing/differentiation_log.csv`: Tier 1 = 12 differentiated by name incl. R00427/R00535 notices; Tier 2 = 47; Tier 3 = 110; not relevant = 3; not a competing synthesis = 7; dispositions from title/type as captured, basis stated); Difference 11 and Background rewritten to match the log exactly | Loop 1 |
| R1-M6 (Major) | R1 | Project 2 declared difference added as Difference 13 — factual, neutral, no framing commitment, no placeholder citation | Loop 1 |
| R1-m1 | R1 | Conscious-choice sentence opens the Differences section | Loop 1 |
| R1-m2 | R1 | ROBINS-I/JBI scope narrowing declared as Difference 12 | Loop 1 |
| R1-m8 / R7-M5 | R1, R7, R6 | Deposit package assembled at `deposit/` (see below); Data availability updated to present-state, no identifier claimed. Loop 1 found the enumeration broader than the package (R6 graded this the loop's only Major); Loop 2 completed the package (search log, screening/adjudication files, both extraction passes, both RoB passes, full-text files, analysis datasets, team log; 93 files, checksums verified by R1, R6, R7) | Loop 2 |
| R1-m10 | R1 | By reading: language of the 99 awaiting-classification records — 64 English, 2 Chinese (R00968, R02668), 33 not determinable from the files, no language guessed — stated in Results; preprints 22/363 (6.1%) and 1 conference abstract (R02897) stated in Results, with the 22 as the denominator of the unrun preprint sensitivity in Difference 9 | Loop 1 |
| R2-M1 (Major) | R2 | Last uncaveated comparative sentence (Discussion–Agreements, "sits above both") now carries the descriptive-only caveat | Loop 1 |
| R2-M2 (Major) | R2 | SoF Table 1: k=34 low-RoB row added (72,123; crude 6,564, 9.1%); excl-registry row given crude 5,392 (45.2%); recovery crudes added to Results text; setting crudes added in SoF and Results — all recomputed exactly by R2 | Loop 1 |
| R2-M4 (Major) | R2 | SoF setting rows (hospitalised, community) added with crudes and τ² (0.83, 1.63) | Loop 1 |
| R2-M6 (Major) | R2 | Q and df printed for all 12 pools in SoF and Results; τ² completed (ascertainment 0.55/1.53; low-RoB 1.61/1.19; setting 0.83/1.63); small-k τ² caution for the k=9–11 complete-recovery pools added in Results and GRADE footnote (d) | Loop 1 |
| R2-M7 (Major) | R2 | Difference 9 retention rationale added for R01110, overlapping cohorts, derived numerators. Loop 1 Minor residual: the "no participant counted twice" gloss was over-absolute; Loop 2 softened it to linked reports, with same-centre partial overlaps declared unquantified | Loop 2 |
| R2-n2 | R2 | "About 19" replaced by the itemised 14 settled-sheet errors (9 frequency log + 5 recovery log), verified by count | Loop 1 |
| R2-n3 | R2 | Methods hand-check sentence corrected to the full scope (independent recomputation, 36/36 recovery-set rebuild, all 13 crude totals exact, 8/8 traces) | Loop 1 |
| R3-06 (Major) | R3 | Recovery-by-ascertainment caveat placed beside the recovery pools in Results | Loop 1 |
| R3-08 (Major) | R3 | R00129 pregnancy applicability statement added (Results–Description); Discussion returns to special populations beyond the paediatric bound | Loop 1 |
| R3-10 | R3 | Chemesthesis finding (C4631) explicitly separated and interpreted in Results–Q2 | Loop 1 |
| R3-11 | R3 | Photobiomodulation enrolment frame (≥4 weeks) added to Abstract and PLS | Loop 1 |
| R4-05 | R4 | Abstract Background uncited "common complaint" claim reframed to the author's training-and-practice wording, consistent with the body | Loop 1 |
| R4-15 (Major) | R4 | T9 added to the headline best-supported sentences in Abstract and Discussion, with its basis stated. Loop 1 new Minor (PLS out of step) closed in Loop 2 with a qualified PLS sentence (one brain-imaging study) | Loop 2 |
| R5 points | R5 | GRADE apparatus verified undisturbed; new SoF rows' certainty labels consistent. Loop 1 Minors closed in Loop 2: footnote (b) I² range corrected to 88.1–99.7%; PLS prednisolone sentence given its low-certainty qualifier | Loop 2 |
| R7-M3 (Major) | R7 | PLS now names all three co-leading explanations (smell, inflammation, direct infection of taste tissue) | Loop 1 |
| R7-M4 (Major) | R7 | Cochrane Handbook reference completed (full editor list, v6.5 updated August 2024, availability; no DOI exists for the online Handbook — citation follows Cochrane's own form); JBI Manual completed with verified DOI 10.46658/JBIMES-20-01 | Loop 1 |
| R7-m5 | R7 | Appendix C header disclosure verified sufficient (incl. the Phase 6 removal note) | Loop 1 |
| R7-m6 | R7 | Peer-review statement finalised (completed Gates 0–6 + loops); accurate on the filing of this report | Loop 1, confirmed Loop 2 |
| R7-n2 | R7 | R02697 "Aign" verified as the source record's own spelling; retained | Loop 1 |
| R1-N1 (new, Loop 1) | R1 | Pre-step process counts bridged: Results flow (double-363 coincidence flagged), Methods extraction, team disclosure, Figure 1 (389 shown pre-step; main-pool stage count flagged). One residual site (Search methods chasing-sources 363) flagged in Loop 2 and closed in Loop 3 with the parenthetical "(the main-pool count as it stood before the eligibility-consistency step)" | Loop 3 |
| R6 observation (Loop 2) | R6 | R02135 (familial cluster report, n=7, Q2-coded) named in Difference 10 alongside the 12 below-threshold case records carrying Q2 codes | Loop 3 |

## Per-loop outcomes

- **Loop 1** (all 7 reviewers; files `loop1_R1.md`–`loop1_R7.md`): every Gate 5 partial and author-action item in scope verified FIXED except one Major (R6: Data availability vs deposit contents — the same root as R7-M5's residual Minor and R1-N2) and six Minors (R2-M7 clause, R4 PLS/T9, R5 footnote (b), R5 PLS qualifier, R1-N1 bridging, R6 R02464/R02393 disclosure). R3 closed with nothing open.
- **Loop 2** (R1, R2, R4, R5, R6, R7; files `loop2_*.md`): the Major discharged by completing the deposit package; all Minors closed except one single-site R1 Minor (chasing-sources 363) and one non-blocking R6 observation (R02135), both then fixed voluntarily.
- **Loop 3** (R1, R6 spot-verifications; files `loop3_R1.md`, `loop3_R6.md`): both verified FIXED. **No reviewer has any Blocker, Major or Minor open.**

## Deposit package

`deposit/` — assembled, **not deposited** (no persistent identifier exists; none is claimed): `protocol-locked.md`, `team-log.md`, `manuscript/` (final md/pdf/docx, identical to the project copies), `data/` (settled extraction, both extraction passes and pilots, RoB passes + adjudicated file, search log, screening/adjudication files, full-text decision and PRISMA files incl. `prisma_counts_phase4.json`, analysis datasets incl. pool logs/hand-check/GRADE assessment and the Q2 Phase 6 annotation, competing-reviews capture + differentiation log), `code/` (meta-analysis, Q2 build, figure and manuscript build scripts), `README.md`, `checksums.sha256` (93 files, all verified OK by three reviewers).

## Escalations to the author

None. No point survived 3 loops — indeed no Blocker or Major survived Loop 2. The Project 2 framing decision itself remains the author's (declared neutrally as Difference 13); the actual deposit/publish steps remain the author's, per the phase scope.
