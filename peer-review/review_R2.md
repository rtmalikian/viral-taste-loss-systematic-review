# Pre-submission peer review — Reviewer R2 (biostatistician)

- **Persona:** R2, biostatistician. Remit: pooling choices and their reporting (logit transform, REML, Hartung–Knapp, Q-based I²), heterogeneity interpretation, prediction intervals, subgroup claims and interaction tests, sensitivity analyses, crude-vs-pooled discrepancies, and internal numerical consistency across abstract, summary of findings (SoF), results, figures and discussion.
- **Date:** 2026-11-21
- **Manuscript reviewed:** `manuscript/manuscript.md` v1.0 (21 November 2026)
- **Files checked against:** all `q1_*_result.json` pool files, `meta_proportions.py`, `analysis_log.md`, `statistician_handcheck.md`, `grade_assessment.md`, `sof_table_draft.md`, `q1_frequency_pool_log.md`, `q1_recovery_pool_log.md`, `q1_frequency_pool.csv`, `q1_recovery_pool.csv`, `q1_recovery_analysis_set.json`, `q2_synthesis_stats.json`. Note: `analysis/analysis_methods_note.md` does not exist; no methods note was available beyond the files above.
- **Overall recommendation: MAJOR REVISION — do not pass the gate yet.** The computations are sound (see verification below); every pooled number I re-derived matches the JSONs. The failures are in *reporting and claim discipline*, concentrated in the abstract, the plain language summary (PLS) and the discussion — exactly the places most readers will read. All are fixable by text edits plus at most one small additional sensitivity pool; no re-analysis of the headline is needed.

## Verification I performed (sample, independently re-derived from the JSONs/CSVs)

All of the following reproduce exactly and are **correctly reported** in the manuscript: headline pool 37.7% (32.9–42.7), k=137, N=155,010, crude 38,607/155,010 = 24.9%, τ² 1.44, I² 99.5% (Q-based), PI 5.3–86.7%; psychophysical 47.4% (37.0–58.1), k=15, N=2,355, I² 93.8%, PI 14.7–82.5%; self-report 36.5% (31.4–41.9), k=122, N=152,655, I² 99.6%, PI 4.7–87.1%; hospitalised 26.8% (22.2–32.1), k=55; community 39.6% (29.0–51.2), k=35; low-RoB excluding R00846 47.3% (37.6–57.1), k=33, N=11,929, I² 98.0%, PI 8.6–89.6%; composite 34.2% (25.3–44.3), k=27; complete recovery ≤4 wk 87.4% (69.7–95.4), k=10, 774/976, I² 93.5%, PI 17.3–99.6%; >4–12 wk 85.2% (70.0–93.5), k=11, 1,789/2,085, I² 95.0%, PI 21.2–99.2%; >12 wk 87.8% (69.5–95.8), k=9, 856/1,012, I² 88.1%, PI 23.7–99.4%; any recovery >12 wk 90.3% (80.6–95.4), k=5, 302/325, I² 44.1%, PI 78.6–95.9%. Figure 2D and Figure 3 captions match these values. The Q2 counts I spot-checked also reconcile (223/388 = 57.5%; 164/223 = 73.5% speculative; Table 3 row sums match `q2_synthesis_stats.json`). The Results section's subgroup paragraph is a model of correct descriptive reporting. The problems below are therefore not computational.

---

## Blocker (1)

**B1 — Abstract claims subgroup differences the protocol forbids claiming.**
*Location:* Abstract, Main results: "Frequencies were **higher** with psychophysical testing (47.4%, 15 studies) than with self-report (36.5%, 122 studies), and **lower** in hospitalised populations (26.8%) than in community populations (39.6%)."
*Justification:* No interaction test exists in any analysis file (confirmed: none in the JSONs, `analysis_log.md`, or `meta_proportions.py` outputs), and the manuscript itself declares in Differences-between-protocol-and-review #4 that subgroup estimates are presented descriptively with "no established subgroup difference" claimed. The abstract — the standalone, most-read text — states both differences as findings, with no confidence intervals for the setting subgroups, no k for hospitalised/community, and no descriptive-only caveat. This directly breaches the locked rule the review set for itself and will be read (and cited) as two established subgroup effects. Fix: report the four estimates neutrally in the abstract (e.g. "pooled estimates by ascertainment were … and …; by setting … and …; no interaction test was performed and no subgroup difference is established") or delete the setting comparison from the abstract.

