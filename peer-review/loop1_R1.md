# Peer-review feedback loop 1 — Re-review, Reviewer R1 (Cochrane methods)

- **Persona:** R1 — Cochrane methods editor
- **Task:** Verification only. Re-check of R1's still-open items from `rereview_R1.md` (Gate 5) against the Phase 6 revised manuscript (`manuscript/manuscript.md`; PDF `manuscript/manuscript.pdf`, 112 pages), plus regression check of the Phase 6 changes in the R1 remit. No manuscript file was edited.
- **Sources checked:** revised manuscript.md and the PDF text layer (pdftotext); `fulltext/prisma_counts_phase4.json`; `competing/differentiation_log.csv` (row-level count); Appendices C/D/E as embedded in the manuscript (row-level count); `scripts/make_figures.py` Figure 1 labels and `manuscript/figure-inspection-log.md` Phase 6 entry; `deposit/README.md` and `deposit/checksums.sha256` (all 17 checksums verified OK).
- **Date:** 2026-11-21

## Summary verdict

**All R1 items carried into Phase 6 are FIXED. No Blocker and no Major in the R1 remit remains open.** Two minor NEW ISSUES are raised (clarity of pre-step process counts; Data availability contents enumeration broader than the assembled package). Neither blocks the gate.

| Item | Verdict |
|---|---|
| Phase 6 item 1 — 26-record exclusion + count harmonisation | **FIXED** (one minor NEW ISSUE, N1) |
| R1-M3 — tiered differentiation log / Difference 11 | **FIXED** |
| R1-M6 — Project 2 declared difference (Difference 13) | **FIXED** |
| R1-m1 — Differences structure declared a conscious choice | **FIXED** |
| R1-m2 (residual) — ROBINS-I/JBI scope as Difference 12 | **FIXED** |
| R1-m8 — deposit package / Data availability honesty | **FIXED** on its reporting terms (one minor NEW ISSUE, N2) |
| R1-m10 — language + preprint/conference-abstract counts | **FIXED** |

---

## Item 1 — Eligibility-consistency exclusion of the 26 and count harmonisation: FIXED

The exclusion is disclosed, not silent, at every level a reader meets it:

- **Abstract — Main results:** "363 were included after full-text assessment, citation chasing and a final eligibility-consistency step, representing 362 unique publications (one paper, Ohla 2022, appears under two record IDs, R01101 and R02974; neither contributed data to any pool). At the final step, 26 records with no primary data (narrative reviews, letters and one hypothesis paper; the class includes C8424) were formally excluded under the locked eligibility for primary studies and are listed in Appendix E; none had contributed data to any pool, so no pooled number changed."
- **Plain language summary:** "Twenty-six records that turned out to be summary articles, letters or an idea paper with no original data of their own were removed from the list at a final check, because the review's rules only allow studies with their own data; they are listed in the review's appendix of excluded studies, and none of them contributed to any result."
- **Methods — Difference 6** gives the full rationale (locked eligibility admits primary studies only; "the same standard applied at full-text screening… and in the resolution of the author-flagged records"), the standard Appendix E reason, and the superseded earlier handling. **Difference 7** restates the Q2 consequence: "the pathogenesis counts from 223 coded studies and 409 assignments to 214 studies and 383 assignments (speculative 157 of 214, 73.4%); every direct-human count in Table 3 is unchanged and no theory verdict changes."
- **Results — Study flow** narrates the step in sequence (389 after chasing → 26 excluded → "363 included records representing 362 unique publications") and **Discussion — Potential biases** (fifth point) re-discloses it, including the superseded first-draft handling ("one (C8424) excluded from synthesis counts, the rest retained in the denominator").

Harmonisation verified by independent recount, not taken on trust:

