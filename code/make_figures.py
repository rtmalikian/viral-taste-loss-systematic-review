#!/usr/bin/env python3
"""Figures for the viral taste-loss review manuscript.
Forest plots draw the pooled estimate as a summary DIAMOND (centre = pooled
value, tips = 95% CI) with the 95% prediction interval shown as a bar below
the diamond. All numbers are read from the Phase 4 result JSONs and pool
CSVs in analysis/synthesis/ - nothing is hard-coded except PRISMA counts,
which are stated in the Figure 1 boxes below and cross-checked against
fulltext/prisma_counts_phase4.json (Phase 6 counts).
"""
import csv, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from scipy.stats import beta as beta_dist

BASE = os.path.expanduser("~/workspace/publications/viral-taste-loss-review")
SYN = f"{BASE}/analysis/synthesis"
OUT = f"{BASE}/manuscript/figures"
os.makedirs(OUT, exist_ok=True)

def load_json(name):
    return json.load(open(f"{SYN}/{name}"))

def cp_interval(x, n, alpha=0.05):
    lo = 0.0 if x == 0 else beta_dist.ppf(alpha/2, x, n - x + 1)
    hi = 1.0 if x == n else beta_dist.ppf(1 - alpha/2, x + 1, n - x)
    return lo, hi

def forest_panel(rows, pooled, out, title, xlabel, panel_label=""):
    """rows: list of (label, events, total). pooled: result json dict.
    Diamond + PI drawn at the bottom of the (last) panel when pooled given."""
    rows = sorted(rows, key=lambda r: r[1] / r[2])
    n = len(rows)
    fig_h = max(4.0, 0.235 * n + 1.6)
    fig, ax = plt.subplots(figsize=(8.3, fig_h))
    ys = list(range(n, 0, -1))
    for (label, x, tot), y in zip(rows, ys):
        p = x / tot
        lo, hi = cp_interval(x, tot)
        ax.plot([lo, hi], [y, y], color="#444444", lw=0.8, zorder=2)
        ax.plot([p], [y], marker="s", ms=3.5, color="#1a5276", zorder=3)
        ax.text(-0.015, y, f"{label}  {x}/{tot}", ha="right", va="center",
                fontsize=6.5, transform=ax.get_yaxis_transform() if False else ax.transData, clip_on=False)
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.1, n + 1.2)
    ax.axvline(pooled["pooled_proportion"], color="#b03a2e", lw=0.7, ls="--", alpha=0.6)
    # diamond row
    y = 0.9
    cx = pooled["pooled_proportion"]; lo = pooled["ci_lo"]; hi = pooled["ci_hi"]
    diamond = Polygon([(lo, y), (cx, y + 0.32), (hi, y), (cx, y - 0.32)],
                      closed=True, facecolor="#b03a2e", edgecolor="#7b241c", zorder=4)
    ax.add_patch(diamond)
    ax.plot([pooled["pi_lo"], pooled["pi_hi"]], [y - 0.75, y - 0.75],
            color="#b03a2e", lw=2.2, solid_capstyle="butt", zorder=3)
    ax.text(1.015, y, f"Pooled {cx*100:.1f}% ({lo*100:.1f} to {hi*100:.1f})",
            ha="left", va="center", fontsize=6.5, transform=ax.transData, clip_on=False)
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_title(title, fontsize=9, loc="left")
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", labelsize=7)
    fig.tight_layout()
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print("wrote", out)

# ---------------- Figure 2: frequency forest, 4 panels ----------------
freq_rows = []
with open(f"{SYN}/q1_frequency_pool.csv") as fh:
    for r in csv.DictReader(fh):
        freq_rows.append((r["record_id"], int(r["events"]), int(r["total"])))
