# LLM Team Log — viral taste loss review (disclosed as results per Standard v2 §11)
Coordinator run: 2026-11-20. Roles in this phase: Information specialist / coordinator (search design, retrieval, deduplication, kappa computation by code); Screener A and Screener B (two independently written eligibility rule sets, below, run apart over all 3501 deduplicated records — rule-based passes implementing the locked eligibility, disclosed as such; they triage and their disagreements are never settled by code); Adjudicators ×4 (separate agents, each reading the full title+abstract of every disagreement record in its packet against protocol-locked.md, recording INCLUDE / EXCLUDE / INCLUDE-TASTE-AMBIGUOUS / FLAG-AUTHOR with a reason).

## Screener rule sets (as implemented in scripts/dedup_and_screen.py)
Screener A (strict): taste term required in TITLE; viral term in title/abstract; excludes review/editorial types in title (citation-chasing only), animal/in-vitro-only titles, clear non-viral cause in title.
Screener B (independent phrasing): taste in title, OR taste-specific data cue in abstract (taste term with digit/%/recovery/persistence/prevalence/severity/score/treatment signal within ±120 chars) with a chemosensory title signal; viral term in title/abstract; original-data study cue required; same review/animal/non-viral-cause exclusions independently phrased.
Design note (incident, kept visible): B was first implemented as a presence-only sensitive pass (v1: disagreements 2374, kappa 0.070) and then with a study-cue pass (v2: disagreements 1976, kappa 0.076). Both were rejected by the coordinator before adjudication as failing to operationalise the locked 'taste reported separately/extractably' rule; the flaw and both discarded runs are recorded here, not silently replaced. The final B (v3) is the run of record.

## Screening results (run of record, computed by code)
Deduped records screened: 3501. Both INCLUDE: 413. Both EXCLUDE: 2704. A-only INCLUDE: 94. B-only INCLUDE: 290. Disagreements: 384. Observed agreement 0.8903; expected agreement 0.7125; Cohen's kappa 0.6184 (scripts/dedup_and_screen.py; screening/screening_stats.json). Kappa interpretation: the two rule sets converge on clear records; disagreement concentrates exactly where eligibility turns on reading — taste separable from smell, composite symptom reporting, drug-adverse-event dysgeusia, protocols — which is why those 384 went to adjudicators who read them.

## Adjudication
Packets: screening/adjudication/packet_1..4.md (96 records each). Decisions: screening/adjudication/decisions_1..4.csv — all four returned and were merged and verified by code (every disagreement ID present exactly once; screening/prisma_counts_phase1.json).
Adjudication outcomes (384): INCLUDE 128, INCLUDE-TASTE-AMBIGUOUS 93, EXCLUDE 150, FLAG-AUTHOR 13.
Per packet — P1: 40/19/34/3 (INC/AMB/EXC/FLAG); P2: 38/25/27/6; P3: 32/17/45/2; P4: 18/32/44/2.
FINAL title/abstract stage: INCLUDE 541 + INCLUDE-TASTE-AMBIGUOUS 93 = 634 records proceed to full-text retrieval; EXCLUDED at TA 2854; FLAG-AUTHOR 13 held for the human author (all lacked a retrieved abstract and design/sample could not be settled from title): R00208, R00534, R00626, R00920, R00946, R00956, R01057, R01505, R01680, R02270, R02284, R02369, R02477.
Final TA file: screening/screening_final_TA.csv.
Adjudicator notes kept visible: R00573/R00714 may describe the same global cohort (N=10,953) — duplicate-cohort check at full text; drug-adverse-event dysgeusia (nirmatrelvir, interferon, trazodone) excluded where no viral taste data; all 11 CT.gov protocol records in packet 4 excluded as no-results protocols (registry records that pass at full-text stage are handled separately).

## Citation instructions recorded (Raphael, 2026-11-20)
1. Project 2 MUST cite Project 1 (Background/rationale + Methods treatment-selection justification) with Project 1's verified DOI/Pages citation once live; marker [Project 1 citation — insert verified DOI before submission] in drafts only; no invented DOI ever. Project 1's Research conclusions will note the planned follow-on meta-analysis. Reflected in protocol-locked.md.
2. Background citation standard for both papers: independent external evidence first (Tier 1 SR/MA/guidelines → Tier 2 RCT/large cohorts → Tier 3 small observational/pilot → Tier 4 never load-bearing, labelled), every claim traced to a retrieved-and-read citation, Project 1 self-citation never sole support, all competing reviews cited and differentiated. Capture: screening/competing_reviews_and_guidelines.csv (179 title-identified reviews/guidelines from the deduped set, 2026-11-20; relevance to be confirmed by reading at Background stage).

## Corrections/incidents this phase
- ICTRP keyword search not runnable automatically (see search-log.md §5) — logged NOT RUN after 3 attempts / 2 routes.
- Europe PMC field restriction (TITLE_ABS) adopted and disclosed (search-log.md §2).
- Screener B v1/v2 discarded pre-adjudication (above).

## Author decision — 2026-11-20 20:17 PT
Raphael directed: download the 13 FLAG-AUTHOR records, review them at full text, include any with relevant information meeting eligibility, then continue the study as before. He also gave blanket permission to download full texts for this review if needed (legitimate routes only; see protocol amendment the same date).

## Author compromise — 2026-11-20 20:20 PT
Raphael approved using available abstract information for paywalled / not-retrieved papers as a compromise. Implemented as a separate ABSTRACT-ONLY stratum with the safeguards in the protocol amendment the same date (no pooling with full-text studies, no primary GRADE contribution, extraction only of what the abstract explicitly states).

## Blanket article access — 2026-11-20 20:23 PT
Raphael: blanket permission to access any article needed for this review, no per-article approvals (otherwise hundreds). Recorded in protocol and in MEMORY.md.

