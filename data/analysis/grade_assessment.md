# GRADE Certainty Assessment — Loss of taste in viral infections (Cochrane-level systematic review, Raphael Malikian)

**Assessor role:** GRADE assessor, Phase 4 synthesis. **Date:** 2026-11-21.
**Sources used (only):** `protocol-locked.md` (critical outcomes: complete recovery, any recovery, time to recovery, any adverse event, serious adverse events, discontinuation due to AEs); `analysis/synthesis/analysis_log.md`; the `*_result.json` files in `analysis/synthesis/` (every pooled number below was read from the JSON, not from the brief); `analysis/synthesis/q1_recovery_analysis_set.json`; `analysis/synthesis/q3_treatment_table.csv` + `q3_treatment_synthesis.md`; `analysis/rob/rob_adjudicated_full.csv` (per-pool RoB distributions computed from this file).
**Abstract-only stratum:** excluded from all primary GRADE ratings, per the locked protocol amendment (abstract-only records do not contribute to primary GRADE).

## Conventions and starting points

- **Q1 frequency and recovery (non-comparative proportions / natural history):** rated under the GRADE approach for prognosis/prevalence-type questions, in which a body of cohort/observational evidence addressing the question **starts at HIGH** and is downgraded for the five domains. This is the more generous of the two defensible conventions; under the classic intervention convention (observational starts LOW) every rating below would be the same or lower, so no conclusion in this document depends on the choice. RoB labels for these pools are the adjudicated JBI bands in `rob_adjudicated_full.csv` (Low / Moderate / Moderate (some concerns) / High).
- **Q3 treatment effects:** RCT bodies **start HIGH** (RoB 2); non-randomised bodies start LOW (ROBINS-I). Where a treatment has both, the rating is anchored on the randomised body and the non-randomised evidence is discussed, not pooled.
- **Q3 harms (cross-intervention body):** the body is dominated by uncontrolled and observational reports with one RCT; it **starts LOW**.
- **Inconsistency** is judged on I², tau² and the 95% prediction interval (PI), not on I² alone. A PI that spans clinically incompatible values is treated as the operative evidence of inconsistency.
- **Indirectness — standing issue for the whole review:** the review question covers viral infections generally, but **every pooled study and every treatment study is SARS-CoV-2** (frequency pool virus count verified: 137/137 SARS-CoV-2; Q3 set: 23/23 SARS-CoV-2). No influenza or other-virus study met any pool mapping. Each rating below therefore carries a virus-scope indirectness judgement for the question as locked; where a rating is already at the floor this is recorded but cannot lower it further. Ratings are, in substance, ratings of the SARS-CoV-2 evidence read against a broader question.
- **Publication bias:** no funnel plot, Egger test or other small-study assessment exists anywhere in the analysis set (searched `analysis/` — none performed). For the proportion pools, funnel asymmetry is in any case uninterpretable at I² ≈ 99%. Judgements below therefore record publication bias as *not formally assessable / undetected* and do **not** downgrade for it except where non-reporting is directly documented (harms, §7). The protocol's pre-named pressure point — absent trial registration for most treatment studies — is handled under RoB/reporting for the individual trials.
- **Upgrading:** considered for every body (large effect, dose–response, opposing residual confounding). **No body is upgraded**, for the reasons stated per outcome. The one very large effect in the review (photobiomodulation) comes from a single small RCT with Some-concerns RoB; GRADE large-effect upgrading applies to observational bodies and is not used to rescue a downgraded single small trial.

---

## 1. (a) Acute taste-dysfunction frequency — SARS-CoV-2, taste-specific

