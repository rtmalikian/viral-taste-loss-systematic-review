#!/usr/bin/env python3
"""Q2 pathogenesis synthesis builder — viral taste loss review (Raphael Malikian).

Source (ONLY): extraction/extraction_settled_full.csv
Settled Q2 fields in that file are named:
  pathogenesis_theories            (task brief's "q2_theory_codes")
  pathogenesis_evidence_directness (task brief's "q2_directness")
There is NO separate q2_evidence_type column in the settled file; study
design (column `design`) is used as the evidence-type breakdown and is
labelled as such in every output.

Protocol taxonomy and grades are used exactly as written in
protocol-locked.md (T1-T11) and extraction_form_v1.1.md field 19:
  direct-human / indirect-human / animal / in-vitro / speculative /
  mixed-as-stated.
The brief's grouped labels map as: "direct human taste-system" =
direct-human; "indirect human" = indirect-human; "animal-in-vitro" =
animal + in-vitro; "inference" = speculative.

C8424 is EXCLUDED from all counts (FLAG-AUTHOR), per brief.

Counts are computed twice, independently (regex token extraction vs.
delimiter-token parsing), and cross-checked with asserts before writing.
Directness is a STUDY-level grade in the settled file: a multi-code study
carries one grade, which is propagated to each of its theory codes. This
limitation is printed in the outputs, not hidden.
"""
import csv, re, json, collections, pathlib

ROOT = pathlib.Path.home() / "workspace/publications/viral-taste-loss-review"
SRC = ROOT / "extraction/extraction_settled_full.csv"
OUT_CSV = ROOT / "analysis/synthesis/q2_theory_counts.csv"
OUT_JSON = ROOT / "analysis/synthesis/q2_synthesis_stats.json"
EXCLUDE = {"C8424"}

THEORIES = {
    "T1": "Direct infection/injury of taste bud / taste receptor cells (incl. ACE2/TMPRSS2 or other viral-entry expression in taste epithelium)",
    "T2": "Sustentacular/supporting-cell or lingual epithelium injury without direct receptor-cell infection",
    "T3": "Cranial nerve involvement (chorda tympani VII, IX, X — neuropathy/inflammation)",
    "T4": "Olfactory-mediated misattribution (retronasal flavour loss reported as 'taste')",
    "T5": "Systemic/local inflammation and cytokine effects on taste bud turnover",
    "T6": "Salivary gland infection/dysfunction altering tastant delivery",
    "T7": "Micronutrient/zinc pathway disruption",
    "T8": "Vascular/microthrombotic or hypoxic injury",
    "T9": "Central gustatory pathway involvement",
    "T10": "Autoimmune/post-viral immune-mediated injury",
    "T11": "Other (specify)",
}
GRADES = ["direct-human", "indirect-human", "animal", "in-vitro",
          "speculative", "mixed-as-stated"]

def parse_regex(s):
    return re.findall(r"T\d+", s or "")

def parse_tokens(s):
    """Independent second method: split on ; and , then take leading T-code."""
    out = []
    for tok in re.split(r"[;,]", s or ""):
        m = re.match(r"\s*(T\d+)\b", tok)
        if m:
            out.append(m.group(1))
    return out

def broad_design(d):
    p = (d or "").split("|")[0].strip()
    if p.startswith("cross-sectional"): return "cross-sectional"
    if p.startswith("prospective cohort"): return "prospective cohort"
    if p.startswith("retrospective cohort"): return "retrospective cohort"
    if p.startswith("case-control"): return "case-control"
    if p.startswith("case series"): return "case series >=10"
    if p.startswith("mechanistic human"): return "mechanistic human"
    if p.startswith("animal/in-vitro"): return "animal/in-vitro (Q2 stratum)"
    if p == "RCT": return "RCT"
    if p.startswith("registry"): return "registry record"
    if "narrative review" in p or "bibliographic" in p:
        return "narrative/bibliographic review (flagged, not primary)"
    return "other (specify)"

DESIGN_GROUPS = ["cross-sectional", "prospective cohort", "retrospective cohort",
                 "case-control", "case series >=10", "mechanistic human",
                 "animal/in-vitro (Q2 stratum)", "RCT", "registry record",
                 "narrative/bibliographic review (flagged, not primary)",
                 "other (specify)"]

rows_all = list(csv.DictReader(open(SRC, newline="", encoding="utf-8")))
excluded_rows = [r for r in rows_all if r["record_id"].strip() in EXCLUDE]
rows = [r for r in rows_all if r["record_id"].strip() not in EXCLUDE]

# --- cross-check the two parsers on every row -------------------------------
for r in rows_all:
    a, b = parse_regex(r["pathogenesis_theories"]), parse_tokens(r["pathogenesis_theories"])
    assert a == b, (r["record_id"], a, b)

q2 = [r for r in rows if r["pathogenesis_theories"].strip()]
no_code = [r for r in rows if not r["pathogenesis_theories"].strip()]
assert len(q2) + len(no_code) == len(rows)

per_theory = {}
for code, label in THEORIES.items():
    sub = [r for r in q2 if code in parse_regex(r["pathogenesis_theories"])]
    grades = collections.Counter(r["pathogenesis_evidence_directness"].strip() for r in sub)
    designs = collections.Counter(broad_design(r["design"]) for r in sub)
    per_theory[code] = {
        "label": label, "n": len(sub),
        "grades": {g: grades.get(g, 0) for g in GRADES},
        "designs": {g: designs.get(g, 0) for g in DESIGN_GROUPS},
        "ids": sorted(r["record_id"].strip() for r in sub),
        "n_sars_cov2_containing": sum(1 for r in sub if "SARS-CoV-2" in r["virus"]),
    }
    assert sum(grades.values()) == len(sub) == sum(designs.values())