- Appendices as embedded in the manuscript: Appendix C = **363** entries; Appendix D = **363** rows under the heading "characteristics of included studies (363 records)"; Appendix E = **87** rows under "studies excluded at full text or at the eligibility-consistency step, with reasons (87)" — i.e. the previous 61 + 26.
- All 26 record IDs in `prisma_counts_phase4.json` (`phase6_eligibility_consistency_step.excluded_records`, incl. C8424) appear in Appendix E, each with the standard reason ("Excluded at the Phase 6 eligibility-consistency step: no original primary data — narrative review / secondary source; used for citation chasing and Background differentiation only" — 26 occurrences), and **none** of the 26 appears in Appendix C or D.
- Question memberships recomputed from `fulltext/final_included.csv` (389 rows) minus the 26: retained = 363; **Q1 339, Q2 280, Q3 82** — exactly as stated in Results — Description of studies ("Question membership… was Q1 339, Q2 280 and Q3 82") and in Figure 1.
- Internal sums reconcile at 363: publication years (73+99+96+44+22+14+15 = 363); virus (360 SARS-CoV-2 + 3 unspecified); RoB tools (153+131+30+8+11+4 = 337, +26 not assessable = 363); final bands (62+214+61+26 = 363). Table 3 "Studies tagged" column sums to 383 assignments, matching Difference 7 and the Q2 text (214 studies, 383 assignments, speculative 157/214 = 73.4%). The old counts 223/409 survive only in the two places that frame them explicitly as the pre-restatement values (Difference 7; Q2 Results closing note).
- `prisma_counts_phase4.json` documents the step (basis, class composition 20 narrative/bibliographic reviews + 4 letters + 1 correspondence + 1 hypothesis paper = 26, pool-by-pool verification that none of the 26 is in any pool file, "pooled_numbers_changed": false) and matches the manuscript.
- **Figure 1 regenerated:** the generator (`scripts/make_figures.py`) labels the final box "INCLUDED TOTAL after the eligibility-consistency step: 363 records (362 unique publications…) (Q1 339, Q2 280, Q3 82; multi-membership)" plus a dedicated Phase 6 box ("26 records with no primary data… formally excluded — Appendix E. None contributed data to any pool, so no pooled number changed. Synthesis set: 363 records"); the Phase 6 entry in `figure-inspection-log.md` records visual inspection of the rebuilt PDF page, and the PDF text layer carries the harmonised headings (Appendices C 363 / D 363 / E 87). One numerical coincidence is correct but worth the gate's awareness (see N1): the pre-step main-pool total and the final total are both 363, because chasing added 26 and the step removed 26.

No regression: pooled estimates, GRADE ratings, the abstract-only stratum (90 + 16 = 106), and the funding tally (restated once, as 103 records with funding not reported — the Gate 5 figure of 117 was on the 389 denominator) are consistent throughout Abstract, PLS, Results and Discussion.

## Item 2 — R1-M3 (tiered differentiation log; Difference 11 rewritten): FIXED

The log exists and its arithmetic is exactly as the manuscript describes. Row-level count of `competing/differentiation_log.csv`: **179 rows** — Tier 1: 10, Tier 1 (notice): 2, Tier 2: 47, Tier 3: 110, "Not relevant — different clinical question": 3, "Not a competing synthesis": 7 (10+2+47+110+3+7 = 179). Every row carries a disposition reason.

- **Difference 11:** "the 179 captured competing reviews are accounted for in tiers rather than differentiated one by one. Twelve captured records are differentiated by name in the Background (Tier 1: the seven 2020 syntheses, the 2023 taste-specific review with its retraction-and-replacement and its expression of concern, the 2022 prognosis meta-analysis and the 2025 photobiomodulation review). Every other captured record is logged individually in a differentiation log deposited with the review (Tier 2: 47…; Tier 3: 110…; 3 records logged as not relevant…; 7 records that are single-patient case reports rather than syntheses), each with its disposition and the reason read from its title and type as captured at screening."
- The 12 Tier 1 records check out individually: R02006, R02155, R02160, R02195, R02254, R02303, R02327, R00428, R00924, R00152 are Tier 1 in the log and differentiated in substance in the Background; R00427 and R00535 are "Tier 1 (notice)" in the log and are addressed with R00428 in the Background ("its record in the captured set carries both a retraction-and-replacement (R00427) and an expression of concern (R00535)").
- **Background** closing of the competing-reviews paragraph mirrors the log: "every captured record is accounted for in a tiered differentiation log deposited with the review (Tier 1: the records differentiated by name here; Tier 2: 47…; Tier 3: 110…; 3 records logged as not relevant…; and 7 records that are single-patient case reports rather than syntheses), each with its disposition and the reason read from its title and type as captured at screening, as declared in the Methods (Difference 11)."

