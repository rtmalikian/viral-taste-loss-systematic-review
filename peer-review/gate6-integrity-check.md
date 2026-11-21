# Gate 6 — Final integrity check (independent, verification only)

**Auditor:** Research-integrity auditor, no prior review of this paper (Gate 6).
**Date:** 21 November 2026.
**Object checked:** `manuscript/manuscript.md` (revision build) and `manuscript/manuscript.pdf` (110 pages, WeasyPrint), against the project's own source files in `analysis/synthesis/`, `fulltext/prisma_counts_phase3.json`, `screening/`, `extraction/`, and `manuscript/peer-review/gate3-editorial-synthesis.md`.
**Method:** Every headline number was re-read from the pool JSONs (not from briefs); PRISMA arithmetic was recomputed; Figure 1 (`manuscript/figures/fig1_prisma.png`) was inspected directly, box by box; full-text searches were run for recommendation language, placeholder text, DOIs, C8424, R01101/R02974, and the contact/ORCID strings; 10 additional numeric claims were spot-checked (Item 7). No manuscript file was edited.

**QA gate re-run (this audit):** `python3 ~/workspace/publications/weekly-series/manuscript_qa_gate.py manuscript/manuscript.pdf` → `PASS manuscript/manuscript.pdf` / `GATE: PASS`.

## Overall verdict: CONFIRMED WITH NOTES

No discrepancy was found in any pooled number, count, GRADE rating, or disclosure checked. The notes are gate-record / author-action items that the manuscript itself carries openly (Item 6), not manuscript errors: no Gate 5 re-review files are present yet, and three author actions (C8424 decision, Project 2 scope, deposit with a persistent identifier) remain open and are stated as open in the text.

---

## Item 1 — Headline numbers vs Phase 4 synthesis — CONFIRMED

Abstract, Plain Language Summary, Summary of Findings (Tables 1–2) and Results all match the source files:

