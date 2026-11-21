#!/usr/bin/env python3
"""Random-effects meta-analysis of proportions (protocol-locked methods).

- Logit transformation of proportions (0.5 continuity correction only where events==0 or events==n)
- REML estimator for tau^2 (Fisher scoring iterations)
- Hartung-Knapp adjustment for the pooled CI
- I^2, tau^2, Q, and a 95% prediction interval (t_{k-2})
- Also reports the crude (unweighted) totals for cross-checking

Usage: meta_proportions.py pool.csv label
pool.csv needs columns: record_id, events, total
Writes <label>_result.json next to this script and prints a summary.
"""
import sys, json, math, csv
import numpy as np
from scipy import stats

def reml_tau2(y, v):
    """REML estimate of tau^2 by direct maximisation of the restricted
    log-likelihood over tau2 >= 0 (grid + golden-section refine).
    Deterministic and independently verifiable."""
    y = np.asarray(y, float); v = np.asarray(v, float)
    def reml_loglik(t2):
        w = 1.0/(v + t2)
        mu = np.sum(w*y)/np.sum(w)
        return -0.5*(np.sum(np.log(v+t2)) + np.log(np.sum(w)) + np.sum(w*(y-mu)**2))
    grid = np.concatenate([[0.0], np.logspace(-8, 2, 400)])
    vals = [reml_loglik(g) for g in grid]
    i = int(np.argmax(vals))
    lo = grid[max(0, i-1)]; hi = grid[min(len(grid)-1, i+1)]
    for _ in range(200):
        m1 = lo + (hi-lo)*0.3819660112501051
        m2 = hi - (hi-lo)*0.3819660112501051
        if reml_loglik(m1) < reml_loglik(m2): lo = m1
        else: hi = m2
    return float((lo+hi)/2)

def pool(events, totals, label):
    events = np.asarray(events, float); totals = np.asarray(totals, float)
    k = len(events)
    p = events/totals
    # continuity correction only for boundary cells
    e = np.where((events==0)|(events==totals), events+0.5, events)
    n = np.where((events==0)|(events==totals), totals+1.0, totals)
    y = np.log(e/(n-e))
    v = 1/e + 1/(n-e)
    tau2 = reml_tau2(y, v) if k > 1 else 0.0
    w = 1.0/(v+tau2)
    mu = np.sum(w*y)/np.sum(w)
    # Hartung-Knapp
    if k > 1:
        q_hk = np.sum(w*(y-mu)**2)/(k-1)
        se_hk = math.sqrt(max(q_hk, 0.0)/np.sum(w))
        se_classic = math.sqrt(1/np.sum(w))
        tcrit = stats.t.ppf(0.975, k-1)
        ci_lo, ci_hi = mu - tcrit*se_hk, mu + tcrit*se_hk
    else:
        se_hk = math.sqrt(1/np.sum(w)); tcrit = stats.norm.ppf(0.975)
        ci_lo, ci_hi = mu - tcrit*se_hk, mu + tcrit*se_hk
    # heterogeneity
    wf = 1.0/v
    mu_f = np.sum(wf*y)/np.sum(wf)
    Q = float(np.sum(wf*(y-mu_f)**2))
    I2 = max(0.0, (Q-(k-1))/Q)*100 if Q > 0 else 0.0
    # prediction interval (t_{k-2})
    if k > 2:
        tp = stats.t.ppf(0.975, k-2)
        pi_lo, pi_hi = mu - tp*math.sqrt(tau2 + se_hk**2), mu + tp*math.sqrt(tau2 + se_hk**2)
    else:
        pi_lo = pi_hi = float('nan')
    inv = lambda x: float(1/(1+math.exp(-x)))
    res = {
        "label": label, "k": int(k),
        "crude_events": int(events.sum()), "crude_total": int(totals.sum()),
        "crude_proportion": float(events.sum()/totals.sum()),
        "pooled_proportion": inv(mu), "ci_lo": inv(ci_lo), "ci_hi": inv(ci_hi),
        "tau2_logit": float(tau2), "I2_percent": float(I2), "Q": Q, "Q_df": int(k-1),
        "Q_p": float(1-stats.chi2.cdf(Q, k-1)) if k > 1 else None,
        "pi_lo": inv(pi_lo) if pi_lo==pi_lo else None, "pi_hi": inv(pi_hi) if pi_hi==pi_hi else None,
        "method": "logit proportions; REML tau2 (profile likelihood); Hartung-Knapp CI; PI t(k-2)",
    }
    return res

if __name__ == "__main__":
    path, label = sys.argv[1], sys.argv[2]
    rows = list(csv.DictReader(open(path)))
    res = pool([float(r["events"]) for r in rows], [float(r["total"]) for r in rows], label)
    out = f"/home/hatch/workspace/publications/viral-taste-loss-review/analysis/synthesis/{label}_result.json"
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(res, indent=1))
