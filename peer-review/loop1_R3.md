# Phase 6 Loop 1 Re-review — R3 (ENT / chemosensory clinician)

**Manuscript:** *Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments* — revised manuscript (`manuscript/manuscript.md`, Phase 6 revision)
**Basis:** Original R3 review (`review_R3.md`), Gate 5 re-review (`rereview_R3.md`: R3-06 and R3-08 PARTIALLY FIXED Majors; R3-10 and R3-11 PARTIALLY FIXED Minors), and line-by-line verification against the revised manuscript and, for R00129, `extraction/extraction_settled_full.csv`.
**Scope of this loop:** Only the still-open items assigned for Phase 6 verification (R3-06, R3-08, R3-10, R3-11) plus the Phase 6 count harmonisation in the clinical passages read (Abstract, plain language summary, Q3). No other items were re-litigated.

**Summary verdict: PASS for R3 remit — all four assigned items FIXED; count harmonisation consistent. No Blocker or Major in the R3 remit remains open.**

---

## R3-06 — Major — Recovery-by-ascertainment caveat beside the recovery pools — **FIXED**

Results, "Q1: recovery and time to recovery," now carries the caveat at the point of use, in the paragraph immediately following the pooled recovery estimates:

> "Two cautions attach to these pools beside the estimates themselves. First, recovery was not subgrouped by ascertainment — ascertainment was not carried as a separable variable in the recovery analysis set (Difference 9) — so the recovery pools inherit the measurement caveat of the frequency pools: whether recovery differs between psychophysically tested and self-reported taste is not answered here."

Placement is correct (same Results subsection as the 87.4% / 85.2% / 87.8% complete-recovery pools, not only in Methods Difference 9 or a GRADE footnote, which was the Gate 5 residual). The wording is clinically accurate: it does not claim a direction for any ascertainment effect on recovery, it correctly ties the recovery pools to the same flavour-versus-gustation measurement caveat that motivates the frequency subgroup (psychophysical 47.4% vs self-report 36.5%), and it states plainly that the question is unanswered in this dataset. The residual from Gate 5 is discharged.

## R3-08 — Major — Special populations: Q1/Q2 pregnancy applicability (R00129) and Discussion return — **FIXED (both halves)**

**(1) Q1/Q2 applicability statement for R00129 — present and verified against extraction.**
Results, "Description of studies," now states:

> "One included cohort (R00129) studied women infected during pregnancy (13 cases, with 10 post-pandemic controls); its outcome is a composite smell-and-taste measure, so it contributes no taste-specific data to Q1, and its Q2 mechanism codes rest on that composite outcome under a mixed-as-stated grade, so the review contains no pregnancy-specific taste evidence for any question."

Verified against `extraction/extraction_settled_full.csv`, row R00129 (Fiorani 2024): N_total "infected during pregnancy 13; post-pandemic negative controls 10; total 23"; `taste_measurement` = composite smell-taste; extractor notes "Composite taste-and/or-smell outcome throughout; taste cannot be separated from smell in this record"; `pathogenesis_theories` = T9; T11; `pathogenesis_evidence_directness` = mixed-as-stated. Every element of the manuscript sentence matches the settled extraction — numbers, composite outcome, absence of taste-specific Q1 data, composite basis and mixed-as-stated grade for the Q2 codes, and the resulting "no pregnancy-specific taste evidence for any question" conclusion. The manuscript does not name the T9/T11 codes in this sentence, but it does not need to for an applicability statement, and nothing in it contradicts them.

**(2) Discussion return beyond the paediatric bound — present.**
Discussion, "Overall completeness and applicability," retains the paediatric bound ("the figures should not be read as applying to children") and now continues:

> "Beyond the paediatric bound, applicability to special populations is limited in stated ways: there is no pregnancy-specific taste evidence for any question (the one pregnancy cohort contributed composite data only); treatment data in older adults rest on a single case at age 87; and no treatment data exist for chronic kidney or liver disease, for immunocompromised patients as an included population, or for pre-existing chemosensory disorders."

All five populations named for this check are covered — pregnancy, older adults, CKD/liver disease, immunocompromise, and pre-existing chemosensory disorders — in the Discussion itself, not only in Results Q3. The phrasing for immunocompromise ("as an included population") is also accurate against the Results Q3 account, where immunocompromised patients appear only as exclusions. Both Gate 5 residuals are discharged.

