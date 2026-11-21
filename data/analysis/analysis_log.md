# Synthesis analysis log (Phase 4, Task 3)

## Data sources (only)
- extraction/extraction_settled_full.csv (389 studies; C8424 excluded from all synthesis, FLAG-AUTHOR)
- analysis/rob/rob_adjudicated_full.csv
- Pool datasets built from settled fields and VERIFIED against full texts by the pool builders:
  q1_frequency_pool.csv (137 studies), q1_frequency_composite.csv (27),
  q1_recovery_pool.csv (42 rows / 28 studies), q1_recovery_composite.csv (35 rows / 24, narrative only).
- Settled-sheet errors found by the builders (frequency ~14 records; recovery 5) are listed in the
  pool logs; full-text values were used and both values recorded. Nothing was silently fixed.

## Methods (protocol-locked)
- Logit-transformed proportions; REML tau^2 (profile restricted likelihood, meta_proportions.py);
  Hartung-Knapp CIs; I^2; 95% prediction intervals (t, k-2 df). Crude totals printed with every pool.
- Recovery pools: ONE row per study x outcome x window (latest timepoint within the window;
  42 rows -> 36 analysis rows; selection recorded in q1_recovery_analysis_set.json).
  Anomaly kept visible: R01110 reports 186/214 recovered at day 90 but 150/214 at mean 9.5 months;
  the latest-timepoint rule puts 150/214 in the >12-week pool.
- Linked cohorts: one record per cohort per pool (builders' duplicate handling in the pool logs).
  R02711 has no taste-separable numerator in its full text and sits in the composite list; its
  preprint R02729 (which does print taste counts) was excluded as the duplicate record - flagged
  for the manuscript, not silently resolved.
- Composite (smell-or-taste) outcomes were pooled ONLY as a separate secondary stratum
  (frequency) or summarised narratively (recovery; known cohort overlaps in that list).

## Headline results (result JSONs alongside)
- Frequency, taste-specific, acute (137 studies, N=155,010): pooled 37.7% (95% CI 32.9-42.7),
  crude 24.9%, I^2 99.5%, tau^2 1.44, 95% PI 5.3-86.7%. EXTREME heterogeneity: the pooled mean
  describes an average across very different settings, not a common frequency; the PI and the
  subgroup estimates are the honest summary.
- By ascertainment: psychophysical testing (k=15) 47.4% (37.0-58.1), I^2 93.8%; self-report
  (k=122) 36.5% (31.4-41.9), I^2 99.6%.
- By population: hospitalised (k=55) 26.8% (22.2-32.1); non-hospitalised/community (k=35)
  39.6% (29.0-51.2).
- Sensitivity: Low-RoB studies only (k=34) 44.4% (33.8-55.6) but crude 9.1% - the set contains the
  60,194-person national registry R00846 (voluntarily reported symptoms, low recorded frequency),
  which is 39% of the entire pool N. Excluding R00846: overall (k=136) and Low-RoB (k=33) pools in
  q1_freq_excl_R00846_result.json / q1_freq_lowrob_excl_R00846_result.json.
- Composite smell-or-taste frequency (k=27, separate stratum): 34.2% (25.3-44.3), I^2 99.4%.
- Complete recovery of taste (taste-specific): <=4 wk (k=10) 87.4% (69.7-95.4), I^2 93.5%;
  >4-12 wk (k=11) 85.2% (70.0-93.5), I^2 95.0%; >12 wk (k=9) 87.8% (69.5-95.8), I^2 88.1%.
  Different study sets per window (not a within-cohort trajectory); PIs are very wide.
- Any recovery (complete+partial): >12 wk (k=5) 90.3% (80.6-95.4), I^2 44.1%; <=4 wk a single
  study (R02302, 63/81 = 77.8%); >4-12 wk NO study reported it separably (empty cell, not filled).
- Time to recovery: reported narratively only - studies report durations in incompatible forms
  (means/medians among recoverers, KM estimates); no pool was forced.
- All pooled studies are SARS-CoV-2. No influenza or other-virus study met any pool mapping:
  the quantitative Q1 answer is a COVID-19 answer; other viruses are narrative-only throughout.