total_assignments = sum(v["n"] for v in per_theory.values())
assert total_assignments == sum(len(parse_regex(r["pathogenesis_theories"])) for r in q2)

stats = {
    "source_file": "extraction/extraction_settled_full.csv",
    "total_rows_in_file": len(rows_all),
    "excluded": {r["record_id"].strip(): {
        "theories": r["pathogenesis_theories"], "directness": r["pathogenesis_evidence_directness"]}
        for r in excluded_rows},
    "analysis_denominator_excl_excluded": len(rows),
    "unique_q2_studies": len(q2),
    "no_theory_code": len(no_code),
    "no_theory_code_ids": sorted(r["record_id"].strip() for r in no_code),
    "total_code_assignments": total_assignments,
    "codes_per_study_distribution": dict(collections.Counter(
        len(parse_regex(r["pathogenesis_theories"])) for r in q2)),
    "q2_directness_overall": dict(collections.Counter(
        r["pathogenesis_evidence_directness"].strip() for r in q2)),
    "q2_design_broad_overall": dict(collections.Counter(broad_design(r["design"]) for r in q2)),
    "q2_sars_cov2_containing": sum(1 for r in q2 if "SARS-CoV-2" in r["virus"]),
    "q2_non_sars_only": sum(1 for r in q2 if "SARS-CoV-2" not in r["virus"]),
    "overall_non_sars_rows": [(r["record_id"].strip(), r["virus"]) for r in rows
                              if "SARS-CoV-2" not in r["virus"]],
    "per_theory": per_theory,
}
OUT_JSON.write_text(json.dumps(stats, indent=1), encoding="utf-8")

# --- CSV --------------------------------------------------------------------
fieldnames = (["theory_code", "theory_label_protocol_locked", "n_studies_tagged",
               "n_direct_human", "n_indirect_human", "n_animal", "n_in_vitro",
               "n_animal_or_in_vitro", "n_speculative_inference", "n_mixed_as_stated"]
              + [f"n_design__{g}" for g in DESIGN_GROUPS]
              + ["n_virus_sars_cov2_containing", "n_virus_non_sars_only",
                 "record_ids"])
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for code in THEORIES:
        v = per_theory[code]; g = v["grades"]
        row = {"theory_code": code, "theory_label_protocol_locked": v["label"],
               "n_studies_tagged": v["n"],
               "n_direct_human": g["direct-human"], "n_indirect_human": g["indirect-human"],
               "n_animal": g["animal"], "n_in_vitro": g["in-vitro"],
               "n_animal_or_in_vitro": g["animal"] + g["in-vitro"],
               "n_speculative_inference": g["speculative"],
               "n_mixed_as_stated": g["mixed-as-stated"],
               "n_virus_sars_cov2_containing": v["n_sars_cov2_containing"],
               "n_virus_non_sars_only": v["n"] - v["n_sars_cov2_containing"],
               "record_ids": ";".join(v["ids"])}
        for dg in DESIGN_GROUPS:
            row[f"n_design__{dg}"] = v["designs"][dg]
        w.writerow(row)
    w.writerow({"theory_code": "UNIQUE_Q2_STUDIES",
                "theory_label_protocol_locked": "Unique studies with >=1 theory code (each study counted once; denominator excludes C8424)",
                "n_studies_tagged": len(q2),
                "n_direct_human": stats["q2_directness_overall"].get("direct-human", 0),
                "n_indirect_human": stats["q2_directness_overall"].get("indirect-human", 0),
                "n_animal": stats["q2_directness_overall"].get("animal", 0),
                "n_in_vitro": stats["q2_directness_overall"].get("in-vitro", 0),
                "n_animal_or_in_vitro": stats["q2_directness_overall"].get("animal", 0) + stats["q2_directness_overall"].get("in-vitro", 0),
                "n_speculative_inference": stats["q2_directness_overall"].get("speculative", 0),
                "n_mixed_as_stated": stats["q2_directness_overall"].get("mixed-as-stated", 0),
                "n_virus_sars_cov2_containing": stats["q2_sars_cov2_containing"],
                "n_virus_non_sars_only": stats["q2_non_sars_only"],
                "record_ids": ";".join(sorted(r["record_id"].strip() for r in q2))})
    w.writerow({"theory_code": "NO_THEORY_CODE",
                "theory_label_protocol_locked": "Studies in settled file (excl. C8424) with blank pathogenesis_theories — contribute nothing to Q2",
                "n_studies_tagged": len(no_code),
                "record_ids": ";".join(stats["no_theory_code_ids"])})
    w.writerow({"theory_code": "TOTAL_CODE_ASSIGNMENTS",
                "theory_label_protocol_locked": "Sum over T1-T11 of n_studies_tagged (a multi-code study counts once under each of its codes)",
                "n_studies_tagged": total_assignments})

print("CROSS-CHECK PASS")
print(f"file rows={len(rows_all)}  excl C8424 denominator={len(rows)}  "
      f"unique Q2={len(q2)}  no code={len(no_code)}  assignments={total_assignments}")
for c in THEORIES:
    print(c, per_theory[c]["n"], per_theory[c]["grades"])
print("wrote", OUT_CSV)
print("wrote", OUT_JSON)
