# Pre-submission peer review — R5

- **Persona:** R5 — GRADE methodologist (Gates 0–6 pre-submission peer review)
- **Date:** 2026-11-21
- **Manuscript:** `manuscript/manuscript.md` — "Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments" (v1.0, 21 November 2026)
- **Files checked against:** `analysis/synthesis/grade_assessment.md`, `analysis/synthesis/sof_table_draft.md`, `analysis/synthesis/treatment_ranking.md`
- **Remit:** Summary-of-findings (SoF) construction and placement; fidelity of every GRADE rating and downgrade reason to the assessment file; empty-cell handling; certainty language in abstract / discussion / conclusions; harms rows; the "no most promising treatment" conclusion versus the ranking file.
- **Overall recommendation:** **Major revision — do not pass the SoF/GRADE gate yet.** The ratings themselves are faithful: I found no invented number, no filled empty cell, and no GRADE rating in Tables 1–2 that contradicts `grade_assessment.md` §7. What fails is the supporting apparatus around the ratings — per-row downgrade traceability has been lost relative to the draft SoF, two rated rows carry certainty labels with no corresponding assessment in the assessment file, the harms downgrade summary is materially incomplete, and three places in the abstract/conclusions state (or frame) results more strongly, or for a different outcome, than the rating allows. All are fixable without re-analysis.

**Severity counts:** Blocker 0 · Major 5 · Minor 7 · Nit 3.

**What passes, for the record:** (i) Placement — Tables 1 and 2 sit after the abstract/plain-language summary and before the Background, with a population statement and the explicit note that all evidence is SARS-CoV-2 and abstract-only records contribute to no row; this is the conventional Cochrane position and is correct. (ii) Empty-cell handling — see the verification note under Minor items: the >4–12-week any-recovery cell is empty everywhere it should be. (iii) Every headline rating in §7 of the assessment file (frequency, all three complete-recovery windows, any recovery >12 weeks, time to recovery, prednisolone, photobiomodulation, zinc composite, all three harms outcomes) appears in Tables 1–2 with the same label, and all three "no evidence" treatment cells (prednisolone recovery, zinc taste-specific, cerebrolysin) appear as explicit rows rather than being omitted.

---

## Major issues

### M1 — Per-row downgrade footnotes have been dropped; two rated bodies have no downgrade reasoning anywhere in the manuscript
- **Severity:** Major
- **Location:** SoF, "Downgrade reasons, in brief" paragraph following Table 2 (manuscript, Summary of findings section).
- **Justification:** The draft SoF (`sof_table_draft.md`) carries per-row footnote markers (a–m) tying each row to its specific domains; the manuscript replaces them with one collective paragraph that never mentions the zinc composite row (assessment: RoB −2, indirectness −1, imprecision −1 — §5.3) or time to recovery (RoB −1, inconsistency −1, indirectness −2, imprecision −1 — §4), so two Very-low ratings in Table 1/Table 2 are justified nowhere in the manuscript.

### M2 — The SoF's cross-reference to in-manuscript GRADE reasoning is circular, and the harms downgrade summary omits two of the three recorded domains
- **Severity:** Major
- **Location:** SoF preamble ("Full GRADE reasoning for each row is in the certainty assessments held with the review files and summarised in the Results") and Results, "Certainty of the evidence"; SoF brief paragraph, harms sentence.
- **Justification:** The Results certainty section contains no per-outcome downgrade summary — it points back to Tables 1–2 and the brief paragraph — so the manuscript nowhere delivers the summarised reasoning the SoF promises; and for harms the brief paragraph cites only "documented non-reporting in 17 of 23 studies," omitting the assessment's recorded indirectness −1 and imprecision −1 and the LOW starting point for the cross-intervention harms body (`grade_assessment.md` §6 and Conventions), making the Very-low harms ratings underivable from the manuscript alone.

### M3 — Subgroup and sensitivity rows in Table 1 carry GRADE ratings that have no corresponding assessment in the assessment file
- **Severity:** Major
- **Location:** Table 1, rows 2–4 (frequency by psychophysical testing; by self-report; low-RoB sensitivity excluding the registry), each rated "Very low."
- **Justification:** `grade_assessment.md` §1 rates the frequency body once (FINAL: VERY LOW) and treats the subgroups/sensitivity pool inside the inconsistency discussion; §7 lists a single frequency rating — there is no separate GRADE assessment for any of the three subgroup rows, so Table 1 presents three certainty labels a reader will take as independently assessed when they are inherited, unlabelled, from the main pool (the draft SoF has the same structure, but the assessment file does not support it as written).

### M4 — Abstract states the photobiomodulation result "with no adverse events reported," conflating non-reporting with zero events
- **Severity:** Major
- **Location:** Abstract, Main results: "Photobiomodulation showed a large complete-restoration proportion in one 36-participant trial at some concerns of bias, with no adverse events reported."
- **Justification:** The assessment file records AEs for this trial as **not reported** (§5.2: "AEs not reported"; §6 lists R00627 among the 17/23 with no harms content) and warns that in this body non-reporting "is evidence about reporting, not about safety"; the abstract's phrasing reads naturally as "no adverse events occurred," which the Very-low harms rating forbids — the plain-language summary gets this right ("that trial did not report side effects") and the abstract should match it.