**Body:** 137 studies, N = 155,010 (crude 38,607/155,010 = 24.9%). Pooled **37.7% (95% CI 32.9–42.7)**, tau² (logit) 1.44, **I² 99.5%**, **95% PI 5.3–86.7%** (`q1_freq_all_result.json`). Subgroups: psychophysical testing k = 15, 47.4% (37.0–58.1), I² 93.8%, PI 14.7–82.5; self-report k = 122, 36.5% (31.4–41.9), I² 99.6%. Hospitalised 26.8% vs community 39.6%. Low-RoB sensitivity excluding the 60,194-person registry R00846: 47.3% (37.6–57.1), k = 33, I² 98.0%, PI 8.6–89.6 (`q1_freq_lowrob_excl_R00846_result.json`).
**Adjudicated RoB of the 137 (computed):** Low 34, Moderate 72, Moderate (some concerns) 20, High 11; tools: JBI analytical cross-sectional 73, JBI cohort 60, JBI case-control 1, JBI case series 3.
**Start:** HIGH (prognosis/prevalence convention, §Conventions).

| Domain | Judgement | Reason |
|---|---|---|
| Risk of bias | **Downgrade −1 (serious)** | Only 34/137 studies are Low RoB; 103/137 are Moderate or worse and 11 are High. Ascertainment is self-report in 122/137 studies, with no validated instrument in most (the recurring JBI rationale in the RoB file), and several large studies use convenience/crowdsourced sampling. Mitigating, and why this is −1 not −2: the estimate is not an artefact of the worst studies — the Low-RoB sensitivity pool is *higher* (44.4% with R00846; 47.3% excluding it) than the main pool, and the psychophysical subgroup (47.4%) brackets the main estimate from above. |
| Inconsistency | **Downgrade −2 (very serious)** | I² 99.5% with tau² 1.44 on the logit scale. The 95% PI (5.3–86.7%) spans frequencies that would support entirely different conclusions about how common taste dysfunction is; the pooled mean is an average across settings, not a common frequency (the analysis log states this explicitly). Pre-specified subgroups explain part of it (hospitalised 26.8% vs community 39.6%; psychophysical 47.4% vs self-report 36.5%) but every subgroup retains I² ≥ 93.8% and a PI wider than 55 percentage points, so subgrouping does not rescue consistency. |
| Indirectness | **Downgrade −1 (serious)** | (i) Virus scope: 137/137 studies are SARS-CoV-2 against a question covering viral infections generally; there is no pooled evidence for influenza or any other virus. (ii) Measurement: "taste" is predominantly self-reported chemosensory complaint, which the protocol itself flags as liable to olfactory misattribution (theory T4); only 15/137 studies used psychophysical gustatory testing. Settings and pandemic phases also vary widely, but that variation is charged to inconsistency, not double-counted here. |
| Imprecision | No downgrade | For the pooled mean: N = 155,010 and CI width ≈ 10 percentage points (32.9–42.7) is precise. The uncertainty that matters — dispersion of true frequencies — is already charged to inconsistency via the PI. |
| Publication bias | Not downgraded (unassessable) | No small-study assessment performed; uninterpretable at this heterogeneity. Early-pandemic, English-language, non-registered prevalence reporting makes bias plausible, but there is no documented evidence of it in the analysis set, and the rating is already at the floor. |

**FINAL: VERY LOW** (HIGH −1 RoB −2 inconsistency −1 indirectness; arithmetic exceeds the floor).
**Interpretation constraint:** the defensible quantitative statements are the subgroup estimates and the PI, not the single pooled mean.

---

## 2. (b) Complete taste recovery, by window (taste-specific pools; different study sets per window — not a within-cohort trajectory)

### 2.1 Complete recovery ≤4 weeks
**Body:** k = 10, N = 976 (774 events). Pooled **87.4% (69.7–95.4)**, I² **93.5%**, tau² 2.06, **PI 17.3–99.6%** (`q1_rec_complete_le4_result.json`). RoB of the 10: Moderate 6, Moderate (some concerns) 3, High 1 (all JBI cohort except one cross-sectional). **Start:** HIGH.

- **RoB −1:** no Low-RoB study in the pool; one High; recovery predominantly self-reported at heterogeneous early timepoints (day 7 to day 28 within one "window").
- **Inconsistency −2:** I² 93.5%; the PI (17.3–99.6%) covers nearly the entire scale — a new comparable cohort could plausibly show almost any complete-recovery proportion.
- **Indirectness −1:** all SARS-CoV-2 vs the general viral question; the ≤4-week window mixes assessments from day 7 to day 28 and survey-recall with test-based ascertainment, so the outcome as pooled is not one timepoint.
- **Imprecision −1:** N = 976 across 10 small cohorts; CI spans 69.7–95.4% (≈26 points), crossing values with different implications for counselling about early recovery. (Charged once; the PI dispersion is under inconsistency.)
- **Publication bias:** not assessable at k = 10; not downgraded.

