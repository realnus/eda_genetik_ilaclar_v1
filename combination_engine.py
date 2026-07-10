#!/usr/bin/env python3
"""
combination_engine.py — Iterative combination-therapy engine for recurrent GBM.

Re-runnable system that:
  1. Loads the tumor vulnerability map + drug library + candidate regimens.
  2. Scores each regimen by how many *truncal* and total vulnerabilities it covers.
  3. Flags uncovered vulnerabilities (gaps) to drive the next iteration.
  4. (Optional, --live) re-queries ClinicalTrials.gov / Open Targets / CIViC via the
     host.mcp connectors for fresh evidence — run inside the `repl` tool where host.mcp exists.

Usage (offline scoring):   python combination_engine.py
Live evidence refresh:     run refresh_evidence() from the repl tool (host.mcp available there).

NOTE: Decision-support only. Not medical advice. All regimens require oncologist review.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name): return json.load(open(os.path.join(HERE, name)))

# Truncal drivers get double weight — they are present in every tumor cell.
TRUNCAL = {"V1_TERT", "V2_TP53"}

def score_regimens(vulns=None, drugs=None, regimens=None):
    vulns    = vulns    or _load("vulnerability_map.json")
    drugs    = drugs    or _load("drug_candidates.json")
    regimens = regimens or _load("candidate_regimens.json")
    all_v = {v["id"] for v in vulns}
    ranked = []
    for r in regimens:
        hit = set(r["vuln_hit"] if "vuln_hit" in r else r.get("vulns_hit", []))
        truncal_hit = hit & TRUNCAL
        score = len(hit) + len(truncal_hit)          # truncal counts double
        ranked.append({
            "name": r["name"],
            "covers": sorted(hit),
            "truncal_covered": sorted(truncal_hit),
            "gaps": sorted(all_v - hit),
            "score": score,
            "precedent": r.get("precedent", ""),
        })
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

def coverage_gaps(vulns=None, drugs=None):
    """Which vulnerabilities have no candidate drug yet -> next-iteration targets."""
    vulns = vulns or _load("vulnerability_map.json")
    drugs = drugs or _load("drug_candidates.json")
    covered = set()
    for d in drugs:
        covered |= set(d["vuln"])
    return sorted({v["id"] for v in vulns} - covered)

def refresh_evidence(mcp):
    """Re-pull live evidence. Pass host.mcp (available in the repl tool).
       Returns dict of fresh trial + Open Targets results."""
    GBM = "MONDO_0018177"
    ev = {}
    ev["ot_targets"] = mcp("clinical-genomics", "open_targets_disease_targets", efo_id=GBM, size=40)
    ev["recruiting_recurrent"] = mcp("clinical-trials", "search_trials",
        condition="recurrent glioblastoma", status=["RECRUITING"], page_size=50, count_total=True)
    return ev



# --- Evidence layer (added iteration 2) -------------------------------------
def evidence_flags(evidence=None):
    """Surface drugs whose highest-grade evidence is a NEGATIVE clinical trial —
       these should be de-prioritized regardless of mechanistic appeal."""
    evidence = evidence or _load("drug_evidence_layer.json")
    negative, clinical, removed = [], [], []
    for drug, val in evidence.items():
        # Provenance keys (e.g. "_removed_disulfiram") archive a removed drug as
        # {"reason": str, "evidence": [ref, ...]} rather than a bare list of refs.
        if drug.startswith("_"):
            refs = val.get("evidence", []) if isinstance(val, dict) else []
            removed.append(drug)
        else:
            refs = val if isinstance(val, list) else []
        for r in refs:
            if not isinstance(r, dict):
                continue
            if r.get("finding","").startswith("NEGATIVE"):
                negative.append((drug, r.get("doi")))
            if "Clinical" in r.get("type","") or "Randomized" in r.get("type",""):
                clinical.append((drug, r.get("year"), r.get("type")))
    return {"negative_trial_drugs": negative, "clinical_grade_drugs": clinical,
            "removed_drugs": removed}



# --- Access-track strategy scoring (added iteration 3) ----------------------
TRACK_LABEL = {"F":"Fast repurpose", "A":"Accessible oncology", "T":"Trial-gated"}

def track_coverage(vulns=None, drugs=None):
    """For each access track (and the combined fast tracks F+A), report which
       vulnerabilities can be engaged NOW vs only via trial drugs."""
    vulns = vulns or _load("vulnerability_map.json")
    drugs = drugs or _load("drug_candidates.json")
    all_v = [v["id"] for v in vulns]
    cov = {tk: set() for tk in TRACK_LABEL}
    for d in drugs:
        cov.setdefault(d.get("track","?"), set())
        cov[d.get("track","?")] |= set(d["vuln"])
    fast = cov.get("F", set()) | cov.get("A", set())   # startable without a trial
    return {
        "by_track": {tk: sorted(cov.get(tk, set())) for tk in TRACK_LABEL},
        "fast_now_covers": sorted(fast),
        "trial_only": sorted(set(all_v) - fast),   # vulnerabilities ONLY trial drugs reach
        "all_vulns": all_v,
    }



# --- Node-level redundancy check (added iteration 5) ------------------------
def node_redundancy(regimen_drugs=None, nodes=None):
    """Given a list of drug names, flag which mechanism NODES have 2+ drugs
       piling on them (potential redundancy = added toxicity without new coverage)
       vs which drugs each open a UNIQUE node. Pass drug names as they appear in
       vulnerability_nodes.json values."""
    nodes = nodes or _load("vulnerability_nodes.json")
    # build node -> drugs, restricted to the regimen if given
    hits = {}
    for v, nd in nodes.items():
        for node, drugs in nd.items():
            clean = [d.replace("(ON-BOARD)","").replace("(mTORC1)","") for d in drugs]
            if regimen_drugs is not None:
                clean = [d for d in clean if any(rd.lower() in d.lower() or d.lower() in rd.lower() for rd in regimen_drugs)]
            if clean:
                hits[f"{v}::{node}"] = clean
    overlapping = {k:v for k,v in hits.items() if len(v) >= 2}
    unique = {k:v[0] for k,v in hits.items() if len(v) == 1}
    return {"overlapping_nodes": overlapping, "unique_nodes": unique,
            "n_nodes_covered": len(hits)}

if __name__ == "__main__":
    print("=== Regimen ranking (truncal drivers weighted 2x) ===")
    for r in score_regimens():
        print(f"\n[{r['score']}] {r['name']}")
        print(f"    covers: {', '.join(r['covers'])}")
        print(f"    truncal covered: {', '.join(r['truncal_covered']) or 'NONE'}")
        print(f"    gaps: {', '.join(r['gaps'])}")
        print(f"    precedent: {r['precedent']}")
    ef = evidence_flags()
    print("\n=== Evidence flags ===")
    def _clean(name): return name.replace("_removed_", "").rstrip("+Cu").capitalize() if name.startswith("_") else name
    print("  NEGATIVE randomized-trial drugs (removed/de-prioritized):",
          [(_clean(d), doi) for d, doi in ef["negative_trial_drugs"]] or "none")
    print("  Clinical-grade drugs (active):",
          [d[0] for d in ef["clinical_grade_drugs"] if not d[0].startswith("_")])
    print("  Removed drugs (provenance kept):", [_clean(d) for d in ef["removed_drugs"]] or "none")
    nr = node_redundancy()
    print("\n=== Düğüm çakışması (aynı mekanizmada 2+ ilaç) ===")
    for node, drugs in nr["overlapping_nodes"].items():
        print(f"  {node}: {drugs}  <- seç-birini / tekrar riski")
    tc = track_coverage()
    print("\n=== Access-track coverage ===")
    print("  Fast tracks (F+A) can engage NOW:", tc["fast_now_covers"])
    print("  Trial-only vulnerabilities:", tc["trial_only"])
    print("\n=== Vulnerabilities with no candidate drug yet ===")
    print(coverage_gaps() or "none — all vulnerabilities have >=1 candidate")