## Major (7)

**M1 — The same untested-difference language recurs in the PLS and Discussion.**
*Locations:* PLS ("Studies that tested taste with standard taste tests **found higher rates** than studies that simply asked people"); Discussion, Quality of the evidence ("the two subgroups **differ by about 11 percentage points** (47.4% versus 36.5%)"); Discussion, Agreements and disagreements ("its psychophysical subgroup (47.4%) **sits well above both**").
*Justification:* The Results paragraph (Q1 frequency) is compliant — it states the estimates are descriptive, intervals overlap, no difference claimed — but that discipline is dropped in every summary layer. A reader of the PLS or Discussion alone receives claimed differences with no interaction test behind them. Add the descriptive-only caveat at each occurrence, or reword to juxtaposed estimates.

**M2 — Crude-vs-pooled discrepancies are reported for the headline pool only; the largest one in the review is invisible.**
*Locations:* Results, Q1 frequency (sensitivity paragraph); SoF Table 1; Results, Q1 recovery.
*Justification:* Headline gap (crude 24.9% vs pooled 37.7%, 12.8 pp) is reported but never explained — with τ² = 1.44 random-effects weights are near-equal, so the pooled mean is not the participant-weighted frequency; one sentence saying so is needed. Worse, the low-risk-of-bias pool is given as "pooled at 44.4%" with **no CI, no I², no PI and no crude** — the JSON (`q1_freq_lowrob_result.json`) shows crude **9.1%** (6,564/72,123) vs pooled 44.4% (33.8–55.6), a 35.3 pp discrepancy driven by R00846, whose own frequency (1,172/60,194 = **1.9%**) is also never stated ("low recorded frequency" is not a number). The overall-excluding-R00846 pool is likewise given as "38.3% (136 studies)" with no CI (JSON: 33.6–43.2). SoF Table 1 gives no events/crudes for the psychophysical and self-report rows, and no crude percentages for any recovery pool (≤4 wk crude is 79.3% vs pooled 87.4%, an 8.1 pp gap the reader cannot see from "774 events / 976"). Report crude alongside pooled for every pool, in text and SoF, as the analysis log itself does.

**M3 — The continuity correction is never reported, although boundary studies sit in the primary and recovery pools.**
*Location:* Methods, Synthesis and GRADE (and Abstract, Data collection and analysis).
*Justification:* `meta_proportions.py` and the hand-check apply +0.5 only to studies with 0 or n events ("only0"). The primary pool contains C8500 (0/81); the recovery pool file contains five boundary rows that enter analysis sets (e.g. R01166 219/219 in complete >12 wk; R00084 44/44 and R01695 65/65 in any >12 wk; R01710 14/14, R01943 20/20 in complete ≤4 wk). On the logit scale these rows are undefined without the correction, so the correction is part of the estimand, not a detail. Cochrane reporting requires it be stated. The hand-check's all-studies-correction sensitivity (τ² 1.41 vs 1.44, conclusions unchanged) also exists and is nowhere reported.

**M4 — Setting subgroups are incompletely reported and silently non-exhaustive; the SoF omits them while the Abstract headlines them.**
*Locations:* Results, Q1 frequency; SoF Table 1; Abstract.
*Justification:* Hospitalised and community estimates are given as point + CI only — no I², τ² or PI (JSONs: hospitalised I² 98.3%, PI 5.5–69.9%; community I² 99.0%, PI 4.5–90.2%), whereas the ascertainment subgroups in the same paragraph get full heterogeneity statistics. Further, hospitalised (55) + community (35) = 90 of 137 studies; the remaining 47 (mixed 36, healthcare workers 8, other 3, per `q1_frequency_pool.csv`) are never mentioned, so the setting comparison reads as a partition of the pool when it covers two-thirds of it. SoF Table 1 contains no setting rows at all. Either report setting subgroups fully (with the residual categories acknowledged) everywhere they appear, or demote them consistently — the current pattern (headline in abstract, partial in results, absent in SoF) is the worst combination.