**FINAL: VERY LOW.**

### 2.2 Complete recovery >4–12 weeks
**Body:** k = 11, N = 2,085 (1,789 events). Pooled **85.2% (70.0–93.5)**, I² **95.0%**, tau² 1.67, **PI 21.2–99.2%** (`q1_rec_complete_4to12_result.json`). RoB: Moderate 6, Moderate (some concerns) 5, Low 0. **Start:** HIGH.

- **RoB −1:** no Low-RoB study; all Moderate or Moderate (some concerns).
- **Inconsistency −2:** I² 95.0%; PI 21.2–99.2% is again near-scale-wide. One large cohort (C8932, 635/701 at mean 63 days) sits alongside small cohorts with materially lower proportions; no subgroup analysis resolves this.
- **Indirectness −1:** all SARS-CoV-2; window mixes 30-day to ~90-day assessments including median-timepoint survey reports (e.g. median 52 and 61 days), so "recovery by >4–12 weeks" is not measured at a uniform time.
- **Imprecision −1:** CI 70.0–93.5% (≈24 points) despite the largest N of the three windows; the width is heterogeneity-driven but the resulting uncertainty about the mean proportion is real and is additional to the PI judgement.
- **Publication bias:** not assessable at k = 11; not downgraded.

**FINAL: VERY LOW.**

### 2.3 Complete recovery >12 weeks
**Body:** k = 9, N = 1,012 (856 events). Pooled **87.8% (69.5–95.8)**, I² **88.1%**, tau² 1.52, **PI 23.7–99.4%** (`q1_rec_complete_gt12_result.json`). RoB: Low 2, Moderate 3, Moderate (some concerns) 4 (all JBI cohort). **Start:** HIGH.

- **RoB −1:** only 2/9 Low; late follow-up cohorts are exposed to attrition and to conditioning on persistence (several cohorts were assembled through follow-up of symptomatic patients), and the analysis set retains a visible anomaly (R01110: 186/214 recovered at day 90 but 150/214 at mean 9.5 months, with the latest-timepoint rule placing 150/214 in this pool) — internal non-monotonicity of that kind is a measurement/attrition warning for the whole window.
- **Inconsistency −2:** I² 88.1% is the lowest of the three windows but still high, and the PI (23.7–99.4%) remains near-scale-wide; study timepoints range from 90 days to 18 months.
- **Indirectness −1:** all SARS-CoV-2; ">12 weeks" pools 90-day status with 8.4-month, 9.5-month and 18-month status — these are different clinical questions (early-persistent vs long-term recovery) averaged together; cohorts reaching this window are survivors of earlier follow-up, not the incident population.
- **Imprecision −1:** N = 1,012, k = 9; CI 69.5–95.8% (≈26 points).
- **Publication bias:** not assessable at k = 9; not downgraded.

**FINAL: VERY LOW.**
**Cross-window note:** the three pooled means (87.4 / 85.2 / 87.8%) must not be read as a flat recovery trajectory — the study sets differ per window, and each window's PI is near-scale-wide.

---

## 3. (c) Any (complete or partial) taste recovery

### 3.1 Any recovery >12 weeks
**Body:** k = 5, N = 325 (302 events). Pooled **90.3% (80.6–95.4)**, I² **44.1%**, tau² ≈ 0.00, **PI 78.6–95.9%** (`q1_rec_any_gt12_result.json`). RoB of the 5: Low 3, Moderate 2 (all JBI cohort). **Start:** HIGH.

