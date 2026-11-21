# Pre-submission peer review — Reviewer R6 (SCEPTIC, standing role)

- **Persona:** Reviewer R6, the Sceptic — adversarial remit: hunt overclaims, untraced numbers, claims stated more strongly than their (mostly GRADE very-low) evidence, silent decisions, abstract-versus-body inconsistencies, SARS-CoV-2-only evidence sounding general, and the C8424 handling.
- **Date:** 2026-11-21
- **Manuscript:** `manuscript/manuscript.md`, Version 1.0, 21 November 2026 — "Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments."
- **Files checked against:** all files in `analysis/synthesis/` (analysis log, all `*_result.json`, Q1 frequency and recovery pool logs, Q2 pathogenesis synthesis + `q2_theory_counts.csv` + `q2_synthesis_stats.json`, Q3 treatment synthesis + `q3_treatment_table.csv`, GRADE assessment, SoF draft, treatment ranking, statistician hand-check) and `team-log.md`.
- **Overall recommendation: DO NOT PASS THE GATE — major revision required before any external step.** The pooled arithmetic is exceptionally clean (see spot checks: 16/16 numeric checks trace exactly, and the independent hand-check reproduces every pool). What fails is not the sums but the framing around them: one headline count the files contradict, one intervention repeatedly credited with a taste result it does not have, an eligibility rule the included set visibly breaks in two places, and a plain-language/practice layer that is calmer than the very-low-certainty evidence underneath it. None of this needs new analysis; all of it needs honest rewording and two eligibility decisions taken openly.

**Counts: Blocker 1 · Major 6 · Minor 9 · Nit 6 · Author-action (C8424 wording) 4.**

---

## Spot checks — manuscript numbers traced to Phase 4 synthesis files (16 checks)

Every check below was read from the synthesis file named, not from the manuscript's own summary of it.