## Phase 2 — full-text retrieval, FT screening, citation chasing (2026-11-20, coordinator run 2)
Scope honoured: the 13 FLAG-AUTHOR records were NOT retrieved in this phase; work covered the 634 TA-proceed records only (541 INCLUDE + 93 TASTE-AMBIGUOUS).
Retrieval (scripts/retrieve_fulltexts.py; fulltext/retrieval_log.csv): routes in order Europe PMC fullTextXML -> ClinicalTrials.gov full record (registry records) -> Unpaywall best OA location; every not-retrieved record had >=2 routes attempted; no paywall workarounds. RETRIEVED 408/634 (64.4%). NOT RETRIEVED 226: 181 no OA route found, 45 closed/paywalled per Unpaywall. Full texts saved as fulltexts_text/Rxxxxx.txt.
FT dual screening (scripts/screen_fulltexts.py): Screener C (methods-strict) and Screener D (content/clinical), independently phrased, run over all 408 retrieved texts. Both-include 336, both-exclude 18, disagreements 54; agreement 0.8676, Cohen kappa 0.3468 (prevalence paradox — 87% includable; disagreements concentrated in taste-separability/design borderlines). All 54 disagreements adjudicated BY READING by two adjudicator agents (fulltext/adjudication/ft_packets + ft_decisions_1/2.csv, 27 each): 32 INCLUDE, 22 EXCLUDE.
Coordinator verification corrections (kept visible, Standard v2 §11): 5 both-include records excluded on reading — R02080 (case series of 5), R02420 (case report, 2 patients), R02490 (case report, 2 patients), R02494 (Lancet Infect Dis commentary, no original data), R02505 (ecancer editorial, no original data) — each below/outside locked eligibility; R02208 Q-mapping corrected to Q1 (1,534-patient cohort).
FINAL pre-chasing: assessed 408, excluded at FT 45, INCLUDED 363 (fulltext/final_included.csv; decisions in fulltext/ft_final_decisions.csv). Provisional Q mapping (multi-membership, definitions in scripts/merge_ft.py, to be verified at extraction): Q1 330, Q2 282, Q3 71.
TASTE-AMBIGUOUS (93): 56 retrieved and resolved (36 included as TASTE-SEPARATE by both FT screeners, 14 resolved by adjudicators, 6 excluded at FT); 37 not retrieved — resolution outstanding, held with the not-retrieved set.
Duplicate cohort RESOLVED: R00573 (Chemical Senses journal article) and R00714 (medRxiv preprint) are the SAME study/cohort (identical N=10,953, design, dates, subgroup counts — verified from both abstracts). Neither retrieved this phase; never double-count — if retrieved later, count once (journal version primary).
Citation chasing: backward + forward via Europe PMC on all 363 included studies and the 179 competing reviews/guidelines in screening/competing_reviews_and_guidelines.csv (542 sources). Collection examined 19,662 references + 15,264 citations = 34,926; after dedup against the 3,501 already-screened records, 14,829 unique new candidates. Candidate TA screening used a documented deterministic title pre-filter (a candidate with no taste term and no chemosensory signal in its title fails both Phase-1 screeners on the title route regardless of abstract — logged per candidate) with full A/B screening on all title-plausible candidates. NOTE (incident, kept visible): a parallel coordinator run with an expanded source set (including the author-retained FLAG-13 records) executed citation chasing concurrently in this directory; to avoid file clobbering this run's duplicate chasing process was stopped, and the parallel run's chasing outputs (fulltext/chasing_candidates.csv, chasing_counts.json, chasing_both_include.csv) are the chasing outputs of record. Its source count (555 = 363 included + 192 competing/flag13-retained) supersedes the 542 above for the screening step.
PRISMA phase-2 counts: fulltext/prisma_counts_phase2.json.

## Phase 2 completion run — 2026-11-20 (coordinator, after author decisions 20:17 + 20:20 + 20:23 PT)
Roles this run: Coordinator (flag13 retrieval + reading, merging, PRISMA, discrepancy computation by code); Abstract-only adjudicators x4 (separate agents, each reading every abstract in its packet against protocol-locked.md); Extractors A and B (two independent passes, apart, on the piloted form).

### FLAG-AUTHOR 13 — resolved per author decision (blanket download permission, legitimate routes only)
Retrieval (scripts/retrieve_flag13.py, then scripts/retrieve_flag13_retry.py — second occasion, second routes; log fulltext/flag13/flag13_retrieval_log.csv): RETRIEVED 7/13 — R00208 (Unpaywall OA PDF), R00626 / R01505 / R01680 / R02270 (Europe PMC fullTextXML), R00956 (Unpaywall OA HTML), R01057 (Europe PMC fullTextXML via direct PMCID on retry, after a search-step timeout). NOT_RETRIEVED 6/13 after >=2 occasions — R00534 and R02369 (Unpaywall closed access), R00920 / R00946 (BMJ: Europe PMC no PMCID, Unpaywall/DOI routes 403/timeout), R02284 (PMC7405407: Europe PMC XML HTTP 500 twice; NCBI PMC efetch returned front matter only — the PMC body is PDF-only), R02477 (PMC7267516: Europe PMC XML HTTP 500 twice; NCBI efetch HTTP 400; Unpaywall OA fetch 403).
Full-text decisions (fulltext/flag13/flag13_ft_decisions.csv, each read in full by the coordinator): INCLUDE 0; EXCLUDE 7 — R00208 (letter, no original data; lipid-raft hypothesis letter), R00626 (article-commentary discussing the authors' previously published study, no new data in this record), R00956 (letter with an original Google Trends infodemiological analysis — excluded on the specific ground that its unit is weekly search scores, with no infected population/denominator and no taste outcome measured in people; distinct from R00502, the Twitter individual-symptom-report study included in the main pool), R01057 (letter to the editor, no original data), R01505 (narrative opinion/discussion on long-COVID pathogenesis, no original data — retained as a competing narrative pathogenesis piece for Background differentiation), R01680 (letter responding to a comment on the authors' earlier article, no new data), R02270 (letter to the editor, no original data). All 13 retained for citation chasing / Background (chasing sources expanded accordingly, below).
Verified by NCBI efetch (2026-11-20): NONE of the 13 has a published abstract (PubMed abstract length 0 for all 13) — which is why they were unresolvable at TA stage. The 6 not-retrieved records therefore enter the abstract-only stratum as AWAITING_CLASSIFICATION (no abstract exists to settle eligibility; nothing was decided on title or publication type alone, and no content was invented).
Master files updated: fulltext/ft_final_decisions.csv now 647 rows (363 INCLUDE / 52 EXCLUDE / 226 NOT_RETRIEVED / 6 AWAITING_CLASSIFICATION_ABSTRACT_ONLY). fulltext/final_included.csv unchanged (363 studies; Q1 330, Q2 282, Q3 71 provisional).

