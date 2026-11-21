# Q1 frequency pool — build log
Primary Q1 outcome (protocol-locked): proportion of people with confirmed infection who have taste dysfunction (ageusia, hypogeusia, dysgeusia, or an abnormal validated gustatory test), assessed acutely / at presentation / during acute illness.
## Sources and a naming note
The ONLY extraction source was `extraction/extraction_settled_full.csv` (389 studies). That file does **not** contain columns named `prevalence_numerator` / `prevalence_denominator` / `prevalence_as_reported`; the settled index fields are `N_total` (R8: all printed totals, labelled) and `taste_prevalence_as_printed` (numerator/denominator and/or % exactly as printed, R2 by-design prefixing). Those two fields were used as the index, and **every number entered in the pool/composite datasets was verified against the study full text** in `fulltexts_text/<record_id>.txt`. Risk-of-bias bands are the adjudicated overall bands from `analysis/rob/rob_adjudicated_full.csv`, copied verbatim.
## Mapping rules applied (exactly as briefed)
- **Taste-specific only** in the primary pool: the numerator counts taste dysfunction separable from smell. Composite-only studies go to the separate composite list, never merged.
- **Denominator**: people with confirmed infection (laboratory-confirmed, or study-defined confirmed cases, e.g. ECDC clinical/radiological hospital cases) assessed for taste. Excluded: denominators restricted to people selected for chemosensory symptoms (incl. all settled `BY-DESIGN SAMPLING` records), case-control designs, and denominators including unconfirmed infections where a confirmed-only frequency was not extractable.
- **Timing**: symptom *history* of the acute illness (whenever ascertained) and tests performed during the acute illness/at presentation map to the outcome. Point prevalence measured only at post-acute follow-up (e.g. taste testing at 3–12 months, persistent/long-COVID cohorts) does not.
- **C8424 excluded from all synthesis** (FLAG-AUTHOR), per instruction.
- **R02711/R02729**: same cohort — only R02711 retained (see duplicates section; full-text verification placed it in the composite stratum, not the taste-specific pool).
- One row per study. Where a paper printed mutually exclusive taste strata (e.g. taste-only + both smell-and-taste), events are the sum of the printed strata; every such derivation is flagged in the per-study note. Where only a percentage and denominator were printed, a derived numerator was used **only** when it is the unique integer consistent with the printed percentage, and is flagged; otherwise the study was excluded as unverifiable.
- Ascertainment: `psychophysical test` where the pooled numerator comes from a gustatory test (validated or standardised bedside/screening test); otherwise `self-report` (questionnaire, interview, records, registry). Population: hospitalised / non-hospitalised-community / mixed / healthcare workers / other, judged from the sampling frame.
## Results
- **Taste-specific pool: 137 studies; total N = 155,010; events = 38,607; crude events/N = 0.2491.** All 137 are SARS-CoV-2 studies — no study of influenza or another named virus in the settled set met the primary-outcome mapping (non-COVID records were reviews, case reports, unconfirmed, or lacked an acute confirmed denominator; see disposition table).
- **Composite smell-or-taste list: 27 studies; total N = 34,402; events = 7,571; crude = 0.2201.** Summarised separately; never merged with the pool.
- **Excluded: 225 studies.** Counts by primary reason (each excluded study counted once, under the first applicable category in the order used at adjudication):
  - Denominator selected/restricted (incl. by-design symptom sampling): 85
  - No extractable or verifiable taste frequency (missing, conflicting, or non-patient denominator): 31
  - Case-control design (no population denominator): 28
  - Not a primary study (review): 20
  - Infection not confirmed (self-report / unconfirmed / mixed without extractable confirmed subset): 14
  - Timing: not acute-phase frequency (follow-up/persistent/convalescent assessment): 13
  - Duplicate/overlapping cohort or record (one version retained): 11
  - Case report / small case series (<10): 9
  - Animal/in-vitro (Q2 only): 5
  - Letter/editorial/correspondence without primary data: 5
  - Composite-only outcome without a valid confirmed/acute denominator: 2
  - Excluded by instruction (FLAG-AUTHOR): 1
  - Registry record, no results posted: 1

