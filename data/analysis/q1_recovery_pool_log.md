# Q1 Recovery Pool — Build Log

Built 2026-11-21 (America/Los_Angeles) from `extraction/extraction_settled_full.csv` (389 studies; ONLY extraction source) with every pooled number verified against `fulltexts_text/<record_id>.txt`. Protocol: `protocol-locked.md` — windows ≤4 weeks, >4–12 weeks, >12 weeks from onset/diagnosis.

## Rules applied
- Candidate universe: the 140 records with a non-'not reported' value in `recovery_complete_as_printed`, `recovery_any_as_printed` or `time_to_recovery_as_printed` (the settled fields corresponding to the task's recovery/time index).
- Pool row requires: taste-specific outcome; explicit events and denominator; denominator = people with taste dysfunction at baseline who were followed/assessed at that timepoint (never the whole infected cohort); assessment timepoint assignable to exactly one protocol window.
- One row per study × outcome × timepoint. Month-based assessments are converted at 30 days/month (1 month → >4–12 wk; 3 months → >12 wk); '4 weeks'/'28 days' → ≤4 wk; 90 days → >12 wk.
- Kaplan–Meier / model-based percentages without printed crude events were NOT converted to counts. Percentage-only reports were converted only where the implied count is exact or the full set of category counts reconciles to the printed denominator (flagged per row).
- Composite smell-or-taste recovery was never merged into the taste-specific pool; poolable composite studies are in `q1_recovery_composite.csv`, labelled.
- Single-arm treated cohorts and per-arm treatment comparisons (recovery recorded in `treatment_recovery_as_printed`) were excluded from the Q1 natural-history pool (they belong to Q3). Case reports/series <10 participants excluded per protocol.
- C8424 (Klimek 2022, narrative review, FLAG-AUTHOR) is EXCLUDED from all synthesis; it was not a candidate (recovery fields not extracted as primary data) and contributes no rows.
- R02711/R02729 are the same Pieruzzini cohort: only R02711 was considered (per instruction); it contributes no rows (no recovery proportion). R02729 excluded as duplicate.
- All pooled studies are SARS-CoV-2. No study of influenza or another named virus yielded a poolable taste-specific recovery proportion — the non-COVID cells are empty, not filled by stretching rules.

## ⚠ Settled-sheet numbers found WRONG / misleading against the full text

1. **R00730 (Turk 2022) — recovery_any.** Settled sheet: 'Seventy (93.3%) patients were recovered … 5 (6.6%) still complain taste loss' (the paper's Discussion). Full-text Results/Abstract/Table: **6 (8%) of 75 with ongoing loss of taste → 69/75 recovered**. The paper is internally inconsistent; the pool uses the primary Results value **69/75**. Settled headline value (70) should be corrected.
2. **R01612 (Goyal 2021) — recovery_any mislabelled.** Settled sheet records '198 (73.6%) patients recovered (taste) after 2 weeks' under recovery_any. Full-text Table 2 shows 198 is the **cumulative COMPLETE recovery** count by 2 weeks (85 in week 1 + 113 in week 2, both under the 'Complete recovery' heading). Pool rows use it as complete recovery; no separate any-recovery figure exists in the paper.
3. **R02358 (Levinson 2020) — taste recovery wrongly coded as not separable.** Settled sheet codes recovery as composite-only. Full text separates taste: of 14 patients with dysgeusia, 11 recovered both senses and 2 recovered taste only → **13/14 taste recovery**, which the pool uses (≤4 wk).
4. **R02856 (Biadsee 2020) — denominator misleading.** Settled sheet records '72 (74.2%) reported normalization of gustatory function', implying a gustatory-dysfunction denominator of 97. Full text: 97 is ALL follow-up participants; baseline GD in the source cohort was 52% and taste dysfunction as an initial symptom was 34/97. The 72/97 figure cannot be verified as a dysfunction-denominator proportion — study excluded from the pool.
5. **R02362 (Renaud 2020) — denominators not flagged.** Settled sheet records full recovery of taste 26 (8.3%), partial 126 (40.3%), no recovery 158 (50.2%). Full-text recovery table denominators are ~313 respondents, far exceeding the 123 patients with taste disorders in the same paper; the recovery items were evidently answered by a broader (smell/taste/flavour) population. Excluded — denominator is not the taste-dysfunction population.

Paper-internal inconsistencies noted (settled sheet had recorded both values correctly; not settled errors): R01943 (11/20 vs 13/20 recovered at day 7 — Results value used), R02773 (complete 200 + partial 3 + persistent 9 = 212 ≠ 209 with GD — complete row only pooled), R00084 (full-text predictor table uses a 42-patient lab subset: 28 complete; the 44-patient text value 33 complete used), R00987 (abstract prints '110/120' at 3 months; Table 2 denominator 129 used), R02322 (abstract 82% vs KM table 86.8% at 30 days — KM-only, excluded).

## Duplicate / overlapping cohorts flagged
- R02711 = R02729 (Pieruzzini preprint/published) — instructed pair; R02729 excluded, R01101-style double-count avoided.
- R01101 = R02974: the SAME Ohla 2022 GCCR paper extracted twice (identical n=1468, Table 2). Both excluded on the merits (KM-style cumulative percentages); neither contributes rows.
- R00572 = R02714 (Boscolo-Rizzo Omicron cohort, n=294/101): R02714 is the preprint; composite rows taken from R00572 only.
- R02358 = R02872 (Levinson 42-patient cohort, preprint + journal versions): rows derived from R02358 only.
- R02285 = R02697 (Vargas-Gandica, same 10 cases, two records): both excluded (duration only).
- R01695 / R02856: same Biadsee cohort at different follow-ups (mean 229 d vs 59 d). Only R01695 contributes rows (proper GD denominator, 65).
- R01110 / R01017: same ANOSVID source cohort (n=354); R01017 is the olfactory-focused record and contributes no rows, so no double-count.
- Boscolo-Rizzo Trieste series overlap: R00488 (pooled Trieste+Treviso, 3-year), C11061 (Trieste, 12-month), R00673 and R00572 are from the same research group's Trieste cohorts and likely share participants. All are in the COMPOSITE list only; do not pool them together without a cohort-overlap sensitivity decision.
- R02139 (Vaira aggregate series) — settled sheet already flags overlap with other Vaira cohorts; excluded (no proportion).

## Candidate-by-candidate disposition (140 candidates)

- **C10400** (Martončíková 2023) — Excluded — 12.9% returned to pre-COVID taste level is a proportion of all 824 participants (not the 733 with taste <10 during infection), and there is no follow-up timepoint (cross-sectional).
- **C11061** (Boscolo-Rizzo 2022) — COMPOSITE LIST: complete >12 weeks 130/187 @ 12 months; any >12 weeks 171/187 @ 12 months.
- **C4631** (Cosentino 2022) — Excluded — composite olfactory/gustatory regression in a 7-patient subgroup; denominator is not a taste-dysfunction population.
- **C6826** (Kobus 2026) — Excluded from Q1 pool — pre-post olfactory-training study; no taste recovery proportion printed. Q3.
- **C8383** (Sbrana 2021) — Excluded — gustatory recovery 65.3% is status at a single cross-sectional survey with time since infection varying/unreported — window unassignable.
- **C8932** (Chiesa-Estomba 2020) — POOLED (taste-specific): complete >4-12 weeks 635/701 @ mean 63 +/- 9 days (range 60-76).
- **R00020** (Hansen 2026) — COMPOSITE LIST: complete >12 weeks 152/356 @ 4 years.
- **R00079** (Mallon 2026) — Excluded — recovery reported only narratively for a mixed-virus follow-up subset (17 of 64 acute children retested); number with baseline hypogeusia among those followed not separable, no events/denominator pair.
- **R00084** (Celik 2025) — POOLED (taste-specific): complete >12 weeks 33/44 @ 90 days post-discharge; any >12 weeks 44/44 @ 90 days post-discharge.
- **R00165** (Abdulrida 2025) — Excluded — time-to-recovery bands only, and for composite "loss of sense" (not taste-only); no recovery proportion.
- **R00185** (Albu 2025) — COMPOSITE LIST: complete >4-12 weeks 20/20 @ 1 month.
- **R00215** (Ayoub 2025) — Excluded — "resolved" 26% is a proportion of the whole post-COVID group (n=82), not of those with taste dysfunction; no standardised timepoint.
- **R00232** (Chiang 2024) — Excluded from Q1 pool — single-arm TREATED case series (oral prednisolone + zinc); recovery is treatment_recovery (Q3), and patients recovering after month 1 were excluded by design.
- **R00268** (Razura 2024) — Excluded — full/any recovery proportions (1403/1881; 97%) have no assignable timepoint: cross-sectional NHIS survey, time since infection varies and is not reported.
- **R00273** (Gentilotti 2024) — Excluded — any-recovery statement is cumulative and approximate (">50% within 5 months", "~2% improvements until month 21") with no events/denominator at a fixed timepoint.
- **R00282** (Alhassoon 2024) — Excluded — recovery rate 70.5% (implied 139/197) is anchored to "after four weeks from recovery" (paper §2.2.2), not to a fixed interval from onset/diagnosis; assessment timing not standardisable to a protocol window.
- **R00322** (Liu 2024) — Excluded — no taste-specific recovery proportion (median dysgeusia duration 12 days only); the 59.16% improvement figure is composite and was not entered as recovery by the settled extraction.
- **R00323** (Fornazieri 2024) — COMPOSITE LIST: complete >4-12 weeks 249/714 @ interview, median 81 days from onset (IQR 60-104).
- **R00334** (Murphy 2024) — Excluded — composite smell/taste duration only (mean 1.47 years among recovered); no recovery proportion, mixed-aetiology survey.
- **R00356** (Vento 2024) — Excluded from Q1 pool — single-arm treated cohort (combination anti-inflammatory protocol); no recovery proportion printed (VAS change only). Q3.
- **R00415** (Liu 2024) — POOLED (taste-specific): any >12 weeks 20/23 @ follow-up interview, median 41 weeks from diagnosis.
- **R00488** (Boscolo-Rizzo 2023) — COMPOSITE LIST: complete >12 weeks 211/267 @ 6-12 months; complete >12 weeks 238/267 @ 2 years; complete >12 weeks 246/267 @ 3 years; any >12 weeks 263/267 @ 3 years.
- **R00494** (Rass 2023) — Excluded — median taste recovery time (14 days) only; 90-day persistence percentages use the whole survey cohort as denominator, not those with baseline taste dysfunction.
- **R00537** (Kumari 2023) — Excluded from Q1 pool — single-arm intervention (CVFLA training); no taste recovery proportion (severity-score change only). Q3.
- **R00539** (Kalava 2023) — Excluded — case series n=6 (<10 threshold) and treated (stellate ganglion block). Q3.
- **R00546** (Fernandez-de-las-Penas 2023) — POOLED (taste-specific): complete >12 weeks 78/89 @ T1, mean 8.4 months post-discharge.
- **R00561** (Al-Shouli 2023) — Excluded — time-to-recovery bands are percentages of the whole infected cohort (n=922), not of the 520 with taste dysfunction; bands are durations, not status at a fixed assessment.
- **R00572** (Boscolo-Rizzo 2023) — COMPOSITE LIST: complete >12 weeks 97/101 @ 6 months; any >12 weeks 99/101 @ 6 months.
- **R00618** (Hennawi 2023) — Excluded — mean duration of ageusia only (3.17 weeks); no recovery proportion.
- **R00625** (Galvin 2023) — Excluded from Q1 pool — treated case series (stellate ganglion blockade); taste outcome is improvement only, no complete-recovery proportion. Q3.
- **R00634** (Zarachi 2023) — Excluded — no exact taste-specific recovery proportion; the 4-week VAS "mild" band (295/300) includes normal scores and is not a recovery count, and the baseline denominator with true dysfunction is not separable.
- **R00673** (Boscolo-Rizzo 2023) — COMPOSITE LIST: complete >12 weeks 44/62 @ 2 years.
- **R00730** (Turk 2022) — POOLED (taste-specific): any >12 weeks 69/75 @ 12-14 months.
- **R00753** (Shaheen 2022) — Excluded — recovery percentages (full 22.7%, partial 63.4%) are status at a single survey with no fixed time since onset (window unassignable) and an unclear denominator (components sum to 94.9%).
- **R00765** (Saraf 2023) — Excluded (also from composite list) — composite resolution 55/58 uses the whole COVID-positive group as denominator, exceeding the number with smell/taste loss; not a dysfunction-denominator proportion.
- **R00801** (Mazzatenta 2022) — Excluded — case series <10 re-evaluated (n=4 of 20; 12 excluded after severe COVID); recovery count (4/20) has a biased, incomplete denominator.
- **R00884** (Pua Torrejon 2022) — Excluded — no recovery proportion at a defined timepoint (only "4 with hypogeusia had not recovered by end of follow-up", follow-up undefined).
- **R00903** (Callejón-Leblic 2022) — Excluded — taste recovery reported only as a time-to-recovery distribution among a recovered subset (n=47) and as whole-cohort status at 12 months; no proportion of baseline taste-dysfunction cases recovered at a timepoint.
- **R00987** (Ferreli 2022) — POOLED (taste-specific): complete >4-12 weeks 79/129 @ 1 month; complete >12 weeks 110/129 @ 3 months; complete >12 weeks 120/129 @ 18 months.
- **R01000** (Catton 2022) — POOLED (taste-specific): complete <=4 weeks 182/229 @ recovery within <=28 days (survey recall).
- **R01037** (Ludwig 2022) — Excluded — no recovery proportions printed (qualitative statements only).
- **R01068** (Nanjo 2022) — Excluded — median taste recovery time (9 days) only; no proportion.
- **R01073** (Tomasino 2022) — Excluded — duration categories only ("some weeks" 33/55, "some days" 16/55); no recovery proportion at a fixed timepoint.
- **R01101** (Ohla 2022) — Excluded — cumulative taste recovery by month is printed only as sex-specific percentages (women 56.07%, men 64.88% by 11 months) from a time-to-event calculation with time-varying denominators; no events/denominator at a single assessment. DUPLICATE RECORD: same GCCR cohort/paper as R02974 (both excluded; neither contributes rows).
- **R01110** (Klopfenstein 2022) — POOLED (taste-specific): complete >12 weeks 186/214 @ day 90; complete >12 weeks 150/214 @ mean 9.5 months (283.9 days).
- **R01115** (Elvan-Tuz 2022) — Excluded — median ageusia duration only; the 1-month non-regression count (58/885) is in an anosmia-selected subgroup and recovery is not reported as a proportion (complement derivation not used).
- **R01148** (Nguyen 2022) — Excluded — recovery (partial 88/103) is reported only among the subgroup already persistent at >6 months, not among all with baseline taste disorders; complete recovery not reported.
- **R01151** (Ciofalo 2022) — POOLED (taste-specific): complete <=4 weeks 35/43 @ day 28 (T4, Burghart Taste Strips = 4).
- **R01166** (Taziki Balajelini 2020) — POOLED (taste-specific): complete >4-12 weeks 183/219 @ within 30 days of GD onset; complete >12 weeks 219/219 @ 6 months.
- **R01202** (Lee 2022) — COMPOSITE LIST: any >12 weeks 186/206 @ questionnaire, mean 113 +/- 31 days from diagnosis.
- **R01224** (Fortunato 2022) — Excluded — complete recovery printed only as Kaplan-Meier estimates (61.3%/69.7%/74.7% at 30/60/90 days) without events or a taste-specific denominator among the 178 followed.
- **R01236** (Patekar 2022) — POOLED (taste-specific): complete >12 weeks 78/80 @ by end of 3-month follow-up.
- **R01237** (Ruiz-Comellas 2022) — Excluded — 61.1% regained taste at 14 days but the denominator is nowhere printed (60 COVID+ with taste alteration gives no integer match); events cannot be verified.
- **R01255** (Sampaio Rocha-Filho 2022) — Excluded — recovery not reported ("improving" in 18/22 persistent cases is not recovery); interview timing variable (>=2 months, median 111.5 days) spans windows.
- **R01298** (Sagar 2022) — POOLED (taste-specific): complete <=4 weeks 20/21 @ by 4 weeks.
- **R01311** (Campos 2022) — Excluded from Q1 pool — treated case series (photobiomodulation, n=10); no numeric recovery proportion in text. Q3.
- **R01369** (Khan 2022) — COMPOSITE LIST: any <=4 weeks 55/102 @ during hospital stay (mean ~12.3 days from onset).
- **R01378** (Chabot 2021) — Excluded — case series n=2 (<10) and treated (turmeric). Q3.
- **R01382** (Ivona 2021) — Excluded — case series n=4 (<10); individual-case outcomes only.
- **R01388** (Juvekar 2022) — Excluded from Q1 pool — non-randomised treatment comparison; recovery reported per treatment arm only (Q3), no untreated/natural-history cohort.
- **R01391** (Teaima 2022) — COMPOSITE LIST: complete >12 weeks 680/1031 @ 6 months; any >12 weeks 908/1031 @ 6 months.
- **R01432** (Aydemir 2021) — Excluded — mean taste recovery time only (6.18 days); text states recovery was total in almost all but prints no taste-specific proportion.
- **R01478** (Kaliavaradan 2021) — POOLED (taste-specific): complete >4-12 weeks 168/172 @ 5 weeks (end of weekly follow-up).
- **R01506** (Sahin 2021) — Excluded — gustatory dysfunction resolved in 16/18, but the assessment timepoint for taste is not reported (survey timing not anchored to diagnosis; resolution times 1-30 days are durations, not an assessment window).
- **R01519** (Aranda Rubio 2022) — Excluded — single case report (n=1), treated (pregabalin).
- **R01522** (Lal 2021) — Excluded — no recovery proportion (mean gustatory recovery 10.8 days only; "complete and early in most" unquantified).
- **R01560** (Albaharna 2021) — Excluded — median ageusia duration only (5 days); recovery not assessed (authors’ stated limitation).
- **R01611** (Dudine 2021) — Excluded — complete 52/78 and any 74/78 verified in FT Table 2, but status is "at time of interview" (Jun-Sep 2020) with time since first-wave infection varying and unreported — window unassignable.
- **R01612** (Goyal 2021) — POOLED (taste-specific): complete <=4 weeks 85/269 @ 1 week; complete <=4 weeks 198/269 @ 2 weeks; complete >4-12 weeks 252/269 @ 1 month; complete >4-12 weeks 264/269 @ 2 months.
- **R01628** (Bhatta 2022) — POOLED (taste-specific): complete >4-12 weeks 40/54 @ 2 months; complete >12 weeks 51/54 @ 4 months.
- **R01692** (Sagar 2021) — Excluded — case series n=6 (<10 threshold); complete recovery in 6/6 with durations 1-35 days but below the protocol case-series size for synthesis.
- **R01695** (Biadsee 2021) — POOLED (taste-specific): complete >12 weeks 40/65 @ mean 229 days (range 191-253); any >12 weeks 65/65 @ mean 229 days.
- **R01705** (Tarifi 2021) — COMPOSITE LIST: complete >4-12 weeks 15/21 @ 6 weeks; any >4-12 weeks 21/21 @ 6 weeks; complete >12 weeks 21/21 @ 6 months.
- **R01706** (Antolín Amérigo 2021) — Excluded — mean taste recovery time only (25.4 days); the printed 66.3% recovery figure is for smell.
- **R01710** (Kandakure 2021) — POOLED (taste-specific): complete <=4 weeks 10/14 @ day 10; complete <=4 weeks 14/14 @ day 14.
- **R01729** (Bertlich 2021) — Excluded — denominator includes baseline normogeusic patients: normogeusia 18/20 at 8 weeks and 17/17 at 6 months are proportions of all followed hyposmia-cohort patients, not of those with baseline taste dysfunction (12/22), which is not separable at follow-up.
- **R01739** (Sehanobish 2021) — POOLED (taste-specific): complete >4-12 weeks 162/209 @ by ~45 days (telephone interview follow-up).
- **R01742** (Printza 2021) — POOLED (taste-specific): complete >4-12 weeks 42/53 @ median 61 days from onset (survey).
- **R01750** (Koyama 2021) — COMPOSITE LIST: complete not assignable 34/355 @ at summarisation of social-media posts (Mar-Jul 2020).
- **R01758** (Riestra-Ayora 2021) — POOLED (taste-specific): complete >12 weeks 87/118 @ 6 months; any >12 weeks 104/118 @ 6 months.
- **R01767** (Cousyn 2021) — Excluded — day-30 complete resolution printed only as a Kaplan-Meier estimate (72.8%, 95% CI) without events; crude events not printed.
- **R01826** (Makaronidis 2021) — Excluded — full resolution 227/343 at "4-6 weeks" after antibody testing: time origin is antibody testing (not onset/diagnosis) and the 4-6-week interval spans the 4-week window boundary; denominator also conflicts with the printed taste-loss n (342 vs 343).
- **R01856** (Gupta 2021) — POOLED (taste-specific): complete >4-12 weeks 148/153 @ by 8 weeks (cumulative recovery intervals).
- **R01864** (Song 2021) — Excluded (also from composite list) — composite "about 80% recovered in 2 weeks" with no events or dysfunction denominator printed.
- **R01878** (Locatello 2021) — POOLED (taste-specific): complete >4-12 weeks 27/39 @ 30 days after first negative swab.
- **R01900** (AlShakhs 2021) — Excluded — time-to-regain bands among those reporting recovery only; no denominator of followed taste-dysfunction cases at a fixed timepoint.
- **R01916** (Kumar 2021) — COMPOSITE LIST: complete <=4 weeks 40/40 @ by end of follow-up (OTD durations 2-15 days).
- **R01941** (Polat 2021) — Excluded — recovery time is composite smell-taste (median 13 days); no taste-specific recovery proportion.
- **R01943** (Yadav 2021) — POOLED (taste-specific): complete <=4 weeks 11/20 @ day 7; complete <=4 weeks 20/20 @ day 14.
- **R01962** (Mubaraki 2021) — Excluded — mean ageusia duration only (10.4 days); no recovery proportion.
- **R01965** (Sahoo 2021) — POOLED (taste-specific): complete <=4 weeks 73/76 @ day 14 after positive swab.
- **R01970** (Kavaz 2021) — COMPOSITE LIST: complete <=4 weeks 24/32 @ resolved <1 week (assessed 4 weeks after end of treatment).
- **R01978** (Andrews 2020) — POOLED (taste-specific): complete >4-12 weeks 41/87 @ median 52 days (questionnaire).
- **R02057** (Jain 2020) — Excluded — composite smell-taste duration only; no taste-specific recovery proportion.
- **R02062** (Taziki Balajelini 2020) — Excluded — complete 55/72 and any 66/72 verified as printed, but assessment at serology 2-3 months after onset (mean 91 +/- 16 days) spans the >4-12wk and >12wk windows — unassignable.
- **R02070** (Rocha-Filho 2020) — Excluded — duration among recovered only (median 5 days); assessment timing not standardised, no proportion at a timepoint.
- **R02077** (Sheng 2021) — COMPOSITE LIST: any <=4 weeks 41/59 @ within 3 weeks of onset.
- **R02082** (Baron-Sanchez 2020) — Excluded — "all subjects recovered taste" (PCR+ subgroup, ~30 with taste disorder) but follow-up was until resolution with a variable end date (mean 38.5 days); no fixed assessment timepoint.
- **R02125** (Kasuga 2021) — Excluded — single case report (n=1); composite VAS outcome.
- **R02135** (Ho 2020) — Excluded — familial cluster n=7 (<10); durations only.
- **R02139** (Vaira 2022) — Excluded — no recovery proportion printed (qualitative "tends to regress within 10 days"); aggregate evaluation series with suspected overlap with other Vaira cohorts.
- **R02140** (Karimi-Galougahi 2022) — COMPOSITE LIST: complete <=4 weeks 27/42 @ 2 weeks.
- **R02166** (Lv 2020) — COMPOSITE LIST: complete >12 weeks 35/39 @ 3 months after discharge.
- **R02180** (Liu 2020) — Excluded — case series n=3 (<10).
- **R02196** (Brandao Neto 2021) — Excluded — taste recovery % (68.3%) at re-interview has an unclear taste-specific denominator (143 re-interviewed had chemosensory loss) and timing spans windows (36-119 days, median 76).
- **R02205** (Rojas-Lechuga 2021) — Excluded — any-recovery counts by severity (42/128 total) are status at a single survey with time since infection not reported — window unassignable.
- **R02210** (Al-Ani 2022) — COMPOSITE LIST: complete <=4 weeks 35/35 @ resolution 3-12 days.
- **R02229** (Mohamud 2020) — Excluded — recovery-time bands are percentages of the whole cohort (n=60), and the ">10 days" band cannot be separated into recovered-after->10-days vs unrecovered; no unambiguous events/denominator at a fixed assessment.
- **R02264** (Villarreal 2021) — Excluded — duration/persistence figures are composite smell-taste; no taste-specific recovery proportion.
- **R02265** (Gamba 2020) — Excluded — average recovery time only (17 days, composite anosmia/dysgeusia wording); "complete recovery after two weeks" stated without a proportion.
- **R02278** (Reiter 2020) — Excluded — "return to very good/good" percentages (73.1% at 14d; 84.2% at 1 month) use all survey respondents as denominator, not those with baseline taste dysfunction.
- **R02285** (Vargas-Gandica 2020) — Excluded — median ageusia duration only (8 days); no recovery proportion. DUPLICATE COHORT of R02697 (same 10 cases).
- **R02302** (Sakalli 2020) — POOLED (taste-specific): complete <=4 weeks 19/81 @ day 20 after diagnosis; any <=4 weeks 63/81 @ day 20 after diagnosis.
- **R02313** (Liang 2020) — Excluded — hypogeusia duration only (7.12 days); no recovery proportion.
- **R02322** (Paderno 2020) — Excluded — complete recovery printed only as Kaplan-Meier rates (86.8% at 30 days; abstract prints 82% — internal discrepancy) without crude events.
- **R02336** (Gómez-Iglesias 2020) — Excluded — resolution time is composite gustatory/olfactory (6.3 days); no taste-specific recovery proportion.
- **R02358** (Levinson 2020) — POOLED (taste-specific): complete <=4 weeks 13/14 @ by end of follow-up (to 25 Mar 2020; dysgeusia durations <=17 days).
- **R02362** (Renaud 2020) — Excluded — FT recovery table denominators (~313 respondents answering taste-recovery items) far exceed the 123 with taste disorders; denominator is not the taste-dysfunction population (likely all with smell/taste/flavour complaints).
- **R02375** (Chary 2020) — COMPOSITE LIST: complete <=4 weeks 52/81 @ day 15; any <=4 weeks 79/81 @ day 15.
- **R02385** (Sayin 2020) — COMPOSITE LIST: any not assignable 21/46 @ at survey (time since infection not reported).
- **R02391** (Meini 2020) — COMPOSITE LIST: complete >4-12 weeks 27/42 @ ~1 month after discharge; any >4-12 weeks 35/42 @ ~1 month after discharge.
- **R02433** (Gelardi 2020) — COMPOSITE LIST: complete not assignable 22/60 @ at assessment (timing not standardised); any not assignable 42/60 @ at assessment (timing not standardised).
- **R02455** (Lee 2020) — Excluded — median ageusia recovery time only (7 days); "most recovered within 3 weeks" unquantified for taste; follow-up N internally inconsistent (196 vs 143).
- **R02464** (Vaira 2020) — Excluded — correspondence/preliminary results, not a primary dataset; composite 67.5% with no denominator.
- **R02506** (Lechien 2020) — Excluded (also from composite list) — composite "recovered both senses 25.5%" has no printed denominator of patients with both dysfunctions.
- **R02693** (Young 2023) — Excluded — case series n=5 (<10), treated (Training N Treatment protocol). Q3.
- **R02697** (Vargas-Gandica 2020) — Excluded — median ageusia duration only; no recovery proportion. DUPLICATE COHORT of R02285 (same 10 cases).
- **R02704** (Boyd 2023) — COMPOSITE LIST: any not assignable 64/426 @ at enrolment, 1-24 months after onset.
- **R02711** (Pieruzzini 2021) — Excluded — no recovery proportion (recovery interval 3 days-5 weeks, composite smell/taste wording). Per task instruction this published version is the retained record of the Pieruzzini cohort; R02729 excluded as its duplicate.
- **R02714** (Boscolo-Rizzo 2022) — Excluded — DUPLICATE COHORT of R00572 (same Boscolo-Rizzo Omicron cohort, n=294/101; R02714 is the Research Square preprint). Composite outcome in any case; R00572 rows are in the composite list.
- **R02729** (Pieruzzini 2020) — Excluded — DUPLICATE COHORT of R02711 (preprint version), per task instruction (use R02711 only). R02711 itself contributes no rows (no proportion).
- **R02773** (Singhal 2023) — POOLED (taste-specific): complete <=4 weeks 200/209 @ by 4 weeks (follow-up until recovery or 4 weeks).
- **R02774** (Dehghani Firouzabadi 2021) — Excluded — complete recovery not reported; only "20.1% had not recovered at 2 months" with the gustatory-manifestation denominator not printed as a single count (complement derivation not used).
- **R02798** (Li 2020) — Excluded — "recovered or almost recovered" 33/42 is status during a cross-sectional survey (3-15 Apr 2020) with time since onset varying/unreported — window unassignable; category also mixes complete and almost-complete.
- **R02856** (Biadsee 2020) — Excluded — normalization 72/97 uses all follow-up participants as denominator; baseline gustatory dysfunction in this cohort is not 97 (previous-cohort GD rate 52%; taste dysfunction as initial symptom 34), so the dysfunction denominator cannot be verified. Earlier follow-up of the R01695 cohort.
- **R02872** (Levinson 2020) — Excluded — DUPLICATE COHORT of R02358 (same 42-patient Levinson cohort; R02358 retained, taste-specific count derived from it).
- **R02911** (Bayrak 2021) — COMPOSITE LIST: complete >4-12 weeks 31/56 @ 1 month.
- **R02945** (Al-Zaidi 2020) — Excluded — "recovered" 16/54 (complete vs partial not distinguished) at a single in-quarantine questionnaire with time since onset varying — window unassignable.
- **R02954** (Chauhan 2022) — Excluded — single case report (n=1), treated (stellate ganglion block).
- **R02974** (Ohla 2022) — Excluded — DUPLICATE RECORD of R01101 (same Ohla 2022 GCCR paper, same n=1468 and Table 2); excluded for the same KM/cumulative-percentage reason as R01101.

## Verification
Code-checked on build: every row has integer events ≤ denominator; (record_id, outcome, window, timepoint) unique per file; C8424 absent from both files; R02729 absent from both files.