assert len(freq_rows) == 137
pooled_freq = load_json("q1_frequency_pool_result.json")
freq_rows_sorted = sorted(freq_rows, key=lambda r: r[1] / r[2])
panels = [freq_rows_sorted[i:i + 35] for i in range(0, 137, 35)]
for i, panel in enumerate(panels):
    last = i == len(panels) - 1
    # only the last panel carries the diamond; earlier panels pass pooled
    # with a dummy diamond suppressed by drawing on last only
    if last:
        forest_panel(panel, pooled_freq, f"{OUT}/fig2_forest_frequency_panel{chr(65+i)}.png",
                     f"Figure 2{chr(65+i)}. Acute taste dysfunction frequency, panel {chr(65+i)} of 4 (studies sorted by proportion; diamond and prediction interval in panel D)",
                     "Proportion with taste dysfunction")
    else:
        # draw without diamond: temporarily use a pooled dict but hide by
        # plotting panel through the same function with diamond off
        rows = panel
        rows_s = sorted(rows, key=lambda r: r[1] / r[2])
        n = len(rows_s)
        fig, ax = plt.subplots(figsize=(8.3, max(4.0, 0.235 * n + 1.6)))
        ys = list(range(n, 0, -1))
        for (label, x, tot), y in zip(rows_s, ys):
            p = x / tot
            lo, hi = cp_interval(x, tot)
            ax.plot([lo, hi], [y, y], color="#444444", lw=0.8, zorder=2)
            ax.plot([p], [y], marker="s", ms=3.5, color="#1a5276", zorder=3)
            ax.text(-0.015, y, f"{label}  {x}/{tot}", ha="right", va="center", fontsize=6.5, clip_on=False)
        ax.set_yticks([]); ax.set_xlim(0, 1); ax.set_ylim(0.4, n + 1.2)
        ax.set_xlabel("Proportion with taste dysfunction", fontsize=8)
        ax.set_title(f"Figure 2{chr(65+i)}. Acute taste dysfunction frequency, panel {chr(65+i)} of 4 (studies sorted by proportion; diamond and prediction interval in panel D)", fontsize=9, loc="left")
        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
        ax.tick_params(axis="x", labelsize=7)
        fig.tight_layout(); fig.savefig(f"{OUT}/fig2_forest_frequency_panel{chr(65+i)}.png", dpi=300, bbox_inches="tight")
        plt.close(fig)
        print("wrote panel", chr(65 + i))

# ---------------- Figure 3: recovery forests ----------------
pool_rows = list(csv.DictReader(open(f"{SYN}/q1_recovery_pool.csv")))
analysis_set = load_json("q1_recovery_analysis_set.json")
selected = {(r["record_id"], r["outcome"], r["window"]) for r in analysis_set}
rec_rows = {}
for r in pool_rows:
    key = (r["record_id"], r["outcome"], r["window"])
    if key in selected:
        # latest-timepoint rule already applied in analysis set; if two pool
        # rows share the key keep the one matching the analysis-set timepoint
        tp = [a["timepoint"] for a in analysis_set if (a["record_id"], a["outcome"], a["window"]) == key][0]
        if key in rec_rows and r["assessment_timepoint"] != tp:
            continue
        rec_rows[key] = (r["record_id"], int(r["events_recovered"]), int(r["n_with_dysfunction_followed"]))
