# Q2 Pathogenesis Synthesis — Loss of Taste in Viral Infections

**Role:** Q2 Pathogenesis Synthesist · **Review:** Cochrane-level systematic review of loss of taste in viral infections (Raphael Malikian)
**Sole data source:** `extraction/extraction_settled_full.csv` (389 studies). No external literature is used anywhere in this document; every count and every study characterisation below traces to the companion file `analysis/synthesis/q2_theory_counts.csv` and to the settled fields named in §1. Record IDs are the only citations used.
**Companion counts file:** `analysis/synthesis/q2_theory_counts.csv` (built by `analysis/synthesis/build_q2_synthesis.py`; counts computed twice by independent parsers and cross-checked — see §8).

---

## 1. Methods and field mapping (read first — three naming facts)

1. **The settled CSV does not contain columns literally named `q2_theory_codes`, `q2_evidence_type` or `q2_directness`.** The settled Q2 fields are:
   - `pathogenesis_theories` — the theory codes (the brief's "q2_theory_codes");
   - `pathogenesis_evidence_directness` — the directness grade (the brief's "q2_directness");
   - `pathogenesis_finding` — the one-sentence finding for the coded taste mechanism.
   There is **no separate evidence-type column**. The "by evidence type" breakdown in the CSV therefore uses the settled `design` field, grouped into the extraction form's closed design vocabulary (extraction form v1.1, R1). That substitution is labelled in the CSV column names (`n_design__…`).
2. **Taxonomy and grades are used exactly as written in `protocol-locked.md` and extraction form v1.1.** Theories T1–T11 are reproduced verbatim in the CSV. The settled directness grades are `direct-human / indirect-human / animal / in-vitro / speculative / mixed-as-stated`. The brief's grouped labels map onto them as: *direct human taste-system* = `direct-human`; *indirect human* = `indirect-human`; *animal-in-vitro* = `animal` + `in-vitro`; *inference* = `speculative`. The CSV carries both the granular grades and the grouped animal/in-vitro column.
3. **Directness is a study-level grade, not a theory-level grade.** A study carries exactly one `pathogenesis_evidence_directness` value, however many theory codes it has. In the per-theory breakdowns that grade is propagated to each of the study's codes, because the settled data contain nothing finer. 108 of the 223 Q2 studies (48.4%) carry ≥2 codes, so this limitation is material: a study graded `direct-human` for one of its mechanisms raises the "direct" count of every theory it is tagged with (a concrete artefact is dissected under T8). The 14 `mixed-as-stated` studies cannot be allocated to a single grade at all and are reported as their own column, never split.

**Exclusion applied:** **C8424 is excluded from every count in this synthesis (FLAG-AUTHOR), as instructed.** Its settled Q2 fields are in fact blank (no theory code, no directness grade, no finding), so the exclusion changes no Q2 count; the analysis denominator is 388 studies (389 − C8424). This is stated so the exclusion is auditable, not assumed.

**Coding rule that shapes everything below (extraction form v1.1, R5):** a theory was coded only where the paper's mechanism was taste-specific or explicitly extended to taste by the paper itself. Smell-only and general viral mechanisms were *not* coded. T4 is the exception that proves the rule: it is coded when a paper proposes that reported "taste" loss is retronasal flavour loss — that is itself a taste claim.

---

## 2. Headline structure of the Q2 evidence base

| Quantity | n | Denominator / note |
|---|---|---|
| Studies in settled file | 389 | — |
| Analysis denominator (C8424 excluded) | 388 | — |
| **Unique studies contributing to Q2 (≥1 theory code)** | **223** | 57.5% of 388 |
| Studies with **no theory code** | **165** | 42.5% of 388; full ID list in the `NO_THEORY_CODE` row of the CSV |
| Total theory-code assignments | 409 | A multi-code study counts once under each of its codes |
| Studies with exactly 1 code / 2 / 3 / 4 / 5 / 6 codes | 115 / 59 / 31 / 11 / 3 / 4 | Sums to 223 studies and 409 assignments |

**Directness of the 223 unique Q2 studies (study-level grade):**

| Grade (protocol wording) | n | % of 223 |
|---|---|---|
| speculative (= inference) | 164 | 73.5% |
| indirect-human | 23 | 10.3% |
| direct-human | 15 | 6.7% |
| mixed-as-stated | 14 | 6.3% |
| animal | 5 | 2.2% |
| in-vitro | 2 | 0.9% |

Three structural facts follow immediately:

- **The Q2 literature is predominantly a literature of proposals, not of tests.** Almost three-quarters of Q2 studies (164/223) are graded speculative: the mechanism appears in the paper's discussion as a proposed explanation, with no measurement of that mechanism in the study itself. Only 38/223 studies (17.0%) carry a human grade of any kind (15 direct-human + 23 indirect-human), and only 7/223 (3.1%) are graded animal or in-vitro.
- **Designs mirror that.** Of the 223 Q2 studies: cross-sectional 78, prospective cohort 55, retrospective cohort 22, case-control 21, other-specified 19, case series ≥10 9, narrative/bibliographic review (flagged "do not extract as primary") 6, animal/in-vitro stratum 5, mechanistic human 4, RCT 2, registry record 2. The designs that dominate (surveys and cohorts assembled for Q1 frequency questions) are designs in which a pathogenesis statement is almost always a discussion remark — which is exactly what the speculative grade records.
- **Taste itself was usually not measured objectively.** Across the 223 Q2 studies, taste measurement was: self-report symptom yes/no or survey 86, patient-reported scale 50, other-as-stated 39, **validated gustatory test only 31 (13.9%)**, composite smell–taste 17. Even among the 15 direct-human studies, only 3 used a validated gustatory test (R00044, R01523, R02414); 5 relied on self-report yes/no. "Direct human" in this dataset therefore means *the mechanism was measured in humans in relation to the taste outcome the study recorded* — it does not guarantee psychophysical taste testing.

### 2.1 Virus composition — the single largest caveat in Q2

**Every one of the 223 Q2 studies (100%) has SARS-CoV-2 in its settled `virus` field.** There is no Q2 evidence base for any other virus:

- 211/223 are coded plainly `SARS-CoV-2`; the remaining 12 carry SARS-CoV-2 variant/qualifier strings (Omicron and other variants, presumed/suspected COVID-19).
- Only 4 Q2 studies mention any second virus/group at all, and in each case SARS-CoV-2 remains the index virus: R00710 (in-vitro work with SARS-CoV-2 **and HCoV-OC43** — the only included record in which a non-SARS-CoV-2 virus was actually experimented on), R00079, R00334 and R00824 (mixed or comparison groups including other/unspecified upper-respiratory infections).
- In the full settled file, only 4 studies have a non-SARS-CoV-2 virus field at all (R00049, R00077, R00210, R00939 — all "unspecified possible viral"), and **none of the four carries a theory code**. Influenza contributes zero Q2 studies: no included study is coded influenza in the `virus` field.

**Consequence for the review:** every pathogenesis statement in this synthesis is, on the included evidence, a statement about SARS-CoV-2. Nothing in Q2 can support a mechanism claim for influenza or any other named virus, and any manuscript wording that generalises a mechanism beyond SARS-CoV-2 goes beyond the included evidence.

### 2.2 Human vs animal/in-vitro composition

By directness grade: human-graded (direct + indirect) 38/223 (17.0%); animal/in-vitro-graded 7/223 (3.1%); speculative 164 (73.5%); mixed-as-stated 14 (6.3%). By design, only 5/223 studies sit in the protocol's animal/in-vitro Q2 stratum. The two tallies differ by 2 because two human prospective-cohort papers (R01479, C8932) are graded `animal` — their taste-mechanism content is mouse ACE2-expression data cited in the paper, not data from their own cohorts (see §8, problem 4). The genuinely experimental model-system core of Q2 is therefore very small: R00710, R01260 (in-vitro) and R01540, R02218, R02709 plus the cited-mouse-data papers R01479, C8932 (animal-graded).

---

## 3. Theory-by-theory synthesis

Counts below are (studies tagged; direct-human / indirect-human / animal / in-vitro / speculative / mixed-as-stated). Full ID lists per theory are in the CSV.

### T1 — Direct infection/injury of taste bud / taste receptor cells — 125 studies (3 / 14 / 4 / 1 / 92 / 11)

The most-tagged theory by a wide margin (125/223 Q2 studies; 56.1%), and the clearest case where tag frequency and evidential weight diverge. 92 of its 125 studies (73.6%) are speculative: cross-sectional surveys (44 of the 125) and cohorts whose discussions invoke ACE2 expression on the tongue as the explanation for the taste loss they counted. The 14 indirect-human studies (R00373, R00391, R01224, R01361, R02128, R02166, R02181, R02210, R02248, R02333, R02455, R02856, R02911, R02932) are of one type: human studies that *cite or restate* ACE2 expression in oral/tongue epithelium as plausibility, without measuring taste tissue — indirect support by citation, not by experiment.

The direct human taste-system evidence for T1 is **three studies, and it is not confirmatory in any simple sense**:

- **R00058** (cross-sectional) measured ACE2, TMPRSS2, furin and NRP1 expression in nasal/pharyngeal samples against dysgeusia and found **no statistically significant association** in adjusted models — direct human evidence *against* a simple entry-factor-expression account, at least at the sampled site.
- **R00840** (cross-sectional genetic-association study) found lower ACE2 gene expression in nasopharyngeal tissue associated with ageusia (OR 1.35 per unit increase in ACE2 delta-CT), with no association for ACE1 or TMPRSS2 — a human association, but in nasopharyngeal, not taste, tissue, and with taste by self-report.
- **R01523** (case-control, validated quantitative taste kit) found altered basic-taste thresholds in COVID-19 patients with taste disorder; it is co-coded T1;T3;T6, so its direct-human grade serves three theories at once (see §1, point 3).

The most taste-bud-specific experimental support for T1 sits **outside** the human stratum: R00710 (in-vitro; SARS-CoV-2 infected cultured human fungiform taste papilla cells, with ACE2 expressed) and the animal-graded expression studies R01540 and R02709 (ACE2/TMPRSS2 co-expression in mouse taste papillae/taste cells), with R01479 and C8932 citing mouse taste-bud ACE2 expression from within human cohort papers. In short: T1 is the field's default hypothesis, carried overwhelmingly by repetition in discussion sections; its direct human evidence is 3 studies (one null), and its most specific mechanistic evidence is in-vitro/animal.

### T2 — Sustentacular/supporting-cell or lingual epithelium injury without direct receptor-cell infection — 18 studies (0 / 1 / 1 / 0 / 15 / 1)

**No direct human evidence at all.** Fifteen of 18 studies are speculative; the remainder are one indirect-human study (R02077 — oral mucosal epithelial inflammation/damage proposed from a prospective cohort), one animal study (R02218 — mouse tongue bulk RNA-seq: ACE2 enriched in basal epithelial cells of *non-gustatory* filiform papillae and **not** in taste papillae or taste buds, a result that fits a supporting/epithelium account better than a receptor-cell account), and one mixed-as-stated study (R00047, a genetic-association study co-coded for other theories).

The character of the support is explicitly analogical. The settled findings show the reasoning being imported from olfaction: R00839 proposes support-cell infection by reference to the olfactory epithelium; R01745 proposes taste receptors are affected "similarly to olfactory support cells"; R02464 argues for non-neuronal supporting-cell targets in "the chemosensitive epithelia" generally; R00657 and R01311 rest on expression/localisation claims about tongue epithelium rather than on any measurement in taste patients. T2 is therefore a theory sustained by analogy with the olfactory sustentacular model plus one mouse expression dataset — plausible within the dataset's own terms, but untested in human taste tissue in any included study.

### T3 — Cranial nerve involvement (VII, IX, X) — 39 studies (1 / 0 / 1 / 2 / 33 / 2)

Thirty-three of 39 studies (84.6%) are speculative — the highest speculative share of any well-populated theory. The single direct-human count is R01523, the multi-code threshold study shared with T1 and T6; it measured taste thresholds, not nerves, so **no included study provides direct human evidence about cranial nerve function in taste loss**. There are no indirect-human studies for T3 at all.

What non-speculative evidence exists is model-system work: R01260 (in-vitro; SARS-CoV-2 directly infected human embryonic stem-cell-derived peripheral sensory neurons via ACE2, absent in ACE2-knockout neurons) and R00710 (co-coded; in-vitro), plus animal-graded R02218. These establish that sensory neurons *can* be infected in vitro; no included human study measures chorda tympani, glossopharyngeal or vagal function in patients with taste loss. T3's presence in 39 papers is a discussion-section presence.

### T4 — Olfactory-mediated misattribution (retronasal flavour loss reported as 'taste') — 64 studies (3 / 4 / 0 / 0 / 51 / 6)

The second most-tagged theory (64) and — despite 51 speculative tags — **the theory with the most coherent direct human taste-specific evidence in the review**, because its direct studies were designed to test exactly this claim: compare what patients report with what objective taste testing shows.

- **R02414** (case series ≥10, Taste Strips): taste-strip testing was normal in all tested patients complaining of taste loss; authors conclude patients confused gustatory with retronasal olfactory function.
- **C11888** (prospective cohort): Taste Strips in 30 participants were normal in 86.7–96.7% per taste quality; reported taste loss attributed to flavour-perception loss from smell dysfunction.
- **C4367** (prospective cohort, survey): 60% of respondents could still differentiate sweet/salty/sour/bitter at first survey (88.9% at follow-up), pointing to smell rather than hypogeusia.

The mixed-as-stated stratum points the same way and quantifies the discordance: R00232 (only 23.5% of smell/taste-loss complainers objectively hypogeusic on the WETT) and C10044 (89% self-reported taste loss vs 7% objectively dysgeusic on taste strips). The 4 indirect-human studies (R00059, R01953, R02166, R02455) include R01953's formal separation of flavour-GD from taste-GD (flavour-GD more frequent and more sensitive for COVID-19) and R00059 (64% reported taste dysfunction vs 16% with taste-identification deficits).

Two cautions keep this from being over-read. First, these studies show that *much reported* taste loss is misattributed flavour loss; they do not show that *all* of it is — the same objective-testing studies retain a minority with genuine gustatory deficits (e.g. 23.5% in R00232). Second, T4 is a claim about measurement and attribution, not a tissue mechanism; it competes with T1/T2/T5 only at the level of "what the symptom report means," and the dataset's own R5 coding rule treats it as such.

### T5 — Systemic/local inflammation and cytokine effects on taste bud turnover — 59 studies (4 / 7 / 1 / 1 / 41 / 5)

The third most-tagged theory (59) and, with T11, one of only two theories reaching 4 direct-human studies. The direct-human four are heterogeneous in what they measured:

- **R00044** (mechanistic human): single-cell transcriptomes of salivary epithelial cells from individuals with bitter taste dysfunction showed downregulation of genes for cytoskeletal dynamics and taste cell–nerve synapse assembly (co-coded T11 for that synapse/turnover specification).
- **R00084** (prospective cohort): procalcitonin and CRP were significantly associated with development of olfactory **and** gustatory dysfunction, and inflammatory ratios predicted recovery — a systemic-inflammation association with a composite chemosensory outcome.
- **R01294** (mechanistic human immunological study): SARS-CoV-2-positive olfactory/taste-dysfunction subjects had increased frequencies of functional virus-specific CD4+/CD8+ T cells with enhanced IFNγ production versus comparators.
- **R00066** (case-control): lower serum tryptophan and higher kynurenine–tryptophan ratio and quinolinic acid in patients with dysosmia/dysgeusia (co-coded T11 for the kynurenine specification).

The 7 indirect-human studies are biomarker-association studies of the same family (R01864 — IL-6/LDH correlated with taste-loss scores; R01878 — IL-10 associated with recovery, authors concluding an inflammatory-mediated condition; R01361 — salivary TLR-4/PGRP-4/soluble ACE2 correlated with viral load; R00373, R01970, R02077, R02704 — the last of these a *negative* result: persistent dysfunction was **not** associated with subjective nasal-inflammation measures). The remaining 41 studies are speculative invocations of "cytokine storm"/inflammation in discussion sections, and one animal and one in-vitro study (R02218, R00710, both co-coded) touch T5 only as one code among several.

Assessment: T5 has real human biomarker evidence, but it is associational, largely measured against composite smell–taste outcomes or self-reported taste, and no included study measures taste bud turnover itself in humans. The "turnover" half of the theory's protocol label is untested in the included human evidence; the "inflammation is associated with the symptom" half is the part with data.

### T6 — Salivary gland infection/dysfunction altering tastant delivery — 26 studies (1 / 3 / 0 / 0 / 19 / 3)

Nineteen of 26 studies are speculative. The single direct-human count is again the shared multi-code study R01523 (taste thresholds; no salivary measurement), so **no included study graded direct-human actually measured salivary gland infection, saliva flow or saliva composition against taste function**. The closest human evidence is indirect: R01361 (mechanistic human; salivary innate-immune markers and soluble ACE2 elevated in COVID-19 saliva and correlated with viral load — saliva measured, but the taste link is the study's framing, graded indirect-human), with R00373 and R00391 restating ACE2 expression in salivary gland cells as plausibility. R00592 (mixed-as-stated) is a bibliographic/narrative review restating ACE2/Furin/TMPRSS2 presence in salivary gland ductal/acinar/myoepithelial cells from the reviewed literature — secondary citation, not primary data (see §8, problem 5). T6 is thus supported by expression plausibility and one salivary-biomarker study, not by any direct test of the tastant-delivery mechanism.

### T7 — Micronutrient/zinc pathway disruption — 8 studies (0 / 0 / 0 / 0 / 5 / 3)

**No direct, indirect, animal or in-vitro evidence in any included study.** All 8 studies are speculative (5) or mixed-as-stated (3): R00592 (narrative review), R00841 (case-control whose measured findings concern other codes), R01955 (an RCT whose paper *proposes* acute zinc deficiency reducing taste bud alkaline phosphatase activity / altering salivary zinc proteins — a proposal recorded in the finding, not a zinc measurement reported for the taste outcome), and discussion-level mentions in R00934, R01068, R01277, R01550 and C11416, typically of the form "zinc deficiency is well known to cause taste dysfunction" (R01550). T7 enters this literature by importation from general taste physiology, not from any measurement in viral taste loss. It is one of the theories resting **only** on indirect/inference-type support — in fact only on inference and unallocatable mixed grades.

### T8 — Vascular/microthrombotic or hypoxic injury — 10 studies (1 / 1 / 0 / 0 / 8 / 0)

Eight of 10 studies are speculative. The apparent direct-human count of 1 is an **artefact of study-level grading**: R00185 is coded T8;T9 and graded direct-human, but its settled finding is a diffusion-MRI study of white matter in taste-related *brain* regions — evidence addressed to T9 (central pathways), containing no vascular, thrombotic or hypoxia measurement for T8. On the finding text, **T8 has no direct human evidence of its own**. Its one indirect-human study is R01957 (case-control): mean D-dimer modestly higher in the dysgeusia group than the non-dysgeusia group (0.54 ± 0.32 vs 0.49 ± 0.51 mg/L FEU, p = 0.008) — a single small biomarker difference, interpreted by its authors toward a vascular account. The remaining mentions are hypothesis lists (R00079, R00356, R00539, R00627, R00884, R01000, R01551, C11416 — hypoxia/microcirculation named among several candidate mechanisms). T8 effectively rests on inference plus one indirect biomarker association.

### T9 — Central gustatory pathway involvement — 30 studies (2 / 1 / 0 / 0 / 24 / 3)

Twenty-four of 30 studies are speculative, typically inferring central involvement from the co-occurrence of taste loss with smell loss or other neurological symptoms (the archetype in the settled file is R00012, coded T9/speculative on the basis that combined smell–taste alterations "likely reflect involvement of the central nervous system and persistent dysfunction of the olfactory pathway" — note that even this founding example reasons *from olfaction*).

The direct human evidence is two studies, of very different kinds:

- **R00185** (prospective cohort, 4-year DW-MRI): ADC values in white matter of taste-related brain regions (frontal operculum, insula, parietal operculum) were significantly elevated, peaking at infection and normalising over follow-up — the only included neuroimaging study tied to taste regions, though taste itself was an enrolment symptom, not a tested outcome.
- **R01073** (cross-sectional): patients with olfactory + gustatory dysfunction showed selectively decreased vividness of taste (and odour) *mental imagery* and lower self-rated taste/flavour — a patient-reported, centrally interpreted finding.

One indirect-human study (R00059, shared with T4) and 3 mixed-as-stated studies (including R00841 — gustatory scores correlating with anterior cingulate volumes, a T9-relevant correlation inside a multi-code study — and R00129, R01413) complete the non-speculative tail. Assessment: T9 has one genuinely direct imaging study (R00185); the bulk of its 30 tags are inference from symptom co-occurrence, frequently by analogy from the olfactory pathway rather than from gustatory data.

### T10 — Autoimmune/post-viral immune-mediated injury — 2 studies (0 / 0 / 0 / 0 / 2 / 0)

**The emptiest theory in the taxonomy.** Two studies, both speculative: R02135 (co-coded T3;T10 — autoimmune injury appears in a list of hypotheses for sensory manifestations) and R03352 (registry record, co-coded T1;T10 — whose finding in fact argues for peripheral neuroepithelial damage). No included study measures an autoantibody, an autoimmune marker, or any immune-mediated injury mechanism in relation to taste. On the included evidence T10 has **essentially no evidence base** — it survives in the literature as a listed hypothesis only. (R01294's and R00830's adaptive-immunity findings, which a reader might expect here, are coded by the extractors under T5/T11 respectively, not T10; this synthesis follows the settled coding.)

### T11 — Other (specify) — 28 studies (5 / 2 / 0 / 0 / 16 / 5)

T11 has the largest direct-human count of any theory (5) — and this must not be read as the best-supported mechanism, because **T11 is not one mechanism**. Its 28 tags collect unrelated specifications, and its 5 direct-human studies test five different things:

- R00044 — salivary epithelial transcriptomic downregulation of taste cell–nerve synapse assembly genes (specification: impaired epithelial turnover / synapse assembly);
- R00066 — kynurenine-pathway activation with quinolinic acid accumulation (serum metabolite case-control);
- R00649 — salivary anti-Spike-NTD IgA titres associated with taste disorders persisting >1 year (prospective cohort);
- R00830 — adaptive immune response (antibody levels — no correlation found; CD8+ T-cell responder trend) in relation to chemosensory dysfunction;
- C4631 — mechanistic human electrophysiology: prolonged masseter inhibitory reflex latencies indicating subclinical peripheral **trigeminal** (CN V) impairment.

Other recurring specifications across the 28: host genetic susceptibility/variation in taste-signalling genes (R00019, R00047 — both mixed-as-stated), sialic-acid receptor binding on taste buds (R01277, R01378, R01628 — all speculative), autonomic dysregulation/dysautonomia (R00625, R02954), nervus terminalis ACE2 entry (R00259), acid sphingomyelinase elevation (R00129), serotonin/tryptophan deficiency via intestinal ACE2 (R01599), oral/lingual microbiome dysbiosis (C0174), hormonal modulation (R02394). **Nine of the 28 T11 rows carry no specification at all in the settled field** (R00634, R00841, R00951, R01045, R01192, R01710, R01920, R01986, R02248) — for those, the "other" mechanism cannot even be named from the extraction. T11 is a residual category doing real work in this literature (genetics, trigeminal, autonomic and sialic-acid proposals all live here), and it should be reported as a set of separate mini-theories, never as a single supported mechanism.

---

## 4. Where the direct human taste-specific evidence is concentrated

All 15 direct-human studies, and what each actually contributes:

| ID | Codes served | What was actually done (per settled finding) |
|---|---|---|
| R00044 | T5; T11 | Salivary epithelial single-cell transcriptomics in bitter taste dysfunction; synapse-assembly gene downregulation |
| R00058 | T1 | Nasal/pharyngeal entry-factor expression vs dysgeusia — **null** |
| R00066 | T5; T11 | Serum tryptophan/kynurenine/quinolinic acid, dysosmia/dysgeusia cases vs controls |
| R00084 | T5 | CRP/procalcitonin association with olfactory+gustatory dysfunction; recovery prediction |
| R00185 | T8; T9 | DW-MRI of taste-related brain regions over 4 years (finding addresses T9, not T8) |
| R00649 | T11 | Salivary anti-Spike-NTD IgA vs taste disorders persisting >1 year |
| R00830 | T11 | Antibody levels (no correlation) and CD8+ responder trend vs chemosensory dysfunction |
| R00840 | T1 | Nasopharyngeal ACE2 expression associated with ageusia; ACE1/TMPRSS2 null |
| R01073 | T9 | Taste mental-imagery vividness and self-ratings (patient-reported) |
| R01294 | T5 | Virus-specific T-cell frequencies/IFNγ in olfactory/taste dysfunction |
| R01523 | T1; T3; T6 | Validated quantitative taste thresholds (sweet/sour/bitter up, salty down) |
| R02414 | T4 | Taste Strips normal in all tested complainers |
| C11888 | T4 | Taste Strips normal in 86.7–96.7% per quality (n=30 tested) |
| C4367 | T4 | Basic-taste differentiation preserved in 60% → 88.9% |
| C4631 | T11 | Trigeminal (masseter inhibitory reflex) electrophysiology |

Concentration, stated plainly: direct human evidence exists in meaningful form for **T4** (three purpose-built objective-testing studies: R02414, C11888, C4367), for **T5** (four biomarker/transcriptomic studies: R00044, R00066, R00084, R01294 — associational, often against composite outcomes), and for **T9** in a single imaging study (R00185). For **T1** the direct human tally is 3 studies including one null result (R00058) and one nasopharyngeal-tissue association (R00840). Everything else in the direct-human column is single-study, multi-code (R01523 serving T1/T3/T6) or residual-category (T11's five unrelated studies).

**Ranking by direct-human count (the brief's headline question):** T11 = 5, T5 = 4, T1 = 3 and T4 = 3 (tied). With the necessary qualifiers: T11's five do not accumulate (five different mechanisms); of the tied pair, T4's three are single-theory, purpose-designed tests of that theory, whereas T1's three include a null. The three best-supported theories by direct human evidence are therefore reported as **T5, T4 and T1** on coherence-adjusted grounds, with the raw-count leader **T11 (5)** named alongside so the count ranking is not hidden.

## 5. Where support is only by analogy or inference from olfaction

The settled findings make the borrowing visible in the papers' own wording:

- **T2** is the clearest case: its support is the olfactory sustentacular-cell model transferred to the tongue (R00839 — support-cell infection proposed from olfactory epithelium expression; R01745 — "similarly to olfactory support cells"; R02464 — non-neuronal targets in chemosensitive epithelia generally; R00951 — sustentacular-cell destruction proposed jointly for taste and smell).
- **T9** tags frequently reason from smell: R00012 infers central involvement from combined smell–taste alteration via "persistent dysfunction of the olfactory pathway"; R01970 (T5) concludes from olfactory neuronal-pathway damage; R02181 (T1) invokes transneuronal spread from the olfactory route.
- **T1's** indirect-human block (14 studies) largely restates oral/nasal ACE2 expression — much of the underlying expression literature is nasal/olfactory — as taste plausibility.
- The extraction rule R5 already excluded smell-only mechanisms that papers did *not* extend to taste; what remains coded is the subset papers explicitly extended — i.e. the analogy is the papers', and the speculative grade is how the dataset marks it. 164 speculative studies is the quantitative footprint of this pattern.

## 6. Theories with essentially no direct evidence

- **T10 (autoimmune/post-viral immune-mediated): no evidence base** — 2 studies, both speculative hypothesis-list mentions (R02135, R03352).
- **T7 (zinc/micronutrient): no direct, indirect, animal or in-vitro evidence** — 5 speculative + 3 mixed-as-stated, all proposals or restatements (R00592, R00841, R00934, R01068, R01277, R01550, R01955, C11416).
- **T2: no direct human evidence** — 15 speculative, 1 indirect-human (R02077), 1 animal (R02218), 1 mixed (R00047).
- **T8: no direct evidence attributable to T8 itself** — its sole direct-human tag (R00185) is a brain-MRI finding addressed to its co-code T9; otherwise 8 speculative + 1 indirect D-dimer association (R01957).
- **T3: no direct human nerve evidence** — its sole direct-human tag is the shared taste-threshold study R01523; its specific support is in-vitro neuronal infection (R01260, R00710).
- **T6: no direct salivary test** — its sole direct-human tag is likewise R01523 (no salivary measurement); specific support stops at indirect salivary biomarkers (R01361).

**Theories resting only on indirect/inference-type evidence (no direct-human grade attributable to the theory's own mechanism): T10, T7, T2, T8, T3, T6** — six of the eleven. Only T1, T4, T5, T9 and the residual T11 have any direct-human-graded study whose finding addresses that theory.

## 7. Virus and system summary (for the manuscript)

- **SARS-CoV-2 vs other viruses:** 223/223 Q2 studies are SARS-CoV-2 (100%); 0 Q2 studies examine influenza or any other virus alone; the only non-SARS-CoV-2 experimentation in Q2 is HCoV-OC43 alongside SARS-CoV-2 in one in-vitro study (R00710). The 4 non-SARS-CoV-2 studies in the settled file (R00049, R00077, R00210, R00939, unspecified possible viral) contribute no pathogenesis content.
- **Human vs animal/in-vitro:** human-graded 38/223 (17.0%; 15 direct + 23 indirect); animal/in-vitro-graded 7/223 (3.1%); animal/in-vitro by design 5/223 (2.2%); speculative (human studies proposing, not measuring) 164/223 (73.5%); mixed-as-stated 14/223 (6.3%). The Q2 base is thus overwhelmingly human *clinical* literature carrying unmeasured mechanism proposals, with a very small experimental core (R00710, R01260, R01540, R02218, R02709, and cited-mouse-data papers R01479, C8932).

## 8. Data problems found in the settled Q2 fields

1. **Field-name mismatch with the brief.** The settled file has no `q2_theory_codes` / `q2_evidence_type` / `q2_directness` columns; the actual fields are `pathogenesis_theories`, `pathogenesis_evidence_directness`, `pathogenesis_finding`, and there is **no evidence-type field at all** — `design` was used for that breakdown (§1). Any downstream code written against the brief's column names will fail on this file.
2. **Directness is study-level, not theory-level** (§1, point 3). 108/223 Q2 studies are multi-code but carry one grade; per-theory directness counts inherit the study's grade for every code. Demonstrated artefact: T8's only "direct-human" study (R00185) contains no vascular measurement — its finding is T9 brain imaging. Per-theory grade breakdowns must be read with the findings, not as theory-specific grades.
3. **`mixed-as-stated` cannot be decomposed.** 14 studies (contributing 39 code assignments across theories) carry a single mixed grade with no per-mechanism split recorded. They are reported as their own column; any synthesis that silently allocates them will overstate certainty.
4. **Design/directness mismatch in 2 studies.** R01479 and C8932 are graded `animal` but their settled `design` is a human prospective cohort — the animal content is mouse data cited in the paper. Human-vs-model tallies differ by exactly these 2 depending on whether grade or design is used; both tallies are reported in §7.
5. **Six Q2-coded records are narrative/bibliographic reviews the extraction form flags "do not extract as primary"** (R00592, R01870, R02248, R02295, R02346, R02354), contributing 16 code assignments (notably R00592 is one of only 3 mixed-grade carriers for T6 and one of only 3 for T7, and R02248 is one of only 2 indirect-human T11 records). They are retained in the counts for completeness and flagged in the CSV design column; a primary-evidence sensitivity count should exclude them. The protocol excludes narrative reviews from synthesis, so the manuscript must decide explicitly whether these 6 stay in Q2 — the settled coding currently includes them.
6. **T11 is under-specified in the settled field.** 9/28 T11 records have no parenthetical specification, so their "other" mechanism is unrecoverable from the extraction alone. Two T11 strings contain nested parentheses (R00259 — nervus terminalis; C4631 — trigeminal nerve) that break naive parenthesis parsing.
7. **Inconsistent separators in `pathogenesis_theories`** (`;` vs `,` vs spaced variants, e.g. "T1 ; T3"). Counts here were produced by two independent parsers (regex token extraction and delimiter-token parsing) that agreed on all 389 rows; a single naive split on ";" would undercount.
8. **No other integrity problems found in the Q2 block:** every study with a theory code has a directness grade and a finding (223/223), no study has a grade or finding without codes, no code outside T1–T11 appears, no study repeats a code, and C8424's Q2 fields are blank (its exclusion is count-neutral but applied throughout, as instructed).

## 9. Verification

Recomputed independently in `build_q2_synthesis.py`: row total 389; denominator after C8424 exclusion 388; unique Q2 studies 223; no-code studies 165 (223 + 165 = 388 ✓); code assignments 409 = sum of the eleven per-theory counts (125 + 18 + 39 + 64 + 59 + 26 + 8 + 10 + 30 + 2 + 28 = 409 ✓); per-theory grade breakdowns and design breakdowns each sum to that theory's total ✓; two independent theory-code parsers agree on every row ✓. All counts in this document are taken from `q2_theory_counts.csv` / `q2_synthesis_stats.json` generated by that script.
