# Peer-review feedback loop 2 — Verification, Reviewer R1 (Cochrane methods)

- **Persona:** R1 — Cochrane methods editor
- **Task:** Verification only, Loop 2. Re-check ONLY the two Minor NEW ISSUES raised in `loop1_R1.md` (N1, N2) against the revised files. No manuscript file was edited.
- **Sources checked:** revised `manuscript/manuscript.md` and the PDF text layer (`pdftotext`; rebuilt PDF, 113 pages); `scripts/make_figures.py` Figure 1 labels (lines 219, 224, 226) and the Loop 2 entry in `manuscript/figure-inspection-log.md`; `deposit/` full file listing, `deposit/README.md`, and `deposit/checksums.sha256` (all checksums re-verified locally).
- **Date:** 2026-11-21

## Summary verdict

**N2 is FIXED. N1 is fixed at every site except one: the citation-chasing sources composition in the Methods still carries its pre-step 363 with no local flag.** That single residual is Minor, clarity only, and non-blocking — no number anywhere is wrong. **No Blocker and no Major remains open in the R1 remit; one Minor (the N1 residual) remains open.**

| Item | Verdict |
|---|---|
| N1 (a) — Results study flow flags the main-pool 363 | **FIXED** |
| N1 (b) — Methods extraction flags its 389 | **FIXED** |
| N1 (c) — LLM team disclosure flags its extraction 389 | **FIXED** |
| N1 (d) — Figure 1 flags the stage count; included-total box shows 389 → 363 | **FIXED** |
| N1 (residual) — chasing-sources composition (555 sources) in Methods | **NOT FIXED — remains open (Minor)** |
| N2 — Data availability enumeration vs the deposit package | **FIXED** |

---

## N1 — Pre-step process counts: FIXED at (a)–(d); one residual site remains

**(a) Results — Study flow: FIXED, verbatim as specified.** "Forty-five reports were excluded at full text, leaving 363 included studies from the main pool (a stage count before citation chasing and before the eligibility-consistency step; the final total after that step is also 363, by coincidence)." The same wording is present in the rebuilt PDF text layer. The following sentences then narrate the sequence in order (chasing added 26 → "The included total after full-text assessment and citation chasing was 389 records" → the eligibility-consistency step excluded 26), so the 389 in Results is bridged by its own narrative sequence as well.

**(b) Methods — Data extraction: FIXED, verbatim as specified.** "Full extraction ran in two fully independent passes over all 389 included records (11,670 cells; the included set as it stood before the Phase 6 eligibility-consistency exclusion)."

**(c) LLM team disclosure: FIXED.** The extraction count now reads "extraction in two independent passes over the 389 records then included (before the Phase 6 eligibility-consistency exclusion) and 11,670 cells…". The disclosure's RoB 389, which Loop 1 already noted was bridged, remains bridged in the same passage: final bands are given "(across the 389 records as extracted; after the Phase 6 eligibility-consistency exclusion of 26 not-assessable records, the retained bands are low 62, moderate 214, high, serious or critical 61, not assessable 26)". For completeness: the Methods — Risk of bias paragraph itself states no 389 numeral (agreement percentage and adjudication counts only), so there is no unflagged pre-step count at that site. A sweep of all 389 occurrences in the main text found no other unbridged site.

**(d) Figure 1: FIXED.** The generator (`scripts/make_figures.py`) now labels the main-pool box "Included from main pool: 363 (stage count, before the eligibility-consistency step below)", and the included-total box reads "Included total before the eligibility-consistency step: 389 records / INCLUDED TOTAL after the step: 363 records (362 unique publications; …) (Q1 339, Q2 280, Q3 82; multi-membership)", above the dedicated Phase 6 step box. The Loop 2 entry in `figure-inspection-log.md` records that Figure 1 was regenerated, page 20 of the rebuilt 113-page PDF was rendered and visually inspected (all boxes legible, no overflow, sequence reads in order), and the QA gate passed on this build. Figure 1 is a placed image, so its text is not in the PDF text layer; the verdict rests on the generator labels plus the recorded visual inspection, as in Loop 1.