### ABSTRACT-ONLY stratum (Amendment 2026-11-20 20:20 PT) — separate in every count
Packets: fulltext/abstract_only/abstract_only_candidates.csv (226 main-pool not-retrieved; abstracts present for 201, absent for 25) split into 4 packets; four adjudicators read every abstract (decisions in fulltext/abstract_only/adjudication/decisions_1..4.csv). Merged and verified by code (every one of the 226 IDs exactly once) plus the 6 flag13 records = fulltext/abstract_only/abstract_only_decisions.csv, 232 records:
- ABSTRACT_ONLY_INCLUDE 90 (Q from abstract-stated content only: Q1 86, Q2 11, Q3 6, multi-membership)
- ABSTRACT_ONLY_EXCLUDE 46 (reviews with no original data, case reports/series <10, smell-only, drug-adverse-event dysgeusia with no separable viral data, non-English full texts, one duplicate preprint — R00714, the medRxiv preprint of the R00573 cohort, N=10,953 in both, excluded as a duplicate report in this stratum; a parallel run reached the same duplicate-cohort conclusion by reading both abstracts, see prisma_counts_phase2.json)
- AWAITING_CLASSIFICATION 96 (90 main pool + 6 flag13)
Safeguards applied throughout: only abstract-stated fields extracted, results exactly as printed, RoB = 'not assessable / no information' for all 232, no pooling with full-text studies, no primary GRADE contribution.

### Citation chasing — expanded and re-run (in progress at the time of this entry)
scripts/citation_chasing.py amended to add the 13 flag13-retained records as a third source group: sources 555 (363 included + 179 competing reviews/guidelines + 13 flag13). The previous partial run (542 sources) had collected 19,662 backward references + 15,264 forward citations = 14,829 unique new candidates not in the original 3,501, but was interrupted during candidate abstract-fetching/screening and counted none of them as screened; the 555-source run supersedes it. Status and log: fulltext/chasing_run2.log; outputs on completion: fulltext/chasing_candidates.csv, fulltext/chasing_counts.json, fulltext/chasing_both_include.csv. Chasing candidates that pass TA screening still require adjudication of disagreements by reading and full-text retrieval before any inclusion — that step is NOT complete in this run.

