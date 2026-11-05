#!/usr/bin/env python3
"""SE effect sizes and comparisons. Local only, no network.
Usage: python3 se_effects.py results.csv   (columns: algo,run,value ; higher_is_better flag via --lower)
Prints per pair: Mann-Whitney U p, Vargha-Delaney A12, Cliff's delta, magnitude; Holm and BH adjusted p.
"""
import sys, csv, itertools, argparse
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

def a12(x, y):
    m, n = len(x), len(y)
    r = sum(1.0 if a > b else 0.5 if a == b else 0.0 for a in x for b in y)
    return r / (m * n)

def mag_a12(a):  # Vargha & Delaney 2000 thresholds on |A-0.5|
    d = abs(a - 0.5)
    return "negligible" if d < 0.06 else "small" if d < 0.14 else "medium" if d < 0.21 else "large"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--lower", action="store_true", help="lower values are better")
    a = ap.parse_args()
    data = {}
    for row in csv.DictReader(open(a.csv)):
        data.setdefault(row["algo"], []).append(float(row["value"]))
    pairs = list(itertools.combinations(sorted(data), 2)); res = []
    for p, q in pairs:
        x, y = data[p], data[q]
        if a.lower: x, y = [-v for v in x], [-v for v in y]
        pv = mannwhitneyu(x, y, alternative="two-sided").pvalue
        A = a12(x, y); res.append((p, q, len(x), len(y), pv, A, 2 * A - 1))
    pvals = [r[4] for r in res]
    holm = multipletests(pvals, method="holm")[1] if pvals else []
    bh = multipletests(pvals, method="fdr_bh")[1] if pvals else []
    print("A,B,nA,nB,p_raw,p_holm,p_bh,A12,cliff_delta,magnitude")
    for r, h, b in zip(res, holm, bh):
        print(f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]:.4g},{h:.4g},{b:.4g},{r[5]:.3f},{r[6]:.3f},{mag_a12(r[5])}")

if __name__ == "__main__":
    main()