**Residual — chasing-sources composition: NOT FIXED.** Loop 1 flagged, as the first-named site of N1, the Methods sentence giving the chasing denominator. It is unchanged and still unflagged locally, in Methods — Search methods: "Citation chasing (backward references and forward citations, through Europe PMC) was performed on all 363 main-pool inclusions, all 179 competing reviews and guidelines, and the 13 author-flagged records retained for chasing: 555 sources in all." No clause identifies this 363 as the pre-chasing, pre-step stage count. The bridging added at (a) and (d) defines that same 363 elsewhere in the manuscript, and the composition is chronologically intelligible (chasing was necessarily performed on the inclusions that existed before chasing), so the residual risk is confined to a reader meeting the Methods sentence in isolation and taking its 363 for the final total it coincidentally equals. That mitigates the issue but does not meet the remedy Loop 1 specified — one clause at each flagged site. One clause closes it, e.g. "all 363 main-pool inclusions (the stage count before citation chasing; the final total after the eligibility-consistency step is also 363 — see Results, Study flow)". **Verdict: N1 remains open as a single-site Minor. Not blocking; no re-analysis, no renumbering, and no other site is affected.**

---

## N2 — Data availability vs the deposit package: FIXED

The Loop 2 fix completed the package rather than trimming the sentence; the sentence in Declarations — Data availability is unchanged, and it is now accurate. Clause-by-clause verification against `deposit/` as assembled:

| Sentence enumerates | Present in `deposit/` |
|---|---|
| Protocol | `protocol-locked.md` |
| Search log | `data/search-log.md` |
| Screening and adjudication files | `data/screening/` — all 13 source files mirrored: `screening_AB.csv`, `screening_final_TA.csv`, `screening_stats.json`, `prisma_counts_phase1.json`, `competing_reviews_and_guidelines.csv`, and `adjudication/` (decisions 1–4, packets 1–4) |
| Extraction sheets (both passes and the settled file) | `data/extraction/` — `extraction_A_full.csv`, `extraction_B_full.csv`, both pilots, `extraction_pilot_settled.csv`, `full_discrepancy_report.json`; settled file at `data/extraction_settled_full.csv` |
| Risk of bias files | `data/rob_pass1_all.csv`, `data/rob_pass2_all.csv`, and the adjudicated `data/rob_adjudicated_full.csv` |
| Analysis datasets and code | `data/analysis/` (31 files: pool CSVs, result JSONs, pool logs, hand-check, GRADE assessment, Q2 Phase 6 note) and `code/` (4 files) |
| LLM team log | `team-log.md` |

Also present, as the task described: `data/fulltext/` (full-text decision, chasing and PRISMA count files), the differentiation log and competing-reviews file, and the manuscript in Markdown, PDF and DOCX. The specific absences Loop 1 named — no search log, no screening files, no first/second extraction passes, no team log — are all cured.

**Package integrity verified, not taken on trust:** `deposit/` contains 94 files; `checksums.sha256` lists 93 (every file except the checksum file itself), and `sha256sum -c` returns **93 OK, 0 FAILED**. `deposit/README.md` lists the expanded contents accurately, including the new directories, and still states plainly "Not yet deposited: no persistent identifier exists for this package and none is claimed" — matching the manuscript sentence's "ready for deposit… No persistent identifier exists for them yet; none is claimed." The underlying author action (make the deposit and insert the verified persistent identifier) remains outstanding by design and honestly disclosed; it is not part of N2. **Verdict: FIXED, closed.**

---

## Blocker / Major / open-item statement

- **Blocker:** none open.
- **Major:** none open in the R1 remit.
- **Minor open:** one — the N1 residual only (the unflagged pre-step 363 in the Methods chasing-sources composition, 555 sources). N2 is closed, and N1 (a)–(d) are closed.
- Everything else in the R1 remit remains as verified in Loop 1; nothing in the Loop 2 changes re-opens any Loop 1 item.
