# Peer-review feedback loop, Loop 2 verification — R5 (GRADE methodologist)

- **Persona:** R5 — GRADE methodologist (Phase 6 verification loop, Loop 2)
- **Date:** 2026-11-21
- **Manuscript checked:** `manuscript/manuscript.md` — "Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments"
- **Remit for this loop:** Verify ONLY the two Minor items left open in `loop1_R5.md`:
  1. GRADE footnote (b) I² range stale at 99.6% against the new k=34 row's 99.7%;
  2. PLS prednisolone sentence lacking a certainty qualifier (residual half of Gate 2 Minor m7).
  No other sections were re-reviewed. The manuscript was not edited.

**Overall verdict: both items are FIXED / CLOSED. No Blocker, no Major, and no Minor remains open in my remit.**

---

## Point 1 — Footnote (b) I² range: **FIXED / CLOSED**

**Current wording (GRADE footnotes, footnote (b)):**

> "Inconsistency (-2 for the pooled proportions; -1 for time to recovery): I squared 88.1 to 99.7% across the proportion pools, and prediction intervals spanning most of the scale; subgroups do not resolve it. Any recovery beyond 12 weeks is the exception (I squared 44.1%, prediction interval 78.6 to 95.9%; no inconsistency downgrade)."

**Verification against SoF Table 1 as printed:**

All I² values printed in Table 1 proportion rows:

| Table 1 row | I² as printed |
|---|---|
| Acute taste dysfunction frequency (k=137) | 99.5% |
| Frequency, psychophysical subgroup (k=15) | 93.8% |
| Frequency, self-report subgroup (k=122) | 99.6% |
| Frequency, hospitalised subgroup (k=55) | 98.3% |
| Frequency, community subgroup (k=35) | 99.0% |
| Frequency, low risk of bias sensitivity (k=34) | **99.7%** |
| Frequency, low RoB sensitivity excl. registry (k=33) | 98.0% |
| Complete recovery, ≤4 weeks (k=10) | 93.5% |
| Complete recovery, >4–12 weeks (k=11) | 95.0% |
| Complete recovery, >12 weeks (k=9) | **88.1%** |
| Any recovery, >12 weeks (k=5) | 44.1% — exception row, see below |
| Any recovery, >4–12 weeks | No evidence — no pool, no I² |
| Any recovery, ≤4 weeks | Single study, not pooled — no I² |
| Time to recovery | Narrative only — no I² |

- **Maximum:** 99.7% is now the correct maximum. It is the low-risk-of-bias sensitivity row (k=34), the row whose addition in Phase 6 created the Loop 1 discrepancy. No proportion pool in Table 1 exceeds it; the next highest is the self-report subgroup at 99.6%, which was the pre-Phase-6 maximum. The footnote's upper bound now includes the new row.
- **Minimum and scoping:** 88.1% remains the correct lower bound *for the scope the footnote has always used* — the downgraded proportion pools to which the −2 inconsistency downgrade in footnote (b) applies. The complete-recovery >12-week pool (88.1%) is the lowest I² among those pools. The only lower I² in Table 1 is the any-recovery >12-week pool at 44.1%, and that pool is — as before — explicitly carved out in the same footnote as "the exception" with "no inconsistency downgrade", consistent with its Low (not Very low) rating in Table 1 and with the GRADE record. The footnote does not claim 88.1% is the minimum across *all* pools including the exception; its range and its exception clause together describe the table exactly. Scoping is unchanged from Loop 1; only the stale upper bound was corrected.
- **No rating implication:** The correction is presentational. 99.7% supports the same −2 inconsistency downgrade as 99.6% did; no rating, downgrade, or certainty statement moves.

**Verdict:** The one-word repair specified in Loop 1 has been made exactly, and the range "88.1 to 99.7%" is now accurate against Table 1 as printed. **Closed.**

## Point 2 — PLS prednisolone certainty qualifier (Gate 2 m7 residual): **FIXED / CLOSED**

**Current wording (Plain language summary):**

> "A steroid tablet (prednisolone) did not improve taste scores in the best-run trial, though the certainty in that result is low."

**Verification:**

- **Qualifier present and correctly calibrated.** The added clause — "though the certainty in that result is low" — now qualifies the previously bare past-tense claim. "Low" is the correct GRADE level for this body: Table 2 rates prednisolone gustatory function Low, footnote (e) records the −1 indirectness and −1 imprecision downgrades producing that rating, and the Abstract's parallel sentence carries the same "(low certainty)" qualification. The PLS, Abstract, Table 2 and footnote (e) are now consistent for the same result, which was the substance of the Loop 1 residual.
- **No distortion of the plain-language register.** The qualifier is written in the PLS's own plain register, not imported GRADE jargon: it uses the same "certainty … is very low / is low" construction the PLS already uses for the recovery outcomes ("the certainty in them is very low"), it is a short subordinate clause that leaves the sentence's factual core ("did not improve taste scores in the best-run trial") intact and readable, and it neither overstates the caveat (it does not say the result is unreliable or might be wrong in a specified direction) nor understates it. It discharges m7 without turning a lay summary sentence into a methods sentence.
- **No meaning change beyond the intended qualification.** The underlying result is unchanged (single low-risk-of-bias trial; gustatory score difference 0.00 as printed in Table 2). The sentence still reports no improvement; it now reports it at the certainty the review actually holds.

**Verdict:** The m7 residual is discharged. **Closed.**

---

## Summary for the editor

| Loop 1 open item | Loop 2 verdict |
|---|---|
| Minor 1 — Footnote (b) range "88.1 to 99.6%" stale against k=34 row's 99.7% | **FIXED / CLOSED** — now reads "88.1 to 99.7%"; maximum verified against Table 1; lower bound and exception scoping (any-recovery 44.1% pool carved out, no inconsistency downgrade) confirmed unchanged and correct |
| Minor 2 — PLS prednisolone sentence without certainty qualifier (Gate 2 m7, PLS half) | **FIXED / CLOSED** — now reads "…did not improve taste scores in the best-run trial, though the certainty in that result is low"; qualifier correctly calibrated to the Low rating and in keeping with the plain-language register |

**Open-items statement: nothing remains open in my remit.** No Blocker, no Major, and no Minor is outstanding from R5. Both Loop 2 changes are verified as printed in `manuscript/manuscript.md`, and neither required or implies any re-analysis or re-rating.
