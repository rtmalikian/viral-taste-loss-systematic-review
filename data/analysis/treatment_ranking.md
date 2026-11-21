# Most promising treatment — ranking and finding (Phase 4, Task 5)

Criteria (pre-stated in the Phase 4 brief): number and quality of comparative studies,
effect consistency, adverse-event profile, risk of bias, GRADE certainty. All data from
analysis/synthesis/q3_treatment_table.csv, rob_adjudicated_full.csv, grade_assessment.md.

## Ranking

| Rank | Intervention | Comparative evidence | Effect (as printed) | RoB | GRADE (taste) | AEs |
|---|---|---|---|---|---|---|
| 1 | Photobiomodulation / low-level laser | 1 RCT (R00627, n=36) + uncontrolled PBM series (R01311) | Complete taste restoration 17/18 (94.4%) at 1 month vs placebo (placebo complete-restoration count NOT printed; partial restoration 7/18) | RoB 2 Some concerns | LOW | Not reported in any PBM study |
| 2 | Oral prednisolone 40 mg x 10 d (+ olfactory training both arms) | 1 RCT (C9634 COCOS, n=115) | NULL for taste: gustatory TST difference 0.00 (95% CI -1.00 to 1.00), p=0.50; VAS difference 0.1, p=0.80 | RoB 2 Low (best-conducted study in Q3) | LOW | Fully reported (only study with comparative AE + discontinuation data: 3 discontinuations, 2 placebo / 1 prednisolone) |
| 3 | Zinc (oral zinc sulfate) | 1 RCT (R01955, n=105 with dysfunction) + large observational exposure study (R00323) | RCT: NO taste-specific estimate exists (composite gustatory/olfactory duration p<0.001 only; printed 7 vs 18 days are SMELL recovery). Observational: oral zinc associated with LOWER total recovery (OR 0.24, 95% CI 0.1-0.5) — direction conflicts | RoB 2 High; R00323 ROBINS-I Serious | Taste: NO EVIDENCE; composite: VERY LOW | RCT: not reported; R00323: 13.9% of zinc users reported AEs |
| 4 | Smell/taste training + medical bundle | 1 non-randomised comparison (R01388, n=84) + routine-care cohort (R01391, no treatment association) | 88.6% vs 63.9% recovery to normal taste (bundle inseparable; components cannot be attributed) | ROBINS-I Serious | Not rated above very low (uncontrolled confounding by spontaneous recovery) | Not reported |
| 5 | Coffee (caffeine) | 1 comparative study (R02883) | Implausible as printed (~98% vs ~1.3% improvement in every subgroup); per-arm n not reported | ROBINS-I Serious in nearly every domain | — | Not reported |
| 6 | Cerebrolysin | 1 RCT registered (R03352, n=160) | NO RESULTS POSTED — no effect estimate exists | Not assessable (registry record) | NO EVIDENCE | Not reported |
| — | All other interventions (13 studies) | None — single-arm pre-post, case series, case reports, or treatment-use survey (R00334) | Uncontrolled improvement proportions only; spontaneous recovery (85-88% complete recovery by every window in Q1) fully explains the direction of every uncontrolled result | ROBINS-I Serious where assessed | — | Mostly not reported (AE content in only 6/23 Q3 studies overall) |

## FINDING: NO PICK for a follow-on meta-analysis

No treatment has comparative evidence sufficient to justify a Cochrane-style
meta-analysis as Project 2. The reason is structural, not a judgement call:

- Every intervention has AT MOST ONE comparative study reporting a taste outcome.
  A meta-analysis pools >=2 studies; for every candidate, the "meta-analysis" would
  be a restatement of a single trial.
- The single best-conducted trial (prednisolone, RoB 2 Low) found NO effect on taste.
- The only positive randomised taste-specific signal (photobiomodulation) rests on
  one 36-participant trial with Some concerns, an incompletely reported placebo arm,
  and no adverse-event reporting (GRADE LOW).
- Zinc — the intervention with the most studies overall — has NO taste-specific
  effect estimate anywhere, and its two comparative sources point in opposite
  directions.
- Cerebrolysin's trial has posted no results.

If a Project 2 is wanted despite this, the defensible framings are different in kind:
(a) a systematic review WITHOUT meta-analysis of photobiomodulation for post-viral
chemosensory dysfunction (rank 1 above — the only positive randomised taste signal,
and the natural candidate for a future adequately powered trial); or (b) deferring
Project 2 until a second comparative study exists for any candidate. Neither is a
meta-analysis, and this report does not dress either up as one.
