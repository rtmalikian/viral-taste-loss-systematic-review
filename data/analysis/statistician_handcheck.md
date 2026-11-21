# Statistician hand-check — Q1 synthesis (independent recomputation)

**Role:** independent statistician hand-checker, Cochrane-level systematic review of loss of
taste in viral infections (Raphael Malikian).
**Date:** 2026-11-21.
**Independence protocol:** all numbers below were computed with my own implementation
(Python/NumPy/SciPy, written from first principles for this check) **before** I opened
`meta_proportions.py` or any `*_result.json`. R/Rscript is not installed on this machine,
so metafor was unavailable; the independent implementation is a from-scratch
logit-proportion random-effects meta-analysis: logit transform, REML tau² by direct
maximisation of the profile restricted log-likelihood, Hartung–Knapp CI (t, k−1 df),
Cochran's Q, I², and 95% prediction interval (t, k−2 df). Continuity correction
+0.5 applied only to studies with 0 or n events (the standard "only0" convention) —
chosen independently; a sensitivity run with the correction applied to all studies is
reported under Item 1. After computing, I read the saved JSONs and `meta_proportions.py`
for the comparison; the original code uses the same standard conventions via a different
code path (grid + golden-section on tau²; mine: grid + bounded optimisation on log tau²),
so the agreement below is a genuine independent-code confirmation, not a re-run.

**Headline: every item AGREES. No discrepancies found.** Two reporting observations
(not errors) are flagged at the end for the coordinator/manuscript.

---

## Item 1 — Primary frequency pool (q1_frequency_pool.csv, k=137) — **AGREE**

| Statistic | Saved (result JSON / as quoted) | My independent recomputation | Difference |
|---|---|---|---|
| k | 137 | 137 | 0 |
| Crude events / total | 38,607 / 155,010 | 38,607 / 155,010 | exact |
| Crude proportion | 0.24906 (24.9%) | 0.24906 | exact |
| Pooled proportion | 0.377 (0.37661229886) | 0.37661229885 | 1.2 × 10⁻¹¹ |
| 95% CI (Hartung–Knapp) | 0.329–0.427 (0.328929–0.426811) | 0.328929–0.426811 | ≤ 1.7 × 10⁻⁸ |
| tau² (logit, REML) | 1.44 (1.43618408) | 1.43618409 | 1.0 × 10⁻⁸ |
| I² | 99.5% (99.53214%) | 99.53214% | < 10⁻⁹ |
| Q (df = 136) | 29,068.716054113036 | 29,068.716054113036 | identical to all printed digits |
| 95% prediction interval | 0.053–0.867 (0.052988–0.867075) | 0.052988–0.867075 | ≤ 4.3 × 10⁻¹⁰ |

Details of my run: mu (logit) = −0.503952; SE (conventional) = 0.104223; SE (HK) = 0.105726;
HK factor q = 1.0290. One boundary study required the continuity correction: C8500 (0/81).
The saved PI is reproduced only when the PI uses the Hartung–Knapp SE (with the conventional
SE my PI is 0.053001–0.867045); the saved code indeed uses the HK SE — consistent and defensible.

*Sensitivity (my code, correction applied to ALL studies instead of boundary-only):*
pooled 0.3774, CI 0.3302–0.4271, tau² 1.4099, I² 99.53%, PI 0.0543–0.8649. Conclusions are
unchanged; only tau² moves at the second decimal (1.41 vs 1.44). The boundary-only
convention the pipeline used is the better-standard one and is what reproduces the saved tau².

*Definitional note:* the reported I² is the Q-based statistic, I² = (Q − df)/Q. A tau²-based
I² (tau²/(tau² + typical within-study variance)) would give 99.37% here — immaterial for this
pool, but see Observation A for a pool where the two definitions diverge sharply.

## Item 2 — Recovery pool: complete recovery >4–12 weeks — **AGREE**