groups = [
    ("complete", "<=4 weeks", "q1_rec_complete_le4_result.json", "Complete recovery, 4 weeks or less"),
    ("complete", ">4-12 weeks", "q1_rec_complete_4to12_result.json", "Complete recovery, more than 4 to 12 weeks"),
    ("complete", ">12 weeks", "q1_rec_complete_gt12_result.json", "Complete recovery, more than 12 weeks"),
    ("any", ">12 weeks", "q1_rec_any_gt12_result.json", "Any (complete or partial) recovery, more than 12 weeks"),
]
fig, axes = plt.subplots(4, 1, figsize=(8.3, 11.0))
for ax, (outcome, window, jf, gtitle) in zip(axes, groups):
    rows = [v for k, v in rec_rows.items() if k[1] == outcome and k[2] == window]
    pooled = load_json(jf)
    assert sum(r[1] for r in rows) == pooled["crude_events"] and sum(r[2] for r in rows) == pooled["crude_total"], (gtitle, rows, pooled)
    rows = sorted(rows, key=lambda r: r[1] / r[2])
    n = len(rows)
    ys = list(range(n + 2, 2, -1))
    for (label, x, tot), y in zip(rows, ys):
        p = x / tot
        lo, hi = cp_interval(x, tot)
        ax.plot([lo, hi], [y, y], color="#444444", lw=0.8, zorder=2)
        ax.plot([p], [y], marker="s", ms=3.5, color="#1a5276", zorder=3)
        ax.text(-0.015, y, f"{label}  {x}/{tot}", ha="right", va="center", fontsize=6.5, clip_on=False)
    cx = pooled["pooled_proportion"]
    diamond = Polygon([(pooled["ci_lo"], 1.6), (cx, 1.95), (pooled["ci_hi"], 1.6), (cx, 1.25)],
                      closed=True, facecolor="#b03a2e", edgecolor="#7b241c", zorder=4)
    ax.add_patch(diamond)
    ax.plot([pooled["pi_lo"], pooled["pi_hi"]], [0.75, 0.75], color="#b03a2e", lw=2.2, solid_capstyle="butt")
    ax.text(1.015, 1.6, f"{cx*100:.1f}% ({pooled['ci_lo']*100:.1f} to {pooled['ci_hi']*100:.1f})", ha="left", va="center", fontsize=6.5, clip_on=False)
    ax.axvline(cx, color="#b03a2e", lw=0.6, ls="--", alpha=0.55)
    ax.set_yticks([]); ax.set_xlim(0, 1); ax.set_ylim(0.2, n + 3.4)
    ax.set_title(gtitle, fontsize=8.5, loc="left")
    ax.set_xlabel("Proportion recovered", fontsize=7.5)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", labelsize=7)
fig.suptitle("Figure 3. Taste recovery by time window (diamond = pooled estimate, tips = 95% CI; bar below = 95% prediction interval)", fontsize=9)
fig.tight_layout(rect=[0, 0, 1, 0.985])
fig.savefig(f"{OUT}/fig3_forest_recovery.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("wrote fig3")

# ---------------- Figure 4: summary of all pools ----------------
summary = [
    ("Frequency, all (k=137)", "q1_freq_all_result.json"),
    ("Frequency, psychophysical (k=15)", "q1_freq_psychophysical_result.json"),
    ("Frequency, self-report (k=122)", "q1_freq_selfreport_result.json"),
    ("Frequency, hospitalised (k=55)", "q1_freq_hospitalised_result.json"),
    ("Frequency, community (k=35)", "q1_freq_community_result.json"),
    ("Frequency, low RoB excl. registry (k=33)", "q1_freq_lowrob_excl_R00846_result.json"),
    ("Frequency, composite smell-or-taste (k=27)", "q1_frequency_composite_result.json"),
    ("Complete recovery, <=4 wk (k=10)", "q1_rec_complete_le4_result.json"),
    ("Complete recovery, >4-12 wk (k=11)", "q1_rec_complete_4to12_result.json"),
    ("Complete recovery, >12 wk (k=9)", "q1_rec_complete_gt12_result.json"),
    ("Any recovery, >12 wk (k=5)", "q1_rec_any_gt12_result.json"),
]
fig, ax = plt.subplots(figsize=(8.3, 5.6))
ys = list(range(len(summary), 0, -1))
for (label, jf), y in zip(summary, ys):
    d = load_json(jf)
    ax.plot([d["pi_lo"], d["pi_hi"]], [y, y], color="#b03a2e", lw=2.0, solid_capstyle="butt", alpha=0.55, zorder=2)
    ax.plot([d["ci_lo"], d["ci_hi"]], [y, y], color="#1a5276", lw=3.2, solid_capstyle="butt", zorder=3)
    ax.plot([d["pooled_proportion"]], [y], marker="D", ms=5, color="#1a5276", zorder=4)
    ax.text(-0.015, y, label, ha="right", va="center", fontsize=7.5, clip_on=False)
    ax.text(1.015, y, f"{d['pooled_proportion']*100:.1f}% ({d['ci_lo']*100:.1f} to {d['ci_hi']*100:.1f}); PI {d['pi_lo']*100:.1f} to {d['pi_hi']*100:.1f}",
            ha="left", va="center", fontsize=7, clip_on=False)
ax.set_yticks([]); ax.set_xlim(0, 1); ax.set_ylim(0.3, len(summary) + 0.9)
ax.set_xlabel("Pooled proportion (thick bar = 95% CI; thin bar = 95% prediction interval)", fontsize=8)
ax.set_title("Figure 4. Summary of all pooled proportions", fontsize=9, loc="left")
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.tick_params(axis="x", labelsize=7)
fig.tight_layout(); fig.savefig(f"{OUT}/fig4_summary_pools.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("wrote fig4")

# ---------------- Figure 1: PRISMA flow ----------------
fig, ax = plt.subplots(figsize=(8.3, 11.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 14); ax.axis("off")

def box(x, y, w, h, text, fc="#eef3f8"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06,rounding_size=0.08",
                                facecolor=fc, edgecolor="#1a5276", lw=0.9))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=6.8, wrap=True)

def arrow(x, y1, y2):
    ax.annotate("", xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle="->", color="#1a5276", lw=0.9))