Judgement: this discharges R1-M3. The Gate 5 partial verdict rested on two absences — no tiering and no per-record log; both now exist, the per-record reasons are present for all 179, and the basis of the Tier 2/3 dispositions (title and type as captured at screening, not full-text reading) is declared in both the Background and Difference 11, so no reader can mistake the log for a read-and-differentiated exercise. The locked standard is met in the tiered-log form the loop adopted, with its one limitation stated on the face of the manuscript.

## Item 3 — R1-M6 (Project 2 declared difference): FIXED

**Difference 13** now declares it, factually and neutrally: "Thirteenth, the protocol committed to a follow-on meta-analysis of the most promising treatment. This review's treatment finding is that no intervention has more than one comparative study with a taste outcome, so no single-treatment meta-analysis is justified on this evidence; the follow-on's form follows that finding and is under author consideration. No framing commitment is made in this review, and no citation of the follow-on appears in it."

The declared-differences count is consistent ("Thirteen differences are declared", First through Thirteenth all present, no Fourteenth). No placeholder citation exists: the only occurrence of the word "placeholder" in the manuscript is the denial in Authors' conclusions — Implications for research ("Its citation of this review will use this review's verified deposit citation once live; no placeholder citation appears in this manuscript"), and that section's follow-on wording ("a follow-on treatment-evidence project arising from this review is planned; its form follows the finding reported here… and it will be framed accordingly when the author settles its scope") is now consistent with the declared difference rather than an undeclared divergence. The item as originally scored — declaration completeness — is cured.

## Item 4 — R1-m1 (Differences structure as conscious choice): FIXED

The Differences section now opens: "This section opens the Methods as a conscious structural choice: every departure from the locked protocol is declared before the methods that embody it are described, so that no departure is discoverable only by comparing the two documents." That is verbatim the remedy the original review asked for.

## Item 5 — R1-m2 residual (ROBINS-I/JBI scope narrowing declared): FIXED

**Difference 12:** "Twelfth, the risk of bias assessment instruction set allocated the tools more narrowly than the protocol's naming of them: ROBINS-I was applied to treatment studies, and non-randomised cohorts outside the treatment question were assessed with JBI cohort checklists. The allocation is described in the risk of bias Methods and is declared here because the protocol named the tools without it." Together with the JBI band thresholds printed at Gate 5 (still present in Methods — Risk of bias), both halves of R1-m2 are now closed.

## Item 6 — R1-m8 (deposit package; Data availability): FIXED on its reporting terms; one minor NEW ISSUE (N2)

**Declarations — Data availability** now reads: "The protocol, search log, screening and adjudication files, extraction sheets (both passes and the settled file), risk of bias files, analysis datasets and code, and the LLM team log have been assembled with the manuscript as a deposit package (with a README listing contents and checksums), ready for deposit in the review's public repository. No persistent identifier exists for them yet; none is claimed."

The wording is honest on the point the item turns on: present-state assembly ("have been assembled… ready for deposit"), preparation only, and no persistent identifier claimed — the future-tense "will be deposited" of the Gate 5 text is gone. The package itself verifies: `deposit/` exists with `README.md` (which states plainly "Not yet deposited: no persistent identifier exists for this package and none is claimed") and `checksums.sha256`, and all 17 checksums verify OK, including the differentiation log, the settled extraction file, the adjudicated RoB file and `prisma_counts_phase4.json`. Actual deposit and insertion of the verified identifier remain, unavoidably, an author action at submission; the manuscript neither claims nor implies otherwise, so nothing in the text is untrue at submission. On that basis the reporting item is FIXED; the gate should still list "deposit and insert PID" as a pre-submission author action, as it did at Gate 3.

## Item 7 — R1-m10 (language and design-flag counts, with methods): FIXED

Both counts are now stated, each with its method, and neither is overclaimed:

- **Language of the 99 awaiting classification** (Results — Study flow): "The 99 records across the strata that remain awaiting classification were examined for language of publication from their titles, journals and abstracts as recorded in the review files: 64 are English-language, 2 are Chinese-language (both published in Chinese journals, with bracketed translated titles in the records), and for 33 the language cannot be determined from the files (30 records with no abstract in the files and English-language titles, and the 3 citation-chasing records, for which no abstract is held); no language was guessed for any record." (64+2+33 = 99.) The 33 undetermined are reported as undetermined, not folded into English — exactly the restraint the item required.
- **Preprints and conference abstract among the 363** (Results — Description of studies): "Twenty-two of the 363 (6.1%) are preprints, identified from their preprint DOI, journal or source as recorded, and one is a conference abstract (R02897, the conference-abstract report of the cohort also reported in full in R01739)." (22/363 = 6.1% ✓.)
- **Difference 9** gives the same denominator for the unrun sensitivity, with its counting method: "The unrun preprint-exclusion sensitivity would have removed 22 records (6.1% of the 363 included), counted from the preprint DOI, journal and source fields as recorded; the size of the unrun sensitivity is stated here even though it was not run." The sensitivity remains declared unrun; the denominator that R1-m10 found unverifiable is now checkable from the manuscript. (The 418 Europe PMC preprint figure elsewhere in the manuscript is the retrieved-records count and is labelled as such; it is no longer the only preprint number in the text.)

---

## New issues

**N1 (Minor, clarity only — no number is wrong). Pre-step process counts are correct in place but only partly bridged.** Methods — Selection of studies states citation chasing "was performed on all 363 main-pool inclusions, all 179 competing reviews and guidelines, and the 13 author-flagged records…: 555 sources in all" — that 363 is the *pre-step* main-pool total, a different referent from the final 363 it coincidentally equals; and Methods — Data extraction ("Full extraction ran in two fully independent passes over all 389 included records") and the RoB process counts use the pre-step 389 without a local flag. The LLM team disclosure does bridge the RoB bands explicitly ("across the 389 records as extracted; after the Phase 6 eligibility-consistency exclusion of 26 not-assessable records, the retained bands are…"), and every figure is historically accurate, so this is a reader-confusion risk, not an inconsistency. One clause at each site (e.g. "as extracted, before the eligibility-consistency step") would close it. Not blocking.

**N2 (Minor). Data availability enumerates a broader package than `deposit/` contains.** The sentence lists "search log, screening and adjudication files, extraction sheets (both passes and the settled file)… and the LLM team log" as assembled in the deposit package, but `deposit/` as assembled contains the protocol, the manuscript, the settled extraction file only, the adjudicated RoB file, the final-included file, the PRISMA count files, the competing-reviews file and differentiation log, and four code files — no search log, screening files, first/second extraction passes, or team log. The `deposit/README.md` lists the actual contents accurately, so the package is honestly described where it is described in detail; the manuscript sentence should either be trimmed to the README's contents or the missing files added to the package before deposit. Not blocking; no identifier or deposit status is misstated.

**Note for the gate (not scored):** Declarations — Pre-submission peer review states the loop "closed with no Blocker or Major item open." For the R1 remit that statement is consistent with this re-review; its truth for the panel as a whole depends on the other reviewers' loop verdicts, which are outside this remit.

## Blocker / Major statement

- **Blocker:** none open. R1-B1 was fixed at Gate 5 and is unaffected by Phase 6 (Appendices D and E verified at 363 and 87 rows respectively in this re-review).
- **Major:** none open in the R1 remit. The two Majors carried into Phase 6 — R1-M3 (partially fixed at Gate 5) and R1-M6 (not fixed at Gate 5, author-action) — are both FIXED. R1-M1, M2, M4, M5 and M7 remain fixed as verified at Gate 5; the Phase 6 restatements touch their counts (notably M4/M7's denominators) only through the disclosed eligibility-consistency step, with no pooled number, rating or verdict changed.
- **Remaining R1 items:** N1 and N2 (both Minor, clarity/accuracy of apparatus, neither requiring re-analysis). R1-m8's underlying author action — make the deposit and insert the verified persistent identifier — remains outstanding by design and is honestly disclosed in the manuscript.
