# Pre-submission peer review — Reviewer R7 (Reporting and Integrity)

- **Persona:** Reviewer R7 — reporting and integrity (declarations, LLM team disclosure, citation integrity, figure/table completeness, plain language summary accuracy, placeholder text)
- **Date:** 2026-11-21
- **Manuscript:** `manuscript/manuscript.md` v1.0, 21 November 2026 — "Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments"
- **Files checked against:** `team-log.md` (Phases 1–4), `manuscript/included_studies_bibliography.md`, `screening/competing_reviews_and_guidelines.csv` (179 rows, skimmed in full)
- **Overall recommendation:** **Do not pass the gate — major revision required.** Two Blockers (a false citation pointer and a false search-reporting claim) must be fixed before any external step; six Majors follow. The underlying counts are unusually clean (see Verified section), so the fixes are reporting fixes, not re-analysis.

**Severity counts: Blocker 2 · Major 6 · Minor 7 · Nit 3 (18 issues total)**

---

## Blockers

**B1 — Blocker — References, "Prior syntheses cited by screening record" paragraph.**
The eight comparator syntheses (R02006, R02155, R02160, R02195, R02254, R02303, R02327, R01505) are cited by record ID only, with the claim that "full details [are] in Appendix C and the competing-reviews file" — verified false for Appendix C: none of the eight IDs appears in Appendix C (which lists only the 389 included studies), and R01505 appears in neither Appendix C nor `competing_reviews_and_guidelines.csv` (it is a FLAG-AUTHOR record per team-log Phase 2), so the manuscript's key Background citations are unresolvable from the manuscript as submitted.

**B2 — Blocker — Abstract (Search methods), Methods (Search methods), Discussion (Potential biases) vs Appendix B.**
Three places state that the unrun databases' "ready strings are printed in an appendix" / "their strings are printed in Appendix B," but Appendix B prints a full string for Embase only; for Scopus, Web of Science, CINAHL and CENTRAL it states the blocks will be "translated to each interface's field codes at run time" — i.e. no ready strings exist in the appendix for four of the five databases, a PRISMA-S reporting claim contradicted by the appendix itself.

## Majors

**M1 — Major — LLM team disclosure (Declarations) vs team-log Phases 2–3.**
The disclosure omits the entire citation-chasing full-text stage and the abstract-only adjudication outcomes: the log records chasing FT screening over 35 retrieved reports (agreement 0.7143, kappa 0.3636 — these two statistics appear nowhere in the manuscript at all), 15 adjudication reads with 2 both-exclude overturns, retrieval of 35/54, and abstract-only decisions over 232 records (90 include / 46 exclude / 96 awaiting) plus 19 chasing records (16 include / 3 awaiting); the disclosure jumps from the 72 chasing title/abstract disagreements directly to extraction, so it does not carry all Phase 1–4 counts as the RAISE 2025 disclosure requires (the Results flow paragraph covers the abstract-only counts, but the disclosure itself — the auditable record — does not).

**M2 — Major — Background ("What earlier reviews did") and Discussion ("Agreements and disagreements with other reviews").**
Differentiation is limited to 2020 syntheses, but the review's own competing-reviews file contains later, more directly comparable syntheses that are never mentioned: the 2023 taste-specific systematic review and meta-analysis in *Chemical Senses* (R00428, with its retraction-and-replacement R00427 and expression of concern R00535 also in the file), the BMJ 2022 recovery-curve meta-analysis (R00924) overlapping the Q1 recovery question, and the 2025 photobiomodulation systematic review (R00152) — which directly contradicts the Discussion's claim that "on treatments, there is no earlier synthesis to agree or disagree with at this scope."

**M3 — Major — Plain language summary, pathogenesis paragraph.**
The PLS states "the explanation with the most direct testing behind it is the smell one," but Table 3 gives T5 (inflammation) 4 direct-human studies against T4's (olfactory misattribution) 3, and the main text names three co-leading theories (T4, T5, T1) without ranking T4 first — the PLS, the section patients will actually read, asserts a ranking the review's own table does not support.