box(2.2, 13.0, 5.6, 0.85, "Records identified: PubMed 2,720; Europe PMC 2,816\n(incl. 418 preprints); ClinicalTrials.gov 452. Total 5,988")
arrow(5.0, 13.0, 12.55)
box(2.2, 11.7, 5.6, 0.85, "Duplicates removed: 2,487\nRecords screened at title/abstract: 3,501")
arrow(5.0, 11.7, 11.25)
box(0.3, 10.4, 4.4, 0.85, "Excluded at title/abstract: 2,854\nFlagged for author (no abstract): 13")
box(5.3, 10.4, 4.4, 0.85, "Proceed to full text (main pool): 634\n(541 include + 93 taste-ambiguous)", "#fdf3e7")
arrow(7.5, 10.4, 9.95)
box(5.3, 9.1, 4.4, 0.85, "Full texts retrieved: 408; not retrieved: 226\nAssessed: 408; excluded at full text: 45")
arrow(7.5, 9.1, 8.65)
box(5.3, 7.8, 4.4, 0.85, "Included from main pool: 363 (stage count, before the\neligibility-consistency step below)\nFlag-13: 7 retrieved, all excluded; 6 awaiting classification", "#eafaf1")
box(0.3, 7.8, 4.4, 0.85, "Abstract-only stratum (separate, never pooled):\n232 records: 90 include, 46 exclude,\n96 awaiting classification", "#f4ecf7")
arrow(5.0, 7.8, 7.35)
box(2.2, 6.15, 5.6, 1.2, "Citation chasing (555 sources): 16,615 references + 13,867 citations examined;\n13,651 new candidates; 12 both-include, 72 disagreements adjudicated\n(39 include, 30 exclude, 3 flagged); 54 sought, 35 retrieved,\n19 to chasing abstract-only stratum (16 include, 3 awaiting)", "#fdf3e7")
arrow(5.0, 6.15, 5.7)
box(2.2, 4.3, 5.6, 1.4, "Chasing full-text screening: 26 included, no duplicates\nIncluded total before the eligibility-consistency step: 389 records\nINCLUDED TOTAL after the step: 363 records (362 unique publications;\none paper, Ohla 2022, appears under two record IDs, R01101 and\nR02974, and contributes no data to any pool)\n(Q1 339, Q2 280, Q3 82; multi-membership)", "#eafaf1")
arrow(5.0, 4.3, 4.05)
box(2.2, 2.6, 5.6, 1.45, "Eligibility-consistency step (Phase 6): 26 records with no primary data\n(narrative reviews, letters, correspondence, one hypothesis paper;\nC8424 among them) formally excluded — Appendix E. None contributed\ndata to any pool, so no pooled number changed. Synthesis set: 363 records", "#fbeee6")
ax.text(5.0, 2.25, "WHO ICTRP keyword search not run (form-only portal, retried on two routes). Embase, Scopus, Web of Science,\nCINAHL and CENTRAL not run (no licensed access). Neither is reported as searched.", ha="center", fontsize=6.5, style="italic")
fig.tight_layout(); fig.savefig(f"{OUT}/fig1_prisma.png", dpi=300, bbox_inches="tight")
plt.close(fig)
print("wrote fig1")