**M5 — Abstract misstates photobiomodulation harms as an observed zero.**
*Location:* Abstract, Main results: "Photobiomodulation showed a large complete-restoration proportion in one 36-participant trial at some concerns of bias, **with no adverse events reported**."
*Justification:* In context this reads as "no adverse events occurred/were found". The body text is careful and correct — adverse events were *not reported* in that trial, and "a zero event count in this body is evidence about reporting, not about safety" (Harms). The abstract sentence contradicts the review's own harms conclusion and is a safety-relevant misstatement. Reword to "adverse events were not reported in that trial" (the PLS already gets this right).

**M6 — Small-k fragility of τ² and the prediction intervals is never acknowledged; the one "reassuring" pool is the most fragile.**
*Locations:* Results, Q1 recovery; Discussion, Summary of main results; SoF Table 1.
*Justification:* The any-recovery >12 wk pool (k=5) has τ² = 0.0013 — a boundary estimate from five studies — a PI computed on t with k−2 = 3 df using the Hartung–Knapp SE, and Q = 7.16 on 4 df. The manuscript calls it "the only pool in the review whose prediction interval stays within one interpretation" and GRADE takes no inconsistency downgrade, without anywhere noting that τ² and the PI at k=5 are themselves estimated with very large uncertainty, or that the Q-based I² (44.1%) vs τ²-based I² (≈0.4%) divergence disclosed in Differences #5 is a symptom of exactly this instability. The same caveat applies, in lesser degree, to the recovery pools at k=9–11. No Q, df or p-value is reported for any pool anywhere in the manuscript, and τ² appears in the text/SoF only for the headline pool (the SoF draft's recovery τ² values — 2.06, 1.67, 1.52 — were dropped from the manuscript SoF). Add τ² (and Q/df) per pool and an explicit small-k caution for the k=5 pool.

**M7 — Sensitivity analyses cover only risk of bias / one registry; three documented analysis choices that move pools have no sensitivity analysis.**
*Location:* Results, Q1 frequency and Q1 recovery; Methods, Synthesis.
*Justification:* (i) R01110's non-monotone pair (186/214 at day 90 vs 150/214 at mean 9.5 months) enters the complete >12 wk pool as 150/214 purely by the latest-timepoint rule — GRADE flags the anomaly, but no sensitivity pool with the day-90 value is reported. (ii) The frequency pool retains flagged overlapping cohorts (e.g. R00934/R01085, same hospital; Boscolo-Rizzo cross-stratum overlap, per `q1_frequency_pool_log.md`) with no exclusion sensitivity. (iii) Derived-numerator studies (documented in both pool logs; R00415's 20/23 in the any >12 wk pool is derivation-only per hand-check Item 4) have no exclusion sensitivity — material when one such study is 1 of only 5 in that pool. At minimum, state explicitly that these sensitivities were not done and why the choices are nonetheless retained.

## Minor (8)

**m1 — Prediction-interval construction is unspecified.**
*Location:* Methods, Synthesis. The JSON method string and code use PI = μ ± t(k−2)·√(τ² + SE²_HK) — i.e. the PI is built on the Hartung–Knapp SE (the hand-check confirms the saved PI reproduces only with the HK SE, not the conventional SE). The manuscript says only "95% prediction intervals". State the df and the SE used; a reader cannot otherwise reproduce 5.3–86.7%.

**m2 — Composite stratum heterogeneity is never reported.**
*Location:* Results, Q1 frequency; Discussion, Agreements. Composite pool is quoted as 34.2% (25.3–44.3) with no I²/PI/τ² (JSON: I² 99.4%, PI 5.2–83.1%, τ² 1.15) and no SoF row. If it is worth pooling "for completeness", its heterogeneity is worth one parenthetical.

