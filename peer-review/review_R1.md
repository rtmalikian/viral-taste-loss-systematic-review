# Pre-submission peer review — Reviewer R1

- **Persona:** R1 — Cochrane methods editor
- **Remit:** Protocol fidelity, Cochrane structure/order, PRISMA 2020 and PRISMA-S reporting completeness, honesty of declared protocol deviations
- **Manuscript:** *Loss of taste in possible viral infection: etiologies, pathogenesis, and the evidence for treatments* — Version 1.0, 21 November 2026 (manuscript.md)
- **Sources read:** manuscript.md; protocol-locked.md (LOCKED v1.0, 2026-11-20, incl. amendment log); team-log.md (Phases 1–4); search-log.md (PRISMA-S log, 2026-11-20); fulltext/prisma_counts_phase3.json
- **Date:** 2026-11-21
- **Overall recommendation:** **Major revision — do not advance beyond this gate** until the Blocker is resolved and each Major is either fixed or explicitly declared in *Differences between protocol and review*. The results themselves are not impugned by this review; the failures are of reporting completeness and undeclared protocol divergence.

**Standing facts applied, not re-litigated:** 389 included / synthesis denominator 388 with record C8424 FLAG-AUTHOR pending the author's decision (disclosed; not scored as an error); Embase / Scopus / Web of Science / CINAHL / CENTRAL and WHO ICTRP not run and disclosed as not run (not scored); the follow-on "Project 2" framing is pending the author's decision and neutrally worded on purpose (scored only as a declaration-completeness item, R1-M6).

**What checks out (verified, no action):** PRISMA flow arithmetic reconciles exactly with prisma_counts_phase3.json at every stage (5,988 retrieved; 2,487 duplicates removed; 3,501 screened; 2,854 title/abstract excludes; 634 to retrieval; 408 assessed; 45 full-text excludes; 363 main-pool includes; chasing 16,615 + 13,867 examined, 13,651 candidates, 26 includes; abstract-only 90 + 16 = 106 includes and 96 + 3 = 99 awaiting classification, matching the Discussion). Summary of Findings sits before Background, as the protocol requires. Discussion carries all five Cochrane subsections. The six declared differences (PROSPERO number, ICTRP, abstract-only amendment, missing interaction tests, Q-based I² definition, C8424) are candid and match the protocol amendment log. RoB tool counts (153 + 131 + 30 + 8 + 11 + 4 + 52 = 389) and final bands (62 + 214 + 61 + 52 = 389) sum correctly.

---

## Blocker (1)

**R1-B1 — No study-level Characteristics of included studies and no Characteristics of excluded studies exist in the manuscript or in any named supplement.**
*Location: Results — Description of studies; Appendix C.*
Justification: Description of studies is aggregate-only (years, journals, provisional Q-membership, virus, RoB tool counts) and Appendix C is a bibliography (author/year/title/journal/DOI/PMID) with no design, population, N, setting, ascertainment or outcome columns; likewise the 61 full-text exclusions (45 main-pool + 9 chasing + 7 FLAG-AUTHOR) are given only aggregate reasons, with per-study reasons nowhere cited — both tables are MECIR-mandatory and PRISMA 2020 items 16b/17, and a generic "files will be deposited" statement does not substitute for them at submission.

## Major (7)

**R1-M1 — The reported subgroup analyses are not the pre-specified subgroups, and the substitution is undeclared.**
*Location: Methods — Differences between protocol and review; Results — Q1: frequency.*
Justification: protocol-locked.md pre-specifies subgroups by virus, confirmation method, duration at enrolment, age, and treatment class, but the manuscript reports only ascertainment (psychophysical vs self-report) and setting (hospitalised vs community) — neither in the locked list — while confirmation, duration and age subgroups are absent with no explanation; Difference 4 declares only the missing interaction tests, not the changed subgroup set.

**R1-M2 — Three of the four pre-specified sensitivity analyses are missing and their omission is undeclared.**
*Location: Methods — Differences between protocol and review; Results — Q1: frequency (sensitivity analyses).*
Justification: the protocol locks sensitivities excluding preprints, excluding TASTE-AMBIGUOUS records reclassified as olfaction-only, and excluding case series/uncontrolled designs, yet only the high-RoB sensitivity (plus a registry-exclusion variant) is reported, and the Differences section never mentions the other three.

**R1-M3 — The locked Background citation standard was not followed and the shortfall is not declared.**
*Location: Background (all subsections); Methods — Differences between protocol and review.*
Justification: protocol-locked.md requires Backgrounds built Tier 1 → Tier 2 → Tier 3 on retrieved-and-read citations with all 179 captured competing reviews (screening/competing_reviews_and_guidelines.csv) cited/differentiated or logged not-relevant with a reason, but the Background differentiates only seven reviews by record ID (R02006, R02155, R02160, R02195, R02254, R02303, R02327, plus R01505), applies no tiering, cites no not-relevant log, and carries its etiology/pathogenesis framing as uncited narrative.