- **RoB — no downgrade:** this is the strongest RoB profile of any Q1 pool (3 Low, 2 Moderate, none worse). Residual concerns (self-reported "partial" recovery thresholds) are charged under indirectness.
- **Inconsistency — no downgrade:** I² 44.1% with Q p = 0.13 and a PI (78.6–95.9%) that stays within one interpretation — most followed patients have at least partially recovered by >12 weeks. This is the only pool in the review whose PI does not cross a decision-relevant boundary.
- **Indirectness −1:** all SARS-CoV-2 vs the general viral question; "any recovery" thresholds for *partial* recovery are study-defined and not standardised, so the outcome is a family of related outcomes rather than one outcome.
- **Imprecision −1:** k = 5 and N = 325 is a small body for a critical outcome; the CI (80.6–95.4%) is ≈15 points wide and the estimate rests on few cohorts, so a small number of additional studies could move it materially.
- **Publication bias:** not assessable at k = 5; not downgraded.

**FINAL: LOW** (HIGH −1 indirectness −1 imprecision).

### 3.2 Any recovery >4–12 weeks — EVIDENCE GAP
**No study reported any (complete-or-partial) taste recovery separably in this window. The cell is empty and was not filled** (analysis log; recovery analysis set contains no such row). **No GRADE rating is possible — this is absence of evidence, not very-low-certainty evidence**, and it must appear in the Summary of Findings as an explicit empty row so the gap is visible rather than silently omitted.
For completeness: any recovery ≤4 weeks rests on a single study (R02302, 63/81 = 77.8% at day 20; RoB High in the analysis set listing for that row's cohort) and is not pooled; if rated it would be VERY LOW (single study, High RoB, imprecision, indirectness).

---

## 4. (d) Time to recovery (narrative evidence only)

**Body:** no pooled estimate exists and none was forced (protocol-compliant). 118 settled records carry a non-blank time-to-recovery field, in mutually incompatible forms: medians/means among recoverers only (e.g. median taste recovery 9 days, R01068; 12 days, R00322; 14 days, R00494; mean ageusia duration 3.17 weeks, R00618), Kaplan–Meier estimates without crude events (excluded from pooling, e.g. R01224, R02322 — the latter internally inconsistent: KM 86.8% vs abstract 82% at 30 days), duration bands as percentages of whole infected cohorts rather than of those with dysfunction (e.g. R00561), and composite smell-and/or-taste durations presented alongside taste-specific ones (e.g. R00334: mean 1.47 years among recoverers, composite).
**Start:** HIGH (prognosis convention) — the rating falls on the domains.

- **RoB −1:** durations are largely retrospective self-report/survey recall; several are conditioned on having recovered (means/medians *among recoverers*), which structurally excludes non-recoverers and biases durations downward.
- **Inconsistency −1:** reported central values range from ~9 days to ~3 weeks for taste-specific medians/means, with other reports (bands, KM curves, the composite 1.47-year mean among recoverers in a long-COVID survey population) describing plainly different populations and estimands; there is no single quantity the reports agree on. (−1 rather than −2 because no pooled I²/PI exists to demonstrate very serious inconsistency formally; the incompatibility of forms is charged jointly here and under indirectness.)
- **Indirectness −2:** the estimand itself shifts across studies — time-to-recovery among recoverers vs KM cumulative recovery vs duration bands over the whole infected cohort — and a substantial share of the duration data is composite smell/taste, not taste. All SARS-CoV-2 adds the standing virus-scope indirectness.
- **Imprecision −1:** no pooled estimate or CI exists; individual reports rarely carry a measure of spread usable across studies.
- **Publication bias:** not assessable for a narrative body; not downgraded separately.

**FINAL: VERY LOW.** The only defensible manuscript statement is a ranged narrative ("in the cohorts reporting taste-specific medians, typically 9–14 days, with a long tail"), explicitly labelled very-low certainty.

---

## 5. (e) Treatment effects on taste outcomes, per intervention (Q3)

Frame for all of §5: 23 treatment studies, all SARS-CoV-2. Only **3 RCTs report any effect estimate** (prednisolone, photobiomodulation, zinc); a fourth RCT (cerebrolysin, R03352) has no results. Everything else is uncontrolled pre-post (ROBINS-I Serious), single-arm, or exposure-descriptive, and — critically — **spontaneous recovery is a complete competing explanation for every uncontrolled improvement reported**, given §2–§3 (roughly 85–90% pooled recovery over time without any treatment attribution). Uncontrolled Q3 findings are therefore not rated as effect evidence for any intervention; they are noted where they conflict with the randomised evidence.

### 5.1 Prednisolone (oral) — C9634 / COCOS
**Body:** 1 RCT, double-blind placebo-controlled, RoB 2 **Low** (all domains Low). Prednisolone 40 mg/day × 10 days + olfactory training vs placebo + olfactory training; 58 vs 57 randomised (57 vs 56 at follow-up). At 12 weeks: Taste Strip Test median 11 (IQR 9–13) vs 11 (9.3–13), **difference 0.00 (95% CI −1.00 to 1.00), p = 0.50**; taste VAS difference **0.1 (−1.00 to 1.3), p = 0.80**. No taste-recovery proportion is reported. **Start:** HIGH.

- **RoB — no downgrade:** Low on all five RoB 2 domains.
- **Inconsistency — not assessable** (single trial); not downgraded, and the absence of replication is charged under imprecision.
- **Indirectness −1:** (i) the cohort was sampled on **persistent olfactory disorders** (objective hyposmia/anosmia required); gustatory function was a **secondary outcome** in a cohort not selected for taste dysfunction — the taste question is answered in an olfaction-defined population; (ii) the trial reports **score outcomes only** — for the review's *critical* outcomes (complete/any recovery proportions) this trial provides **no evidence at all**, and the rating here applies to gustatory score, an important-but-not-critical outcome; (iii) all participants received olfactory training, so the estimand is prednisolone *added to* training; (iv) standing virus-scope indirectness (SARS-CoV-2, persistent >4 to ≤12 weeks only).
- **Imprecision −1:** single trial, n = 115. The score CIs are narrow around zero (±1 TST point) and do exclude large score effects, which is why this is −1 and not −2; but with one unreplicated trial and no recovery-proportion data, the optimal information size for the review's critical outcomes is not met.
- **Publication bias:** single registered-trial body; not assessable, not downgraded.
- **Supportive/conflicting non-randomised evidence (not rated):** every positive steroid-associated finding is uncontrolled or bundled (R00232 pre-post prednisolone+zinc, ROBINS-I Serious; R00356 multi-drug protocol, Serious; R01388 non-randomised bundle, Serious) and is fully explained by natural history per §2. Direction is inconsistent across design tiers, which reinforces — but is not needed for — the rating.

**FINAL: LOW** for the effect of oral prednisolone on gustatory function scores at 12 weeks (no effect found). **No evidence** from this trial for complete/any recovery proportions.

### 5.2 Photobiomodulation / low-level laser therapy — R00627
**Body:** 1 RCT, 1:1 blinded, RoB 2 **Some concerns** (D1 randomisation Some concerns; D2–D5 Low). Single-session diode laser to the tongue (settled dose 940 nm, 1 W, 4 J/cm², 6 min; the paper's abstract conclusion says 810 nm — internal discrepancy as printed) vs placebo light; **18 vs 18**, persistent taste loss ≥4 weeks. Complete taste restoration at 1 month **17/18 (94.4%)** laser (p < 0.001 vs placebo; the placebo arm's complete-restoration count is not printed — partial restoration 7/18 (38.9%) was more frequent with placebo, p = 0.041); 13/18 (72.2%) of the laser group had restored taste at 1 week vs 13/18 (72.2%) of placebo only at 4 weeks (p < 0.001). AEs not reported. The only other PBM study (R01311, n = 10, ROBINS-I Serious, uncontrolled) reports improvement in all cases with numbers in a figure only. **Start:** HIGH.

- **RoB −1:** Some concerns overall (randomisation process), compounded by the internal 940 nm vs 810 nm discrepancy, which leaves the intervention as delivered not fully certain.
- **Inconsistency — not assessable** (single RCT); not downgraded separately.
- **Indirectness — no downgrade:** population (persistent post-COVID taste loss ≥4 weeks), intervention and outcome (complete taste restoration) map directly onto the review question, apart from the standing SARS-CoV-2-only scope, which for a single-intervention rating is noted but not charged again here — the binding problems are RoB and imprecision. Follow-up is 1 month only; durability is unknown (recorded as a limitation, not a downgrade).
- **Imprecision −2 (very serious):** n = 36 total, 18 per arm, single centre, single trial. The headline proportion rests on 17 events in one arm; the comparator arm's complete-restoration count is not even printed, so no confidence interval for the comparative effect can be constructed from the publication. Effects of this apparent size from samples of this size are fragile — a handful of outcome reclassifications would erase the contrast.
- **Publication bias:** not assessable (single small trial, no second trial to compare); not downgraded beyond the above.
- **Upgrading considered and refused:** the effect is large, but large-effect upgrading is a tool for observational bodies; applying it to a single 36-participant RCT with randomisation concerns would invert GRADE's logic.

**FINAL: LOW** (HIGH −1 RoB −2 imprecision).

### 5.3 Zinc — R01955
**Body:** 1 RCT, RoB 2 **High** (D4 measurement High; D1, D2, D5 Some concerns). Zinc sulfate 220 mg (50 mg elemental) twice daily vs no zinc, in **105** patients with olfactory dysfunction (49 vs 56). The only between-group result is **composite**: median duration of recovery of gustatory **and/or** olfactory function significantly shorter with zinc (p < 0.001; no composite medians printed). The printed durations 7 days (5–9) vs 18 days (14–22) are **smell recovery only** (Table 5, full-text verified). **No taste-specific effect estimate exists in this trial.** AEs not reported. **Start:** HIGH.

*Taste-specific outcome:* **NO EVIDENCE — not rateable.** Any GRADE number attached to "zinc for taste recovery" would be a rating of an estimate that does not exist.
*Composite smell-and/or-taste outcome (the only rateable body):*
- **RoB −2 (very serious):** RoB 2 overall High driven by a High measurement domain — recovery judged by unblinded physician decision/self-report with no validated gustatory test, in an open trial with no placebo and no ITT analysis; randomisation and selective-reporting domains also carry Some concerns (no registration/protocol).
- **Inconsistency — not assessable** within the RCT body (single trial). Note, outside the formal domain: the observational zinc signal points the **opposite way** (R00323: oral zinc associated with *lower* odds of total composite recovery, OR 0.24, 95% CI 0.1–0.5; ROBINS-I Serious) — the wider evidence base is directionally contradictory, which is recorded here as context and would preclude any future upgrade.
- **Indirectness −1:** the outcome is a smell-and/or-taste composite in a cohort selected for **olfactory** dysfunction; it cannot isolate a taste effect. Plus standing SARS-CoV-2-only scope.
- **Imprecision −1:** no effect size, no CI and no composite medians are printed — only a p-value (p < 0.001) on n = 105. The magnitude of any composite effect is unquantifiable from the publication.
- **Publication bias:** not assessable; not downgraded.

**FINAL (composite outcome only): VERY LOW** (HIGH −2 RoB −1 indirectness −1 imprecision). **Taste-specific: no evidence.**

### 5.4 Cerebrolysin — R03352 (for completeness)
Registry-record RCT (NCT06208540, n = 160 enrolled), **no results posted (hasResults: false)**. **No evidence — not rateable**, for efficacy or harms. It must appear in the SoF as an explicit no-results row.

---

## 6. (f) Harms across Q3 — any AEs, serious AEs, discontinuation due to AEs

**Body:** of 23 treatment studies, **AE content is present in 6 and "not reported" in 17** — including two of the four randomised studies (R00627 photobiomodulation, R03352 cerebrolysin) and the zinc RCT (R01955). Only **C9634** provides full comparative AE reporting: 3 AEs in the prednisolone group (sleeplessness with psychological disorders requiring deblinding; restlessness with treatment stopped; stomach irritation requiring omeprazole); mild side-effects 9/58 (15.5%) prednisolone vs 5/57 (8.8%) placebo; **no serious AEs**; **3 participants stopped treatment because of side-effects (2 placebo, 1 prednisolone)**. The only other quantitative source is observational and multi-drug: R00323 — 55/483 (11.4%) of medication users reported AEs (chloroquine/hydroxychloroquine 22.4%, azithromycin 14.3%, **oral zinc 13.9%**); most common upper abdominal pain and nausea; **4 subjects (0.8%) had cardiac arrhythmia**; "no other severe adverse events reported". Remaining content: transient expected SGB effects (R00539, n = 6), and two statement-only assurances with no counts (R00356 "always well-tolerated"; R02693 "no adverse events were reported", n = 5), plus one n = 1 note about the *prior* drug (R01519, clonazepam somnolence in an 87-year-old).
**Start:** LOW (body dominated by non-randomised/uncontrolled reports; §Conventions).

- **Risk of bias / reporting bias −1 (floor reached):** non-reporting in 17/23 studies (74%) is documented selective absence, not missing-at-random: harms ascertainment was unsystematic or absent in nearly the whole body, and two of the six "present" sources are unquantified reassurance statements. Zero reported events in such a body is evidence about reporting, not about safety.
- **Inconsistency — not formally downgraded:** there are too few comparable reports for estimates to agree or disagree; the incoherence is charged under RoB/reporting and imprecision rather than double-counted.
- **Indirectness −1 (recorded; floor already reached):** the only multi-user AE rates (R00323) concern self-chosen acute-COVID drug exposures (including agents not given for taste dysfunction) in a composite smell/taste population, not assigned taste treatments; the one directly applicable source (C9634) covers a single 10-day prednisolone course.
- **Imprecision −1 (recorded; floor already reached):** serious events are rare-event outcomes; the entire comparative safety denominator is 115 randomised participants in one trial plus one observational denominator of 483 medication users across many drugs. A zero SAE count in n = 115 cannot exclude clinically important serious harm for any intervention, and for 22 of 23 treatment studies there is no usable safety denominator at all.
- **Publication bias:** subsumed in the documented non-reporting above; not double-counted.

**FINAL: VERY LOW for any adverse events; VERY LOW for serious adverse events; VERY LOW for discontinuation due to AEs.** Discontinuation is the thinnest of the three: the *only* data in the entire review are C9634's 3 stops (2 placebo, 1 prednisolone); for every other intervention the outcome is simply unreported. No statement stronger than "harms are essentially uncharacterised outside one prednisolone trial" is supported.

---

## 7. Summary of final ratings

| # | Outcome | Final GRADE |
|---|---|---|
| a | Acute taste-dysfunction frequency (SARS-CoV-2, taste-specific) | **VERY LOW** |
| b1 | Complete recovery ≤4 weeks | **VERY LOW** |
| b2 | Complete recovery >4–12 weeks | **VERY LOW** |
| b3 | Complete recovery >12 weeks | **VERY LOW** |
| c1 | Any recovery >12 weeks | **LOW** |
| c2 | Any recovery >4–12 weeks | **NO EVIDENCE (empty cell — not rated)** |
| d | Time to recovery (narrative) | **VERY LOW** |
| e1 | Prednisolone — gustatory score at 12 wk (no recovery-proportion data) | **LOW** |
| e2 | Photobiomodulation — complete taste restoration at 1 month | **LOW** |
| e3 | Zinc — taste-specific effect | **NO EVIDENCE (no taste-specific estimate exists)** |
| e3′ | Zinc — composite smell-and/or-taste recovery duration | **VERY LOW** |
| e4 | Cerebrolysin — any outcome | **NO EVIDENCE (RCT with no results)** |
| f1 | Any adverse events (Q3, across interventions) | **VERY LOW** |
| f2 | Serious adverse events (Q3) | **VERY LOW** |
| f3 | Discontinuation due to AEs (Q3) | **VERY LOW** |

**No upgrading factors were applied to any body.** Every rating is a rating of SARS-CoV-2 evidence read against a review question that covers viral infections generally; for non-SARS-CoV-2 viruses there is no rateable quantitative evidence for any outcome in this review.