**m3 — Randomised-trials harms count is ambiguous against the files.**
*Location:* Results, Harms: "absent in 17, **including two of the four randomised studies**". Per `grade_assessment.md` §6, three of the four randomised records contribute no AE content (R00627 not reported; R01955 not reported; R03352 no results posted). If "two" counts only trials with results, say so; as written it disagrees with the GRADE file.

**m4 — Prednisolone harms: "3 adverse events" vs "9 of 58 mild side effects" is unreconciled.**
*Location:* Results, Harms; SoF Table 2. Both numbers appear (3 AEs in the prednisolone group; mild side effects 9/58 vs 5/57) with no statement of how they relate (subset? separate categories as printed?). One clarifying clause, sourced to the trial's reporting, is needed to prevent an apparent internal contradiction.

**m5 — PLS presents prediction-interval endpoints as observed variation.**
*Location:* PLS: "the true figure varied a great deal from study to study, **from about 5 in 100 to about 87 in 100** across settings." Those are the PI endpoints (5.3–86.7%), i.e. a modelled range for a new setting's true proportion, not the observed range of study estimates (which is never reported in the manuscript — itself a gap at I² 99.5%: add the observed range or median/IQR of study proportions in Results). Reword the PLS to "in a new setting, the true figure could plausibly be anywhere from about 5 to about 87 in 100".

**m6 — Practice implications overstate the frequency CI.**
*Location:* Authors' conclusions, Implications for practice: "reported by **roughly a third to a half** of patients". The pooled CI tops at 42.7%; "a half" is supported only by the PI, which is stated separately in the same sentence. Align the gloss with the CI (e.g. "roughly a third to two-fifths, with a far wider range across settings").

**m7 — SoF certainty ratings for subgroup/sensitivity rows have no corresponding GRADE bodies.**
*Location:* SoF Table 1 (psychophysical, self-report and low-RoB-sensitivity rows, each "Very low"). `grade_assessment.md` rates only the overall frequency body (§1); the subgroups are discussed inside it but not separately rated. Either add the per-row assessments to the GRADE file or footnote the SoF rows as carrying the parent body's rating.

**m8 — Subgrouping that raises I² is not remarked on.**
*Location:* Results, Q1 frequency. Self-report I² (99.6%) exceeds the overall I² (99.5%) and community I² is 99.0% — the Discussion's "subgrouping does not resolve" inconsistency is correct, but Results presents the subgroup I² values without noting that one exceeds the parent pool's, which a statistical reader will spot. One clause suffices.

## Nit (3)

**n1 — I² definition lives in the wrong section.** The Q-based definition (Differences #5) is cross-referenced from Synthesis as "as defined above", but a Methods reader encounters the term before the definition's home section is obvious. Repeat the one-line formula in Synthesis.

**n2 — Vague counts in a systematic review.** "About 19 to 20 further included records" (Results, Study flow) / "about 19" (Discussion; team disclosure) for the no-primary-data flag. The settlement log holds an exact count; a Cochrane-level review should print it.

**n3 — Archive hygiene (from hand-check Observation B).** `q1_freq_all_result.json` is numerically identical to `q1_frequency_pool_result.json`, and `q1_freq_composite_all_result.json` to `q1_frequency_composite_result.json`. Tidy or annotate before deposit so the archive does not appear to contain duplicate analyses. Relatedly, Methods understates the hand-check ("primary pool and one recovery pool in full") — the hand-check in fact re-ran all pools; the manuscript may fairly say so.

## What is done well (for the record)

Logit + REML + Hartung–Knapp is an appropriate, protocol-locked method set for single-arm proportions and is independently reproduced to machine precision; the Q-based I² definition is named and its one material divergence (any recovery >12 wk) is disclosed; the pooled mean at I² 99.5% is explicitly framed as "an average across very different settings, not a common frequency" with the PI foregrounded; recovery windows are correctly warned against being read as a within-cohort trajectory in Abstract, Results, Figure 3 caption and Discussion; the empty any-recovery >4–12 wk cell is shown as empty in SoF, Abstract and Results; composite outcomes were never merged into the taste-specific pool; and time-to-recovery was correctly not pooled. None of the issues above requires changing a single pooled number — they require the summary layers to be as disciplined as the analysis already is.