### M5 — Practice implications frame the prednisolone null as evidence about speeding recovery, an outcome the trial never reported
- **Severity:** Major
- **Location:** Authors' conclusions, Implications for practice: "no treatment has been shown in a reliable trial to speed that recovery: the best-conducted trial found no effect of prednisolone on taste scores…"
- **Justification:** The prednisolone trial's Low rating applies to gustatory **scores** at 12 weeks only; for complete/any recovery the same trial is a "No evidence" row in Table 2 and in the assessment file (§5.1: "for the review's critical outcomes… this trial provides no evidence at all"), so citing it under a claim about recovery speed substitutes an important outcome for the critical one the sentence is about.

---

## Minor issues

### m1 — Any-recovery ≤4 weeks is rated Very low in Table 1 on a conditional, unlisted basis
- **Severity:** Minor
- **Location:** Table 1, row "Any taste recovery, 4 weeks or less" (1 study, not pooled, 63/81, Very low).
- **Justification:** The assessment file gives no §7 rating for this outcome — §3.2 says only "if rated it would be VERY LOW" (single study R02302, High RoB) — and the manuscript row omits both the study identifier and its High RoB, so the rating's basis is weaker and less visible than the table implies.

### m2 — Abstract's GRADE summary sentence omits the zinc composite rating
- **Severity:** Minor
- **Location:** Abstract, Main results, final GRADE sentence.
- **Justification:** The sentence enumerates the Very-low bodies (frequency, complete recovery, time to recovery, harms) and the Low bodies, but the zinc composite smell-and/or-taste outcome — rated VERY LOW in the assessment file (§5.3) and in Table 2 — appears in neither list, so the abstract's certainty inventory is incomplete for a row the SoF rates.

### m3 — Abstract's empty-cell sentence is ambiguous against the complete-recovery row directly above it
- **Severity:** Minor
- **Location:** Abstract, Main results: "No study reported any recovery separably in the more-than-4-to-12-week window; that cell is empty."
- **Justification:** Read without the SoF's outcome labels, "any recovery" contradicts the preceding sentence's pooled complete recovery of 85.2% in the same window; the Results text ("Any recovery at more than 4 to 12 weeks has no separable evidence at all") and the research-implications phrasing ("any separable any-recovery estimate") are precise, and the abstract should use that form. **Verification, not a defect:** in the SoF itself, in the Results, in the Discussion and in both conclusions sections, the >4–12-week any-recovery cell is never filled from the neighbouring windows — Table 1 shows it as 0 studies / "No evidence… The cell is empty and was not filled" / Not rated, exactly as `grade_assessment.md` §3.2 requires. Empty-cell handling **passes**.

### m4 — Harms rows in Table 2 are compressed relative to the draft SoF and lose decision-relevant content
- **Severity:** Minor
- **Location:** Table 2, "Any adverse event" row (participants column: "See text").
- **Justification:** The draft SoF itemises in-table the prednisolone trial's three named adverse events, the R00323 drug-specific rates (chloroquine/hydroxychloroquine 22.4%, azithromycin 14.3%, oral zinc 13.9%), the stellate-ganglion-block transient effects (n = 6), the two statement-only assurances and the n = 1 clonazepam note; the manuscript's single compressed row omits all of these (the zinc 13.9% figure appears nowhere in the manuscript), leaving the Very-low harms rating resting on two summary fractions only.

### m5 — "Roughly a third to a half" counselling range in the practice implications is not a figure from the analysis files
- **Severity:** Minor
- **Location:** Authors' conclusions, Implications for practice, first paragraph.
- **Justification:** The pooled frequency is 37.7% (95% CI 32.9 to 42.7) at Very-low certainty with a 5.3–86.7% prediction interval; "a third to a half" (≈33–50%) exceeds the pooled CI's upper bound and matches no single estimate in the assessment file (the nearest is the psychophysical subgroup, 47.4%), so the patient-facing range should be tied to a named estimate or to the CI/PI it is drawn from. The same sentence does carry the prediction interval, which mitigates but does not remove the mismatch.

### m6 — Publication-bias attribution for harms differs from the assessment file
- **Severity:** Minor
- **Location:** SoF brief paragraph: "Publication bias was not formally assessable for any row and was not downgraded except as documented non-reporting of harms."
- **Justification:** In the assessment file the harms non-reporting is charged under risk of bias/reporting bias (§6), with publication bias explicitly "subsumed… not double-counted"; the manuscript's wording re-attributes that downgrade to publication bias, which misstates which domain carries it.