**Analysis-set rebuild (independent):** `q1_recovery_pool.csv` holds 12 rows for
complete × >4–12 weeks covering 11 studies. The only study with two rows in the window is
R01612 (1 month: 252/269; 2 months: 264/269); the latest-timepoint rule selects **2 months
(264/269)**. My full rebuild of the entire recovery analysis set (one row per study ×
outcome × window, latest timepoint parsed from the timepoint strings) reproduces
`q1_recovery_analysis_set.json` **exactly — 36/36 rows identical**, including all six
multi-row groups (R01612 ×2 windows, R01710, R01943, R00987, R01110).

The 11 studies in my rebuilt >4–12-week complete-recovery set (identical to the saved set):
C8932 (635/701), R00987 (79/129), R01166 (183/219), R01478 (168/172), R01612 (264/269),
R01628 (40/54), R01739 (162/209), R01742 (42/53), R01856 (148/153), R01878 (27/39),
R01978 (41/87).

| Statistic | Saved | Mine | Difference |
|---|---|---|---|
| k | 11 | 11 | 0 |
| Crude events / total | 1,789 / 2,085 | 1,789 / 2,085 | exact |
| Pooled proportion | 0.852 (0.85239010859) | 0.85239010859 | 1.1 × 10⁻¹² |
| 95% CI (HK) | 0.700–0.935 (0.699768–0.934671) | 0.699768–0.934671 | ≤ 1.3 × 10⁻¹² |
| tau² (REML) | 1.67478871 | 1.67478871 | 3.8 × 10⁻¹⁰ |
| I² | 95.0% (95.00693%) | 95.00693% | identical |
| Q (df = 10) | 200.27763535806793 | 200.27763535806787 | 6 × 10⁻¹⁴ |
| 95% PI | 0.211557–0.992018 | 0.211557–0.992018 | ≤ 5 × 10⁻¹¹ |

No boundary (0/n) studies occur in this pool, so the continuity-correction convention is
irrelevant here. (A tau²-based I² would be 96.88% vs the reported Q-based 95.01% — same
definitional note as Item 1.)

## Item 3 — Crude totals of every saved pool — **AGREE (all 13 distinct pools, exact)**

Each pool was re-summed from the CSVs using the pool definitions in the CSV columns
(psychophysical = ascertainment "psychophysical test"; self-report = "self-report";
hospitalised = population "hospitalised"; community = population "non-hospitalised-community";
Low-RoB = rob "Low"; recovery pools = my rebuilt analysis set). Every saved
`crude_events`/`crude_total` (and k) matches my sums **exactly**:

| Pool (result file) | k saved / mine | Events saved / mine | Total saved / mine |
|---|---|---|---|
| Frequency overall (q1_frequency_pool / q1_freq_all) | 137 / 137 | 38,607 / 38,607 | 155,010 / 155,010 |
| Psychophysical | 15 / 15 | 1,123 / 1,123 | 2,355 / 2,355 |
| Self-report | 122 / 122 | 37,484 / 37,484 | 152,655 / 152,655 |
| Hospitalised | 55 / 55 | 4,324 / 4,324 | 25,150 / 25,150 |
| Community (non-hospitalised) | 35 / 35 | 6,120 / 6,120 | 18,742 / 18,742 |
| Low RoB only | 34 / 34 | 6,564 / 6,564 | 72,123 / 72,123 |
| Overall excl. R00846 | 136 / 136 | 37,435 / 37,435 | 94,816 / 94,816 |
| Low RoB excl. R00846 | 33 / 33 | 5,392 / 5,392 | 11,929 / 11,929 |
| Composite smell-or-taste (q1_frequency_composite / _all) | 27 / 27 | 7,571 / 7,571 | 34,402 / 34,402 |
| Recovery complete ≤4 wk | 10 / 10 | 774 / 774 | 976 / 976 |
| Recovery complete >4–12 wk | 11 / 11 | 1,789 / 1,789 | 2,085 / 2,085 |
| Recovery complete >12 wk | 9 / 9 | 856 / 856 | 1,012 / 1,012 |
| Recovery any >12 wk | 5 / 5 | 302 / 302 | 325 / 325 |

