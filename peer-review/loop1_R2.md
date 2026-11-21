# Peer-review feedback loop, Loop 1 re-review — Reviewer R2 (biostatistician)

- **Persona:** R2, biostatistician. Scope of this re-review: only my still-open items from Gate 5 (`rereview_R2.md`) — R2-M1 (residual), R2-M2 (residual), R2-M4 (residual), R2-M6 (residual), R2-M7 (residual), R2-n2 (residual), R2-n3 — plus the Phase 6 26-record exclusion check. Verification only; the manuscript was not edited.
- **Date:** 2026-11-21
- **Manuscript re-reviewed:** `manuscript/manuscript.md` (Phase 6 revised version)
- **Method:** every number below was recomputed by me from the source files — the `analysis/synthesis/q1_*_result.json` files, independent re-summing of `q1_frequency_pool.csv` / `q1_frequency_composite.csv` / `q1_recovery_pool.csv` / `q1_recovery_composite.csv`, the two pool build logs, `statistician_handcheck.md`, and an independent re-derivation of the Q2 counts from `extraction/extraction_settled_full.csv` (parsing `pathogenesis_theories` / `pathogenesis_evidence_directness` and excluding the 26 Appendix E Phase 6 records). Manuscript values were not taken on trust.

**Headline verdict: 7 of 8 items FIXED; 1 item (R2-M7) STILL OPEN at Minor level only (a single over-absolute clause in an otherwise present and substantially accurate rationale). No Blocker remains open. No Major remains open.**

---

## Item 1 — R2-M1 residual: uncaveated "sits above both" sentence in Discussion, Agreements — **FIXED**

Discussion, Agreements and disagreements now reads: "its psychophysical subgroup's point estimate (47.4%) sits above both — a descriptive comparison of point estimates only, with no interaction test performed and no subgroup difference established — which is the opposite of what a simple misattribution story would predict for tested taste." The descriptive-only caveat is now attached to the sentence itself, in the exact form Gate 5 asked for. This was the last uncaveated comparative sentence in the manuscript; with it, M1 is fully closed.

## Item 2 — R2-M2 residual: SoF low-risk-of-bias row, excl-registry crude, recovery and setting crudes — **FIXED**

Every number verified against the result JSONs **and** against my own re-summing of the pool CSVs (the two agree exactly):

- **SoF Table 1, low risk of bias row (original k=34 pool) — present and correct:** 34 studies, 72,123 participants, crude 6,564 events = 9.1% (my CSV sum: 6,564/72,123 = 9.10%), pooled 44.4% (33.8 to 55.6), I² 99.7%, tau squared 1.61, Q 13,050.9 (df 33), prediction interval 5.5 to 91.7%. JSON (`q1_freq_lowrob_result.json`): tau² 1.6079, Q 13,050.95, PI 0.0549–0.9166 — all round to the printed values.
- **SoF excl-registry row — crude and tau squared now present and correct:** crude 5,392 events, 45.2% (my CSV sum after removing R00846 from the low-RoB subset: 5,392/11,929 = 45.20%), tau squared 1.19 (JSON 1.1895), Q 1,565.6 (df 32; JSON 1,565.64), pooled 47.3% (37.6 to 57.1) — all correct. The same crude/tau²/Q now also appear in the Results Q1 text.
- **Recovery crudes in Results recovery text — now present and correct:** ≤4 weeks crude 79.3%, 774 events (774/976 = 79.30%); >4–12 weeks crude 85.8%, 1,789 events (1,789/2,085 = 85.80%); >12 weeks crude 84.6%, 856 events (856/1,012 = 84.59%); any recovery >12 weeks crude 92.9%, 302 events (302/325 = 92.92%). All match the JSON crude totals.
- **Setting crudes in SoF and Results — now present and correct:** hospitalised crude 17.2%, 4,324 of 25,150 (my CSV sum: 4,324/25,150 = 17.19%); community crude 32.7%, 6,120 of 18,742 (6,120/18,742 = 32.65%). Both appear in SoF Table 1 and in the Results Q1 paragraph.