### m7 — Flat "no effect / did not improve" wording for the Low-certainty prednisolone result in abstract and plain-language summary
- **Severity:** Minor
- **Location:** Abstract ("Oral prednisolone showed no effect on gustatory scores in the one low-risk-of-bias trial") and Plain language summary ("A steroid tablet (prednisolone) did not improve taste scores in the best-run trial").
- **Justification:** The rating is LOW (§5.1: single trial, −1 indirectness, −1 imprecision), for which GRADE-concordant phrasing is of the "may result in little to no difference" type; the manuscript's unqualified past-tense statements are defensible for the point estimate (difference 0.00, CI −1.00 to 1.00) but are stronger than the Low label the same abstract assigns two sentences later, and neither sentence carries the certainty qualifier that the recovery statements in the same sections do carry.

---

## Nits

### n1 — Tau-squared values dropped from Table 1 recovery rows
- **Severity:** Nit
- **Location:** Table 1, complete-recovery rows (≤4 weeks; >4–12 weeks; >12 weeks) and any-recovery >12 weeks row.
- **Justification:** The draft SoF reports tau² for every pool (2.06, 1.67, 1.52, 0.00 respectively); the manuscript retains tau² only for the headline frequency row, a small completeness loss in a table whose inconsistency argument rests on dispersion.

### n2 — Photobiomodulation row omits the only placebo-arm figure that is printed
- **Severity:** Nit
- **Location:** Table 2, photobiomodulation row.
- **Justification:** The draft SoF and the assessment file (§5.2) both record placebo partial restoration 7/18 (38.9%); the manuscript row notes only that the placebo complete-restoration count is not printed, discarding the one piece of comparator context the publication does provide.

### n3 — Cerebrolysin row omits the trial registration identifier given in the source files
- **Severity:** Nit
- **Location:** Table 2, cerebrolysin row (the identifier NCT06208540 appears in the Results text but not in the SoF).
- **Justification:** The draft SoF carries "(R03352, NCT06208540)" in the row itself; for a no-results registry row, the registration number is the row's only verifiable anchor and belongs in the table.

---

## Cross-checks that passed (no issue raised)

- **Every §7 rating reproduced:** frequency VL; complete recovery ≤4 / >4–12 / >12 weeks all VL; any recovery >12 weeks LOW; time to recovery VL; prednisolone (scores) LOW; photobiomodulation LOW; zinc taste-specific NO EVIDENCE; zinc composite VL; cerebrolysin NO EVIDENCE; any AEs / serious AEs / discontinuation all VL — all match Tables 1–2 exactly, including the "Not rated as effect evidence" label for the 19 non-randomised intervention studies.
- **Downgrade reasons that are stated are correct:** frequency/complete-recovery (RoB, very serious inconsistency, indirectness, plus imprecision for recovery only — the brief paragraph's wording preserves the assessment's no-imprecision-downgrade for frequency); any recovery >12 weeks "indirectness and imprecision only" (§3.1 exactly); prednisolone indirectness + imprecision with no RoB downgrade (§5.1 exactly); photobiomodulation RoB + very serious imprecision with **no** indirectness downgrade (§5.2 exactly — the manuscript correctly does not charge the standing virus-scope indirectness twice here); "No body of evidence was upgraded" (§Conventions/§5.2 upgrading refusal).
- **Numbers:** every k, N, event count, pooled estimate, CI, I² and prediction interval in Tables 1–2 that I compared matches the draft SoF and the assessment file, including the low-RoB sensitivity row (k = 33, N = 11,929, 47.3%) and the harms fractions (9/58 vs 5/57; 55/483; 4/483 arrhythmia; 3 discontinuations, 2 placebo / 1 prednisolone). No number was invented, and the unprinted placebo complete-restoration count for photobiomodulation is correctly reported as not printed rather than reconstructed.
- **"No most promising treatment" vs the ranking file:** consistent. `treatment_ranking.md` concludes "NO PICK for a follow-on meta-analysis" on the structural ground that every intervention has at most one comparative study reporting a taste outcome; the manuscript's Discussion ("No intervention has more than one comparative study with a taste outcome, which is why this review names no most promising treatment… there is nothing for a follow-on meta-analysis to pool"), its abstract conclusions, and its research implications (a follow-on project "framed accordingly," with photobiomodulation named only as the candidate for an adequately powered **trial** — the ranking file's own framing (a)) all carry that finding faithfully and do not smuggle in a ranking the file refused to make.
- **Harms certainty language in the body text:** the Harms section ("A zero event count in this body is evidence about reporting, not about safety"), the plain-language summary ("this review cannot say which treatments are safe"), and the practice implications ("the safety of every intervention in this set is essentially uncharacterised outside one prednisolone trial") all stay within the assessment file's stated constraint (§6). The abstract photobiomodulation phrase (M4) is the sole exception.
- **Recovery certainty language in the body text:** the Results and Discussion consistently pair the pooled recovery percentages with their different-study-sets warning and near-scale-wide prediction intervals, and the practice implications attach "very low certainty" / "low certainty" to the recovery figures they quote — concordant with the ratings.

## Note to the editor
M1 and M2 are two facets of one repair (restore per-row GRADE footnotes in the SoF, as drafted in `sof_table_draft.md`, and make the Results certainty section summarise them). No Major in this review requires re-analysis — all are presentational or phrasing repairs against files that already contain the correct material.