| # | Manuscript claim (location) | Synthesis source | Verdict |
|---|---|---|---|
| 1 | Acute frequency pooled 37.7% (95% CI 32.9–42.7); k=137; N=155,010; crude 38,607 (24.9%); I² 99.5%; tau² 1.44; 95% PI 5.3–86.7% (Abstract, SoF Table 1, Results Q1) | `q1_freq_all_result.json` (pooled 0.37661, CI 0.32893–0.42681, I² 99.532%, tau² 1.4362, PI 0.05299–0.86707) | **PASS — exact** |
| 2 | Psychophysical subgroup 47.4% (37.0–58.1), k=15, N=2,355, I² 93.8%, PI 14.7–82.5% (SoF, Results) | `q1_freq_psychophysical_result.json` (0.47434, CI 0.36974–0.58124, PI 0.14721–0.82508) | **PASS — exact** |
| 3 | Self-report subgroup 36.5% (31.4–41.9), k=122, N=152,655, I² 99.6%, PI 4.7–87.1% (SoF, Results) | `q1_freq_selfreport_result.json` (0.36486, CI 0.31361–0.41935, PI 0.04674–0.87064) | **PASS — exact** |
| 4 | Hospitalised 26.8% (k=55) vs community 39.6% (k=35) (Abstract, Results) | `q1_freq_hospitalised_result.json` (0.26834, k=55); `q1_freq_community_result.json` (0.39569, k=35) | **PASS on numbers** (framing: see Major 3) |
| 5 | Complete recovery ≤4 wk 87.4% (69.7–95.4), k=10, N=976, 774 events, I² 93.5%, PI 17.3–99.6% (SoF, Results) | `q1_rec_complete_le4_result.json` (0.87361, I² 93.46%, PI 0.17298–0.99564) | **PASS — exact** |
| 6 | Complete recovery >4–12 wk 85.2% (70.0–93.5), k=11, N=2,085, 1,789 events, I² 95.0%, PI 21.2–99.2%; >12 wk 87.8% (69.5–95.8), k=9, N=1,012, 856 events, I² 88.1%, PI 23.7–99.4% (SoF, Results) | `q1_rec_complete_4to12_result.json`; `q1_rec_complete_gt12_result.json` | **PASS — exact, both windows** |
| 7 | Any recovery >12 wk 90.3% (80.6–95.4), k=5, N=325, 302 events, I² 44.1%, PI 78.6–95.9%, GRADE low (SoF, Abstract) | `q1_rec_any_gt12_result.json` (0.90291, CI 0.80605–0.95415, I² 44.10%, PI 0.78573–0.95932); `grade_assessment.md` §3.1 (LOW) | **PASS — exact** |
| 8 | Composite smell-or-taste frequency 34.2% (25.3–44.3), k=27, kept separate (Results, Discussion) | `q1_frequency_composite_result.json` (0.34178, CI 0.25286–0.44342, k=27) | **PASS — exact** (I² 99.4% and PI omitted in text: Minor 5) |
| 9 | Low-RoB sensitivity 44.4% (k=34); excluding the 60,194-participant registry R00846 (39% of pool N): overall 38.3% (k=136), low-RoB 47.3% (37.6–57.1), k=33, N=11,929 (Results, SoF) | `q1_freq_lowrob_result.json` (0.44406); `q1_freq_excl_R00846_result.json` (0.38285, k=136); `q1_freq_lowrob_excl_R00846_result.json` (0.47291, CI 0.37646–0.57144, N=11,929); 60,194/155,010 = 38.8% | **PASS — exact** (crude 9.1% of low-RoB pool omitted: Minor 5) |
| 10 | Q2: 223/388 studies coded (57.5%), 409 assignments; speculative 164 (73.5%), indirect-human 23 (10.3%), direct-human 15 (6.7%), mixed 14 (6.3%), animal 5 (2.2%), in-vitro 2 (0.9%); human grade any kind 38 (17.0%); validated gustatory test 31/223 (13.9%), 3/15 direct-human (Results Q2) | `q2_synthesis_stats.json`; `q2_pathogenesis_synthesis.md` §2 | **PASS — exact, all figures** |
| 11 | Table 3 per-theory counts, all 11 rows (e.g. T1 125 = 3/14/5/92/11; T4 64 = 3/4/0/51/6; T5 59 = 4/7/2/41/5; T7 8 = 0/0/0/5/3; T10 2 = 0/0/0/2/0; T11 28 = 5/2/0/16/5) | `q2_theory_counts.csv` (animal + in-vitro columns combined in the manuscript's "Animal or in-vitro" column) | **PASS — all 11 rows reconcile** (but see Major 2: the counts include 6 narrative reviews) |
| 12 | Prednisolone (C9634): TST difference 0.00 (95% CI −1.00 to 1.00), p=0.50; VAS difference 0.1 (−1.00 to 1.3), p=0.80; n=115 (58 vs 57); mild side effects 9/58 (15.5%) vs 5/57 (8.8%); no serious AEs; 3 discontinuations (2 placebo, 1 prednisolone); GRADE low (SoF Table 2, Results Q3, Harms) | `q3_treatment_table.csv` (C9634 row); `q3_treatment_synthesis.md` §1, §10; `grade_assessment.md` §5.1 | **PASS — exact, all figures** |
| 13 | Photobiomodulation (R00627): 17/18 (94.4%) complete restoration at 1 month, p<0.001, placebo complete count not printed; n=36; dose 940 nm, 1 W, 4 J/cm², 6 min vs 810 nm in the paper's abstract conclusion; AEs not reported; GRADE low (Abstract, SoF, Results) | `q3_treatment_table.csv` (R00627 row); `grade_assessment.md` §5.2 (LOW: −1 RoB, −2 imprecision) | **PASS — exact** |
| 14 | Zinc (R01955): n=105; no taste-specific estimate; printed 7 vs 18 days are smell recovery only; composite p<0.001 with no medians printed; observational zinc OR 0.24 (95% CI 0.1–0.5) in the opposite direction (SoF, Results) | `q3_treatment_table.csv` (R01955, R00323 rows, full-text verification notes); `grade_assessment.md` §5.3 (taste-specific: NO EVIDENCE; composite: VERY LOW) | **PASS on the numbers in SoF/Results detail — FAIL on the summary framing** (see Major 1) |
| 15 | Harms: AE content in 6/23, absent in 17/23; R00323 55/483 (11.4%) AEs, 4 (0.8%) cardiac arrhythmia; serious AEs reported in 2/23; discontinuation in 1/23; all GRADE very low (Abstract, SoF, Harms) | `q3_treatment_synthesis.md` §10; `grade_assessment.md` §6 | **PASS — exact** |
| 16 | Process numbers: searches 5,988 = 2,720 + 2,816 (418 preprints) + 452; dedup 2,487 → 3,501 screened; TA agreement 0.890, kappa 0.618, 384 disagreements (128/93/150/13); FT agreement 0.868, kappa 0.347, 54 disagreements; chasing 555 sources, 13,651 candidates, 72 disagreements (39/30/3), +26 included; extraction 11,670 cells, 5,405 differ (46.3%), 1,197 substantive (10.3%), 4,208 wording-only; RoB agreement 75.3%, kappa 0.603, 96 + 3 adjudicated (40/56); final bands low 62 / moderate 214 / high-serious-critical 61 / not assessable 52; virus split 385 SARS-CoV-2 + 4 unspecified = 389; abstract-only 90 + 16 = 106 includes, 96 + 3 = 99 awaiting (Methods, Results flow, Discussion, Disclosure) | `team-log.md` Phases 1–4; `analysis_log.md`; `grade_assessment.md` conventions | **PASS — every figure traces; flow arithmetic closes (2,854 + 634 + 13 = 3,501; 408 + 226 = 634; 408 − 45 = 363; 363 + 26 = 389; 90 + 46 + 96 = 232)** |

**Sceptic's concession, stated once:** I could not find a pooled estimate, confidence interval, prediction interval, GRADE rating, or Q2/Q3 count in the manuscript that misquotes its synthesis file. The statistician hand-check's "all agree" verdict survives my re-checking. Every failure below is a failure of framing, denominators, or disclosure — which, in a review whose entire value is trustworthiness, is not a lesser category.

---

## BLOCKER

**B1 — The headline "389 studies" counts the same paper twice.**
*Location:* Abstract (Main results), Plain language summary, Results (Study flow; Description of studies), Discussion (Summary of main results), Appendix C heading.
*Justification:* The synthesis files state in two places that R01101 and R02974 are the same paper (the Ohla 2022 GCCR study, identical n=1,468 and Table 2) extracted under two record IDs (`analysis_log.md`, Task 3; `q1_recovery_pool_log.md`, duplicate list) — so the included set is 389 *records* but at most 388 unique studies, before C8424 is even considered, and the manuscript nowhere discloses the duplication. No pooled number changes (both records were excluded from every pool on their merits), but a Cochrane-level review cannot submit a PRISMA flow, abstract, and appendix whose first number its own analysis log contradicts; the fix (report records vs studies, de-duplicate the count everywhere) is trivial and must happen pre-submission.

## MAJOR

**M1 — Zinc is repeatedly credited with a taste result it does not have.**
*Location:* Plain language summary ("only three proper randomised trials reported a result for taste"); Results Q3 ("three interventions have any randomised effect estimate"); Discussion, Summary of main results ("3 randomised trials with a taste-relevant estimate"); Abstract, Main results (same "taste-relevant estimate" phrasing).
*Justification:* GRADE and the SoF are explicit that the zinc trial (R01955) contains **no taste-specific estimate at all** — its only between-group result is a composite smell-and/or-taste duration, and its printed 7 vs 18 days are smell recovery only (`grade_assessment.md` §5.3: taste-specific = NO EVIDENCE) — so only two RCTs (prednisolone, photobiomodulation) report any taste outcome, and calling zinc the third "taste-relevant" trial breaks the review's own taste-separability rule exactly where the review elsewhere polices it hardest. The PLS sentence is the worst version: a lay reader is told three trials "reported a result for taste."

**M2 — Six narrative reviews sit inside the Q2 synthesis counts, against the stated eligibility, with no protocol-difference entry.**
*Location:* Results Q2 and Table 3 (223 studies, 409 assignments presented as the pathogenesis evidence base); Eligibility criteria ("narrative reviews… were excluded from synthesis"); Methods, Differences between protocol and review (six differences listed — this is not one of them).
*Justification:* The Q2 synthesis itself flags that 6 of the 223 coded records are narrative/bibliographic reviews the extraction form marks "do not extract as primary" (R00592, R01870, R02248, R02295, R02346, R02354; 16 code assignments, including load-bearing ones for T6 and T7), and states the manuscript "must decide explicitly whether these 6 stay in Q2" (`q2_pathogenesis_synthesis.md` §8, problem 5) — the manuscript instead presents the 223/409 counts clean in Results and discloses the six only in Discussion limitations, after the counts have done their work. Either exclude and recount, or add a seventh declared protocol difference and a Table 3 footnote; the current position — eligibility says excluded, Results say included, Discussion says "no silent position" — is the silent decision this review exists to avoid.

**M3 — Five of the 23 "treatment studies" are below the review's own size threshold for synthesis, undisclosed as a deviation.**
*Location:* Eligibility criteria ("Case reports of fewer than 10… were excluded from synthesis"); Results Q3 and SoF Table 2 (denominator of 23 throughout, including harms "6 of 23").
*Justification:* The Q3 set of 23 includes an n=1 pregabalin case (R01519), an n=1 stellate ganglion block case (R02954), an n=2 turmeric report (R01378), an n=5 protocol series (R02693) and an n=6 block series (R00539) (`q3_treatment_table.csv`) — records the printed eligibility excludes from synthesis — and while the text honestly labels the turmeric and pregabalin reports as cases, it never reconciles their presence in the synthesis denominator with the eligibility rule, so every "of 23" fraction (comparators 8/23, harms 6/23) is built on a set the Methods say should not exist.

**M4 — Subgroup contrasts are stated as findings in the Abstract without the "no established difference" caveat the review itself mandates.**
*Location:* Abstract, Main results ("Frequencies were higher with psychophysical testing (47.4%…) than with self-report (36.5%…), and lower in hospitalised populations (26.8%) than in community populations (39.6%)"); Discussion, Quality of the evidence ("the two subgroups differ by about 11 percentage points").
*Justification:* Protocol difference #4 declares that no interaction test was run and "no subgroup difference is claimed as established," and Results honours that ("presented descriptively… intervals overlap") — the Abstract drops the caveat entirely and the Discussion re-asserts the 47.4 − 36.5 = 10.9-point gap as a fact about measurement, so the two most-read summaries of the review claim exactly what the Methods say cannot be claimed.

**M5 — The practice implications quote a patient-facing frequency range that no estimate supports: "roughly a third to a half."**
*Location:* Authors' conclusions, Implications for practice.
*Justification:* The pooled frequency is 37.7% with 95% CI 32.9–42.7% — a third to roughly two-fifths; "a half" traces to no headline number (only to subgroup/sensitivity *point* estimates of 47.3–47.4% whose own intervals run far wider), so the one sentence in the review a clinician is invited to repeat to a patient silently widens the interval the GRADE very-low evidence actually produced. Give the CI and the prediction interval (which the same paragraph, to its credit, does give) and drop "to a half," or source the range explicitly to the subgroups.

**M6 — The plain language summary strips the recovery findings of both caveats that make them honest.**
*Location:* Plain language summary ("roughly 85 to 88 in every 100 had recovered completely, whether they were checked at a few weeks or after three months").
*Justification:* The body states twice that the three windows rest on *different study sets* and "must not be read as a within-cohort trajectory," and each window's prediction interval is near-scale-wide (17.3–99.6%, 21.2–99.2%, 23.7–99.4%) at very low certainty — the PLS keeps the reassuring 85–88% range, presents it as a time course ("whether checked at a few weeks or after three months"), gives the frequency prediction interval two paragraphs earlier but no recovery uncertainty at all, and so tells lay readers the one version of the result the review's own Results section forbids.

## MINOR

**m1 — "About 19 to 20" is not an acceptable count for the review's own included set.**
*Location:* Results, Study flow; Discussion, Potential biases ("about 19 to 20 further included records carry the same no-primary-data flag").
*Justification:* The exact number of R1(d)-flagged no-primary-data records exists in the settlement log the manuscript cites; a systematic review that reports 5,988/3,501/389 to the unit cannot report a component of its own denominator as "about 19 to 20."

**m2 — Derived numerators are pooled without a Methods statement of the derivation rule.**
*Location:* Methods, Synthesis and GRADE (silent); Discussion, Potential biases (discloses only R00415, 20/23).
*Justification:* Both pool logs show multiple pooled numerators that are unique-integer derivations from rounded printed percentages rather than printed counts (frequency: e.g. R00753 184/194, R01628 54/188, R01037 41/50; recovery: R00415 20/23) under a "unique integer only" rule stated in `q1_frequency_pool_log.md` but nowhere in the manuscript — the reader is told every number was verified against full texts, not that some were reconstructed from percentages.

**m3 — A non-monotonic recovery study inside the >12-week pool is never mentioned.**
*Location:* Results Q1 recovery; SoF Table 1 (>12-week complete recovery row).
*Justification:* R01110 reports 186/214 recovered at day 90 but 150/214 at a mean 9.5 months, and the latest-timepoint rule places the *lower, later* value in the >12-week pool (`analysis_log.md`; `grade_assessment.md` §2.3 calls it a measurement/attrition warning for the whole window) — a reader of the manuscript gets 87.8% with no hint that one of its nine studies shows recovery falling over time.

**m4 — The one-version rule's cost to the taste pool is undisclosed.**
*Location:* Methods, Synthesis ("Linked reports of one cohort were handled one record per cohort per pool"); Results Q1 frequency (silent).
*Justification:* The retained Pieruzzini record R02711 has no taste-separable numerator and sits in the composite list, while its excluded preprint R02729 *does* print taste-specific counts (23/124 hypogeusia) — flagged in `q1_frequency_pool_log.md` as a discrepancy "for the review team," absent from the manuscript, so the taste pool silently forgoes a study the rule, applied the other way, would have admitted.

**m5 — Sensitivity and composite reporting is selective in the direction of tidiness.**
*Location:* Results Q1 frequency.
*Justification:* The low-RoB pool is reported as "44.4%" with no CI and without its crude proportion of 9.1% — the very figure that shows the registry's distortion (`grade_assessment.md` §1); the excl.-registry overall pool (38.3%) is given without its CI (33.6–43.2%, in the result JSON); and the composite pool is given without its I² (99.4%) or prediction interval, although every taste-specific pool carries both.

**m6 — Two Discussion/Q3 characterisations assert numbers they do not print.**
*Location:* Results Q3 (coffee: "printed figures are implausible and whose per-arm numbers are not reported"; stellate ganglion block: "three uncontrolled reports" with no figure anywhere in text or SoF).
*Justification:* The synthesis prints the coffee figures (≈98% vs ≈1.3% improvement in every subgroup, `q3_treatment_synthesis.md` §9) and the block series' 74.4% improvement in 145/195 (R00625) — "implausible" without the figures asks the reader to take the scepticism on trust, in a review that elsewhere prints every number it judges.

**m7 — Nearly a third of the frequency pool vanishes from the population description.**
*Location:* Results Q1 frequency (hospitalised k=55 + community k=35 reported; Abstract likewise).
*Justification:* 55 + 35 = 90 of 137 studies; the remaining 47 (mixed, healthcare-worker and other frames, per the pool log's population coding) are never described, so the setting story the subgroup paragraph tells covers only two-thirds of the evidence it summarises.

**m8 — The Abstract overstates the citation-chasing coverage.**
*Location:* Abstract, Search methods ("Citation chasing was performed on all included studies and all competing reviews").
*Justification:* The chasing sources were the 363 pre-chasing inclusions + 179 competing reviews + 13 flagged records = 555 (`team-log.md`, Phase 2/3); the 26 studies chasing itself added were not then chased, and no single-round limitation is stated — "all included studies" is true of a set that did not yet include a quarter of the chasing yield.

**m9 — The "no most promising treatment" conclusion is honestly derived but its derivation is hidden.**
*Location:* Abstract, Authors' conclusions; Discussion, Summary of main results; Implications for research.
*Justification:* I verified the conclusion against `treatment_ranking.md`: the ranking by pre-stated criteria puts photobiomodulation #1, prednisolone #2, zinc #3, and the NO PICK finding follows structurally (at most one comparative taste study per intervention, so nothing exists to pool) — the manuscript asserts the no-pick without ever reporting that a ranking was performed or what it ordered, so the reader cannot distinguish "ranked, then declined" from "never ranked"; one sentence reporting the rank order would close this. (The conclusion itself: **upheld, not an overclaim.**)

## NITS

**n1 — "73.5% of the grades were speculative" mislabels the unit.**
*Location:* Abstract, Main results. *Justification:* Directness is a study-level grade — 164 of 223 *studies* are speculative (`q2_synthesis_stats.json`); "grades" invites a per-assignment reading the data do not support, and the body (Results Q2) phrases it correctly.

**n2 — The Abstract's empty-cell honesty is selective.**
*Location:* Abstract, Main results. *Justification:* The Abstract foregrounds the empty any-recovery >4–12-week cell but omits the existing single-study any-recovery ≤4-week result (63/81, 77.8%, R02302) that the SoF carries — the gap is showcased, the thin positive is not.

**n3 — "Found 4 studies… and none that mapped" momentarily implies a contrast that does not exist.**
*Location:* Discussion, Overall completeness. *Justification:* The 4 unspecified-virus studies also mapped to no pool; the sentence structure ("found 4… and none that mapped") reads as though mapping failed only for other viruses.

**n4 — The child-data sentence elides the cerebrolysin trial's eligibility.**
*Location:* Results Q3 ("Treatment data in children exist only as one adolescent case series"). *Justification:* R03352 enrolled ages 10–70 (children eligible, no results posted, `q3_treatment_table.csv`) — true for *data*, but the eligibility-versus-data distinction is left for the reader to construct.

**n5 — One Background claim carries no number in a review that numbers everything else.**
*Location:* Background ("SARS-CoV-2 produced taste complaints at a scale no previous virus had generated in the literature"). *Justification:* Unquantified and unsourced in its paragraph; harmless as narrative, conspicuous against the manuscript's own standard.

**n6 — Three descriptive tallies cannot be traced to any Phase 4 synthesis file.**
*Location:* Results, Description of studies (172 journals; publication years 81/109/102/46/22/14/15; RoB tools JBI cross-sectional 153, cohort 131, case-control 30, case series 8, ROBINS-I 11, RoB 2 4, not assessable 52). *Justification:* Both tallies sum correctly to 389 and nothing in the synthesis files contradicts them, but no file in my remit contains them — recorded as a verification gap, not a discrepancy; the deposit should include the table they came from.

---

## Author-action list — C8424 (per standing instruction: the item itself is a pending AUTHOR decision, not an error; wording problems only)

The numeric handling verifies clean: C8424 is absent from every pool, the Q2 counts (its settled Q2 fields are blank), and the Q3 table (`statistician_handcheck.md` Item 5; `q2_synthesis_stats.json`; `q3_treatment_synthesis.md` count note), and 389/388 is stated consistently in Abstract, Methods difference #6, Results flow, and Disclosure. What needs the author's decision, and then harmonisation, is the language:

- **A1 — Plain language summary:** gives "The review included 389 studies" with no mention of the flag or the 388 synthesis denominator — the lay summary is the one place the known-ineligible record is counted without any caveat.
- **A2 — Discussion, Summary of main results:** "included 389 studies and synthesised 388 of them" overstates independently of the decision — the numbers actually synthesised per question are 223 (Q2-coded), 137 (frequency pool) and 23 (Q3); 388 is a post-flag denominator, not a synthesised count, and the sentence should say so.
- **A3 — Version 1.0 carries unresolved decision language into a dated, submission-ready text:** "flagged for the author's decision" appears in the Abstract, Methods, Results, Discussion and Disclosure, and Appendix C lists C8424 among "included studies (389)" although the eligibility rules exclude narrative reviews with no primary data — whichever way the author decides, every count, the PRISMA diagram, and Appendix C must be re-harmonised to the decision before submission; the manuscript cannot go out mid-decision.
- **A4 — The flag is applied to one record while its analogues await the same logic:** ~19–20 further records carry the same no-primary-data flag (see Minor m1) and 6 narrative reviews sit inside the Q2 counts (see Major M2) — the author decision should be taken for the class, not for C8424 alone, or the 389/388 split will read as cleaner than the underlying eligibility position is.

## What the sceptic could NOT fault (for the gate record)

- SARS-CoV-2-only evidence is **not** allowed to sound general in the Abstract, Background, SoF ("All evidence in every row is SARS-CoV-2"), Discussion, or practice implications ("For non-COVID viral illness, the review offers no numbers at all") — this remit item passes, with the sole leaks at M1 (zinc framing) and n3.
- GRADE strength is respected in the body: very-low bodies are never summarised without their prediction intervals in Results, no body is upgraded, the empty >4–12-week any-recovery cell is shown as empty in the SoF rather than filled, and harms non-reporting is reported as a result ("evidence about reporting, not about safety").
- The "no most promising treatment" conclusion is honestly derived (see m9) — the manuscript does not dress a single 36-participant trial up as a recommendation, and the prednisolone null in the best-conducted trial is given equal prominence with the photobiomodulation signal.

**Gate recommendation restated: hold at this gate. Fix B1, M1–M6 (all are wording, counting, or disclosure fixes against files that already exist); take the A1–A4 decisions as one author decision; minors and nits at the author's discretion except m1 and m2, which a Cochrane-level methods section should not ship without.**