M2 is fully closed: crude is now reported alongside pooled for every pool, in text and SoF.

## Item 3 — R2-M4 residual: SoF setting rows with crudes and tau squared — **FIXED**

SoF Table 1 now contains both setting rows, fully reported:

- Hospitalised: 55 studies, 25,150 participants, crude 4,324 events, 17.2%; pooled 26.8% (22.2 to 32.1); I² 98.3%; **tau squared 0.83** (JSON 0.8293); Q 3,228.5 (df 54); PI 5.5 to 69.9% (JSON 0.0548–0.6987). All correct.
- Community: 35 studies, 18,742 participants, crude 6,120 events, 32.7%; pooled 39.6% (29.0 to 51.2); I² 99.0%; **tau squared 1.63** (JSON 1.6302); Q 3,331.1 (df 34); PI 4.5 to 90.2% (JSON 0.0446–0.9017). All correct.

The "report fully everywhere" branch of M4 is now executed; M4 is fully closed.

## Item 4 — R2-M6 residual: Q/df for every pool; tau squared for subgroup pools; small-k caution for k=9–11 recovery pools — **FIXED**

**Q and df — verified pool by pool against the JSONs, in both SoF Table 1 and the Results text:**

| Pool | Manuscript Q (df) | JSON Q (df) | Verdict |
|---|---|---|---|
| Frequency, all | 29,068.7 (136) | 29,068.72 (136) | ✓ |
| Psychophysical | 227.2 (14) | 227.17 (14) | ✓ |
| Self-report | 28,788.9 (121) | 28,788.87 (121) | ✓ |
| Hospitalised | 3,228.5 (54) | 3,228.53 (54) | ✓ |
| Community | 3,331.1 (34) | 3,331.05 (34) | ✓ |
| Low RoB (k=34) | 13,050.9 (33) | 13,050.95 (33) | ✓ |
| Low RoB excl. registry | 1,565.6 (32) | 1,565.64 (32) | ✓ |
| Composite | 4,273.9 (26) | 4,273.91 (26) | ✓ |
| Complete recovery ≤4 wk | 137.6 (9) | 137.62 (9) | ✓ |
| Complete recovery >4–12 wk | 200.3 (10) | 200.28 (10) | ✓ |
| Complete recovery >12 wk | 67.4 (8) | 67.39 (8) | ✓ |
| Any recovery >12 wk | 7.2 (4) | 7.16 (4) | ✓ |

Tau squared is now also printed for the ascertainment pools (psychophysical 0.55, JSON 0.5458; self-report 1.53, JSON 1.5316), the setting pools (item 3 above) and both low-RoB pools (items 2 above) — no pool in SoF Table 1 now lacks tau squared, Q or df.

**Small-k tau-squared caution for the k=9–11 complete-recovery pools — present in both required places:** Results, Q1 recovery ("the complete-recovery pools rest on 9 to 11 studies each, so their tau squared estimates (2.06, 1.67 and 1.52) and prediction intervals are themselves imprecise, the same fragility the five-study any-recovery pool carries explicitly" — the three tau² values verified: JSONs 2.0646, 1.6748, 1.5217) and GRADE footnote (d) ("the tau squared estimates for the complete-recovery pools rest on 9 to 11 studies each and are themselves imprecise, so their prediction intervals carry the same fragility noted for the five-study pool in Table 1"). M6 is fully closed.

## Item 5 — R2-M7 residual: retention rationale in Difference 9 — **STILL OPEN (Minor residual only)**

The rationale is now **present** for all three features, in Difference 9: "Three features whose exclusion sensitivities were not run are nonetheless retained, for stated reasons: the R01110 record enters its pool under the pre-stated latest-timepoint rule and its non-monotonic values are flagged in the Results; the overlapping cohorts are handled one record per cohort per pool, so no participant is counted twice in any pool; and each derived numerator is the unique integer consistent with the printed percentage and denominator, flagged in the pool logs."

