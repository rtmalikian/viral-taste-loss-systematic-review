# Phase 6 annotation — q2_synthesis_stats.json (2026-11-21)

`q2_synthesis_stats.json` and `q2_theory_counts.csv` in this directory are the
Phase 4 synthesis outputs. Their builder excluded only C8424, so they show the
pre-restatement counts (223 coded studies, 409 assignments, speculative 164).

At the Phase 6 eligibility-consistency step, all 26 no-primary-data records
were formally excluded. The restated Q2 counts — the ones printed in the
manuscript (Results Q2 and Table 3) — are: 214 coded studies, 383 assignments,
speculative 157 (73.4%), indirect-human 22, direct-human 15, mixed-as-stated
13, animal 5, in-vitro 2; per-theory tagged counts T1 117, T2 17, T3 35,
T4 61, T5 56, T6 24, T7 7, T8 10, T9 28, T10 2, T11 26. Method: study-level
directness propagated to each of a study's codes over
extraction/extraction_settled_full.csv minus the 26 records listed in
fulltext/prisma_counts_phase4.json; the method reproduces the Phase 4 files
exactly when only C8424 is excluded. The Phase 4 files are retained unchanged
as the audit record.