**R1-M4 — Three pre-specified Important outcomes are listed in Methods and then never reported.**
*Location: Methods — Eligibility criteria (Outcomes); Results (absence); Summary of findings.*
Justification: quality of life, proportion with persistent dysfunction at ≥12 weeks, and smell–taste discordance appear as Important outcomes in both protocol-locked.md and the manuscript's own Methods, but no Results section, SoF row, or explicit "no separable evidence" statement accounts for any of them (discordance is touched only narratively inside the T4 pathogenesis account) — PRISMA 2020 requires results, or an explicit empty accounting, for every outcome named in Methods.

**R1-M5 — The abstract-only stratum has no Results-level synthesis, so the Discussion claim made for it is unsupported in the text.**
*Location: Results (absence); Discussion — Overall completeness and applicability.*
Justification: the 2026-11-20 abstract-only amendment (protocol-locked.md) assigns the 106 abstract-only includes a role of "narrative evidence mapping, gap analysis," but no Results subsection maps or summarises them, while the Discussion asserts the stratum "maps the same territory… to show that the retrieval gap does not hide a second, different literature" — a conclusion no presented analysis supports; either present the mapping or delete/soften the claim.

**R1-M6 — AUTHOR-ACTION: the protocol's Project 1 → Project 2 commitment was changed in substance and the change is not listed among the declared differences.**
*Location: Methods — Differences between protocol and review; Authors' conclusions — Implications for research.*
Justification: protocol-locked.md commits the Research conclusions to state that a follow-on meta-analysis of the most promising treatment is planned, whereas the manuscript (correctly, on the Task 5 no-pick finding in team-log.md) names no most promising treatment and states only that a follow-on project "is planned… framed accordingly when the author settles its scope" — the neutral wording is accepted as pending the author's decision, but once settled the divergence must be added as a seventh declared difference so the deviation list is complete.

**R1-M7 — Locked special-population reporting is discharged for only two of eight populations, with no per-treatment accounting.**
*Location: Results — Q3: treatments (final paragraph).*
Justification: protocol-locked.md locks eight special-population extraction fields (pregnancy/lactation, children, older adults/frailty, immunocompromise, diabetes, chronic kidney/liver disease, polypharmacy, pre-existing chemosensory disorders) with per-treatment dose-adjustment/contraindication reporting, but the manuscript reports only children (one case series) and pregnancy (exclusion in two trials) in a single closing sentence and is silent — not even "no data reported" — on the other six.

## Minor (10)

**R1-m1 — Cochrane structural conventions are only partly followed.**
*Location: Methods (subsection order and headings).*
Justification: "Differences between protocol and review" opens Methods, where Cochrane places it at the end of Methods, and PRISMA-style headings ("Eligibility criteria") replace the Cochrane "Criteria for considering studies / Types of studies, participants, interventions, outcomes" structure — tolerable in a Cochrane-level (not Cochrane) review, but the choice should be conscious and consistent.

**R1-m2 — The ROBINS-I scope was narrowed after lock without declaration, and the JBI band-mapping thresholds are not in the manuscript.**
*Location: Methods — Risk of bias.*
Justification: protocol-locked.md assigns ROBINS-I to "non-randomised treatment/cohort" studies, but the manuscript assigns ROBINS-I to treatment studies only and JBI cohort checklists to 131 cohorts (a choice pre-specified only in the post-lock rob_instructions.md, per team-log.md Phase 4), and the "pre-stated mapping from checklist proportions to overall bands" is asserted without its thresholds appearing in the manuscript or a named supplement.

**R1-m3 — The locked comparative-effect analysis plan never appears in Methods.**
*Location: Methods — Synthesis and GRADE.*
Justification: protocol-locked.md locks risk ratios for recovery and mean/standardised mean differences for scores where ≥2 studies map, but the Synthesis paragraph describes proportion pooling only and never states the comparative plan or that no outcome reached the ≥2-study threshold for it, leaving the prednisolone/photobiomodulation score results in Table 2 without a stated analysis framework.

**R1-m4 — PROSPERO status is ambiguous between "prepared" and "submitted."**
*Location: Title-block Registration note; Methods — Differences (First).*
Justification: the manuscript states a "PROSPERO-ready form was prepared" and that "no PROSPERO registration number had been issued," which can be read as implying a submission is pending; protocol-locked.md records only that a form was prepared and no number exists — state plainly whether the form was submitted to PROSPERO or not (PRISMA 2020 item 24).

