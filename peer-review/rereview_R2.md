# Gate 5 re-review — Reviewer R2 (biostatistician)

- **Persona:** R2, biostatistician. Re-review of the revised manuscript against my Gate 2 review (`review_R2.md`) only. Verification only; no manuscript file was edited, and no new issues are raised except clear regressions (none found).
- **Date:** 2026-11-21
- **Manuscript re-reviewed:** `manuscript/manuscript.md` (revised version, 21 November 2026)
- **Editorial synthesis checked:** `gate3-editorial-synthesis.md` (my items are C-B2 in part, and the R2-M1 to R2-M7 / R2-m1 to R2-m8 themes)

**Summary verdict: BLOCKER CLEARED — revision substantially successful. Of my 7 Majors, 2 are fully FIXED, 5 are PARTIALLY FIXED, and 0 are NOT FIXED; all 8 Minors are FIXED. No remaining text anywhere claims an established subgroup difference, and no regression was found. The five partials are reporting-completeness gaps (SoF setting rows and some crudes, Q/df, τ² for subgroup pools, and the retention rationale in M7), not claim errors — they should be closed or explicitly waived before Gate 6, but none of them re-opens the Blocker.**

---

## Blocker

### B1 — Abstract claims subgroup differences the protocol forbids claiming — **FIXED**
Abstract, Main results now reports the four estimates neutrally with study counts, including the setting counts previously missing: "Pooled estimates by ascertainment were 47.4% for psychophysical testing (15 studies) and 36.5% for self-report (122 studies), and by setting 26.8% in hospitalised (55 studies) and 39.6% in community (35 studies) populations; no interaction test was performed and no subgroup difference is established." The former "higher … than" / "lower … than" finding language is gone.

## Majors

### M1 — Same untested-difference language in PLS and Discussion — **PARTIALLY FIXED**
Two of the three cited locations are fully repaired: the PLS now says the two figures are "reported side by side, not as a proven difference" and that "the review did not run the test that would show whether that gap is real"; Discussion, Quality of the evidence now reads "sit about 11 percentage points apart (47.4% versus 36.5%; descriptive only, with no interaction test)", and Overall completeness likewise tags its comparison "(… descriptive only)". Practice implications contain no subgroup claim at all. The residual is Discussion, Agreements and disagreements: the softened wording "its psychophysical subgroup's point estimate (47.4%) sits above both" still appears with no descriptive-only caveat in that paragraph — it is point-estimate language, not an established-difference claim, but it is the one uncaveated comparative sentence left.

### M2 — Crude-vs-pooled discrepancies reported for the headline pool only — **PARTIALLY FIXED**
The core gaps are closed. Results now explains the headline gap ("the pooled value is a mean of study-level proportions, while the crude 24.9% is participant-weighted and dominated by the largest cohorts", at τ² = 1.44 near-equal weights); the low-risk-of-bias pool is now given in full in Results as "44.4% (33.8 to 55.6), against a crude proportion of 9.1% (6,564 of 72,123) — the widest crude-to-pooled gap in the review", with R00846's own frequency now stated numerically ("1.9%, 1,172 of 60,194"); and the overall-excluding-R00846 pool now carries its CI ("38.3% (33.6 to 43.2; 136 studies)"). SoF Table 1 now gives crudes for the headline, psychophysical (1,123 events, 47.7%), self-report (37,484 events, 24.6%) and every recovery row (79.3%, 85.8%, 84.6%, 92.9%). Remaining: the SoF low-risk-of-bias row has been redefined as the excluding-registry pool (33 studies, 11,929 participants) and gives no crude or events for it, the original 44.4% pool has no SoF row, recovery crudes appear in the SoF but not in the Results recovery text, and the setting pools have no crudes anywhere (see M4).