**M4 — Major — References, "Methods, guidance and prior synthesis" list.**
All eight methods/guidance citations (Cochrane Handbook, PRISMA 2020, PRISMA-S, RAISE 2025, RoB 2, ROBINS-I, JBI, GRADE) are given without DOIs, volume, pages or full author lists ("and others" throughout) — incomplete references for a manuscript claiming Cochrane-level/PRISMA 2020 reporting, and the RAISE 2025 statement on which the AI disclosure rests is itself not fully citable from this list. (No citation or DOI in the manuscript was found to be invented; the defect is incompleteness, not fabrication.)

**M5 — Major — Declarations, Data availability.**
Data availability is future-tense only — files "are held with the review files and will be deposited in the review's public repository," with no repository named and "no persistent identifier exists for them yet" — so at submission a reader cannot retrieve the protocol, search log, extraction sheets, RoB files, code or team log on which every verifiability claim in the manuscript depends.

**M6 — Major — Results, Harms paragraph vs Table 2 / team log.**
The Harms text introduces "3 adverse events in the prednisolone group" alongside "mild side effects in 9 of 58 (15.5%) versus 5 of 57 (8.8%)"; the "3 adverse events" figure appears nowhere in Table 2, the GRADE summary or the team log (which records only the 9/58 vs 5/57 comparison, no serious AEs, and 3 discontinuations), leaving two unexplained, apparently conflicting harm counts for the review's best-conducted trial.

## Minors

**m1 — Minor — Plain language summary, treatments paragraph.**
"Only three proper randomised trials reported a result for taste" overstates the zinc trial, which per Table 2 and the Q3 text reported no taste-specific estimate at all (composite smell-and/or-taste duration only) — a wording the PLS itself contradicts two sentences later ("Zinc… has never been tested in a way that measures taste on its own").

**m2 — Minor — Plain language summary, opening paragraph.**
"This review gathered every study it could find" overstates completeness given five databases not searched and the WHO ICTRP search not run (honestly reported in the main text, smoothed over in the PLS).

**m3 — Minor — Discussion, "Overall completeness and applicability."**
"The abstract-only stratum (106 includes across both chasing rounds)" mislabels the stratum: the 106 = 90 main-pool + 16 citation-chasing includes (per Results flow and team log), so "both chasing rounds" misattributes the main-pool 90.

**m4 — Minor — Discussion, "Potential biases in the review process."**
"Six narrative reviews inside the Q2 coding" is not traceable to the team log, which records only "about 19 to 20" records carrying the R1(d) no-primary-data flag in total (settlement log) with no Q2 subset of six stated anywhere in the files provided.

**m5 — Minor — Appendix C / included_studies_bibliography.md (format).**
The bibliography does not uniformly deliver the References section's promised "title, journal, DOI and PMID": verified counts are 29 of 389 entries with no PMID and 11 with no "DOI" label (preprints carrying the DOI inside the title line, three ClinicalTrials.gov registry records — R03352, R03416, R03494 — with neither journal nor DOI/PMID, and journal-only entries such as R02773, R02897, R02945 with neither identifier).

**m6 — Minor — Declarations, Pre-submission peer review statement.**
The statement is written in the completed past tense ("The draft received structured multi-agent pre-submission peer review… Gates 0 to 6") while that very gate process is still in progress (this R7 review is part of it), and the gate report is only "held with the review files" with no deposit route — the statement will be accurate only once the gate closes and should be finalised after, not before, the panel reports.

**m7 — Minor — LLM team disclosure, incidents list.**
The disclosure's incident list, though good, omits three log-recorded items: the batch-11 assembly repair (27 extraction rows caught short of Q3 fields and repaired with blanks), the RoB error taxonomy in the disclosure itself (four arithmetic errors, three tool-scope errors — present in Methods, absent from the disclosure), and the named duplicate-cohort pairs (R00573/R00714; R01101 = R02974, the same paper under two IDs), which the manuscript body never identifies.

## Nits

**n1 — Nit — Title block vs Declarations, Correspondence.**
Correspondence is complete in Declarations (Raphael Malikian, rtmalikian@gmail.com, Palmdale, CA, USA, ORCID 0009-0008-4326-4205 — all present and consistent with the header email), but the ORCID appears only there and not in the title block, where only the email is given.