As a bonus, I also re-ran my full meta-analysis on all eight frequency subgroup/composite
pools and the other three recovery pools: every pooled proportion agrees with the saved
value to ≤ 2.5 × 10⁻¹⁰, every Q is identical to machine precision, and tau²/I²/CIs agree
at all reported digits (e.g. psychophysical 0.474339; self-report 0.364856; hospitalised
0.268341; community 0.395693; Low-RoB 0.444058; excl-R00846 0.382853; Low-RoB-excl 0.472913;
composite 0.341783; recovery ≤4 wk 0.873608, I² 93.46%; recovery >12 wk 0.878279, I² 88.13%;
any >12 wk 0.902907, I² 44.10%, tau² 0.001347).

Housekeeping note: `q1_freq_all_result.json` is numerically identical to
`q1_frequency_pool_result.json`, and `q1_freq_composite_all_result.json` to
`q1_frequency_composite_result.json` (same pool saved under two labels). Not an error —
flagged only so nobody cites them as two different analyses.

## Item 4 — Trace check: 8 randomly sampled pool rows — **AGREE (8/8 verified)**

Sampling: seeded RNG (seed 20261121), 4 rows from each Q1 dataset
(frequency rows #44, #71, #89, #134; recovery rows #4, #5, #21, #38 in file order).
Each was checked against `extraction/extraction_settled_full.csv`, and against
`fulltexts_text/<id>.txt` where the settled sheet did not itself carry the number.

1. **R01085 — frequency 64/316 — VERIFIED (direct, settled sheet).** Settled
   `taste_prevalence_as_printed` prints "20.3 per cent (64/316) of COVID-19-positive
   patients"; N_total confirms the 316 COVID-positive denominator (of 909 ILI patients).
   Pool correctly uses the COVID-positive denominator.
2. **R01628 — frequency 54/188 — VERIFIED (derived, settled sheet).** Settled prints taste
   disturbance in 28.7% of 188 with subtype shares hypogeusia 20.2% / ageusia 6.9% /
   parageusia 1.6%; these map to unique integers 38 + 13 + 3 = 54 (and 0.287 × 188 = 53.96).
   Subtype denominators 13/38/3 are corroborated by the settled recovery field's follow-up
   percentages. Pool value correct.
3. **R01916 — frequency 34/141 — VERIFIED (direct, settled sheet).** Settled prints
   "Dysgeusia was reported by 34 patients (24.1%)"; N_total = 141; 34/141 = 24.1%.
4. **R02774 — frequency 72/305 — VERIFIED (derived, full text).** The settled sheet carries
   no single gustatory numerator (only olfactory-gustatory dysfunction 103/305 plus category
   percentages of the 103). Full text confirms the printed categories; the six
   gustatory-involving categories (isolated hypogeusia 16.5%, isolated ageusia 13.6%,
   hyposmia+hypogeusia 16.5%, hyposmia+ageusia 13.6%, anosmia+dysgeusia 7.8%,
   anosmia+ageusia 1.9% of 103) map to unique integers 17 + 14 + 17 + 14 + 8 + 2 = **72**;
   the smell-only categories (25.2%, 6.8%) are correctly excluded. The builder's derivation
   is documented verbatim in `q1_frequency_pool_log.md`. Pool value correct.
5. **R01612 — recovery complete ≤4 wk, 2 weeks, 198/269 — VERIFIED (settled sheet).**
   Settled recovery bands: 85 recovered by week 1 + 113 in week 2 = 198 cumulative; the
   settled sheet also prints directly "198 (73.6%) recovered (taste) after 2 weeks".
   Denominator 269 = participants with taste loss (269/574, settled prevalence field).
6. **R01710 — recovery complete ≤4 wk, day 10, 10/14 — VERIFIED (direct, settled sheet).**
   Settled prints "complete recovery in 10 (71.42%) by day 10" for the isolated-ageusia
   subgroup (14/200). Note: this row sits in the pool CSV but is correctly **not** in the
   analysis set — the day-14 row (14/14) is the selected latest timepoint.
7. **R01856 — recovery complete >4–12 wk, by 8 weeks, 148/153 — VERIFIED (direct,
   settled sheet).** Settled prints "148 (96.73%) patients had complete recovery of taste
   (GD)" with GD denominator 153; printed recovery intervals sum to 148 (15 + 11 + 119 + 3).
8. **R00415 — recovery any >12 wk, 20/23 — VERIFIED (derived, settled + full text;
   lowest-certainty trace).** No integer numerator is printed anywhere: the settled sheet
   and the full-text body both print "87% of GD patients reported that they had recovered"
   at the follow-up interview (median 41 weeks), and GD prevalence 57.5% of 40 → n = 23.
   0.87 × 23 = 20.01 → 20; the mapping is unique (20/23 = 87.0%; 21/23 = 91.3%). The paper's
   Tables 1–2 were not readable in the scraped full text, so the numerator rests on this
   derivation, which is documented in the pool CSV note. Inputs are full-text-confirmed;
   pool value accepted, with the derivation-dependence noted here for the record.

## Item 5 — Sanity: excluded record and duplicate pairs — **AGREE**

- **C8424:** absent from every dataset checked — frequency pool, frequency composite,
  recovery pool, and recovery composite. ✓
- **R02711 / R02729 (known duplicate pair):** neither appears in the taste-specific
  frequency pool (137 unique record IDs, no duplicates) or the recovery pool. R02711
  appears **only** in the composite list (as the protocol intends — it has no
  taste-separable numerator), and R02729 appears in **no** dataset. No pool contains
  both members. ✓
- No record ID is duplicated within the frequency pool or the composite list; the taste
  pool and composite list share no record IDs.
- Additional documented duplicate pairs spot-checked: R02358 is pooled (frequency +
  recovery) and its duplicate R02872 is absent everywhere; R02798 is in the frequency
  pool and its twin record R01427 is absent. The Biadsee cohort appears as R02365 in the
  *frequency* pool and R01695 in the *recovery* pool — different questions, so no pool
  double-counts a cohort; R02856 is absent everywhere. ✓

---

## Observations for the coordinator (not discrepancies — nothing was changed)

- **Observation A — I² definition should be named in the manuscript.** The reported I² is
  the Q-based (Q − df)/Q statistic. For the "any recovery >12 weeks" pool (tau² = 0.0013,
  Q = 7.16, df = 4) the Q-based I² is 44.1% while a tau²-based I² would be ≈ 0.4%. Both
  statistics are in legitimate use, but a reader recomputing from tau² alone will not
  reproduce 44.1%; the Methods should state the definition explicitly.
- **Observation B — duplicate result files.** `q1_freq_all_result.json` ≡
  `q1_frequency_pool_result.json` and `q1_freq_composite_all_result.json` ≡
  `q1_frequency_composite_result.json`. Harmless, but worth tidying before deposit so the
  archive does not appear to contain two distinct analyses of the same pool.
- **Observation C — R00415 numerator is derivation-only** (Item 4, trace 8): 20/23 rests on
  a printed rounded percentage (87%) × a derived denominator (23), because the paper's
  tables were unreadable in the retrieved full text. The derivation is unique and
  documented, but if a cleaner full text is ever obtained, this is the one sampled number
  worth re-confirming against a printed count.

## Overall verdict

**AGREE on all five items.** The primary pool, the >4–12-week recovery pool, all 13 crude
totals (and, beyond the brief, all 11 other pooled estimates) reproduce independently to
rounding/machine precision; the recovery analysis set rebuilds exactly; all 8 traced rows
verify against the settled extraction sheet or full text; and the C8424 exclusion and
duplicate-pair handling are exactly as the protocol requires.