| Claim | Manuscript | Source file | Match |
|---|---|---|---|
| Acute taste dysfunction, pooled | 37.7% (95% CI 32.9–42.7), k=137, N=155,010, crude 38,607 (24.9%), I² 99.5%, PI 5.3–86.7%, tau² 1.44 | `q1_freq_all_result.json`: pooled 0.3766, CI 0.3289–0.4268, k=137, crude 38,607/155,010, I² 99.53%, PI 0.0530–0.8671, tau² 1.4362 | Exact (rounded) |
| Psychophysical subgroup | 47.4% (37.0–58.1), k=15, N=2,355, I² 93.8%, PI 14.7–82.5 | `q1_freq_psychophysical_result.json`: 0.4743, k=15, 1,123/2,355, I² 93.84% | Exact |
| Self-report subgroup | 36.5% (31.4–41.9), k=122, N=152,655, I² 99.6%, PI 4.7–87.1 | `q1_freq_selfreport_result.json`: 0.3649, k=122, 37,484/152,655, I² 99.58% | Exact |
| Hospitalised subgroup | 26.8% (22.2–32.1), k=55 | `q1_freq_hospitalised_result.json`: 0.2683, CI 0.2217–0.3207, k=55, N=25,150 | Exact |
| Community subgroup | 39.6% (29.0–51.2), k=35 | `q1_freq_community_result.json`: 0.3957, CI 0.2902–0.5119, k=35, N=18,742 | Exact |
| Complete recovery ≤4 wk | 87.4% (69.7–95.4), k=10, N=976, I² 93.5%, PI 17.3–99.6 | `q1_rec_complete_le4_result.json`: 0.8736, 774/976, I² 93.46% | Exact |
| Complete recovery >4–12 wk | 85.2% (70.0–93.5), k=11, N=2,085, I² 95.0%, PI 21.2–99.2 | `q1_rec_complete_4to12_result.json`: 0.8524, 1,789/2,085, I² 95.01% | Exact |
| Complete recovery >12 wk | 87.8% (69.5–95.8), k=9, N=1,012, I² 88.1%, PI 23.7–99.4 | `q1_rec_complete_gt12_result.json`: 0.8783, 856/1,012, I² 88.13% | Exact |
| Any recovery >12 wk | 90.3% (80.6–95.4), k=5, N=325, I² 44.1%, PI 78.6–95.9, tau² 0.0013 flagged as a fragile boundary estimate | `q1_rec_any_gt12_result.json`: 0.9029, 302/325, I² 44.10%, tau² 0.00135 | Exact (manuscript is more precise than `sof_table_draft.md`'s rounded tau² 0.00; no conflict) |
| Any recovery >4–12 wk | Stated in Abstract, SoF Table 1 and Results as **no separable evidence / empty cell, not rated, not filled** | `grade_assessment.md` §3.2 and `analysis_log.md`: no such row exists in the recovery analysis set; no `q1_rec_any_4to12` JSON exists | Exact |
| Any recovery ≤4 wk | Single study only, R02302, 63/81 = 77.8% at day 20, not pooled | `grade_assessment.md` §3.2; arithmetic 63/81 = 77.8% | Exact |

Subgroup wording is descriptive throughout: the Abstract states "no interaction test was performed and no subgroup difference is established", and Results/Discussion repeat that qualification.

**GRADE ratings — CONFIRMED against `grade_assessment.md` §7 summary table, row by row:** frequency Very low; complete recovery at all three windows Very low; any recovery >12 weeks Low; any recovery >4–12 weeks No evidence / not rated; time to recovery Very low; prednisolone (gustatory score) Low, with "No evidence" for its recovery proportions; photobiomodulation Low; zinc taste-specific No evidence; zinc composite Very low; cerebrolysin No evidence; harms (any AE, serious AE, discontinuation) Very low. SoF subgroup rows (psychophysical, self-report, low-RoB sensitivity) are explicitly labelled "Very low (parent body rating; not separately assessed)", which matches the GRADE assessor's framing. No body is upgraded in either document, and the manuscript's GRADE footnotes reproduce the downgrade pattern (RoB, inconsistency, indirectness, imprecision; PBM RoB −1 / imprecision −2; zinc composite RoB −2) in `grade_assessment.md` and `sof_table_draft.md`.

## Item 2 — Internal count consistency — CONFIRMED

- **389 records / 388 unique publications:** Abstract, Results (Study flow), Discussion, LLM team disclosure and Figure 1 all state 389 records representing 388 unique publications, with the duplicate pair disclosed by name and ID everywhere it matters: "one paper (Ohla 2022) appears under two record IDs (R01101, R02974), and neither record contributed data to any pool." `fulltext/final_included.csv` has 389 rows; `prisma_counts_phase3.json` gives main pool 363 + chasing 26 = 389.
- **Synthesis denominator 388 with C8424 flagged, NOT silently resolved:** Abstract ("excluded from all synthesis counts (denominator 388)"), Methods Difference 6 ("Its inclusion was not silently changed. It is flagged for the author's decision"), Results, Discussion, team disclosure, and Figure 1's final box ("C8424 … is FLAG-AUTHOR pending the author's decision and is excluded from all synthesis counts") all carry the flag in the same terms. `q2_synthesis_stats.json` independently shows the same handling: total rows 389, C8424 excluded, analysis denominator 388. No location in the manuscript treats C8424 as decided.
- **26 flagged no-primary-data records:** Stated exactly in Results ("In total, 26 included records (C8424 among them)… none of the 26 contributes data to any pool or to the treatment table, and the other 25 sit inside the synthesis denominator"), in Discussion ("26 flagged in total, counted exactly from the settled design fields"), and in Figure 1's final box.
- **PRISMA flow — text vs Figure 1 vs source file:** All three agree, and the arithmetic closes at every step (verified by recomputation and by direct inspection of `fig1_prisma.png`): retrieved 5,988 (PubMed 2,720 + Europe PMC 2,816 incl. 418 preprints + ClinicalTrials.gov 452); duplicates removed 2,487 → screened 3,501; excluded at title/abstract 2,854, flagged for author 13, proceed to full text 634 (541 + 93 taste-ambiguous); retrieved 408 / not retrieved 226; assessed 408, excluded at full text 45 → main-pool included 363; abstract-only stratum 232 = 90 include + 46 exclude + 96 awaiting; citation chasing from 555 sources (363 + 179 + 13), 16,615 references + 13,867 citations, 13,651 candidates, 26 included, chasing abstract-only 19 = 16 + 3; total 389. The Abstract's Limitations figures also reconcile: 245 reports never retrieved = 226 main-pool + 19 chasing; 99 awaiting classification = 96 + 3. Appendix E's 61 excluded reports reconcile as 45 main-pool full-text + 7 retrieved author-flagged + 9 chasing full-text exclusions.

## Item 3 — No clinical or medication recommendation — CONFIRMED

Full-text search for recommendation / prescribing language found no recommendation for or against any intervention anywhere. The operative statements are the opposite: Abstract ("The treatment literature cannot support a recommendation for or against any intervention"), Plain Language Summary ("This review makes no recommendation for or against any treatment"), and Authors' conclusions ("This review makes no recommendation for or against any treatment for viral taste dysfunction, and nothing in it should be read as one"). Every dose printed is framed as a studied/reported dose — prednisolone 40 mg/day for 10 days, zinc sulfate 220 mg twice daily, photobiomodulation 940 nm / 1 W / 4 J/cm² / 6 minutes — and Table 2 carries the explicit disclaimer: "Doses in Table 2 are the studied doses as printed in the trials. They are reported descriptively and are not recommended doses." The one "should not" addressed to clinicians is a caution against extrapolating COVID-19 frequencies to influenza, not a treatment recommendation.

## Item 4 — No placeholder text, no invented DOI, no placeholder follow-on citation; Project 2 worded neutrally — CONFIRMED

- No `TODO`/`TBD`/`XXX`/lorem or placeholder markers exist in the manuscript. The single occurrence of the word "placeholder" is the manuscript's own statement that none appears (Implications for research, final paragraph).
- No DOI is claimed for this review, its deposit, or any follow-on project. Data availability states: "No persistent identifier exists for them yet; none is claimed." Registration states no PROSPERO number exists and none is claimed. The 19 DOIs in the methods/prior-synthesis reference list are syntactically complete, paired with PMIDs, and correspond to the comparator records discussed; the ~402 unique DOIs in Appendix C are per-study identifiers as recorded in the review files (the `10.1097/…00000000000…` forms are those publishers' standard article-number DOIs, not placeholders). No DOI was found in a placeholder pattern.
- **Follow-on (Project 2) wording is neutral and matches its source:** the manuscript never names a "Project 2" intervention pick. It reports the finding from `analysis/synthesis/treatment_ranking.md` — "no intervention has the comparative evidence a follow-on meta-analysis would need" / "there is nothing for a follow-on meta-analysis to pool" — reports the pre-stated ranking transparently (photobiomodulation first, prednisolone second, zinc third) while stating "The ranking does not change the conclusion", and closes: "a follow-on treatment-evidence project arising from this review is planned; its form follows the finding reported here … and it will be framed accordingly when the author settles its scope. Its citation of this review will use this review's verified deposit citation once live; no placeholder citation appears in this manuscript."

## Item 5 — Contact rule — CONFIRMED

- Title block (line 5): "**Raphael Malikian, rtmalikian@gmail.com** — Palmdale, CA, USA. ORCID 0009-0008-4326-4205".
- Declarations, Correspondence: "**Correspondence.** Raphael Malikian, rtmalikian@gmail.com, Palmdale, CA, USA. ORCID 0009-0008-4326-4205."
Both carry name, email and ORCID exactly as required. This is also consistent with the project QA gate's contact/ORCID scan printing PASS on the revision PDF.

## Item 6 — Gate record coherence — CONFIRMED WITH NOTES

**Files present in `manuscript/peer-review/` at the time of this audit:** `gate0-gate1.md`, `review_R1.md`–`review_R7.md` (the seven Gate 3 reviews), and `gate3-editorial-synthesis.md`. **No `rereview_R*.md` files are present** — Gate 5 re-reviews had not arrived in the folder when this check ran, so Gate 5 closure cannot be confirmed from the record yet. That is a record-completeness note, not a manuscript discrepancy.

**The 8 consolidated Blockers from Gate 3 — each addressed in the revised manuscript:**

| Blocker | Where addressed in the revision |
|---|---|
| C-B1 Duplicate paper R01101 = R02974 undisclosed | Disclosed in Abstract, Results (Study flow), Discussion (Potential biases), LLM team disclosure, and Figure 1; counts restated as 389 records / 388 unique publications throughout (Item 2) |
| C-B2 Subgroup differences stated as findings, no interaction test | Subgroups now presented descriptively everywhere; Abstract and Results state no interaction test was performed and no subgroup difference is established; Methods Difference 4 declares the protocol divergence |
| C-B3 T4 misattribution claims overstate the cited evidence | Q2 Results rewritten with the evidence as cited: two purpose-built objective-testing studies (R02414; C11888, normal strips in 86.7–96.7% per quality) plus one self-differentiation survey (C4367) explicitly labelled "not a psychophysical test", and the counterweight stated (23.5% objectively hypogeusic in R00232, graded mixed); Discussion notes the psychophysical subgroup sitting *above* self-report is "the opposite of what a simple misattribution story predicts" |
| C-B4 "No other virus" claim absolute / unqualified | Qualified everywhere it appears: "in the searches run and the records retrieved and classified, no included study of influenza or any other named virus mapped to any pool" (Abstract, Background, Discussion), with the search-net limit (generic virus terms in title/abstract) declared |
| C-B5 Six narrative reviews inside Q2 counts, undeclared | Declared as Methods Difference 7, naming all six IDs (R00592, R01870, R02248, R02295, R02346, R02354; 16 assignments), with the primary-evidence sensitivity count (217 studies, 393 assignments, speculative 160/217 = 73.7%) and the statement that no direct-human count and no theory verdict changes — independently consistent with `q2_synthesis_stats.json` |
| C-B6 Comparator citations unresolvable from the manuscript | Background now differentiates the comparator syntheses by record ID, and the References section resolves them with full citations, DOIs and PMIDs (R02006, R02155, R02160, R02195, R02254, R02303, R02327, R00428 with its retraction R00427 and expression of concern R00535, R00924, R00152, R01505) |
| C-B7 "Ready strings printed in Appendix B" false for 4 of 5 databases | Appendix B now prints a ready string for each of Embase, Scopus, Web of Science, CINAHL and CENTRAL, each marked "String prepared, run pending access", under a header stating none was searched and the review must not imply otherwise |
| C-B8 No characteristics-of-included / -excluded tables | Appendix D (characteristics, 389 records) and Appendix E (excluded at full text, 61 reports with reasons) are now in the manuscript and as deposited files (`appendix_D_characteristics.md`, 389 data rows; `appendix_E_excluded.md`, 61 data rows), and Results points to both |

**Major themes:** likewise addressed in the revision as far as this audit sampled them — protocol divergences for subgroups/sensitivities declared (Differences 4 and 9, listing the analyses not run); the three pre-specified Important outcomes accounted for in Results (quality of life: no separable outcome; persistent dysfunction ≥12 weeks: 189 records, non-poolable; smell–taste discordance: narrative via T4); abstract-only stratum mapped by question in Results; special-population reporting expanded in Q3 Results with an explicit age-applicability bound in Discussion; crude-vs-pooled reported for the main and low-RoB pools including the low-RoB crude 9.1%; continuity-correction convention stated in Methods; setting subgroups shown as non-exhaustive (90 of 137; remaining 47 itemised); PBM harms wording corrected ("adverse events were not reported in that trial"); tau² printed per pool in Table 1 with the small-k fragility of the any-recovery >12-week PI stated; T5 composite-outcome caveat and T4 category caveat stated; practice-conclusion wording corrected to "roughly a third to two-fifths" (matching the 37.7% pooled estimate, replacing the Gate 3-flagged "a third to a half"); GRADE footnotes restored under the SoF tables; prednisolone "3 adverse events" vs "9 of 58 mild side effects" reconciled as separate categories as printed in the trial; LLM disclosure extended to the chasing full-text stage and abstract-only adjudication.

**Author-action items — explicitly carried, not silently resolved (as Gate 3 required):**
1. **C8424 decision** — still pending the author's decision; flagged identically in Abstract, Methods, Results, Discussion, team disclosure and Figure 1 (Item 2).
2. **Project 2 framing decision** — carried as the author's to settle; manuscript wording is neutral (Item 4).
3. **Data/code deposit with a persistent identifier** — manuscript states the files "will be deposited in the review's public repository with the manuscript" and that no persistent identifier exists yet and none is claimed. Open author action, honestly stated.

## Item 7 — Spot-checks (10 additional numeric claims, different sections) — ALL CONFIRMED

1. **Search/screening (Methods):** TA screening agreement 0.890, kappa 0.618, 384 disagreements over 3,501 records — `screening/screening_stats.json`: agreement 0.8903, kappa 0.6184, disagreements 384, n=3,501. Exact.
2. **Full-text screening (Methods):** agreement 0.868, kappa 0.347, 54 disagreements over 408 reports — `fulltext/ft_stats.json`: agreement 0.8676, kappa 0.3468, disagreements 54, retrieved_screened 408. Exact.
3. **Extraction (Methods):** two passes over 389 records, 11,670 cells, 5,405 differing (46.3%) — `extraction/full_discrepancy_report.json`: studies 389, total cells 11,670, cells differing 5,405, rate 0.4632. Exact (the 1,197 substantive / 4,208 wording-only split is from the settlement log, consistent with the manuscript's percentages).
4. **Composite stratum (Q1 Results):** smell-or-taste composite pooled 34.2% (25.3–44.3), k=27, I² 99.4%, tau² 1.15, PI 5.2–83.1, kept separate from the taste-specific pool — `q1_frequency_composite_result.json`: 0.3418, CI 0.2529–0.4434, k=27, I² 99.39%, tau² 1.1459, PI 0.0521–0.8307. Exact.
5. **Low-RoB sensitivity (Q1 Results):** 34 low-RoB studies pooled 44.4% (33.8–55.6), crude 9.1% (6,564/72,123); excluding the registry, 47.3% (37.6–57.1), k=33, N=11,929 — `q1_freq_lowrob_result.json` (0.4441, crude 6,564/72,123 = 9.10%) and `q1_freq_lowrob_excl_R00846_result.json` (0.4729, k=33, N=11,929). Exact.
6. **Registry R00846 (Q1 Results):** 60,194 participants, own frequency 1.9% (1,172/60,194), "39% of the entire pool's participants" — recoverable arithmetically from the two JSONs above (72,123 − 11,929 = 60,194; 6,564 − 5,392 = 1,172; 1,172/60,194 = 1.95%; 60,194/155,010 = 38.8%). Exact.
7. **Q2 totals and Table 3 (Pathogenesis Results):** 223 coded studies, 409 assignments, speculative 164/223 = 73.5%, direct-human 15, indirect-human 23, mixed 14, animal 5, in-vitro 2 — `q2_synthesis_stats.json` matches on every count, and its per-theory grades reproduce every row of Table 3 (e.g. T1 125 tagged, 3 direct; T5 59, 4 direct; T11 28, 5 direct; T7 8, 0 direct/indirect/animal/in-vitro; T10 2, both speculative). Exact.
8. **Prednisolone trial (Q3 Results / Table 2):** Taste Strip Test difference 0.00 (95% CI −1.00 to 1.00), p=0.50; taste VAS difference 0.1 (−1.00 to 1.3), p=0.80; 115 randomised (58 vs 57) — `q3_treatment_synthesis.md` §1 and `grade_assessment.md` §5.1 print identical values. Exact.
9. **Harms (Harms Results / Table 2):** prednisolone trial mild side effects 9/58 (15.5%) vs 5/57 (8.8%) on placebo, no serious AEs, 3 discontinuations (2 placebo, 1 prednisolone); observational R00323 55/483 (11.4%) with AEs, 4 subjects (0.8%) cardiac arrhythmia — `grade_assessment.md` §6 prints the same counts; arithmetic verified (9/58 = 15.5%, 5/57 = 8.8%, 55/483 = 11.4%, 4/483 = 0.8%). Exact.
10. **Stellate ganglion block (Q3 Results):** largest series n=195, improvement in 145/195 = 74.4% — `q3_treatment_synthesis.md`: R00625 case series n=195, "74.4% (n=145) reported improvement in taste after right-sided SGB"; arithmetic 145/195 = 74.4%. Exact.

Supporting recomputations that also closed: publication-year tally in Description of studies sums to 389 (81+109+102+46+22+14+15); RoB band tally sums to 389 (low 62 + moderate 214 + high/serious/critical 61 + not assessable 52); the statistician's independent hand-check (`statistician_handcheck.md`) reproduces the primary pool to ~10⁻¹¹ and the >4–12-week complete-recovery pool exactly, consistent with the manuscript's claim about it.

---

## Summary of notes (none is a manuscript discrepancy)

1. Gate 5 re-reviews (`rereview_R*.md`) are **not yet present** in `manuscript/peer-review/`; Gate 5 closure is therefore not evidenced in the record at audit time.
2. Three Gate 3 author actions remain open and are carried openly in the manuscript: the C8424 decision, the Project 2 scope/framing decision, and the data/code deposit with a persistent identifier (none claimed until live).

**Verdict: CONFIRMED WITH NOTES** — the revised manuscript's numbers, counts, GRADE ratings, disclosures and wording match the project's source files at every point checked; the open items are the pending Gate 5 record and the three declared author actions.