**n2 — Nit — Appendix C / bibliography, entry R02697.**
The entry retains literal HTML markup ("<strong>Ageusia and Anosmia, a Common Aign of COVID-19?…</strong>") carried over from the source record, including the apparent "Aign" for "Sign" typo — leftover markup in a submission-ready bibliography.

**n3 — Nit — References, prior-syntheses paragraph (grouping).**
R01505 is grouped under "Prior syntheses… [in] the competing-reviews file," but per the team log it entered via the FLAG-AUTHOR route and was retained for Background differentiation — the grouping misstates its provenance even once B1's pointer is fixed.

---

## Verified — no issue found (checked, not assumed)

- **Included-studies appendix:** Appendix C contains exactly **389 entries, all unique IDs (363 R-IDs + 26 C-IDs, matching the team log's 363 main-pool + 26 chasing inclusions)**, and is **identical in IDs, order and content to the standalone `included_studies_bibliography.md` (389/389)**; flagged record C8424 is correctly present in both (included, excluded from synthesis only). Duplication of the same list in two places is a drift risk on future edits, not a current discrepancy.
- **Declarations completeness (present):** Funding (None) and Conflicts of interest (None) appear in both the front matter and Declarations; the AI-assistance note names the tool (Muse Spark, Meta), invokes RAISE 2025, states purposes and human checks, and assigns full responsibility to the human author; no PROSPERO number is claimed anywhere (honestly stated as not issued).
- **LLM disclosure numbers that do check out against the team log:** title/abstract screening agreement 0.890 / kappa 0.618 / 384 disagreements (128/93/150/13); full-text agreement 0.868 / kappa 0.347 / 54 disagreements (32/22) + 5 coordinator exclusions; chasing 555 sources / 13,651 candidates / 72 disagreements (39/30/3); extraction 11,670 cells, 5,405 textual differences (46.3%), 1,197 substantive (10.3%), 4,208 wording-only; pilot 195 differing cells, 31 substantive; RoB agreement 75.3% / kappa 0.603 / adjudication siding 40/56; final RoB bands 62/214/61/52; both discarded Screener B implementations, the chasing output bug, the scratch-file collision and the C8424 flag are all disclosed.
- **Flow and table arithmetic:** 5,988 − 2,487 = 3,501; 363 + 26 = 389 (synthesis denominator 388 after C8424); abstract-only 90 + 46 + 96 = 232 and 90 + 16 = 106; awaiting classification 96 + 3 = 99 as stated in Discussion; publication-year counts sum to 389; RoB tool counts (153+131+30+8+11+4+52) and band counts each sum to 389; Table 3 theory tags sum to the stated 409 assignments and every row sums to its stated total; Q2 proportions (223/388 = 57.5%; 164/223 = 73.5%) recompute correctly.
- **Figures and tables:** Figures 1, 2A–2D, 3 and 4 are all embedded, all seven image files exist in `manuscript/figures/`, every figure has a caption, and every figure and Tables 1–3 is cross-referenced in the text; Figure 2's panel ranges (1–35, 36–70, 71–105, 106–137) correctly partition the 137-study pool.
- **Plain language summary (accurate parts):** 38-in-100 frequency, 5-to-87 prediction range, 85–88-in-100 complete recovery, "different groups of people" caveat, very-low certainty, six-of-eleven theories with no direct human test, prednisolone null result, photobiomodulation single 36-participant trial, and harms reported in only 6 of 23 studies all match the main text and Tables 1–2.
- **Placeholder text / invented identifiers:** none found — no TODO/TBD/lorem text, and the team log's draft-only marker "[Project 1 citation — insert verified DOI before submission]" is correctly absent; the manuscript's closing statement that "no placeholder citation appears in this manuscript" was verified true, and no DOI for this review or its follow-on is claimed anywhere.
- **Author framing:** the title block describes the author as "not currently licensed or practising as a clinician"; the phrase "former physician" appears nowhere in the manuscript.

*— End of R7 review. Recommendation restated: hold the gate; fix B1–B2, address M1–M6, and re-verify the disclosure against the team log before submission.*
