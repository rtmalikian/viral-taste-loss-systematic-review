# Search log — PRISMA-S — all searches run 2026-11-20 (America/Los_Angeles)
Retrieval script: scripts/retrieve.py (E-utilities / Europe PMC REST / ClinicalTrials.gov API v2). All counts below are from the script's logged output (data/retrieval_counts_all.json, data/retrieval.log). Full retrieval in every source run — no capped or relevance-ranked samples were used as a searched source.

## 1. PubMed / MEDLINE — RUN IN FULL
Interface: NCBI E-utilities (esearch + esummary + efetch abstracts), 2026-11-20.
String exactly as run:
("Taste Disorders"[Mesh] OR ageusia[tiab] OR dysgeusia[tiab] OR hypogeusia[tiab] OR "taste loss"[tiab] OR "loss of taste"[tiab] OR "gustatory dysfunction"[tiab] OR "taste dysfunction"[tiab] OR "taste disorder"[tiab] OR "taste disorders"[tiab]) AND ("Virus Diseases"[Mesh] OR viral[tiab] OR virus[tiab] OR COVID-19[tiab] OR SARS-CoV-2[tiab] OR influenza[tiab] OR "common cold"[tiab] OR coronavirus[tiab] OR "upper respiratory"[tiab])
Hits: 2720. Retrieved: 2720 (titles, metadata and abstracts via efetch; records with no abstract in PubMed carry an empty abstract and were screened on title).
Note: an earlier same-day scoping count with a shorter string (without "taste disorder(s)" / "upper respiratory") returned 2596; the locked string above supersedes it and is the string of record.

## 2. Europe PMC — RUN IN FULL
Interface: Europe PMC REST API, cursorMark paging, pageSize 1000, resultType core, 2026-11-20.
String exactly as run (title/abstract fields — full-text search deliberately NOT used; an unrestricted test returned 27,975 hits dominated by full-text mentions, a non-specific set; the field restriction is part of the locked strategy and is reported here per PRISMA-S):
(TITLE_ABS:ageusia OR TITLE_ABS:dysgeusia OR TITLE_ABS:hypogeusia OR TITLE_ABS:"taste loss" OR TITLE_ABS:"loss of taste" OR TITLE_ABS:"gustatory dysfunction" OR TITLE_ABS:"taste dysfunction" OR TITLE_ABS:"taste disorder" OR TITLE_ABS:"taste disorders") AND (TITLE_ABS:viral OR TITLE_ABS:virus OR TITLE_ABS:"COVID-19" OR TITLE_ABS:"SARS-CoV-2" OR TITLE_ABS:influenza OR TITLE_ABS:coronavirus OR TITLE_ABS:"common cold" OR TITLE_ABS:"upper respiratory")
Hits: 2816. Retrieved: 2816.

## 3. medRxiv / bioRxiv preprints — RUN via Europe PMC preprint index
Route: the Europe PMC set above includes source SRC:PPR records; subset counted at retrieval: 418 preprint records retrieved within the 2816. The medRxiv API has no keyword search (date/DOI endpoints only; API availability verified 2026-11-20, HTTP 200) — the Europe PMC PPR index is the keyword route and is reported as such. Preprints are flagged in the dataset and excluded in a pre-specified sensitivity analysis.

## 4. ClinicalTrials.gov — RUN IN FULL
Interface: API v2, 2026-11-20. Query exactly as run: query.term = ageusia OR dysgeusia OR hypogeusia OR "taste loss" OR "loss of taste" (all-fields term search), pageSize 100 with pageToken paging, countTotal=true.
API total for the query: 452. Retrieved: 452 study records (title + brief summary + conditions). Trial records were deduplicated against bibliographic records by NCT/title and screened on the same eligibility rules; registry-only records that pass screening proceed to full-record retrieval at the full-text stage.

## 5. WHO ICTRP — NOT RUN (blocked for automated keyword search; logged honestly)
Attempts 2026-11-20 (three): (1) https://trialsearch.who.int/Search.aspx — redirected to NoAccess.aspx; (2) a direct trial-record URL (Trial2.aspx?TrialID=…) loaded, confirming the portal serves individual records but its keyword search is a form-POST interface with no accessible query URL or API; (3) portal home loaded with the same result. Per Standard v2 the source was retried by a second route before being logged. Status: keyword search NOT RUN. Ready string for a manual author run: Condition = ageusia OR dysgeusia OR hypogeusia OR "taste loss"; no other limits. Any manual-run yield will be added as a dated amendment and counted in PRISMA. The manuscript must state ICTRP was not searched automatically and why.

## 6. NOT RUN — no licensed access (never implied as searched)
Embase, Scopus, Web of Science, CINAHL, Cochrane CENTRAL. Ready string (PubMed syntax above translates directly; Embase version): ('taste disorder'/exp OR ageusia:ti,ab OR dysgeusia:ti,ab OR hypogeusia:ti,ab OR 'taste loss':ti,ab OR 'loss of taste':ti,ab OR 'gustatory dysfunction':ti,ab) AND ('virus disease'/exp OR viral:ti,ab OR virus:ti,ab OR 'covid 19':ti,ab OR 'sars-cov-2':ti,ab OR influenza:ti,ab OR coronavirus:ti,ab OR 'common cold':ti,ab).

## Totals at this phase
Records retrieved: PubMed 2720 + Europe PMC 2816 + ClinicalTrials.gov 452 = 5988.
Duplicates removed at deduplication (DOI, then PMID, then NCT, then normalised title; script scripts/dedup_and_screen.py): 2487.
Records screened at title/abstract: 3501.
Citation chasing: not yet due — performed on all full-text inclusions and excluded reviews at the full-text stage and counted in PRISMA then.