Accuracy, checked against the files:

- **R01110 — accurate.** The latest-timepoint rule is pre-stated in Methods, Synthesis ("taking the latest time point within the window"), and Results prints both values (186 of 214 at day 90; 150 of 214 at a mean of 9.5 months) and states the rule places the later value in the >12-week pool.
- **Derived numerators — accurate.** The unique-integer rule is stated identically in Methods, and the hand-check's traced derivations (R01628, R02774, R00415) each confirm uniqueness; derivations are flagged in both pool logs.
- **Overlapping cohorts — rationale present, one clause over-absolute.** For linked reports of the same cohort the claim holds exactly: the frequency pool log documents one-retained/one-excluded handling for every identical-cohort pair, the Boscolo-Rizzo cross-stratum overlap sits in different strata so no pooled estimate double-counts it, and the hand-check (Item 5) confirms no pool contains both members of any documented duplicate pair. But the log also flags **retained same-centre cohorts with overlapping periods** — R00934 / R01085 / R02057 (ESIC Faridabad), R01255 / R02070 (Oswaldo Cruz, overlapping 2020 periods), and R02438 (retained with an overlap flag) — for which partial participant overlap is possible and unquantified. For those, "so no participant is counted twice in any pool" asserts more than the files establish.

*What remains (one clause):* soften the gloss to what the files support, e.g. "the overlapping cohorts are handled one record per cohort per pool, so no linked report of the same cohort contributes twice to any pool" (optionally noting the flagged same-centre partial overlaps). This is a wording-precision fix in a single sentence; the Major-level requirement of M7 — state that the sensitivities were not done **and** why the choices are retained — is met, so I grade the residual **Minor**, not Major.

## Item 6 — R2-n2 residual: itemised settled-sheet error count in the LLM team disclosure — **FIXED**

The disclosure now reads "14 settled-sheet numeric errors itemised in the pool build logs (9 in the frequency pool log, 5 in the recovery pool log)". I counted the itemised entries in both logs: `q1_frequency_pool_log.md`, section "Settled-sheet errors and gaps found against full texts", lists exactly **9** bulleted records (R00193, R01081, R01185, R01900, R01926, R01145, R01878, R01611, R00273); `q1_recovery_pool_log.md`, section "Settled-sheet numbers found WRONG / misleading against the full text", lists exactly **5** numbered items (R00730, R01612, R02358, R02856, R02362). 9 + 5 = 14, as printed. (For the record: the frequency log's nine are headed "errors and gaps" — most are settled-sheet omissions of a printed numerator rather than wrong numbers, and the separate paper-level errors transcribed into the settled sheet are correctly not counted. The disclosure's count is exact against the logs as itemised.)

## Item 7 — R2-n3 residual: Methods hand-check sentence understated the scope — **FIXED**

Methods, Synthesis now states the full scope: "an independent from-scratch implementation reproduced the primary pool and one recovery pool in full (the primary pool agreeing to about 10 to the minus 11), rebuilt the entire recovery analysis set exactly (36 of 36 rows), reproduced all 11 other pooled estimates and the crude totals of all 13 pools exactly, and verified 8 of 8 traced pool rows against the settled extraction sheet or full text; every item agreed." Checked element by element against `statistician_handcheck.md`: Item 1 (primary pool in full; pooled proportion difference 1.2 × 10⁻¹¹) ✓; Item 2 (one recovery pool in full; analysis-set rebuild 36/36) ✓; Item 3 (crude totals of all 13 distinct pools exact, plus full re-runs of all 11 other pooled estimates) ✓; Item 4 (trace check 8/8 verified) ✓. The sentence is now accurate and complete. (The duplicate-JSON archive half of n3 is a deposit-hygiene point, not manuscript text; the hand-check itself flags it as harmless, and I do not hold it open against the manuscript.)