## Settled-sheet errors and gaps found against full texts (NOT silently fixed — pooled values use the full-text values)
Settled-sheet **omissions** (numerator printed in the full text but absent from `taste_prevalence_as_printed`; pooled with the full-text numerator):
- **R00193**: settled recorded only '8.5%' from the Discussion; full text Results print altered taste in **112 (8.5%)** of 1,331. Settled also labelled measurement 'composite smell-taste' although a taste-specific count is printed.
- **R01081**: settled gave '67.4%' without a numerator; full text Table prints 'Taste disfunction **205 (67.4%)**'.
- **R01185**: settled gave '28%' without a numerator; full text prints '**14 patients (28%)** scoring in the range of hypogeusia'.
- **R01900**: settled gave '64.6%' without a numerator; full text prints '64.6% (**177 participants**)'.
- **R01926**: settled gave '46.8%' without a numerator; full text prints '**1205 (46.8%)** patients complained of subjective GD'.
- **R01145**: settled gave percentages/CIs only; full text Table prints Taste **91 (26.9%)** of 338 (Omicron cohort) and 253 (57.4%) of 441 (historical).
- **R01878**: settled could not resolve GD n (38 vs 39); full text states '33 referred OD and **39 GD** (29 both, 4 only OD, 10 only GD)'.
- **R01611**: settled denominator ambiguous (104 vs implied 103); full text Table 2 base is **103** (79 (76.7%)).
- **R00273**: settled reported '424 (87.42%) in the follow-up table population' without identifying the denominator; full text confirms the figure but the ~485 denominator is an undefined subset of the 1,187 cohort — study excluded (see table).
**Paper-level errors transcribed into the settled sheet** (settled faithfully copied the paper; the paper itself is wrong/inconsistent — pooled handling noted):
- **R00980**: paper text says 614 recruited, but every table/percentage uses **641** (409 mild = 63.8%; smell/taste No 216 + Yes 425 = 641). Composite pooled as 425/641.
- **R02249**: abstract prints 65.6% for 76 gustatory-impairment cases; strata sum to 76/106 = **71.7%**. Pooled 76/106.
- **R02166**: abstract prints 39/196 as 19.9% and Results text as 9.7%; 19.9% is correct.
- **R00165**: 105/133 printed as 78.2% (true 78.9%). Study excluded on confirmation grounds.
- **R01822**: dysgeusia 404 printed as 6.9% — that percentage uses the pre-exclusion registry total (5,868); pooled denominator is the analysed population (5,399; 7.5%).
- **R02199**: text states ageusia 5/57 (8.7%); Table 1 strata sum to 4. Pooled as printed in text (5/57), flagged.
- **R01899**: 718 (68.8%) of 1,043 is internally consistent, but the paper's '286 without taste dysfunction' sums to 1,004, not 1,043.
- **R00618**: ageusia printed as 51.1% (~1,276) while the routed taste-loss subgroup is n=1,282, and a Table 2 checklist gives loss of taste in 106 (4.2%). Pooled 1,282/2,497 (the paper's own routed group), flagged.
- **R00579**: headline 195/405 verified in full text Table (195 (48.1%) of 405); the sex-strata figures in the settled sheet (102/180 + 89/217 = 191) come from a differently-based subgroup table in the paper.
## Linked / duplicate cohorts
- **R02711 / R02729 (Pieruzzini, Venezuela)**: same cohort (published + medRxiv preprint). Per instruction only R02711 is retained and R02729 excluded. **However**, full-text verification of R02711 shows it prints **no taste-separable numerator**: the VOTT+ group (66/144 PCR-positive) is combined smell-and-taste test dysfunction, and within-group percentages (e.g. 'anosmia and ageusia in 30%') have no counts. R02711 is therefore in the **composite** list (66/144, psychophysical test), not the taste-specific pool — pooling it as taste-specific would breach the protocol's taste-specific rule. Ironically the excluded preprint R02729 *does* print taste-specific counts (23/124 hypogeusia); it remains excluded per the one-version rule, and the discrepancy is flagged here for the review team.
- **R01701 / R02319 (Petrocelli, Bologna)**: identical cohort (N=300, mean age 43.6, 75% female, gustatory dysfunction 184 in both). R01701 retained; R02319 excluded as duplicate.
- **R02365 / R01695 / R02856 (Biadsee, Israel)**: one hotel-quarantine cohort reported three times (original cross-sectional, journal follow-up, Research Square preprint). R02365 (67/128) retained; R01695 and R02856 excluded as duplicates.
- **R01669 / C11061 (Boscolo-Rizzo, Trieste)**: identical cohort (eligible 433; baseline 315; follow-up 268; isolated taste 16; combined 152). R01669 retained; C11061 excluded as duplicate.
- **R00572 / R02714 (Boscolo-Rizzo, Omicron BA.1)**: same study (baseline 338; follow-up 294; taste involvement 85). Journal version R00572 retained; Research Square preprint R02714 excluded.
- **R01017 / R02244 (Nord Franche-Comté)**: R02244 (1–14 Mar 2020, n=70) is a period subset of the ANOSVID cohort R01017 (1 Mar–31 May 2020, n=353). R01017 retained; R02244 excluded. R02438 (same hospital, outpatient presenters grouped by PCR result, 30 Mar–3 Apr 2020) uses a different sampling frame and is retained with an overlap flag.
- **R02358 / R02872 (Levinson, Tel Aviv)**: identical cohort and numbers (42 analysed; dysgeusia 14). R02358 retained; R02872 excluded.
- **R01739 / R02897 (Sehanobish, Montefiore)**: R02897 is the conference abstract of R01739 (same N=486). R01739 retained; abstract excluded (its percentages are also internally impossible: 'both' 58% > anosmia 33%).
- **R02349 / R02932 (Dawson, CDC household study)**: identical study/numbers (42 cases; taste loss 24). R02349 retained; R02932 excluded.
- **R01427 / R02798 (Li, Wuhan)**: same study (N=187, 3–15 Apr 2020). The published letter's numbers sat in an unavailable supplement (R01427 excluded at extraction); the Research Square preprint record R02798 carries the data (42/187) and is pooled. Not double-counted.
- **Boscolo-Rizzo Trieste/Treviso series (cross-stratum overlap)**: R01669 (taste pool), R00488 and R00457 (composite list) draw on overlapping March–April 2020 Trieste/Treviso mild-case populations from the same group. They sit in *different* strata (taste-specific vs composite) so no double-count occurs within either pooled estimate, but the overlap is flagged for sensitivity reporting.
- **Same-centre flags (retained, different frames/periods)**: R00934 / R01085 / R02057 (ESIC Faridabad: inpatients Jul–Sep 2020; OPD Sep 2020; May–Jun 2020 cohort); R01255 / R02070 (Oswaldo Cruz Recife, overlapping 2020 periods); R01129 / R01185 (Regensburg: 8-month follow-up vs acute phase — R01129 excluded on timing, so no pool overlap).

## Verification
Code checks passed: pool and composite IDs unique; events ≤ total for every row; every pooled/composite numerator and denominator was traced to the full text (digit-presence check plus targeted reading of all 44 initially ambiguous records). Where a pooled value is a sum of printed strata or a unique-integer derivation from a printed percentage, the per-study note below says so explicitly.

## Disposition of every settled study (389)
| record_id | disposition | events | total | note |
|---|---|---|---|---|
| C0174 | EXCLUDE |  |  | No taste-dysfunction prevalence (group mean scores only) |
| C0464 | EXCLUDE |  |  | VERIFY: parent-reported ageusia/hypogeusia during illness 30.2% (Table 2) - numerator/base unclear (61 completed; 30.2% is not an integer share of 61) / Full-text check: ageusia/hypogeusia 30.2% (Table 2) with no counts and no identifiable denominator base (61 completed; 30.2% is not an integer share) - not verifiable |
| C10044 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C10140 | POOL | 11 | 37 | VERIFY: subjective taste alteration 11 (30%) - denominator 37 enrolled vs 27 tested; 4 pre-existing ageusia cases may overlap / Full-text verified: Table 1 base is all 37 enrolled (11 (30%) subjective taste alteration after COVID-19); the 27 q-Sticks tested subset was smell testing only. Four pre-existing stroke-related ageusia cases are a separate history line |
| C10400 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C11061 | EXCLUDE |  |  | Duplicate cohort of R01669: identical Trieste cohort (eligible 433, baseline 315, follow-up 268; isolated taste 16, combined 152) - chasing-record duplicate |
| C11369 | EXCLUDE |  |  | Confirmation mixed incl. 30.9% symptom-diagnosed only; taste frequency for confirmed subset not extractable |
| C11416 | EXCLUDE |  |  | Persistent dysgeusia/ageusia >=1 year after diagnosis (not acute); confirmation method not stated |
| C11888 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C2161 | EXCLUDE |  |  | No taste numbers in text (supplementary figures only) |
| C2971 | POOL | 19 | 349 | Taste impairment 19/349 hospitalised non-severe patients (hyposmia strata 8+11 reconcile) |
| C3251 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C4367 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C4506 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| C4631 | EXCLUDE |  |  | Enrolment conditional on new-onset olfactory disorder (chemosensory-selected denominator); mechanistic pilot |
| C5051 | EXCLUDE |  |  | Outcome is taste problem in the last month in a 2022 survey of ever-infected farmworkers (not acute-phase ascertainment) |
| C5334 | POOL | 15 | 92 | Taste impairment 15/92 hospitalised patients |
| C6826 | EXCLUDE |  |  | Cohort sampled on persistent chemosensory dysfunction >=12 weeks; no taste-specific frequency |
| C7163 | EXCLUDE |  |  | Chemosensory-complaint cohort; no taste-dysfunction proportion printed (mean tVAS only) |
| C8383 | POOL | 401 | 541 | Taste dysfunction 401/541 test-positive frontline health professionals |
| C8424 | EXCLUDE |  |  | FLAG-AUTHOR (C8424 excluded from all synthesis per task instruction) |
| C8500 | POOL | 0 | 81 | No taste disturbances 0/81 self-perceived asymptomatic confirmed patients (within 2 weeks of diagnosis) |
| C8521 | POOL | 2 | 23 | Change in sense of taste 2/23 PCR-positive outpatient children |
| C8582 | EXCLUDE |  |  | Cohort sampled on persisting olfactory disorders; no taste-specific frequency |
| C8932 | POOL | 718 | 1043 | Gustatory dysfunction 718/1043 laboratory-confirmed mild COVID-19 patients |
| C9634 | EXCLUDE |  |  | RCT in persistent olfactory-disorder cohort; no taste frequency outcome |
| R00004 | EXCLUDE |  |  | Infection self-reported only; denominator is a vaccinated survey sample with and without COVID-19, not confirmed infections |
| R00006 | POOL | 507 | 5348 | Ageusia during illness via surveillance telephone follow-up; analysed N=5348 |
| R00012 | EXCLUDE |  |  | VERIFY timing wording: post-discharge questionnaire - ageusia history vs current / Full-text check: questionnaire recorded anosmia/ageusia 'during and/or after' COVID-19 in a post-COVID referred sample - outcome window mixes acute and post-acute presence; acute frequency not isolable |
| R00019 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00020 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00042 | EXCLUDE |  |  | Timing: Taste Strips measured 3-12 months post viral clearance (follow-up point prevalence, not acute) |
| R00044 | EXCLUDE |  |  | Denominator is a long-COVID cohort (post-acute selected population); mechanistic study |
| R00047 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00049 | EXCLUDE |  |  | General-population survey; infection self-reported/unspecified, no confirmed-infection denominator |
| R00058 | POOL | 38 | 104 | VERIFY: sampled ~75 days post-diagnosis; dysgeusia history vs current status unclear / Full-text verified: at ~75-day visit participants were asked whether they had experienced gustatory dysfunction 'at any time during their COVID-19 illness' - acute history; dysgeusia 38/104 |
| R00059 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00066 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00077 | EXCLUDE |  |  | No viral-infection cohort (NHANES general population, pre-COVID cycles) |
| R00079 | EXCLUDE |  |  | Acute-group numerator not printed (percentages only for severe hypogeusia) and acute group sizes internally inconsistent (30 vs 34 swapped between abstract and methods) |
| R00084 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00113 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00129 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00132 | POOL | 321 | 5014 | Taste disorders on hospital record forms, older adults hospitalised with confirmed COVID-19 |
| R00138 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00165 | EXCLUDE |  |  | Denominator includes PCR-negative (33%) and untested (7%) participants; confirmed-only subset not extractable. Also 105/133 printed as 78.2% (arithmetic mismatch) |
| R00170 | POOL | 111 | 347 | VERIFY denominator: 1179 records analysed but only 347 eligible/included - check inclusion basis / Full-text verified: 347 eligible/included of 1179 records analysed (paper's analysis population, Table N=347); dysgeusia 111/347 |
| R00185 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00193 | POOL | 112 | 1331 | VERIFY numerator: taste-specific 8.5% stated in discussion only; numerator not in settled sheet / Full-text verified: altered taste in 112 (8.5%) of 1331 - numerator printed in full text results (settled sheet recorded only the discussion percentage) |
| R00205 | COMPOSITE | 1261 | 11353 | Composite smell and/or taste disorders on J-SPEED forms at discharge |
| R00210 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00215 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00232 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00245 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00259 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00266 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00268 | EXCLUDE |  |  | Infection self-reported only (NHIS survey) |
| R00273 | EXCLUDE |  |  | VERIFY denominator for acute taste impairment 424 (87.42% implies N~485; cohort N=1187, model N=1061) / Full-text check: acute taste impairment 424 (87.42%) implies denominator ~485, an undefined subset of the 1187-patient cohort (follow-up table population); unselected confirmed-infection denominator cannot be verified |
| R00282 | POOL | 197 | 413 | Events = printed strata summed: taste only 14 + both smell and taste 183 |
| R00316 | POOL | 75 | 414 | Assessed days 2 and 7 of hospitalisation (acute) |
| R00322 | POOL | 19893 | 35566 | Events = taste only 4347 + both 15546 (printed strata summed) |
| R00323 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00334 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00356 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00358 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00365 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00366 | EXCLUDE |  |  | Denominator restricted to patients selected for persistent smell loss >1 week (chemosensory-symptom-selected) |
| R00373 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00391 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00405 | POOL | 132 | 300 | Events = taste only 27 + both 105 among 152 with OTDs (printed strata summed); denominator PCR-positive presenters |
| R00415 | POOL | 23 | 40 | VERIFY numerator printed: settled sheet gives 57.5% of 40 (=23) without explicit numerator / Full-text verified: gustatory loss 57.5% of the 40 followed patients = 23 (exact integer; Table 2) |
| R00457 | COMPOSITE | 57 | 88 | Acute-phase self-reported smell or taste dysfunction (composite). Taste Strips data are 1-3 year follow-up only, not acute - not pooled |
| R00459 | EXCLUDE |  |  | No taste frequency reported (gustometry scores only); olfactory-dysfunction clinic population |
| R00474 | EXCLUDE |  |  | Composite frequency denominator is the whole population cohort including COVID-negative participants; confirmed-infection subgroup not extractable |
| R00488 | COMPOSITE | 267 | 403 | Baseline (acute) composite smell or taste alteration. FLAG: possible cohort overlap with R00457 (same group, Trieste/Treviso, Mar 2020 mild cases) - not proven identical; retained with flag |
| R00494 | EXCLUDE |  |  | VERIFY: survey acute taste disorders reported as percentages only (68% Austria n=479; 74% Italy n=427); numerators not in settled sheet / Full-text check: acute taste disorders reported only as percentages by country (68% of 479; 74% of 427); numerators not printed anywhere in full text |
| R00502 | EXCLUDE |  |  | No patient denominator (Twitter infodemiology; unit of analysis is tweets) |
| R00537 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00539 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00546 | POOL | 89 | 1266 | Ageusia at infection onset/hospitalisation (T0); denominator = 1266 completing all follow-ups |
| R00561 | EXCLUDE |  |  | Infection self-reported only |
| R00572 | POOL | 85 | 294 | Acute-phase taste involvement = only taste 18 + smell and taste 67 (printed strata summed); denominator 294 with baseline type breakdown |
| R00574 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00579 | POOL | 195 | 405 | National registry sample of diagnosed patients; dysgeusia 195/405 as printed (sex strata sum to 191 - check at verification) |
| R00592 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R00599 | EXCLUDE |  |  | Long-COVID/reinfection cohorts surveyed >=60 days post-test for persistent dysfunction (not acute frequency) |
| R00606 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00618 | POOL | 1282 | 2497 | VERIFY: ageusia 51.1% vs taste-affected n=1282 (51.3%) vs Table 2 loss of taste 106 (4.2%) - major internal inconsistency / Full-text verified: routed subgroup 'who lost taste only or both = 1282' of 2497. FLAG: paper also prints 51.1% (implies ~1276) and a conflicting Table 2 checklist figure (106, 4.2%) - pooled numerator is the paper's own routed taste-loss group size |
| R00625 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00627 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00632 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R00634 | EXCLUDE |  |  | Dysfunction prevalence not extractable: VAS mild band (0-3) includes normal scores 0-1 per authors' own smell analysis; moderate+severe at onset = 110/300 not pooled |
| R00637 | COMPOSITE | 750 | 3439 | Composite taste or smell disorders (TSD) in serology-positive general-population cohorts |
| R00648 | POOL | 53 | 1250 | Children referred to post-COVID clinic (not chemosensory-selected); dysgeusia during acute phase 53/1250 |
| R00649 | EXCLUDE |  |  | No taste frequency (numerator/denominator) reported |
| R00657 | POOL | 287 | 686 | Events = taste only 131 + both 156 = 287 (matches printed taste-dysfunction group n=287); mild/asymptomatic isolation-facility patients |
| R00659 | POOL | 18 | 41 | All 18 subgroup-A patients had gustatory dysfunction at presentation (acute history); denominator all 41 post-COVID patients |
| R00665 | EXCLUDE |  |  | Infection self-reported only (no test/clinician confirmation stated) |
| R00673 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00710 | EXCLUDE |  |  | Animal/in-vitro (Q2 stratum only); no human frequency denominator |
| R00712 | POOL | 66 | 140 | Complete loss of taste 66/140 per Table 1 (47.1% consistent); results text says 65 - verify |
| R00722 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00730 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00731 | COMPOSITE | 284 | 688 | Composite smell or taste alterations at T1 (during hospitalisation): 41.3% of 688 = 284 STA cases as printed |
| R00753 | POOL | 184 | 194 | VERIFY numerator: gustative dysfunction 94.8% of 194 printed without numerator in settled sheet (~184) / Numerator derived: gustative dysfunction 94.8% of 194 - 184 is the unique consistent integer (184/194=94.8%); no count printed |
| R00761 | COMPOSITE | 667 | 2250 | Composite loss of taste or smell within 24h of positive test (CFCT program); strata sum checks pass |
| R00765 | EXCLUDE |  |  | Infection status by respondent declaration (self-report confirmation); test type not stated |
| R00770 | EXCLUDE |  |  | Denominator includes serology-negative and clinical-signs-only volunteers (mixed confirmation incl. unconfirmed); confirmed-only frequency not extractable |
| R00774 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R00779 | POOL | 55 | 187 | GGT hypogeusia during acute phase (within 15 days of symptom onset) |
| R00782 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00786 | POOL | 38 | 100 | Taste identification test disorder 38/100 in COVID-19 inpatients (healthy controls not in denominator) |
| R00801 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R00824 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R00830 | POOL | 19 | 44 | Events = isolated ageusia 1 + ageusia with anosmia 13 + isolated dysgeusia 5 (Table A1 strata summed); acute-episode retrospective questionnaire |
| R00839 | COMPOSITE | 94 | 259 | Composite strong decrease/loss of taste or smell during first 14 days (Predi-COVID) |
| R00840 | POOL | 10 | 102 | Ageusia 10/102 hospitalised patients |
| R00841 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R00846 | POOL | 1172 | 60194 | Gustatory dysfunction 1172/60194 confirmed cases in national reporting system |
| R00849 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R00855 | POOL | 25 | 58 | Taste Strips gustatory dysfunction at inclusion (PCR within 10 days, acute); subjective figure 27/58 also printed - test-based value pooled |
| R00872 | POOL | 49 | 237 | Loss of taste 49/237 admitted patients |
| R00884 | POOL | 41 | 280 | Hypogeusia 41/280 children; confirmation all laboratory routes (PCR/antigen/serology). Internal inconsistency: both-symptoms 33 (text) vs 32 (abstract); total hypogeusia 41 consistent |
| R00887 | EXCLUDE |  |  | Long-COVID rehabilitation population selected for neurologic symptoms; cross-sectional post-acute assessment, not acute frequency |
| R00902 | EXCLUDE |  |  | Composite outcome is persistent disorders at 3 months (not acute); confirmation not reported |
| R00903 | POOL | 76 | 102 | VERIFY denominator basis: acute taste = both 70 + isolated taste 6 among 102 (12-month questionnaire respondents of 421 initial cohort) / Full-text verified: 102 of 421 completed the second questionnaire; acute-phase taste dysfunction among them = both smell and taste 70 + isolated taste 6 = 76/102 (24.2% response - flagged) |
| R00934 | POOL | 175 | 402 | Gustatory dysfunction 175/402 inpatients. FLAG: possible overlap with R01085 (same hospital/authors, different sampling frame - inpatients vs OPD) |
| R00939 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R00951 | COMPOSITE | 209 | 1785 | Composite olfactory/gustatory dysfunction 209/1785 (11.7%) |
| R00980 | COMPOSITE | 425 | 641 | VERIFY denominator: composite 425 (66.3%) implies 641 (table groups 409+232) vs 614 in text / Full-text verified: all internal percentages use N=641 (409 mild = 63.8%; 412 male = 64.3%; smell/taste No 216 + Yes 425 = 641). The '614 recruited' in the paper text is inconsistent with its own tables - 641 used |
| R00987 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01000 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01006 | POOL | 155 | 300 | Events = loss of taste in 59 women + 96 men (printed sex strata summed; percentages reconcile) |
| R01017 | POOL | 214 | 353 | Events = taste disorders 192 (olfactory-dysfunction group) + 22 (no-OD group); group denominators 229+124=353 reconcile |
| R01036 | EXCLUDE |  |  | Outcome is current gustatory deficit at 6-11 month reassessment (follow-up point prevalence, not acute); numerator not printed |
| R01037 | POOL | 41 | 50 | VERIFY numerator: gustatory symptoms during COVID-19 in 82% of 50 (=41) printed as percentage only in settled sheet / Full-text verified: gustatory symptoms during COVID-19 in 82% of 50 = 41 (exact integer) |
| R01045 | POOL | 194 | 322 | Objective gustatory test disorders 194/322 in early-stage (<5 days) patients. Abstract combined counts (192) differ - verify |
| R01058 | POOL | 126 | 241 | Bedside taste test impairment 126/241 (hypogeusia 60 + ageusia 66) |
| R01068 | POOL | 92 | 227 | Taste disorders 92/227 hospitalised patients (medical records) |
| R01073 | POOL | 60 | 80 | VERIFY: GD total = OD+GD 55 + selective GD 5; classification at ~151 days post-negativization - history vs current status unclear / Full-text verified: groups defined by acute-phase history - 'during the acute phase of disease 68.75% had co-present OD + GD' (55/80) plus selective GD 5/80 = gustatory dysfunction 60/80 (assessed ~151 days post-negativization, retrospective classification) |
| R01081 | POOL | 205 | 305 | VERIFY numerator: taste disorder 67.4% at diagnosis; ageusia n=92 is 45% of TD subgroup - TD numerator not directly printed in settled sheet / Full-text verified: Table prints 'Taste disfunction 205 (67.4%)' at diagnosis - numerator omitted from settled sheet |
| R01085 | POOL | 64 | 316 | Dysgeusia 64/316 COVID-positive OPD presenters with influenza-like illness. FLAG: possible overlap with R00934 (same hospital; different frame/period) |
| R01101 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01110 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01115 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01125 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01126 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01129 | EXCLUDE |  |  | Timing: Taste Strips at 8 months after COVID-19 (follow-up point prevalence, not acute) |
| R01137 | COMPOSITE | 54 | 85 | Composite smell and/or taste dysfunction at admission. FLAG: denominator restricted to patients hospitalised with headache complaints; confirmation clinical per MoH guideline (no test named) |
| R01145 | POOL | 91 | 338 | VERIFY numerators: altered taste 26.9% (Omicron cohort n=338) and 57.4% (historical n=441) printed with CIs only in settled sheet / Full-text verified: Table prints Taste 91 (26.9%) for the Omicron-period cohort (n=338). Historical comparator cohort (253/441, 57.4%) not pooled - one row per study |
| R01148 | COMPOSITE | 1676 | 3737 | VERIFY numerator: acute taste disorders 37.8% of 3737 (~1413) printed as percentage only in settled sheet; composite 1676/3737 available / Taste-specific numerator not printed (37.8% only; 1412 vs 1413 ambiguous) - not pooled. Composite smell and/or taste disorders 1676/3737 printed - moved to composite list |
| R01151 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01166 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01168 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01173 | EXCLUDE |  |  | Long-COVID survey population selected for persisting symptoms >=6 months; outcome is persistent gustatory dysfunction (not acute) |
| R01183 | EXCLUDE |  |  | No taste frequency printed (ability ratings only); infection status self-reported test outcome |
| R01185 | POOL | 14 | 51 | VERIFY numerator: Taste Strips hypogeusia 28% of 51 (~14) printed as percentage only. FLAG: same Regensburg source cohort as R01129 (acute phase vs 8-month follow-up; R01129 excluded on timing) / Full-text verified: '14 patients (28%) scoring in the range of hypogeusia' - numerator omitted from settled sheet. Same Regensburg source cohort as R01129 (excluded on timing) |
| R01192 | EXCLUDE |  |  | Infection self-reported only |
| R01193 | EXCLUDE |  |  | Assessment ~131 days post-diagnosis in a subgroup selected for no reported olfactory dysfunction (follow-up assessment, not acute frequency) |
| R01202 | POOL | 169 | 498 | Loss of taste 169/498 (taste-only 24 + both 145 reconcile) |
| R01211 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01216 | EXCLUDE |  |  | Clinician (pediatrician) survey - percentages are respondent proportions, no patient denominator |
| R01217 | EXCLUDE |  |  | Long-term (median 264 days) composite OD/GD prevalence; not acute; no acute taste-specific frequency |
| R01224 | POOL | 184 | 488 | Ageusia at baseline 184/488 paucisymptomatic-mild home-quarantined cases (follow-up subset selection does not affect baseline frequency) |
| R01233 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01236 | POOL | 80 | 300 | Gustatory examination dysfunction 80/300 admitted patients |
| R01237 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01255 | POOL | 201 | 288 | Hypogeusia/ageusia during acute phase 201/288 (inpatients + health workers interviewed >=2 months later) |
| R01260 | EXCLUDE |  |  | Animal/in-vitro (Q2 stratum only); no human frequency denominator |
| R01268 | EXCLUDE |  |  | Timing: gustatory testing at 4 months post-outbreak (follow-up point prevalence, not acute) |
| R01277 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01290 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01294 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01298 | POOL | 21 | 25 | Gustatory dysfunction 13/16 unvaccinated + 8/9 vaccinated = 21/25 physician participants |
| R01300 | POOL | 19 | 58 | SSTT day-1 taste loss = both smell and taste 17 + taste only 2 (printed counts summed); composite was 21/58 |
| R01311 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01321 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01347 | EXCLUDE |  |  | VERIFY: internal discrepancy - dysgeusia 10/86 (Discussion) vs 20 among 35 with OD (Results) / Full-text check confirms irreconcilable internal discrepancy: Results 'of those that had OD, 20 had dysgeusia' vs Discussion 'dysgeusia documented in 10 (11.6%) of our patients' - 20 cannot exceed the stated total of 10 |
| R01361 | POOL | 5 | 25 | VERIFY: loss of taste 20% with ambiguous denominator (30 recruited vs 25 saliva-assessed) / Full-text verified: Figure 1A percentages use the saliva-assessed cohort (n=25; 72% SOB = 18/25); loss of taste 20% = 5/25 as presenting symptom. Mechanistic study - flagged |
| R01369 | POOL | 77 | 224 | Objective dysfunction = mild 36 + moderate 18 + severe 14 + ageusia 9 = 77/224 (224-147 normal). Note symptom-overlap counts imply 76 - 1-person discrepancy flagged |
| R01371 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01378 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01382 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01384 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01388 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01391 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01408 | POOL | 85 | 272 | RT-PCR-positive strata summed across periods: 83/224 + 2/48 = 85/272 |
| R01412 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01413 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01416 | EXCLUDE |  |  | No taste data reported (smell outcomes only); cohort selected on smell loss; infection self-reported |
| R01427 | EXCLUDE |  |  | No extractable frequency: prevalence only in supplementary Table S1 not present in full text / Same study as pooled R02798 (preprint record with extractable data) - not double-counted |
| R01432 | POOL | 41 | 133 | Taste impairment 41/133 hospitalised patients |
| R01445 | EXCLUDE |  |  | No taste prevalence printed; sample selected for reported recovery; confirmation mixed incl. 60.6% self-diagnosed |
| R01476 | POOL | 47 | 80 | Gustatory dysfunction 47/80 hospitalised patients (confirmation: 91% RT-PCR, remainder ECDC clinical/radiological - study-defined confirmed) |
| R01478 | POOL | 172 | 639 | Hypogeusia/dysgeusia 172/639 admitted patients |
| R01479 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01482 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01498 | EXCLUDE |  |  | Letter/editorial without original denominator data |
| R01501 | POOL | 80 | 277 | Gustatory = isolated 25 + both 19.9% of 277 (~55) = 80/277; both-stratum numerator to verify |
| R01503 | EXCLUDE |  |  | Letter/editorial without original denominator data |
| R01506 | POOL | 18 | 171 | Gustatory dysfunction 18/171 diagnosed patients |
| R01518 | POOL | 25 | 46 | Some degree of taste loss 25/46 mild home-managed patients (acute, median 6.5 days since onset) |
| R01519 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R01522 | POOL | 36 | 435 | Gustatory dysfunction 36/435 admitted patients (only gustatory 12 + both 24) |
| R01523 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01526 | EXCLUDE |  |  | Composite anosmia-ageusia percentages only, by self-reported test status; no confirmed-infection numerator/denominator |
| R01529 | EXCLUDE |  |  | No taste frequency printed (figure-only data) |
| R01540 | EXCLUDE |  |  | Animal/in-vitro (Q2 stratum only); no human frequency denominator |
| R01550 | POOL | 98 | 167 | Alteration of taste 98/167 admitted patients |
| R01551 | POOL | 18 | 144 | Dysgeusia 18/144 test-positive at drive-through testing centre (at presentation) |
| R01560 | POOL | 86 | 270 | Ageusia 86/270 patients |
| R01562 | POOL | 215 | 500 | Diminished taste = extreme reduction 163 + moderate reduction 52 = 215/500 (matches printed 43%) |
| R01585 | POOL | 27 | 43 | Gustatory dysfunction 27/43 test-positive at testing centre |
| R01599 | EXCLUDE |  |  | No taste frequency (numerator/denominator) reported |
| R01611 | POOL | 79 | 103 | VERIFY denominator: 79 printed as 76.7% implies N=103 vs final sample 104 / Full-text verified: Table 2 base is 103 (one missing taste response from final sample 104): taste dysfunctions 79 (76.7%) |
| R01612 | POOL | 269 | 574 | Change/loss of taste 269/574 admitted patients |
| R01619 | POOL | 48 | 200 | Ageusia 48/200 isolation-facility patients |
| R01626 | EXCLUDE |  |  | Self-reported diagnoses (Reddit); composite keyword exposure; no valid denominator |
| R01628 | POOL | 54 | 188 | VERIFY counts: taste disturbance 28.7% of 188; type percentages imply 38+13+3=54 / Derived from printed percentages, each mapping to a unique integer: hypogeusia 20.2%=38, ageusia 6.9%=13, parageusia 1.6%=3; total 54/188 = 28.7% as printed |
| R01632 | EXCLUDE |  |  | VERIFY: internal inconsistency - headline 56.2% of 209 vs sensitivity 41.1% and age strata ~41-43% / Full-text check: paper reports taste dysfunction in 56.2% of infected (Table 2) but diagnostic-validity sensitivity of 41.1% for the same quantity in a differently-based analysis; subsample bases unclear and figures irreconcilable |
| R01655 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01669 | POOL | 168 | 268 | Taste involvement at baseline = isolated taste 16 + combined smell and taste 152 = 168/268. FLAG: Trieste Mar 2020 cohort overlaps R00488 Trieste subset (same baseline n=315 source) - cross-stratum overlap, flagged |
| R01672 | COMPOSITE | 114 | 889 | Composite ICD-10 R43 smell and taste disturbances 114/889 COVID-positive registry patients |
| R01676 | COMPOSITE | 117 | 2892 | Composite smell or taste loss 117/2892 hospitalised patients (EHR) |
| R01677 | POOL | 39 | 98 | Ageusia 39/98 admitted patients (isolated 7 + with anosmia 32) |
| R01682 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01692 | EXCLUDE |  |  | Case series n=6 (<10); no population denominator |
| R01695 | EXCLUDE |  |  | REVISED: duplicate cohort - follow-up report (n=97 subset) of the Biadsee cohort whose original report R02365 (67/128) is pooled; same during-disease outcome |
| R01701 | POOL | 184 | 300 | Gustatory dysfunction 184/300 at baseline (within 7 days of onset, home isolation) |
| R01702 | EXCLUDE |  |  | Denominator restricted to subgroup selected for cutaneous manifestations (39 of 997 hospitalised patients) |
| R01705 | COMPOSITE | 22 | 86 | Composite smell/taste dysfunction 22/86 symptomatic admitted patients |
| R01706 | EXCLUDE |  |  | Mixed confirmation: only 161/234 with definitive PCR/antibody diagnosis, remainder presumed clinical; confirmed-subset frequency not extractable |
| R01709 | EXCLUDE |  |  | Convalescent antibody-positive cohort assessed ~7 months after infection; gustatory reduction not established as acute-phase ascertainment |
| R01710 | POOL | 22 | 200 | Ageusia = isolated 14 + with anosmia 8 = 22/200 |
| R01721 | EXCLUDE |  |  | No taste frequency (numerator/denominator) reported |
| R01726 | COMPOSITE | 58 | 93 | Joint hyposmia/dysgeusia item 58/93 (taste-specific not reported); confirmation swab and/or clinical-radiologic with swab-negative excluded |
| R01728 | EXCLUDE |  |  | Denominator restricted to patients selected for anosmia (trial enrolment conditional on anosmia <=15 days) |
| R01729 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01736 | COMPOSITE | 118 | 176 | Composite impaired smell or taste 118/176 COVID-positive survey respondents (test result self-reported) |
| R01737 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01739 | POOL | 242 | 486 | Ageusia 242/486 COVID group (435 RT-PCR-positive + 51 probable clinical - study-defined cases) |
| R01742 | POOL | 54 | 150 | Taste loss 54/150 consecutive diagnosed patients |
| R01745 | POOL | 91 | 151 | Gustatory dysfunction 91/151 (ageusia 59 + dysgeusia 32) |
| R01750 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01758 | POOL | 118 | 195 | Gustatory dysfunction 118/195 RT-PCR-positive health workers (controls not in denominator) |
| R01760 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01761 | EXCLUDE |  |  | Acute-phase numerator not extractable (figures only in Table 2 not reproduced in text; 'most patients' only) |
| R01767 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01777 | POOL | 4 | 58 | Loss of taste (self-report or clinical exam) 4/58 COVID-positive at testing centres (3 self-report + 1 exam) |
| R01778 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01781 | EXCLUDE |  |  | Taste not separable: 438/1000 is smell disturbance with taste abnormalities OR other complaints - not a valid taste or composite frequency |
| R01794 | EXCLUDE |  |  | Taste change reported only for whole survey sample (COVID and non-COVID combined); COVID-subgroup frequency not reported |
| R01822 | POOL | 404 | 5399 | VERIFY denominator: dysgeusia n=404 printed as 6.9% which matches registry N=5868, not analysed N=5399 (7.5%) / Full-text verified: dysgeusia n=404. Paper's 6.9% uses the pre-exclusion registry total (5868); pooled denominator is the analysed clinical-data population (5399), giving 7.5% - flagged |
| R01826 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01840 | EXCLUDE |  |  | Confirmation inadequate: 61.6% never tested, status self-reported; dysgeusia frequency not restricted to confirmed infections |
| R01848 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01851 | POOL | 51 | 1983 | Ageusia (complete loss only assessed) 51/1983 community care facility admissions at presentation questionnaire |
| R01856 | POOL | 153 | 387 | Gustatory dysfunction 153/387 patients |
| R01861 | POOL | 10 | 21 | Taste dysfunction 10/21 symptomatic COVID-19 patients (healthy controls not in denominator) |
| R01864 | EXCLUDE |  |  | VERIFY numerator: loss of taste 20.6% printed without numerator (denominator 1206 included vs 1172 completing follow-up also possible) / Full-text check: loss of taste 20.6% of 1172 with no numerator printed; 241 vs 242 both round to 20.6% - numerator not verifiable |
| R01870 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R01878 | POOL | 39 | 119 | VERIFY GD numerator: salt-alteration 33 (86.8%) implies GD n=38, but GD recovery analysis uses 39 / Full-text verified: '33 referred OD and 39 GD (29 both, 4 only OD, 10 only GD)' - gustatory dysfunction 39/119 admissions |
| R01884 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01885 | EXCLUDE |  |  | Claims-coded counts only (taste disorder 5, mixed 4, with overlapping ICD codes) and two candidate denominators (11018 cases vs 7590 matched claims); frequency not cleanly extractable |
| R01891 | POOL | 69 | 300 | VERIFY: taste disorders = isolated 23 + combined 46 = 69 among 150 with alterations (abstract says 159) - denominator all 300 enrolled / Full-text verified: taste disorders = isolated 23 + combined 46 = 69 (stated directly as 'Sixty-nine patients (46%) reporting taste disorders' among the alteration subgroup); denominator all 300 enrolled. Alteration-total inconsistencies (150/152/159) do not affect the taste components |
| R01899 | POOL | 718 | 1043 | VERIFY denominator: 718 with taste disorders (68.8% of 1043) but 718+286 without = 1004, not 1043 / Full-text verified: 718 (68.8%) of 1043 - mutually consistent. The '286 without taste dysfunction' figure in the paper sums inconsistently (718+286=1004) and appears to use a different subset base - flagged |
| R01900 | POOL | 177 | 274 | VERIFY numerator: dysgeusia 64.6% of 274 (~177) printed as percentage only / Full-text verified: '64.6% (177 participants) reported that they lost their sense of taste' - numerator omitted from settled sheet |
| R01908 | EXCLUDE |  |  | VERIFY: internal inconsistency - 'both dysfunction 66.4% of 250' (=166) conflicts with gustatory counts among 179 with OD (reduced 34.6% + different 31.8% = ~119) / Full-text check confirms irreconcilable figures: '66.4% had both olfactory as well as gustatory dysfunction' (=166/250) conflicts with gustatory breakdown among the 179 with olfactory dysfunction (~119 with GD); taste total not reliably extractable |
| R01916 | POOL | 34 | 141 | Dysgeusia 34/141 adolescents with mild-moderate COVID-19 |
| R01917 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01920 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R01923 | POOL | 19 | 51 | Subjective taste alteration 19/51 consecutive hospitalised patients |
| R01926 | POOL | 1205 | 2579 | VERIFY numerator: gustatory dysfunction 46.8% of 2579 (~1207) printed as percentage only / Full-text verified: '1205 (46.8%) patients complained of subjective GD' - numerator omitted from settled sheet |
| R01938 | POOL | 33 | 94 | Taste impairment = taste only 3 + both smell and taste 30 = 33/94 inpatients (test-based) |
| R01941 | EXCLUDE |  |  | VERIFY numerators: normogeusic 49.8% / ageusic 33.1% of 217 printed as percentages only (dysfunction ~109 if counts reconcile) / Full-text check: only percentages printed (normogeusic 49.8%, ageusic 33.1%); percentages do not reconcile to a unique count set (33.1% of 217 is not an integer share) |
| R01943 | POOL | 20 | 152 | Dysgeusia 20/152 admitted patients |
| R01944 | COMPOSITE | 93 | 311 | Composite anosmia/ageusia in 93/311 test-positive community participants (PCR and/or IgG) |
| R01953 | EXCLUDE |  |  | Taste-gustatory dysfunction reported only for whole sample (13/809 incl. negatives); frequency among 58 confirmed positives not extractable |
| R01955 | EXCLUDE |  |  | No taste-specific prevalence printed (gustatory grouped with olfactory); cohort selected for olfactory dysfunction |
| R01957 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R01962 | POOL | 525 | 1022 | VERIFY numerator: ageusia 51.4% of 1022 (~525) printed as percentage only / Numerator derived: ageusia 51.4% of 1022 - 525 is the unique consistent integer (525/1022=51.4%); no count printed |
| R01965 | POOL | 76 | 718 | Altered taste 76/718 admitted mild-moderate patients (baseline day 3 post-PCR) |
| R01970 | COMPOSITE | 32 | 53 | Composite smell/taste dysfunction 32/53 COVID-positive (surveyed 4 weeks after treatment; retrospective) |
| R01978 | POOL | 54 | 78 | VERIFY: UK taste dysfunction 69.2% - London cohort denominator/numerator not clear in settled sheet (Padua subset was smell-selected) / Full-text verified: London cohort Table - taste dysfunction 54 (69.2%) of 78 London HCWs (Padua subset was smell-selected and is not used) |
| R01986 | POOL | 47 | 100 | VERIFY numerator printed: taste dysfunction 47% of 100 severe COVID-19 patients on objective testing / Full-text verified: taste dysfunction in 47% of the 100 objectively tested severe COVID-19 patients = 47/100 |
| R01991 | COMPOSITE | 22 | 108 | VERIFY numerator: composite anosmia and/or ageusia 20.4% of 108 (~22) printed as percentage only / Full-text verified: Table 1 - Ageusia/anosmia Yes 22 (20.4%) of 108 |
| R02002 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R02030 | POOL | 25 | 59 | Self-reported taste loss 25/59 COVID-19 patients (grouping by smell loss does not restrict denominator) |
| R02057 | POOL | 92 | 410 | Taste dysfunction 92/410. FLAG: same centre (ESIC Faridabad) as R00934/R01085 but earlier period (May-Jun 2020 vs Jul-Sep/Sep 2020) |
| R02062 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R02064 | POOL | 49 | 1065 | Taste disorder 49/1065 admitted confirmed patients (EHR) |
| R02070 | POOL | 29 | 73 | Hypogeusia/ageusia 29/73 admitted patients. FLAG: same hospital (Oswaldo Cruz Recife) as R01255, overlapping period - possible partial overlap |
| R02077 | POOL | 62 | 217 | Dysgeusia 62/217 hospitalised surveillance cases |
| R02082 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02084 | COMPOSITE | 28 | 59 | Composite 'loss of tasting and smelling' 28/59 - FLAG: denominator is symptomatic residents only (of 128 confirmed quarantined) |
| R02094 | COMPOSITE | 15 | 62 | Composite olfactory or gustatory dysfunction on admission 15/62 isolation-facility patients; taste-specific for full cohort not reported |
| R02103 | POOL | 64 | 76 | Psychophysical taste dysfunction 64/76 confirmed cases at screening centres |
| R02107 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R02116 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02125 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R02128 | POOL | 103 | 327 | Confirmed-only strata summed: hospitalised 26/198 + hospital outpatients 77/129 = 103/327; untested primary-care stratum (27/63) excluded from pool |
| R02135 | EXCLUDE |  |  | Familial case cluster n=7 (<10); 5/7 cases presumed (not confirmed) |
| R02137 | POOL | 25 | 230 | Self-reported taste dysfunction 25/230 patients |
| R02139 | EXCLUDE |  |  | Denominators mix patients (556) and evaluations (801); aggregate report overlapping the group's previously published cohorts (duplicate-series aggregation) |
| R02140 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02145 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02154 | POOL | 66 | 111 | Dysgeusia 66/111 surveyed survivors of ED cohort (34% response - noted) |
| R02156 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02166 | POOL | 23 | 196 | Gustatory dysfunction = taste only 9 + both 14 = 23/196 (3-month post-discharge interview, acute history). Paper prints 39/196 as both 19.9% and 9.7% - abstract value correct |
| R02180 | EXCLUDE |  |  | Case series n=3 selected for olfactory/gustatory dysfunction |
| R02181 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R02196 | EXCLUDE |  |  | VERIFY numerator: decreased general taste 76.2% of 655 (~499) printed as percentage/CI only; severe/total subset 298 printed / Full-text check: decreased general taste 76.2% of 655 with no numerator; subgroup derivations disagree (497-500) - numerator not verifiable |
| R02199 | POOL | 5 | 57 | VERIFY: ageusia 5/57 in text vs Table 1 strata summing to 4 (0/34 + 4/23) / Full-text verified: text states 'Ageusia was reported by only 5/57 (8.7%) patients' - pooled as printed. FLAG: Table 1 strata (0/34 + 4/23) sum to 4 - one-patient discrepancy in the paper |
| R02205 | POOL | 128 | 197 | Loss of taste 128/197 COVID-positive outpatients (controls not in denominator) |
| R02208 | POOL | 526 | 1197 | Dysgeusia 526/1197 confirmed patients (outpatient 434 + inpatient 92 strata reconcile) |
| R02210 | POOL | 28 | 141 | Any ageusia 28/141 primary-care patients (alone 16 + with anosmia 12) |
| R02218 | EXCLUDE |  |  | Animal/in-vitro (Q2 stratum only); no human frequency denominator |
| R02229 | POOL | 17 | 60 | Ageusia 17/60 hospitalised pneumonia patients |
| R02238 | POOL | 91 | 138 | Any gustatory dysfunction at baseline (within 4 days of onset) = isolated 22 + combined 69 = 91/138 |
| R02244 | EXCLUDE |  |  | Duplicate/overlapping cohort: same hospital (Nord Franche-Comte, Trevenans) and period subset (1-14 Mar 2020, n=70) of R01017 ANOSVID cohort (1 Mar-31 May 2020, n=353) which is pooled - excluded to avoid double counting |
| R02248 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02249 | POOL | 76 | 106 | Gustatory impairment at T0 = 30+17+24+5 = 76/106 (strata sum). Abstract prints 65.6% for 76 cases - arithmetic error in paper (76/106=71.7%) |
| R02264 | POOL | 161 | 230 | Taste alteration 161/230 healthcare workers |
| R02265 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02278 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02279 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02280 | EXCLUDE |  |  | Letter/response with no primary data (cites other studies) |
| R02285 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02291 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02294 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02295 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02302 | POOL | 81 | 172 | Loss of taste 81/172 patients (severity strata 11+18+52 reconcile) |
| R02313 | POOL | 33 | 86 | Hypogeusia 33/86 hospitalised patients |
| R02319 | EXCLUDE |  |  | Duplicate cohort of R01701: identical N=300, mean age 43.6, 75% female, and identical gustatory-dysfunction total (184) - same Bologna (Bellaria-Maggiore) series; R01701 retained |
| R02322 | POOL | 135 | 151 | Gustatory dysfunction 135/151 home-quarantined patients (recruited via prior survey - self-selection flag) |
| R02332 | EXCLUDE |  |  | Letter/editorial without original denominator data |
| R02333 | EXCLUDE |  |  | Case-control design (no population denominator) |
| R02336 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02346 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02349 | POOL | 24 | 42 | Loss of taste 24/42 laboratory-confirmed household cases |
| R02354 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02358 | POOL | 14 | 42 | Dysgeusia 14/42 hospitalised mild COVID-19 patients |
| R02362 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02365 | POOL | 67 | 128 | Changes in taste during disease 67/128 hotel-quarantined patients (original report of the Biadsee cohort) |
| R02366 | POOL | 100 | 394 | Gustatory dysfunction vs full screened denominator as printed: isolated 7 + with olfactory 93 = 100/394 PCR-confirmed screened patients |
| R02375 | EXCLUDE |  |  | VERIFY: taste-involved combinations printed as percentages (33+32+6+2+5+1=79%) with unclear base (115 vs 81 with disorders) / Full-text check: taste-involved combination percentages (of the 81 with disorders) derive inconsistently (64 vs 65) and parageusia/cacogeusia cases are additional - taste total not reliably extractable |
| R02380 | POOL | 92 | 198 | Taste disorder 92/198 test-positive primary-care patients (at presentation, pre-result) |
| R02385 | POOL | 46 | 64 | Any taste dysfunction = 64 - 18 normal taste = 46/64 (type categories overlap and were not summed) |
| R02389 | POOL | 32 | 56 | VERIFY numerator: dysgeusia/ageusia as overall symptom in 57.1% of 56 positive survey completers (~32) / Numerator derived: dysgeusia/ageusia as overall symptom in 57.1% of 56 positive survey completers = 32 (unique integer; Table 1) |
| R02390 | POOL | 89 | 141 | Ageusia 89/141 confirmed cases (community 57/92 + admitted 32/49 reconcile) |
| R02391 | POOL | 41 | 100 | Gustatory dysfunction 41/100 discharged patients (illness history at 1-month interview) |
| R02393 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R02394 | POOL | 923 | 1942 | Taste disorder 923/1942 home-isolated patients (sex strata reconcile) |
| R02414 | COMPOSITE | 26 | 63 | Composite loss of smell and/or taste 26/63 hospitalised patients (taste testing in 10 patients showed normal function - noted) |
| R02419 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02430 | POOL | 67 | 103 | VERIFY counts: gustatory dysfunction 65.0% of 103; decreased 25.2% (~26) + none 39.8% (~41) implies 67 / Derived from printed percentages, all reconciling uniquely: decreased 25.2%=26 + none at all 39.8%=41 = 67/103 (65.0% as printed) |
| R02433 | POOL | 52 | 72 | Dysgeusia = isolated 18 + with anosmia 34 = 52/72 PCR-positive primary-care patients |
| R02438 | POOL | 62 | 95 | Dysgeusia 62/95 PCR-positive outpatients. FLAG: same hospital (Nord Franche-Comte) as R01017 - different sampling frame (presenters grouped by result), possible partial overlap |
| R02443 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R02455 | COMPOSITE | 488 | 3191 | Composite anosmia or ageusia 488/3191 newly diagnosed patients |
| R02464 | EXCLUDE |  |  | Correspondence reporting preliminary composite figures (~80%) with no primary numerator/denominator |
| R02488 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02506 | POOL | 342 | 385 | Gustatory dysfunction 342/385 assessed (32 who did not remember excluded by authors) |
| R02693 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02694 | EXCLUDE |  |  | VERIFY: poorer taste sensitivity in 30% (Results) vs 35% (Discussion) of 39 positives; no counts printed / Full-text check: poorer taste sensitivity in 30% (Results) vs 35% (Discussion) of 39 positives; no counts printed - discrepant and unverifiable |
| R02697 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02704 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R02709 | EXCLUDE |  |  | Animal/in-vitro (Q2 stratum only); no human frequency denominator |
| R02711 | COMPOSITE | 66 | 144 | FULL-TEXT VERIFIED: no taste-separable numerator printed - VOTT+ group (66/144 PCR-positive) is combined smell-and-taste test dysfunction; within-group percentages lack counts. Placed in composite stratum per protocol taste-specific rule; R02729 excluded as its duplicate (see log) |
| R02714 | EXCLUDE |  |  | Duplicate cohort of R00572: same Omicron BA.1 study (baseline 338, follow-up 294, taste involvement 85) - Research Square preprint version; journal version R00572 pooled |
| R02718 | COMPOSITE | 554 | 1211 | Composite loss of smell/taste in 554/1211 staff with SARS-CoV-2 IgG detected (either assay) |
| R02729 | EXCLUDE |  |  | Duplicate cohort: preprint of R02711 (same cohort); published version pooled instead |
| R02737 | COMPOSITE | 18 | 231 | Composite anosmia and/or ageusia 18/231 hospitalised patients |
| R02770 | EXCLUDE |  |  | No taste prevalence printed; infection self-reported |
| R02773 | POOL | 209 | 772 | Gustatory dysfunction 209/772 (ageusia 152 + hypogeusia 44 + parageusia 13 reconcile) |
| R02774 | POOL | 72 | 305 | VERIFY: gustatory categories among 103 with OGD are percentages only (sum 69.9% of 103, ~72); whole-cohort GD prevalence not printed / Derived from printed category percentages among the 103 with OGD, each mapping to a unique integer: isolated hypogeusia 17 + isolated ageusia 14 + hyposmia/hypogeusia 17 + hyposmia/ageusia 14 + anosmia/dysgeusia 8 + anosmia/ageusia 2 = 72/305 |
| R02798 | POOL | 42 | 187 | Taste disorders 42/187 (22.46%). NOTE: same study as R01427 (published letter, Wuhan, 3-15 Apr 2020, N=187) whose numbers sat in an unavailable supplement - preprint record carries the data; R01427 not double-counted |
| R02856 | EXCLUDE |  |  | Duplicate cohort: follow-up preprint of the Biadsee cohort (original R02365 pooled; journal follow-up R01695 also duplicate) |
| R02872 | EXCLUDE |  |  | Duplicate record of R02358: identical Levinson Tel Aviv cohort (admitted 45, analysed 42, dysgeusia 14/42) |
| R02883 | EXCLUDE |  |  | Not a primary study (review); no primary denominator |
| R02897 | EXCLUDE |  |  | Duplicate: conference abstract of R01739 (same Montefiore cohort, N=486, ageusia 50%); abstract percentages internally impossible (both 58% > anosmia 33%) |
| R02911 | COMPOSITE | 56 | 105 | Combined smell and taste dysfunction 56/105. FLAG: sex counts as printed sum to 95, not 105 - denominator per stated total |
| R02932 | EXCLUDE |  |  | Duplicate record of R02349: identical Dawson household study (90 enrolled, 42 cases, taste loss 24/42) |
| R02945 | POOL | 54 | 65 | Taste dysfunction 54/65 quarantined hospital patients (confirmation PCR and/or CT - study-defined) |
| R02954 | EXCLUDE |  |  | Case report (<10 / no population denominator) |
| R02974 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R03352 | EXCLUDE |  |  | Denominator selected by chemosensory-symptom status (by-design sampling); no population denominator |
| R03416 | EXCLUDE |  |  | Registry record with no results posted (hasResults: false); registry case-control design |
| R03494 | EXCLUDE |  |  | Registry record with no results posted (hasResults: false) |