## R3-10 — Minor — Chemesthesis finding (C4631) separated and interpreted — **FIXED**

Results, Q2, T11 paragraph, now reads in full substance:

> "…trigeminal electrophysiology — the last being the set's one chemesthesis finding, prolonged masseter inhibitory reflex latencies, C4631. That finding is a trigeminal (chemesthesis) measure, not a gustatory one: the taxonomy has no chemesthesis category, so it sits in the residual category, is separated out here, and should not be read as evidence about gustatory mechanisms; chemesthesis outcomes were not otherwise separated in the eligibility criteria or synthesised as an outcome."

This discharges the item. The finding is no longer buried as unlabelled "trigeminal electrophysiology": it is explicitly labelled a trigeminal/chemesthesis measure, explicitly denied gustatory-evidence status, and the structural reason it sits in T11 (no chemesthesis category in the taxonomy) and the limits of the handling (not otherwise separated in eligibility, not synthesised) are stated rather than left implicit. That is the clinical interpretation the original item asked for — a reader can no longer count C4631 toward a gustatory mechanism. No further separation is possible without a new taxonomy category and re-coding, which the manuscript now honestly declares it has not done.

## R3-11 — Minor — Photobiomodulation enrolment frame (persistent taste loss ≥4 weeks) in Abstract, PLS and Results Q3 — **FIXED (all three)**

- **Abstract, Main results:** "Photobiomodulation, tested in people with taste loss of at least 4 weeks, showed a large complete-restoration proportion in one 36-participant trial…"
- **Plain language summary, treatments paragraph:** "A light treatment applied to the tongue (photobiomodulation), tested in people whose taste loss had lasted at least 4 weeks, produced a large recovery figure in one small trial of 36 people…"
- **Results, Q3, photobiomodulation paragraph:** "…in people with persistent taste loss of at least 4 weeks, a single session of diode laser to the tongue produced complete taste restoration at one month in 17 of 18 (94.4%)…"

The enrolment frame is present in all three places. The Abstract and PLS use duration phrasing ("of at least 4 weeks" / "had lasted at least 4 weeks") rather than the word "persistent," but the meaning is identical and unambiguous in context: in all three places a reader can now tell that the only positive randomised signal does not address acute-phase taste loss, which was the substance of the item. The Gate 5 residual (frame in Results only) is discharged.

## Phase 6 count harmonisation — clinical passages read (Abstract, PLS, Q3) — **CONSISTENT, no issue**

- **Included total 363:** Abstract ("363 were included… representing 362 unique publications"), plain language summary ("The review included 363 records"), Description of studies ("The 363 included records…"; "Question membership… was Q1 339, Q2 280 and Q3 82 on the provisional mapping"), and Discussion summary ("This review included 363 records (362 unique publications)") all agree.
- **Q3 mapping 82:** Description of studies (Q3 82, provisional mapping) and Results Q3 opening ("Eighty-two included records carried a Q3 mapping on the provisional classification, but only 23 studies actually tested an intervention…") agree, with the mapping-to-synthesis distinction stated in both places.
- **Treatment set 23:** Abstract ("only 23 studies tested an intervention"), plain language summary ("Only 23 studies tested any treatment… reported in only 6 of the 23 treatment studies"), Results Q3 (23 throughout, including harms "6 of the 23"), and Discussion (23) all agree. No stale treatment denominator was found in the passages read.

The 389 figure elsewhere in the manuscript is the pre-exclusion extraction total, explicitly framed as such, and does not appear as an included total in any of the clinical passages checked; it is not an inconsistency in this harmonisation.

---

## Closing statement

- **R3-06: FIXED. R3-08: FIXED (both halves). R3-10: FIXED. R3-11: FIXED (all three locations). Count harmonisation: consistent.**
- **NEW ISSUE: none** arising from the Phase 6 changes in the passages checked.
- **Blocker / Major status in the R3 remit: no Blocker remains open, and no Major remains open.** The two Majors carried as PARTIALLY FIXED at Gate 5 (R3-06, R3-08) are now fully fixed, and the two Minors in this loop (R3-10, R3-11) are also fixed. From the ENT/chemosensory remit, there is nothing left in this loop that blocks submission.