## Item 8 — The 26-record exclusion: no pooled number changed; restated Q2 counts — **FIXED (independently verified)**

**The 26 records** (Appendix E, Phase 6 eligibility-consistency step): C8424, R00592, R00774, R00849, R00939, R01126, R01168, R01290, R01321, R01371, R01482, R01498, R01503, R01599, R01655, R01721, R01848, R01870, R02248, R02280, R02295, R02332, R02346, R02354, R02419, R02488.

- **No pooled number changed — verified, not assumed.** I intersected the 26 IDs with every pool file: `q1_frequency_pool.csv` (137 rows) — overlap **none**; `q1_frequency_composite.csv` (27 rows) — **none**; `q1_recovery_pool.csv` (42 rows) — **none**; `q1_recovery_composite.csv` (35 rows) — **none**. As a further check, none of the 26 appears in `q3_treatment_table.csv` either. Since none of the 26 contributed a row to any pool, no pooled estimate, crude total, Q, tau squared or prediction interval can have changed at this step — consistent with every value I re-derived in items 2–4 matching the pre-existing result JSONs exactly.
- **Restated Q2 counts re-derive from the settled extraction sheet.** Re-parsing `extraction/extraction_settled_full.csv` independently: excluding only C8424 (the original builder's rule) reproduces the original counts exactly — **223 coded studies, 409 assignments, 164 speculative**. Excluding all 26 reproduces the manuscript's restated counts exactly — **214 coded studies, 383 assignments, speculative 157 of 214 = 73.4%** — with the full restated grade distribution (indirect-human 22, direct-human 15, mixed as stated 13, animal 5, in-vitro 2) also matching the Q2 Results text. The difference is exactly the 9 code-carrying records among the 26 (R00592, R01599, R01870, R02248, R02280, R02295, R02332, R02346, R02354), carrying exactly **26 assignments** between them, and their settled designs match Difference 7's breakdown (six narrative/bibliographic reviews, one hypothesis paper — R01599 — and two letters). Every per-theory row of Table 3 (counts and all five directness columns, with animal + in-vitro combined as the table presents them) also re-derives exactly under the restated set, and every direct-human count is unchanged from the original set, as Difference 7 claims.

*Observation (not an open item):* the deposited `q2_synthesis_stats.json` still reports the pre-restatement counts (223 / 409), because `build_q2_synthesis.py` excludes only C8424. The manuscript's restated counts are the correct arithmetic from the same source file, as shown above, but the deposited stats file should be regenerated or annotated at deposit so the archive does not appear to contradict the manuscript.

---

## Overall verdict

- **Blocker remaining open in my remit: NONE.** (The single Blocker, B1, was cleared at Gate 5 and the Phase 6 text introduces no new subgroup-difference claim; the one sentence Loop 1 was asked to check now carries its caveat — item 1.)
- **Major remaining open in my remit: NONE.** R2-M1, R2-M2, R2-M4 and R2-M6 are fully FIXED, with every Phase 6 number I was asked to check reproducing exactly from the JSONs and from independent re-summing of the pool CSVs. R2-M7's Major-level requirement is met; its one residual clause is Minor.
- **Minor remaining open: ONE** — the over-absolute "no participant is counted twice in any pool" gloss in Difference 9 (item 5), fixable by the one-clause softening suggested there.
- **Nits:** R2-n2 and the manuscript half of R2-n3 are FIXED (items 6–7). One non-blocking archive observation on `q2_synthesis_stats.json` is recorded under item 8.

The statistical reporting is now complete and internally consistent at every point I re-derived: all 13 pools carry pooled estimate, CI, crude, I², tau squared, Q/df and prediction interval in SoF Table 1 and the Results, and the Phase 6 eligibility-consistency step demonstrably changed no pooled number.