**R1-m5 — Two PRISMA / PRISMA-S reporting elements are missing from the manuscript (present only in the search log).**
*Location: Methods — Search methods; Results — Description of studies.*
Justification: the deduplication method (DOI → PMID → NCT → normalised title, in search-log.md and scripts/dedup_and_screen.py) is never described in the manuscript, and although funding/conflicts of included studies was an extraction field, no summary of included-study funding sources appears in the Results (PRISMA-S deduplication reporting; PRISMA 2020 item on included-study funding).

**R1-m6 — Risk of bias is presented only in aggregate.**
*Location: Results — Description of studies.*
Justification: final bands and tool counts are given, but no per-study RoB table, summary figure, or explicit pointer to one is provided in the Results, so no individual study's rating can be checked from the manuscript as submitted (the deposit statement in Declarations should name the RoB file as the per-study source).

**R1-m7 — Title block omits ORCID and location.**
*Location: Title block.*
Justification: the title block carries name and email only, while the author's ORCID (0009-0008-4326-4205) and Palmdale, CA location — both in the protocol-locked.md header — appear only once, in Declarations Correspondence; Cochrane title blocks and the author's own manuscript contact rule put ORCID with the corresponding-author line at the top.

**R1-m8 — AUTHOR-ACTION: data/code availability is future-tense at submission.**
*Location: Declarations — Data availability.*
Justification: protocol-locked.md requires analysis code and datasets to be published with the manuscript, but the manuscript states files "will be deposited" and that "no persistent identifier exists for them yet" — deposit before submission and insert the verified identifier; until then PRISMA 2020 item 27 is incompletely met (no placeholder identifier may be invented, per the protocol's own citation-linkage rule).

**R1-m9 — Results-level Q2 counts silently include the six narrative reviews disclosed only in the Discussion.**
*Location: Results — Q2: pathogenesis; Table 3.*
Justification: Discussion — Potential biases discloses six narrative reviews inside the Q2 coding, but the Results denominator (223 studies, 409 assignments) and Table 3 carry no flag identifying them, so a reader of the Results alone cannot tell how much of the speculative grade mass is review prose rather than primary-study discussion.

**R1-m10 — Language handling and design-flag counts cannot be traced through the flow.**
*Location: Results — Study flow; Description of studies.*
Justification: the protocol logs non-English records as awaiting classification and includes conference abstracts and preprints "flagged," but neither the flow text nor Description of studies states how many of the 99 awaiting-classification records are non-English or how many of the 389 includes are conference abstracts/preprints, so the language restriction's impact and the preprint sensitivity denominator (see R1-M2) are unverifiable from the manuscript.

## Nit (4)

**R1-n1 — The medRxiv API check in the locked search plan is not mentioned in the manuscript.**
*Location: Methods — Search methods.*
Justification: protocol-locked.md lists a "medRxiv API date-range check logged separately" within the preprint route and search-log.md §3 records it, but the manuscript describes Europe PMC's preprint index alone — one clause would close the PRISMA-S trail.

**R1-n2 — No statement on peer review of the search strategies.**
*Location: Methods — Search methods / Appendix A.*
Justification: PRISMA-S recommends reporting whether strategies were peer reviewed (e.g. PRESS); the manuscript is silent either way — a single "not peer reviewed" sentence, if that is the fact, satisfies the item.

**R1-n3 — Abstract wording slightly overstates eligibility breadth and omits a limitations statement.**
*Location: Abstract — Selection criteria; Abstract (whole).*
Justification: "human studies of any design with a denominator" reads broader than the locked exclusions detailed two sentences later in the same paragraph, and the structured abstract contains no limitations-of-evidence sentence (limitations appear only in the Discussion), against PRISMA for Abstracts.

**R1-n4 — One locked screening-stage exclusion rule is dropped from the manuscript's eligibility list.**
*Location: Methods — Eligibility criteria (Exclusions).*
Justification: protocol-locked.md excludes at screening "records with neither title nor abstract information on taste or virus"; the manuscript's Exclusions paragraph omits this rule (it is the rule that generated the 13 FLAG-AUTHOR records the manuscript otherwise describes), a small fidelity gap in an otherwise complete list.

---

## Counts

| Severity | Count |
|---|---|
| Blocker | 1 (R1-B1) |
| Major | 7 (R1-M1–M7; M6 is AUTHOR-ACTION) |
| Minor | 10 (R1-m1–m10; m8 is AUTHOR-ACTION) |
| Nit | 4 (R1-n1–n4) |
| **Total** | **22** |

**Gate advice:** hold at this gate. R1-B1, R1-M1, R1-M2, R1-M4 and R1-M5 are fixable from files already held with the review (extraction sheets, excluded-study decisions, abstract-only decisions) without new analysis; R1-M3 requires either the Background work or an explicit declared deviation; R1-M6 and R1-m8 await the author personally.