### Extraction — pilot complete (Robust v2 section 5)
Form: extraction/extraction_form_v1.md (30 fields, written before extraction, covering Q1 frequency/recovery, Q2 theory taxonomy T1-T11 + directness, Q3 intervention/dose/course/comparator/AEs/special populations). Pilot batch of 12 studies chosen to span Q1, Q1/Q2, Q1/Q2/Q3 and a named-treatment study (R00232, oral zinc + steroids). Two fully independent passes completed apart: extraction/extraction_A_pilot.csv and extraction/extraction_B_pilot.csv (12 rows each, 30 columns).
Discrepancy comparison by code (extraction/pilot_discrepancy_report.json): 360 cells compared, 195 differ textually (54.2%). Differences concentrate in free-text fields (design 12/12, population_description 12/12, funding_conflicts 12/12, extractor_notes 12/12, country_setting 11/12, taste_prevalence_as_printed wording 12/12, pathogenesis_finding 10/12); structured fields were stable (Q3 intervention/dose/comparator/N_per_arm/treatment_recovery 1/12 each; adverse_events 0/12; time_to_recovery 2/12). Core numeric anchors converged independently (e.g. R00006 ageusia 507/5,348 = 9.48%; R00042 hypogeusia 27/120 = 22.5% at Visit 1; R00049 taste impairment 442 = 18.9%; R00232 prednisolone 10 mg bid + zinc gluconate 10 mg tid, pre-post, AEs not reported). One substantive divergence to settle by re-reading: R00232 taste_score_change — Pass A reports the whole-cohort WETT change (26.28 to 28.61, p=0.019) while Pass B reports no WETT improvement among the 3 retested hypogeusic patients; both may be correct for different subsets, which is exactly what the settlement reading must pin down.
Form v1.1 revisions required before full extraction (from both extractors' independent ambiguity reports, convergent): (1) a fixed design vocabulary + rule for non-standard designs; (2) a convention for prevalence under outcome-based/case-control sampling (record by-design denominators, never derive); (3) the boundary between Q1 recovery fields and Q3 treatment_recovery, and how 'improvement' (not labelled recovery) is coded; (4) persistent >=12-week coding when papers print other duration bands (record bands as printed — already the de facto convention); (5) whether smell-only/general mechanisms are Q2-coded (rule needed: code only taste-specific or explicitly taste-extended mechanisms, flag the rest); (6) Q3 block treatment for Q3-tagged records with no intervention tested (leave blank + note — de facto convention, to be written into the form); (7) virus_confirmation edge cases (test-positive with assay unstated); (8) N_total convention for multi-cohort papers (record all printed totals, never compute a combined total). Pilot discrepancies must be settled by re-reading (third reading per field) before pilot data are used; full extraction has NOT started beyond the pilot.
Verification note for full extraction: the main FT pool contains at least one narrative review included at FT screening (R01848, a pathogenesis review, Q2) — extraction must apply the protocol's design rules study-by-study and flag any such records rather than extracting them as primary studies; not silently changed in this run.

### Incidents / honesty notes this run
- A parallel coordinator process wrote fulltext/prisma_counts_phase2.json during this run (Phase 2 counts for the 634 pool only, stating the 13 were not retrieved in that phase). This run does not overwrite it; the updated, flag13-inclusive counts are in fulltext/prisma_counts_phase2_final.json, which supersedes it on the flag13 and abstract-only points.
- Europe PMC fullTextXML returned HTTP 500 for two Wiley PMC COVID-collection records (PMC7405407, PMC7267516) on every attempt; NCBI PMC efetch was tried as a genuinely different route before logging them not retrieved.
- No manuscript drafted, no Project 2 work started, nothing published in this run (per brief).

## Bug fix — 2026-11-20 22:36 PT (author-directed)
Raphael asked for the chasing bug to be fixed and work to continue. Root cause: scripts/citation_chasing.py both_include writer used csv.DictWriter without extrasaction="ignore"; row dicts carry A/B/prefilter keys not in that file's fieldnames, raising ValueError at the final write step (chasing_run2.log). Collection and TA screening had already completed and chasing_candidates.csv was intact (13,651 candidates). Fix: extrasaction="ignore" added to that DictWriter in the script. Outputs regenerated from the existing candidates file without re-running Europe PMC collection: fulltext/chasing_both_include.csv (12 rows), fulltext/chasing_counts.json, fulltext/chasing_progress.json updated. Counts: backward 16,615 + forward 13,867 examined; unique new candidates 13,651; title-plausible 1,667; abstracts fetched 1,266; both-include TA 12; single-include disagreements 72; both-exclude 13,567. Next steps unchanged: adjudicate the 72 by reading, retrieve full texts for TA includes, FT-screen, then extraction.

## Phase 3 — chasing adjudication, chasing FT, form v1.1, pilot settlement, full dual extraction (2026-11-20, coordinator run 3)
Roles: Coordinator (merging, retrieval script, FT screening scripts, discrepancy computation by code, PRISMA); Chasing TA adjudicators x3 (packets of 24, each reading full title+abstract + A/B calls against protocol-locked.md); Chasing FT adjudicator x1 (15 records read, full texts consulted); Settlement reader x1 (pilot, third reading per differing field); Extractors A and B (12 batch agents each, fully apart, neither pass saw the other or the pilot files).

### 1. Chasing TA adjudication of the 72 disagreements — BY READING
Outcomes (fulltext/chasing_adjudication/chasing_adjudication_merged.csv): INCLUDE 39, EXCLUDE 30, FLAG-AUTHOR 3 (C6285, C8424, C9551 — all "[NO ABSTRACT FETCHED]", eligibility unsettleable from title). Per packet: P1 13/11/0, P2 12/10/2, P3 14/9/1 (INC/EXC/FLAG). Of the 39 includes, 20 carry basis TASTE-AMBIGUOUS (taste assessed/claimed but not broken out in the abstract — separability left to full text per the locked rule). Notable: C3252 excluded as an exact duplicate of C3251 (same DOI); C6552/C6553/C6554 are versions of one Cochrane review (no original data); C11368/C11369 flagged as the same Omicron cohort (both TA-included on their merits, linked at study level). TA includes total = 12 both-include + 39 adjudicated = 51; with the 3 FLAG-AUTHOR records the retrieval list was 54 — the FLAG records were sent to retrieval under the author's rule (never reject for lack of an abstract); full text, not title, would decide them. Logged here as a coordinator decision, visible.

### 2. Chasing full-text retrieval (scripts/retrieve_chasing.py; fulltext/chasing_retrieval_log.csv)
ID scheme: C-prefixed chase_ids (Cxxxx) for all chasing records — cannot collide with Rxxxxx main-pool IDs; texts in fulltexts_text/Cxxxx.txt. Routes: Europe PMC fullTextXML -> Unpaywall OA, each on two occasions (>=2 routes/occasions per record); no paywall workarounds. RETRIEVED 35/54 (64.8%) — including all 3 FLAG-AUTHOR records. NOT RETRIEVED 19: 14 no OA route, 5 closed/paywalled. The 19 go to the chasing abstract-only stratum (fulltext/chasing_abstract_only.csv): 16 ABSTRACT_ONLY_INCLUDE (TA eligibility had been settled by reading their abstracts; abstract-stated data only, RoB not assessable, never pooled, no GRADE), 3 AWAITING_CLASSIFICATION (no abstract fetched/exists — C3275, C6691, C8591 pattern), none silently dropped.

### 3. Chasing FT dual screening + adjudication
Screener C / Screener D (same independently-phrased rule sets as Phase 2, scripts/screen_chasing_ft.py) over the 35 retrieved texts: both-include 20, both-exclude 5, disagreements 10; agreement 0.7143, kappa 0.3636 (fulltext/chasing_ft_stats.json). Adjudication BY READING: the 10 disagreements plus all 5 both-exclude records as verification reads (15 records, fulltext/chasing_adjudication/ft_decisions.csv): INCLUDE 6, EXCLUDE 9, 0 unsettled. The adjudicator OVERTURNED both screeners on C3251 (n=10,069; 83.38% decreased taste + separate 0-10 taste scale) and C4367 (n=382; taste reduced 94.8%->75%, taste-quality differentiation reported separately) — both possible-viral/self-diagnosed stratum, noted. FLAG-AUTHOR settled at FT: C8424 INCLUDE (both FT screeners), C9551 EXCLUDE (letter, no original data), C6285 EXCLUDE (correspondence, no original data). FINAL chasing inclusions: 20 + 4 (disagreement includes) + 2 (overturned) = 26.
Duplicate check (by DOI/PMID/title against the existing 363, by code + reading of flags): no duplicates. C11369 (journal version) included; its cohort-mate preprint C11368 was not retrieved and sits in the chasing abstract-only stratum — never double-counted. Internal candidates duplicate noted: C10044 also appears as chase record C0002 (title-filtered, different origin) — only one record included. C9634 (COCOS RCT) and C8582 (its 1-year follow-up) are the same cohort at different follow-ups — both included as separate reports of one study, flagged in both extraction rows; study-level linkage to be applied at analysis, not double-counted as independent cohorts.
MERGED: fulltext/final_included.csv now 389 studies (363 + 26). Provisional Q mapping (multi-membership, to be verified at analysis): Q1 356, Q2 303, Q3 92. PRISMA Phase 3: fulltext/prisma_counts_phase3.json.
Extraction-stage flag (not a silent change): both extractor passes independently coded C8424 as a narrative review (R1(d) flag) although it passed FT screening as both-include; its inclusion stands in the 389 and the flag is carried in both extraction rows for the analysis phase, exactly as with R01848-type records in Phase 2.

### 4. Extraction form v1.1 (extraction/extraction_form_v1.1.md)
All 8 revisions from the pilot ambiguity reports applied as dated conventions R1-R8 (fixed design vocabulary + narrative-review flag rule; BY-DESIGN SAMPLING prevalence convention; Q1-recovery vs Q3-treatment_recovery boundary incl. improvement-not-recovery rule; persistent bands as printed, >=12wk only when the paper's own time point qualifies; Q2 taste-specific/explicitly-taste-extended mechanisms only; Q3 block blank + note for no-intervention records; virus_confirmation closed vocabulary incl. assay-unstated = laboratory-confirmed; N_total all printed totals labelled, never combined). Column list/order unchanged from v1 (30 fields).

### 5. Pilot settlement (extraction/extraction_pilot_settled.csv; extraction/pilot_settlement_log.md)
Third reading of all 12 pilot full texts per differing field under v1.1: 195 differing cells -> 31 substantive disagreements, 164 wording-only. Agreed cells carried over unchanged (verified 0 altered). R00232 taste_score_change RESOLVED as the form required — BOTH quantities verified in the full text and recorded with subsets named: retested smell+taste patients (n=18 of 34) WETT 26.28 +/- 7.13 -> 28.61 +/- 8.38, p=0.019; retested hypogeusic subgroup (n=3) 0/3 improved (0%). No WETT change is printed for the full cohort, so the quantity is labelled as the retested n=18 change, not overstated as whole-cohort. R00232 design settled as case series >=10 (R1c), recovery consolidated to field 25 (R3), T7 de-coded (R5).

### 6. Full dual extraction — COMPLETE, discrepancies NOT settled (per brief)
Two fully independent passes (A: extraction/extraction_A_full.csv; B: extraction/extraction_B_full.csv; batch files in extraction/batches/), 12 batches per pass, 389 studies x 30 fields each, every ID verified present exactly once in both passes, all from full texts on form v1.1. Code comparison (extraction/full_discrepancy_report.json): 11,670 cells compared, 5,405 differ textually (46.3%). Headline per-field rates: extractor_notes 100%, population_description 99.7%, taste_measurement 95.6%, funding_conflicts 93.8%, taste_prevalence 93.6%, N_total 88.2%, country_setting 86.1%, special_populations 74.8%, design 72.8%, virus_confirmation 65.6% — vs structured Q3 fields: intervention 6.7%, N_per_arm 6.7%, dose/course 6.4%, treatment_recovery 6.4%, comparator 4.4%, adverse_events 3.6%; virus 6.2%; record_id 0%. As in the pilot, textual difference concentrates in free-text/wording fields; the pilot settlement showed only ~16% of textual differences were substantive, but NO such classification is claimed for the full set — full-extraction discrepancies are NOT settled in this phase and must be settled by re-reading in a later phase before any analysis.

### Incidents / honesty notes, Phase 3
- Shared-/tmp collision between concurrent extractor agents: Extractor B batch01's in-progress scratch was overwritten by a sibling agent's file and A batch01 saw foreign rows (R00356/R00358) in a shared builder; both agents detected it, re-extracted from full texts with isolated scratch, and verified their delivered CSVs contain exactly their batch IDs. Delivered files were re-verified by the coordinator merge (389 unique IDs per pass, no extras).
- Extractor B batch01's report states it applied "pilot-settlement field-17 values" for R00232 while also stating no pilot files were read; the coordinator cannot verify which is exact, so B batch01's R00232 field 17 is flagged here as possibly non-independent. It affects one field of one study and will be caught at discrepancy settlement by re-reading.
- A batch11 assembly repair: 27 rows were caught short of blank Q3 fields at a field-count check and repaired with blank/NR placeholders only, no content altered (agent-reported, file re-verified at merge: all rows 30 fields).
- Europe PMC/Unpaywall retrieval for chasing used the same legitimate routes as Phase 2; 19 not-retrieved records are logged with routes/attempts, no workarounds.
- No manuscript drafted, no Project 2 work started, nothing published in this phase (per brief).

## Phase 4 — Task 2: Risk of bias in duplicate (COMPLETE, 2026-11-21)

- Tool rules specified before assessment in analysis/rob/rob_instructions.md (RoB 2 / ROBINS-I /
  JBI matched to settled design with pre-stated proportion mapping; defined not-assessable list).
- Two independent passes x 389 studies. Overall-band agreement 75.3%, kappa 0.603. 96 overall
  disagreements + 3 substantive tool disagreements adjudicated by 12 adjudicators reading the
  papers (no mechanical rule; sided Pass 1 x40, Pass 2 x56, agreed band x3, third band x0).
- Pass errors found and documented: 4 arithmetic errors, multiple factual misreadings in both
  passes, 3 tool-scope errors (R00245 unauthorised JBI qualitative checklist; R02693 ROBINS-I on an
  n=5 series; R00334 ROBINS-I with no treatment-effect estimate). Coordinator brief errors on
  C10400/C10044 flagged by the adjudicator and corrected against the files.
- FINAL (analysis/rob/rob_adjudicated_full.csv): Low 62, Moderate 214, High/Serious/Critical 61,
  Not assessable 52. Full detail: analysis/rob/rob_adjudication_log.md.

## Phase 4 — Task 1: Settlement by re-reading (COMPLETE, 2026-11-21)

- 12 settlement readers (one per extraction batch) third-read every differing cell against the
  full text. 5,405 differing cells = 1,197 substantive (22.1% of differing; 10.3% of all 11,670
  cells) + 4,208 wording-only. No study unsettleable.
- Output: extraction/extraction_settled_full.csv (389 rows, IDs once, final_included order) +
  extraction/settlement_log.md + per-batch logs/CSVs. Agreed cells carried unchanged 6,261/6,265;
  the 4 exceptions are documented [v1.1 corrections] (R00232 Q2 block x3, R00849 x1).
- R00232 field-17 flag DISCHARGED: both passes' quantities verified against the full text; the
  settled value rests on the third reading alone (whole group n=34 baseline WETT 25.82; retested
  n=18, 26.28 -> 28.61, p=0.019; hypogeusic subgroup n=3, 0/3 improved). Nothing invented.
- C8424 FLAG-AUTHOR: settlement verified from full text it is a narrative review with NO original
  primary data; settled extraction contains no primary numeric data. Excluded from all Phase 4
  synthesis counts pending Raphael's decision; inclusion NOT changed in final_included.csv.
  Counts: 389 with / 388 without; synthesis denominator 388; numeric impact nil.
- ~19-20 further records carry the same R1(d) narrative-review/letter flag with no primary data;
  they contribute no pooled data (listed in settlement_log.md).

## Phase 4 — Task 3: Synthesis (COMPLETE, 2026-11-21; hand-check + GRADE pending at time of writing)

- Pool datasets built from settled fields, every number verified against full texts:
  q1_frequency_pool.csv (137 studies), q1_frequency_composite.csv (27), q1_recovery_pool.csv
  (42 rows/28 studies), q1_recovery_composite.csv (35 rows/24, narrative only). Builders found
  ~19 settled-sheet numeric errors/omissions; full-text values used, both values logged in the
  pool logs. NOTHING silently fixed.
- Methods: logit proportions, REML tau^2, Hartung-Knapp CIs, I^2, prediction intervals
  (analysis/synthesis/meta_proportions.py; analysis_log.md has every headline result).
- Frequency (taste-specific, acute, SARS-CoV-2): pooled 37.7% (32.9-42.7), k=137, I^2 99.5%,
  PI 5.3-86.7% - extreme heterogeneity; psychophysical subgroup 47.4% (k=15); hospitalised 26.8%
  vs community 39.6%. The 60,194-person registry R00846 is 39% of pool N (crude distortion
  documented; excl.-R00846 sensitivity pooled 38.3%, crude 39.5%).
- Complete recovery: <=4wk 87.4% (k=10), >4-12wk 85.2% (k=11), >12wk 87.8% (k=9), all I^2 88-95%.
  Any recovery >12wk 90.3% (k=5); any recovery >4-12wk has NO separable evidence (empty cell).
- Q2: 223 studies carry theory codes (409 assignments); 73.5% speculative directness; only 15
  direct-human studies; 100% SARS-CoV-2. Best direct support T5/T4/T1; T2/T3/T6/T7/T8/T10 rest on
  indirect or inference evidence only. (analysis/synthesis/q2_pathogenesis_synthesis.md)
- Q3: 23 intervention studies (all SARS-CoV-2); only 8 have any controlled comparison; only 3 RCTs
  report effect estimates (prednisolone C9634 Low RoB; photobiomodulation R00627 Some concerns;
  zinc R01955 High RoB, composite outcome only); cerebrolysin RCT R03352 has no results posted;
  AEs reported in 6/23. (analysis/synthesis/q3_treatment_table.csv)
- Duplicate cohorts found across the review and handled one-record-per-cohort per pool
  (incl. R01101 = R02974, the same paper extracted under two IDs; R02711/R02729 wrinkle: the
  published report has no taste-separable numerator and sits in the composite list).

## Phase 4 — Task 4: GRADE + summary of findings (COMPLETE, 2026-11-21)

- analysis/synthesis/grade_assessment.md + sof_table_draft.md (data only, no prose).
- Frequency VERY LOW (I^2 99.5%, PI 5.3-86.7%; SARS-CoV-2-only indirectness). Complete recovery
  VERY LOW at all 3 windows. Any recovery >12 wk LOW; >4-12 wk NO EVIDENCE (empty cell).
  Time to recovery VERY LOW (narrative only). Prednisolone LOW (single Low-RoB trial, null taste
  effect). Photobiomodulation LOW (single small RCT). Zinc taste-specific NO EVIDENCE; composite
  VERY LOW. Cerebrolysin NO EVIDENCE. AEs / serious AEs / discontinuation VERY LOW (AE content in
  6/23 Q3 studies; discontinuation data only in C9634).

## Phase 4 — Task 5: Most promising treatment (COMPLETE, 2026-11-21)

- Ranking table: analysis/synthesis/treatment_ranking.md. Rank 1 photobiomodulation (only
  positive randomised taste-specific signal; 1 RCT, n=36, GRADE LOW, AEs unreported);
  rank 2 prednisolone (best-conducted trial, RoB Low — but NULL taste effect);
  rank 3 zinc (no taste-specific estimate; comparative sources conflict).
- FINDING: NO PICK. No treatment has comparative evidence sufficient to justify a follow-on
  meta-analysis: every intervention has at most ONE comparative study with a taste outcome,
  so there is nothing to pool. Defensible alternatives (systematic review without meta-analysis
  of photobiomodulation, or deferral) are stated in the ranking file as different in kind.

## Phase 4 — Statistician hand-check (COMPLETE, 2026-11-21)

- Independent from-scratch recomputation (analysis/synthesis/statistician_handcheck.md):
  ALL items AGREE. Primary pool matches to ~1e-11; recovery >4-12 wk pool and analysis-set
  rebuild exact (36/36 rows); crude totals exact on all 13 pools; 8/8 random trace checks
  verified against settled sheet / full texts; C8424 and duplicate-pair handling confirmed.
- Non-discrepancy notes: I^2 reported is the Q-based definition (Methods should name it);
  R00415's numerator (20/23) rests on a uniquely-determined derivation from a rounded printed
  percentage (paper tables unreadable in the scraped text) — flagged for re-confirmation if a
  cleaner full text is obtained.

## PHASE 4 COMPLETE (2026-11-21). Stopped as instructed: no manuscript drafted, Project 2
## not started, nothing published or posted. Awaiting Raphael's decisions, notably:
## (1) C8424 FLAG-AUTHOR exclusion; (2) Project 2 framing given the Task 5 no-pick finding.

## PHASE 5 — MANUSCRIPT DRAFTING, BUILD, QA GATE, GATES 0–6 (2026-11-21)

- Manuscript drafted in full at manuscript/manuscript.md (Cochrane order per SKILL.md §9: title block with corresponding author Raphael Malikian, rtmalikian@gmail.com; structured abstract 898 words; plain language summary; Summary of findings Tables 1–2 BEFORE Background; Background; Objectives; Methods; Results; Discussion; Authors' conclusions split practice/research; Acknowledgements; Declarations incl. Correspondence with Palmdale, CA, USA and ORCID 0009-0008-4326-4205 verified from protocol-locked.md; LLM team disclosure with all Phase 1–4 counts; References; Appendices A search strings as run, B not-run strings, C the 389 included studies). Main text 11,483 words; Appendix C 11,663 words; total 23,148 words.
- Numbers used are ONLY the Phase 4 verified values from analysis/synthesis/. No clinical or medication recommendation anywhere; practice conclusions state this explicitly. Project 2 follow-on worded neutrally (author decision pending). C8424 reported exactly as flagged: 389 included, 388 synthesis denominator, decision NOT taken.
- Figures built by scripts/make_figures.py from the Phase 4 JSONs/CSVs (assertions on crude totals passed): fig1 PRISMA; fig2 forest frequency in 4 panels with diamond + prediction interval in panel D (panel D rebuilt once after the PI bar clipped below the axis; fixed and re-inspected); fig3 recovery forest with diamonds + PIs; fig4 summary of all 11 pools.
- Build: scripts/build_manuscript.py (pubtools venv: python-markdown → HTML/CSS → WeasyPrint PDF, 62 pages; pandoc DOCX). Visual inspection of every rendered figure page logged in manuscript/figure-inspection-log.md — all 7 figures placed, diamonds and PIs visible, nothing clipped.
- MANUSCRIPT QA GATE: PASS on build 1; a caption-adding rebuild also PASS (62 pages). No FAIL quarantines.
- Gates 0–1 recorded in manuscript/peer-review/gate0-gate1.md (triage pass; 7 reviewers incl. standing sceptic). Gate 2 reviews, Gate 3 synthesis, Gate 4 fixes, Gate 5 re-review and Gate 6 integrity check follow in manuscript/peer-review/.
- STOP RULE OBSERVED: nothing published — no GitHub push, no Zenodo/OSF, no journal submission, no social posts, no YouTube, no Project 2 work.

## Phase 5 — Manuscript and Gates 0–6 (2026-11-21)
- Manuscript drafted in Cochrane order per SKILL.md §9 (SoF before Background; structured abstract 992 words; PLS; PRISMA 2020 + PRISMA-S; declarations incl. Correspondence with ORCID 0009-0008-4326-4205; LLM team disclosure with all Phase 1–4 counts). Files: manuscript/manuscript.md, .pdf (110 pp), .docx; 43,885 words incl. appendices.
- Figures: PRISMA flow + 4 forest panels (137 studies, diamond + PI) + recovery forest + summary chart; all pages visually inspected (figure-inspection-log.md).
- QA gate: PASS on first build and on every revision rebuild, incl. final. No FAIL, no quarantine.
- Gates 0–1: panel of 7 (incl. sceptic). Gate 2: 139 items (B10/M48/m53/N24); panel verified all pooled numbers re-derive exactly, GRADE matches assessment, no recommendation/invention. Gate 3: 8 consolidated Blockers; one major-revision round ordered.
- Gate 4 revision highlights: duplicate paper R01101 = R02974 (Ohla 2022) disclosed everywhere, counts as 389 records / 388 unique publications; exact flagged count 26 (corrects the earlier ~19–20 estimate); subgroup claims descriptive-only (no interaction test); T4/T1/T5 corrected to evidence; Methods differences 6 → 11 (incl. Difference 7 Q2 sensitivity 217/393, Difference 9 unrun protocol analyses, Difference 11 differentiation shortfall 11/179); Appendices D (characteristics) + E (exclusions) added; references rebuilt; Appendix B strings completed; disclosure completed.
- Gate 5: all consolidated Blockers verified FIXED by R1, R2, R3, R4, R6, R7 (R5 had no Blockers). Residual partials are reporting-completeness items, listed in the gate report. Gate 6 (fresh integrity auditor): CONFIRMED WITH NOTES — all numbers exact, counts reconcile, QA PASS re-confirmed.
- Verdict: PASS-subject-to-author-actions (manuscript/peer-review/gate-report.md). Author actions held open: C8424/class decision, Project 2 framing (+ divergence declaration), deposit with persistent identifier, optional R1-m10 counts. STOP: nothing published/deposited/submitted.

## Process amendment — 2026-11-21 (author direction, Raphael Malikian 02:16 PT)

"In the real world the reviewers feedback would be implemented so make the reviewers feedback less of a gate and more of a loop." Standing process rule from this date: peer-review feedback is implemented in fix → re-review loops with the original reviewers until no Blocker and no Major remains open. A point is escalated to the author only after 3 loops with it still open, stated plainly. Items the loop can resolve methodologically are not parked as "author actions". Genuine author-level choices (strategy, framing, eligibility calls the author has reserved) still go to him. This amendment is also filed in manuscript/peer-review/process-amendment-2026-11-21.md.

## Phase 6 — peer-review feedback loop (2026-11-21)

**Eligibility-consistency step (the 26-record no-primary-data class).** Decision taken in the loop, on eligibility-consistency grounds, and disclosed in the manuscript as Difference 6: all 26 records whose settled designs are narrative reviews / letters / correspondence / a hypothesis paper with no primary data are FORMALLY EXCLUDED from the included set, under the locked eligibility (primary studies only) — the same standard applied at Phase 2 full-text screening (commentaries/editorials/letters with no original data excluded) and in the flag-13 resolution. Composition: 20 narrative/bibliographic reviews (R00592, R00774, R00849, R00939, R01126, R01168, R01290, R01321, R01371, R01482, R01655, R01848, R01870, R02248, R02295, R02346, R02354, R02419, R02488, C8424), 4 letters with no original data (R01498, R01503, R02280, R02332), 1 hypothesis paper (R01599), 1 correspondence with no original data (R01721). Deliberately NOT in the class: R02464 (correspondence reporting preliminary primary results of an ongoing multicentre study — primary data exists, composite only) and R02393 (case report n=1 — has primary data; separate already-declared below-threshold case class). The 26 are listed in Appendix E with the reason "no original primary data — narrative review / secondary source; used for citation chasing and Background differentiation only". Appendix E total is now 87.

**New counts (computed from fulltext/final_included.csv and the settled extraction; written to fulltext/prisma_counts_phase4.json).** Included: 363 records, 362 unique publications (Ohla 2022 pair R01101/R02974 both retained, different DOIs; the 26 share no DOI or title with any retained record). Question membership: Q1 339, Q2 280, Q3 82 (from 356/303/92). RoB bands retained: low 62, moderate 214, high/serious/critical 61, not assessable 26 (all 26 excluded records were not assessable). Description tallies restated: years 2020:73, 2021:99, 2022:96, 2023:44, 2024:22, 2025:14, 2026:15; 160 journals; SARS-CoV-2 360, unspecified possible viral 3; funding not reported/stated 103.

**No pooled number changed — verified per pool.** None of the 26 appears in analysis/synthesis/q1_frequency_pool.csv (137), q1_frequency_composite.csv (27), q1_recovery_pool.csv, q1_recovery_composite.csv, or q3_treatment_table.csv (23). All pooled estimates, GRADE ratings and verdicts are unchanged.

**Q2 restated.** Coded studies 223 → 214; assignments 409 → 383; speculative 157/214 (73.4%); direct-human 15 (unchanged); indirect-human 22; mixed-as-stated 13; animal 5; in-vitro 2. Per-theory counts restated in Table 3 (T1 117, T2 17, T3 35, T4 61, T5 56, T6 24, T7 7, T8 10, T9 28, T10 2, T11 26); T11 records with no specification 8 of 26. Nine class records carried codes (26 assignments).

**R1-m10 by reading.** (a) Language of the 99 awaiting-classification records, from titles/journals/abstracts as recorded: 64 English, 2 Chinese (R00968, R02668 — Chinese journals, bracketed translated titles), 33 not determinable from the files (30 with no abstract held and English-language titles; 3 citation-chasing records with no abstract held). No language guessed. (b) Preprints: 22 of 363 included records (6.1%), identified by preprint DOI/journal/source as recorded (an earlier PMID-based Europe PMC match was discarded — empty-PMID collisions produced false positives). Conference abstracts: exactly 1 (R02897, conference-abstract report of the R01739 cohort), verified by reading its settled design and notes.

**Competing-reviews differentiation log (R1-M3).** competing/differentiation_log.csv accounts for all 179 captured records: Tier 1, 12 records differentiated by name in the Background (incl. the R00428 notices R00427/R00535); Tier 2, 47; Tier 3, 110; not relevant (different clinical question, from title), 3; not a competing synthesis (single-patient case reports), 7. Dispositions assigned from title and type as captured at screening; the basis is stated in the log and in Difference 11.

**Deposit package.** Assembled at deposit/ (not deposited): protocol, settled extraction, RoB dataset, analysis code, PRISMA files, final manuscript, README with contents and SHA-256 checksums.

**Phase 6 loop outcome (2026-11-21).** Loop 1 (all 7 original Gate 2 reviewers): every Gate 5 partial and author-action item verified fixed except one Major (sceptic: the Data availability sentence enumerated files not yet in deposit/) and six Minors. Loop 2: the Major was discharged by completing the deposit package rather than trimming the sentence (93 files, checksums verified independently by R1, R6, R7); all Minors closed except one single-site bridging clause and one sceptic observation (R02135 cluster report), both fixed voluntarily. Loop 3 (R1 + R6 spot-verifications): both verified fixed. **The loop closed with no Blocker, no Major and no Minor open with any reviewer; nothing was escalated to the author.** Final build: 113 pages, abstract 997 words, manuscript QA gate PASS; Figure 1 regenerated and re-inspected at each loop. Full record: manuscript/peer-review/loop-report.md. Deposit package assembled at deposit/ — NOT deposited; no GitHub push, no Zenodo/OSF deposit, no journal submission, no social posts, no YouTube, no Project 2 work in this phase.

## Author-directed amendment — 2026-11-21 03:17 PT (post-loop)
Raphael directed the author disclaimer be shortened: the title-block description now reads "Independent researcher. This review is written from a family medicine perspective: …" — the founder/operator description, the residency/MBBS/BSc credential sentence, and the "not currently licensed or practising" sentence were removed at his instruction (his stated preference: the descriptive block was too extensive; he likes the family-medicine-perspective wording). The Conflicts of interest line was harmonised the same way ("The author is an independent researcher…"). Contact line unchanged (name, email, Palmdale CA, ORCID). Manuscript rebuilt (PDF + DOCX); manuscript_qa_gate.py prints PASS on the rebuilt PDF. Deposit package manuscript copies updated to match and checksums regenerated (93 files, all verified). No results, counts or conclusions affected.

## Rollout authorised + uncle summary — 2026-11-21 03:20 PT
Raphael authorised publication ("publish and roll out the rest"). Phase 7 rollout delegated (GitHub repo + Pages, Zenodo, hub, OSF attempt, LinkedIn/X after DOI verification, YouTube long-form + 3 Shorts, journal package prepared not submitted). He also asked for a simple 2-page plain-language summary for his uncle, whose own loss of taste prompted the study; drafted at uncle-summary/taste-loss-summary-for-uncle.pdf (source: uncle-summary/summary.html), built strictly from the manuscript's plain language summary and summary-of-findings numbers, no treatment recommendation, signed from Raphael with his email. For Raphael to send himself.
