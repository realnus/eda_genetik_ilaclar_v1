# Deep Dive — The Synthetic-Lethal Core (Paxalisib + WEE1/ATR)

**Why this regimen deserves the closest look.** Of the three regimens in the main dossier,
this one rests on the tumor's *actual genetics* rather than on repurposing hope — and the
previous iteration showed why that matters (the most rigorously tested repurposing drug,
disulfiram, failed its randomized trial). This core targets the **truncal p53 loss** that is
present in essentially every tumor cell.

> **Decision-support only — not a prescription.** This regimen is largely trial-gated and
> carries overlapping toxicities. It must be evaluated and managed by your oncologist.

![Synthetic-lethal mechanism]({{artifact:bc9663bd-fc16-4cbe-a0fe-a57adb0e23fd}})

---

## 1. The mechanism, in plain terms

Your wife's tumor has **lost p53** (four TP53 variants, VAF ~24–25%, truncal). p53 normally
runs the **G1/S checkpoint** — the first quality-control gate that halts a cell with DNA damage
*before* it copies its DNA. With p53 gone, that gate is permanently open.

That forces the tumor to lean entirely on its **backup gate — the G2/M checkpoint** — to pause
and repair damage before dividing. The G2/M gate is run by **WEE1** (and, upstream, **ATR** and
**CHK1**). 

**The synthetic-lethal move:** give a DNA-damaging treatment (radiation or an alkylator) *and*
simultaneously **remove the backup gate** with a WEE1 or ATR inhibitor. The tumor cell, unable
to pause, enters mitosis with catastrophic unrepaired damage and dies (**mitotic catastrophe**).
Normal cells — which still have p53 and the G1/S gate — are relatively spared. That selectivity
is the entire point: it is lethal *specifically because* the tumor is p53-null.

**A second sensitizer:** the truncal **TERT promoter C250T** drives telomere replication stress,
which independently makes cells more dependent on ATR — so an ATR inhibitor hits V1 and V2 at once.

**Getting into the brain:** **paxalisib** is engineered to cross the blood–brain barrier, and
adavosertib and several ATR inhibitors have documented CNS/tumor exposure — a non-trivial
requirement that many drugs fail.

---

## 2. Primary evidence (verified via OpenAlex, GBM-anchored)

| Claim | Reference | Grade |
|-------|-----------|-------|
| **WEE1 is overexpressed in GBM and is the major G2-checkpoint regulator; inhibiting it during DNA damage causes mitotic catastrophe and radiosensitizes GBM in vivo** | Mir et al., *Cancer Cell* 2010 — [10.1016/j.ccr.2010.08.011](https://doi.org/10.1016/j.ccr.2010.08.011) | Foundational preclinical |
| ATR inhibitors are synthetic-lethal in p53/ATM-deficient tumors | *Nat Commun* 2016 — [10.1038/ncomms13837](https://doi.org/10.1038/ncomms13837) | Preclinical mechanism |
| Adavosertib (WEE1i) + radiation feasible in diffuse glioma | *Neuro-Oncol Adv* 2022 — [10.1093/noajnl/vdac073](https://doi.org/10.1093/noajnl/vdac073) | Clinical (early-phase) |
| Paxalisib Phase 2, newly diagnosed GBM, unmethylated MGMT | Wen et al., ASCO 2022 — [10.1200/jco.2022.40.16_suppl.2047](https://doi.org/10.1200/jco.2022.40.16_suppl.2047) | Clinical (Phase 2) |
| DDR-inhibitor (ATR/CHK1/WEE1) landscape in GBM | *Neuro-Oncol Adv* 2021 review — [10.1093/noajnl/vdab015](https://doi.org/10.1093/noajnl/vdab015) | Review |

The Mir 2010 paper is the keystone: it established WEE1 as the GBM "gatekeeper against mitotic
catastrophe," confirming that the exact vulnerability your wife's tumor carries (checkpoint
dependence) is druggable and radiosensitizing in glioblastoma models.

---

## 3. Currently recruiting trials that fit a recurrent IDH-wildtype GBM

*(Live from ClinicalTrials.gov this session. Eligibility text confirms each accommodates
recurrent disease; final eligibility is always determined by the trial team.)*

### ⭐ NCT05765812 — Debio 0123 (WEE1 inhibitor) + temozolomide ± radiotherapy
- **Phase 1/2, RECRUITING.** Conditions: **IDH-wildtype GBM** / Grade III astrocytoma — a direct match to the tumor's IDH status.
- Recurrence-eligible; requires measurable/non-measurable disease by RANO; stable/decreasing low-dose steroids.
- **16 sites — USA, Spain, Switzerland.** Enrollment 116. Primary completion 2028-09.
- **Why it matters:** this is the cleanest available test of the **WEE1 arm** of this exact strategy, in the right molecular subtype.

### ⭐ NCT03970447 — GBM AGILE (adaptive platform; **paxalisib is an arm**)
- **Phase 2/3, RECRUITING.** Has a **dedicated Recurrent GBM inclusion arm**; KPS ≥ 60; IDH-wildtype.
- **63 sites — USA, Canada, France, Germany, Australia, Switzerland.** Enrollment 2250. Primary completion 2028-06.
- **Why it matters:** the **largest access route to paxalisib for recurrent GBM.** Its adaptive design continuously rotates in the best-performing regimens, so a single enrollment can route to the current most-promising arm.

### NCT07391215 — 5G-PEARL: paxalisib + temozolomide
- **Phase 1/2, RECRUITING.** Malignant glioma / GBM, age ≥ 16.
- **1 site — United Kingdom.** Enrollment 64. Primary completion 2029-01.
- **Why it matters:** a focused paxalisib+TMZ combination, but single-site (UK) — access depends on geography.

---

## 4. Safety & sequencing — what to raise with the oncologist
- **Myelosuppression** is the shared dose-limiting toxicity of WEE1/ATR inhibitors combined with alkylators/radiation. Sequencing and dose de-escalation are central.
- **WEE1/ATR inhibitors are given intermittently, timed around the DNA-damage source** (radiation or TMZ) — the *timing* is the therapy, not continuous dosing.
- **Paxalisib** causes on-target **hyperglycemia** and oral mucositis; pairing with **metformin** is synergistic here because metformin also improves glycemic control — a rare case where a toxicity and a second drug's benefit align.
- **Access reality:** this core is largely trial-gated. The realistic routes are (a) the trials above, or (b) off-label targeted-agent use under an oncologist, which is harder to obtain and to fund.

---

## 5. How this feeds the iterative system
`synthetic_lethal_core.json` stores this analysis in machine-readable form; the trial list can
be refreshed by re-running the engine's `refresh_evidence()` against ClinicalTrials.gov. **Next
possible iterations:** (1) pull full eligibility exclusion criteria to pre-screen fit (prior
therapies, lab thresholds); (2) map the nearest recruiting sites to your location; (3) add the
specific WEE1/ATR agents' documented BBB-penetration data; (4) monitor GBM AGILE arm rotations.