### M3 — Continuity correction never reported — **FIXED**
Methods, Synthesis and GRADE now states it exactly: "A continuity correction of 0.5 was applied only to studies with zero or complete events, which are undefined on the logit scale without it; the hand-check's sensitivity applying the correction to all studies did not change any conclusion." Both the "only boundary studies" rule and the previously unreported all-studies-correction sensitivity are now in the manuscript. (The Abstract's analysis sentence still does not mention the correction, but the Methods statement satisfies the reporting requirement I raised.)

### M4 — Setting subgroups incompletely reported and silently non-exhaustive; absent from SoF — **PARTIALLY FIXED**
Results now reports the setting pools with heterogeneity and prediction intervals — hospitalised "26.8% (22.2 to 32.1; 55 studies; I squared 98.3%; prediction interval 5.5 to 69.9%)" and community "39.6% (29.0 to 51.2; 35 studies; I squared 99.0%; prediction interval 4.5 to 90.2%)" — and explicitly acknowledges non-exhaustiveness: "The two setting subgroups cover 90 of the 137 studies; the remaining 47 (mixed sampling frames 36, healthcare workers 8, other 3) sit in neither." The Abstract now gives their k values in neutral form (B1). Remaining: τ² is still not given for either setting pool, and SoF Table 1 still contains no setting rows at all, so the "report fully everywhere or demote consistently" choice is still not fully executed.

### M5 — Abstract misstates photobiomodulation harms as an observed zero — **FIXED**
Abstract, Main results now reads, verbatim in the form requested: "Photobiomodulation showed a large complete-restoration proportion in one 36-participant trial at some concerns of bias; adverse events were not reported in that trial." This now agrees with the Harms section's "a zero event count in this body is evidence about reporting, not about safety".

### M6 — Small-k fragility of τ² and prediction intervals never acknowledged — **PARTIALLY FIXED**
The specific flag the editorial round asked for is fully in place in two locations. SoF Table 1, any-recovery >12 weeks row: "tau squared 0.0013 (a boundary estimate from five studies; the prediction interval rests on 3 degrees of freedom and is itself fragile)"; Results, Q1 recovery repeats it: "its tau squared is a boundary estimate (0.0013) from five studies and its prediction interval rests on 3 degrees of freedom, so the narrow interval is itself fragile." τ² has also been restored to the SoF for the headline pool (1.44) and all complete-recovery pools (2.06, 1.67, 1.52), and the Q-based vs τ²-based I² divergence for this pool (44.1% vs about 0.4%) remains disclosed in Differences #5. Remaining: no Q, df or p-value is reported for any pool anywhere in the revised manuscript, τ² is still missing for the ascertainment, setting and low-risk-of-bias subgroup pools, and there is no equivalent small-k τ² caution for the k = 9–11 recovery pools (GRADE footnote (d) notes their size and interval width only).

### M7 — Three documented analysis choices with no sensitivity analysis — **PARTIALLY FIXED**
The "not done" half is now stated explicitly and completely. Differences #9 lists among the analyses not run: "nor exclusion sensitivities for the R01110 timepoint choice, the retained overlapping cohorts, or the derived-numerator studies", alongside the other unrun locked sensitivities. The underlying rules are also visible (latest-timepoint rule in Methods/Results, with R01110's 186/214 vs 150/214 pair now printed in Results; the uniquely-determined-integer derivation rule in Methods; R00415's derived 20/23 numerator flagged in Discussion, Potential biases). Remaining: no sentence states *why* these choices are nonetheless retained — Difference #9 declares the omission without a retention rationale, and for the overlapping cohorts no reason is given anywhere.

## Minors — spot-check: 8 fixed, 0 not fixed

- **m1 Prediction-interval construction — FIXED.** Methods now specifies it in full: "95% prediction intervals constructed as the pooled estimate plus or minus t on k minus 2 degrees of freedom times the square root of (tau squared plus the Hartung-Knapp variance)" — df and HK SE both stated, as requested.
- **m2 Composite stratum heterogeneity — FIXED.** Results now gives the composite pool as "34.2% (25.3 to 44.3; I squared 99.4%; tau squared 1.15; prediction interval 5.2 to 83.1%)". (It still has no SoF row, but the heterogeneity reporting I asked for is present.)
- **m3 Randomised-trials harms count — FIXED.** Harms now reads "absent in 17, including three of the four randomised records (the photobiomodulation and zinc trials reported none; the cerebrolysin trial has posted no results)", consistent with the GRADE footnote (h) wording "including three of the four randomised records".
- **m4 Prednisolone "3 adverse events" vs "9 of 58" — FIXED.** Harms now reconciles them in one sentence: the trial "reports, as separate categories in the paper, 3 named adverse events in the prednisolone group (…) and mild side effects in 9 of 58 (15.5%) versus 5 of 57 (8.8%) on placebo".
- **m5 PLS prediction-interval endpoints as observed variation — FIXED.** PLS now uses the modelled framing verbatim in substance: "in a new setting the true figure could plausibly be anywhere from about 5 in 100 to about 87 in 100"; and Results now also supplies the observed distribution I noted as missing: "Individual study proportions ran from 0.0% to 94.8% (median 39.8%; interquartile range 24.0 to 58.8%)".
- **m6 Practice implications overstate the frequency CI — FIXED.** Implications for practice now reads "reported by roughly a third to two-fifths of patients in the study populations (pooled 37.7%, 95% CI 32.9 to 42.7)", with the wide prediction interval stated separately — aligned with the CI, as requested.
- **m7 SoF subgroup certainty ratings without GRADE bodies — FIXED.** By the labelling route I offered: the psychophysical, self-report and low-risk-of-bias SoF rows now each read "Very low (parent body rating; not separately assessed)".
- **m8 Subgrouping that raises I² not remarked on — FIXED.** Results now states it in one clause: "Subgrouping does not reduce heterogeneity: the self-report subgroup's I squared exceeds the whole pool's."

## Nits — brief spot-check (not part of the Minor tally)

- **n1 I² definition in the wrong section — FIXED.** The Q-based definition is now repeated in Methods, Synthesis itself: "I squared (Q-based: (Q minus degrees of freedom) divided by Q)", in addition to Differences #5.
- **n2 Vague counts — PARTIALLY FIXED.** The cited no-primary-data flag is now exact everywhere it appears ("26 included records (C8424 among them) carry a settled-design flag…"; "26 flagged in total, counted exactly from the settled design fields"). A separate vague count survives in the LLM team disclosure ("about 19 settled-sheet numeric errors").
- **n3 Archive hygiene / hand-check scope — NOT FIXED (in the manuscript).** Methods still understates the hand-check as "the primary pool and one recovery pool in full"; the duplicate-JSON archive point cannot be verified from the manuscript text and was not checked in this re-review.

## Special-attention checks requested for this re-review

- **I² definition in Methods:** present, in Synthesis, in formula form (see n1 / M6).
- **Prediction-interval construction:** present, with t on k−2 df and the Hartung–Knapp variance (see m1).
- **Continuity-correction wording:** present, "only to studies with zero or complete events", plus the all-studies sensitivity (see M3).
- **Subgroup claims descriptive-only, no interaction test implied:** Abstract — yes, explicit caveat; PLS — yes, explicit caveat; Results — yes, explicit ("no subgroup difference is claimed as established"); Discussion — caveated in Quality of the evidence and Overall completeness, one uncaveated point-estimate sentence remains in Agreements (M1); practice implications — no subgroup claim made. No location claims or implies an established difference.
- **Crude-vs-pooled explanations:** headline explained, low-RoB gap now fully numerated; residual SoF/text gaps as in M2.
- **τ² boundary-estimate flag, any-recovery >12 week pool:** present in both SoF Table 1 and Results, with the 3-df fragility of its prediction interval (see M6).

## Regressions

None found. No pooled number checked in this re-review differs from the values verified at Gate 2, and no summary layer has acquired a new unsupported claim.
